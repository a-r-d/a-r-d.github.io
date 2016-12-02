---
author: Aaron Decker
comments: true
date: 2014-01-22 02:30:46+00:00
layout: post
link: http://ard.ninja/blog/full-text-search-sphinx-mysql-innodb/
slug: full-text-search-sphinx-mysql-innodb
title: Full text search with Sphinx and MySQL InnoDB
wordpress_id: 276
---

First get [sphinx download package](http://sphinxsearch.com/downloads/release/). Then get some other packages we may need:

```
apt-get install libmysqlclient-dev
apt-get install g++
apt-get install libexpat-dev
```

Config, make, install

```
./configure --with-mysql
make
make install
```

All the results should be in ./src - you will find 3 executable files that will be needed, they are:

	* indexer
	* search
	* searchd


I did this in /opt/sphinx (Note: I wasn't too certain I would continue to use Sphinx when I put it on my system I didn't do anything very permanent or integrated- hence installing under /opt/). Next we will need to add a config file- I will add a file called sphinx.conf to "/opt/sphinx/src/sphinx.conf".

```
source src1
{
    type  = mysql

    sql_host=localhost
    sql_port=3306
    sql_db=REDACTED
    sql_user=REDACTED
    sql_pass=REDACTED

    sql_query_range = SELECT MIN(id),MAX(id) FROM table_name_here
    sql_range_step = 1000
    sql_query = SELECT * FROM table_name_here WHERE id>=$start AND id<=$end

}

# Define the index.
index members
{
    # Which source to use
    source = src1

    # Path where to store the index data
    path = /opt/sphinx/var/data/members

    # Charset of the data
    charset_type = utf-8

    # Minimum lenght of a word to be indexed.
    min_word_len = 3

}

# Indexer definition
indexer
{
    # Memory limit for the indexer
    mem_limit = 32M
}

# Searchd settings
searchd
{
    # Port to listen on
    listen = 3312

    # Next few are the paths to log files
    log           = /opt/sphinx/var/log/searchd.log
    query_log = /opt/sphinx/var/log/query.log

    # Maximum amount of concurrent searches to run - 0 for unlimited
    max_children = 30

    # Path to pid file
    pid_file = /opt/sphinx/var/log/searchd.pid
}

```

We will add a few more directories for the log file and test file:
```
mkdir /opt/sphinx/var
mkdir /opt/sphinx/var/log
mkdir /opt/sphinx/var/data
mkdir /opt/sphinx-php
```


Sphinx api docs are located [here](http://sphinxsearch.com/wiki/doku.php?id=php_api_docs).


The next problem to solve is the issue of an ever-growing database. We cannot re-index a huge db every time now can we? For this we must use the ["Delta Index Updates"](http://sphinxsearch.com/docs/archives/1.10/delta-updates.html) feature.

The steps are:
1. Create a sphinx counter table (so we can keep track of our last id updated).
2. You will need to add two sources- a main and a delta.
3. In the main you will pull all the records less than the max and update the record of the max id
4. In the delta you will pull all the records greater than the max id, then for your post query you should re-update with new max ID.

{% highlight sql %}

CREATE TABLE sph_counter
(
    counter_id INTEGER PRIMARY KEY NOT NULL,
    max_doc_id INTEGER NOT NULL
);

{% endhighlight %}



```
source main
{
    # We will use the xmlpipe2 datasource
    type  = mysql

    # Command which should be executed to get the xml. The following php script outputs the required xml to stdout
    #xmlpipe_command  = php /opt/sphinx-php/makeindex.php
    sql_host=localhost
    sql_port=3306
    sql_db=REDACTED
    sql_user=REDACTED
    sql_pass=REDACTED

    #sql_query_range = SELECT 3500000,MAX(id) FROM table_name_here
    sql_range_step = 1000
    sql_query_pre = SET NAMES utf8
    sql_query_pre = REPLACE INTO sph_counter SELECT 1, MAX(id) FROM table_name_here
    #sql_query = SELECT * FROM table_name_here WHERE id >= $start AND id<=$end
    sql_query = SELECT * FROM table_name_here WHERE id <= (select max_doc_id FROM sph_counter where counter_id=1)

}

source maindelta : main
{
        sql_query_pre = SET NAMES utf8
        sql_query = SELECT * from table_name_here where id > (select max_doc_id FROM sph_counter WHERE counter_id=1)
}



# Define the index.
index members
{
    # Which source to use
    source = main

    # Path where to store the index data
    path = /opt/sphinx/var/data/members

    # Charset of the data
    charset_type = utf-8

    # Minimum lenght of a word to be indexed.
    min_word_len = 3

}

index membersdelta
{
        source = maindelta
        path = /opt/sphinx/var/data/membersdelta
        charset_type = utf-8
        min_word_len = 3
}


# Indexer definition
indexer
{
    # Memory limit for the indexer
    mem_limit = 32M
}

# Searchd settings
searchd
{
    # Port to listen on
    listen = 3312

    # Next few are the paths to log files
    log           = /opt/sphinx/var/log/searchd.log
    query_log = /opt/sphinx/var/log/query.log

    # Maximum amount of concurrent searches to run - 0 for unlimited
    max_children = 30

    # Path to pid file
    pid_file = /opt/sphinx/var/log/searchd.pid
}
```


Notice how we do "source maindelta: main"? This causes us to inherit settings from the main source. Next we will go over the relevant index commands. First we have the big one- index all:

```
# it seems that this command re-indexes all of the sources every time.
./indexer --all
```

DO this when searchd is running.
```
./indexer --rotate
```

Once we have both indexes built we may want to merge them:
```
./indexer --merge members membersdelta
```

Now lets do a test search- I have indexed about a gigabyte of chat records from a popular bitcoin-related website.

```
./search bitcoin

displaying matches:
1. document=14559545, weight=1617
2. document=23588637, weight=1612
3. document=25349448, weight=1607
4. document=25349548, weight=1607
5. document=25349655, weight=1607
6. document=28222881, weight=1607
7. document=2946423, weight=1604
8. document=8347522, weight=1604
9. document=21633204, weight=1604
10. document=21633278, weight=1604
11. document=21781013, weight=1604
12. document=23107998, weight=1604
13. document=23129561, weight=1604
14. document=23129608, weight=1604
15. document=32941392, weight=1604
16. document=35398549, weight=1604
17. document=1394556, weight=1599
18. document=4642739, weight=1599
19. document=6456179, weight=1599
20. document=7595116, weight=1599

words:
1. 'bitcoin': 84622 documents, 91520 hits

index 'membersdelta': query 'bitcoin ': returned 0 matches of 0 total in 0.000 sec

words:
1. 'bitcoin': 0 documents, 0 hits
```

Excellent so basic search is working. What next? We need to get the indexer pulling in our changes. I will start ./searchd and then run the indexer only on our delta.

```
./searchd

#user --rotate when searchd has a lock on the index.
./indexer --rotate membersdelta
```


Next I will put the deltaindexer on a 5 minute cron job:

```
# make a sym link for config, it has a default location:
ln -s /opt/sphinx/src/sphinx.conf /usr/local/etc/sphinx.conf

#put in cron:
*/5 * * * * /opt/sphinx/src/indexer --rotate membersdelta > /tmp/cronlog.txt
```


In the next post I will show you a PHP script to interact with Sphinx + MySQL to get textual searching on my large InnoDB database.
