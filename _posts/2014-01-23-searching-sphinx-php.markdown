---
author: Aaron Decker
comments: true
date: 2014-01-23 05:30:21+00:00
layout: post
link: http://ard.ninja/blog/searching-sphinx-php/
slug: searching-sphinx-php
title: Searching Sphinx From PHP
wordpress_id: 287
---

Searching Sphinx from PHP is fairly simple, however the search syntax is a little hard to get used to. I will show some examples to give you an idea of an easy way to use it, especially if you are only indexing a few fields out of your DB.

Here is a [good link detailing extended search in sphinx](http://www.sanisoft.com/blog/2011/03/07/extended-query-syntax-in-sphinx-search-engine/).

{% highlight php %}

function basicSphinxSearch(
  $qry, $field_name, $page, $per_page, $only_historical){

  // Connect to sphinx server
  $sp = new SphinxClient();

  // Set the server
  $sp->SetServer('localhost', 3312);

  // SPH_MATCH_ALL will match all words in the search term
  // SPH_MATCH_EXTENDED2 will allow us to match specific fields only!
  if( $field_name != null ){
    $sp->SetMatchMode(SPH_MATCH_EXTENDED2);
  } else {
    $sp->SetMatchMode(SPH_MATCH_ALL);
  }

  // I will sort by ID descending rather than closest match.
  // I am trying to get the latest match first.
  $sp->SetSortMode(SPH_SORT_EXTENDED, '@id DESC');

  // Setting limits on the query- written for readability:
  if( $page == 0)
    $sp->SetLimits(0, $per_page);
  else
    $sp->SetLimits($page * $per_page, $page * $per_page + $per_page);

  // We want an array with complete per match information including the document ids
  $sp->SetArrayResult(true);

  // Will we specify field or search whole index?
  $sp_qry = "";
  if($field_name != null){
    $sp_qry = "@(".$field_name.") ".$qry;
  } else {
    $sp_qry = $qry;
  }

  // You have to specify both indexes if you want to search them!
  // Check last blog post for example of how I set up the indexes.
  $results = null;
  if( !$only_historical ){
    $results = $sp->Query($sp_qry, 'members membersdelta');
  } else {
    $results = $sp->Query($sp_qry, 'members');
  }

  // Returning empty arrays if we get no result or bad result (e.g. server error / down)
  if($results == null || count($results) == 0)
    return array();
  if(!isset($results["matches"]))
    return array();
  if(count($results["matches"]) == 0 )
    return array();

  // I will extract the arrays and build a query.
  // I will do this because I will not index all of my rows
  // and will need to consult MySQL for the full data.
  // I will build and "in()" query from the ids.
  $ids = array();
  foreach( $results["matches"] as $res){
    array_push($ids, $res["id"]);
  }
  $ins = "";
  $i = 0;
  $len = count($ids);
  foreach( $ids as $id ){
    if( $i < $len - 1)
      $ins .= "$id,";
    else if($i == $len - 1)
      $ins .= "$id";
    $i++;
  }

  // write our In query that selects in() on the primary key, with an order by.
  $final_qry = "select * from table_name_here where id in($ins) order by created desc";

  // I am using RedBean PHP in my example but you can use whatever here.
  $rows = R::getAll($final_qry);
  return $rows;
}

{% endhighlight %}


Well this single function just about covers most of your use cases. You will either want to search Sphinx for a single word or multiple words on all of the indexed fields or you will want to specify one or more specific fields to search. I also deal with limit cases and paging. However keep in mind your pages will not go far- you have to increase "max_results" in searchd config to have more than the default 1000 results.

In this example I'm also showing you how to search on multiple indexes with Sphinx as well as access the data you get back from the search results, which I promptly use to turn around and query MySQL.  
