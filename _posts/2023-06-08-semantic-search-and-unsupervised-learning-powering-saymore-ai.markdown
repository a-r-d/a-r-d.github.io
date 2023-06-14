---
author: Aaron Decker
comments: true
date: 2023-06-08
layout: post
slug: 2023-06-08-semantic-search-and-unsupervised-learning-powering-saymore-ai
title: The Semantic Search Engine and Unsupervised Learning Powering Saymore.ai
description:
---

I have been dabbling in machine learning for years now, and when I was doing corporate gigs for large companies there was always some [interesting application for some data we had](https://patents.justia.com/patent/20200096349), especially with unsupervised learning.

[Bounty](https://bounty.co) has obviously been a little different, but as we scaled past 100k users and 10k videos produced we started to have enough data to do interesting things with.

## What can you do with 10k TikTok videos?

We still do human-in-the-loop reviews of the titktok videos. Right now it's not a large expense and it's fairly low skilled but it's complex enough that it's hard to make some algorithm to do it without some incredible massive training set (multi modal GPT-4 will be a different story but it's not out yet).

Ideally though, of course I would like to use machine learning to handle video reviews, but it's not something I prioritized because I knew the current state of publicly accessible video analysis models is not good.

I'm going to get to [saymore.ai](https://saymore.ai) eventually, but I need to explain how we got there.

## What is in a TikTok video?

Our videos are generally product reviews, or experiences with products. A good Bounty video can be a simple review, or it can be a very creative use of the product. Some brands provide a specific brief to creators and others do not.

The range of videos we get is all over the place. Originally I disregarded transcribing the videos because with some brands the customers would submit a lot of videos with only music and no discernable language in the audio.

But when I saw some other brands videos I realized this was very demographic dependent. [Skinny Mixes](https://www.skinnymixes.com/) is a good example: their customers are women who are talking about using the products as dieting aids and flavor enhancers, and sharing recipes.

These videos almost all had great audio to transcribe.

## Using TikTok video transcription data

After you have transcription data you simply have a text string in english of what people said in the video.

I used openAIs whisper AI, which is rudimentary (no timestamps, no multiple speaker detection) but highly accurate.

But what can you do with this text? Ah... this is where the magic happens. The magic of semantic vector embeddings!

## What are semantic vector embeddings?

OpenAI provides a special API designed for cheaply turning text into high dimensional semantic vectors.

Specifically the "high dimensional semantic vectors" producd by the openAI `text-embedding-ada-002` model ([here](https://platform.openai.com/docs/guides/embeddings)) which allows a user to bulk submit sets of text and it returns vectors for each set of text with 1536 dimensions.

When used with a vector database (e.g. [Pinecone](https://www.pinecone.io/) or [Weaviate](https://weaviate.io/)) you can do similarity searches by comparing vectors using cosine similarity (or some other strategy) and then you because these are semantic vectors (meaning relationships are based on the actual meaning of words and phrases) you are able do searches that pull out vectors that **mean** similar things.

Unlike simple keyword searches, doing searches on semantic vector datasets can be deeply satisfying in how it can pull back strikingly relevant results based on the meaning of words, rather than just dumbly matching keywords.

#### The transcript text:

```
Okay, so I got this subscription. It's called Bokksu. It looks really, really, really good. So it has Japanese snacks. So here, there's a guide to them that come in this one. Welcome to Bokksu. That introduces you to how their company is made and stuff. Then there's cultural themes, support small businesses. They're always improving. And four, there are always new experiences. And then there's always quality curations. And it's made to share. It's nice because there's quite a lot of treats to come here. See, it is definitely made to share, even though I'd probably just eat it all myself. And then it tells you where all the snacks come from. And a list of all the snacks. See, like there's this white strawberry, which looks really good. And the organic in matcha tea. Strawberries are actually a chocolate in them. I tried them. They're really good. Then there's vegetable apare tomato, 20th century pear biscuit, handmade yuzu sake candy, which is really good. I've had one of those. Let's see some don don yaki. Seaweed tempura as well. Let's see some zawawa sabu, I don't know, maybe I'm pronouncing it wrong. Then some one bite sesame seed mochi, which is really good. I've tried that before. And then we also have matcha stick chocolate cake, which looks delicious. Then a kinako azuki crunch. I think I've heard of azuki, but I forgot what it is, but I'm hoping it's good. This one's soka senbei umazarabe, which looks pretty good based on the picture. So yeah, as you can see, there's plenty and plenty of treats that you can try here. Can't wait for my next box. Honestly, can't wait to try my first one. So yeah. You guys have a nice day. Love you guys.
```

#### The vector embedding output:

```
[0.0007146759, -0.017298298, 0.013004298, 0.008037662, -0.008547234, 0.0104496395, -0.01532795, -0.046146914, -0.0182495, -0.02617166, 0.006590475, -0.010381697, -0.01229769, -0.014403924, 0.0069845445, -0.004083377, 0.03446071, -0.010082747, 0.0020179083, -0.031063559, -0.009980832, 0.009301403, -0.0030438483, -0.013853586, 0.01131931, 0.005360706, 0.0050787423, 0.008880155, 0.0016391259, 0.017040115, 0.013772055, 0.01914635, 0.0016450708, -0.014702874, -0.006926793, -0.012188981, -0.008737475, 0.002214943, -0.003777633, -0.03337362, 0.008017279, 0.0013783944, -0.0024527437, 0.004888502, -0.022502735, 0.0065531065, -0.01493388, -0.0026412858, 0.003473588, 0.011353282, 0.019689893, -0.005567932, -0.03671642, 0.00025712195, 0.006012959, -0.008418143, -0.008676326, -0.021442823, 0.016809108, -0.026986975, 0.0057106125, 0.027734349, -0.019078406, -0.0074261744, 0.015925849, -0.012358839, -0.034786835, -0.010293371, -0.02108952, -0.0020756598, -0.010259399, 0.008418143, 0.0022421204, -0.0056188894, 0.02675597, -0.004990416, -0.039406963, -0.026334722, 0.016088912, -0.016958583, 0.0039950507, -0.018127203, -0.00205188, 0.025845533, 0.005523769, 0.032177825, -0.008030867, 0.013065447, 0.00030531903, 0.00048579273, -0.0008174397, -0.016646044, 0.0018854194, -0.013710906, -0.021007989, 0.011244574, -0.006260951, 0.027802292, -0.011495963, -0.023589823, 0.00018270308, 0.025261223, -0.015015412, -0.016034558, -0.04313024, 0.00020754476, 0.007432969, -0.01786902, 0.025274811, 0.011672614, -0.0011584288, 0.022176608, -0.014186507, -0.03973309, -0.0035126552, -0.00539128, 0.019744247, -0.017597247, -0.017216766, -0.0143631585, -0.010619497, 0.022027133, 0.024907919, 0.0030081782, 0.037042547, 0.012528697, -0.0269598, -0.024907919, 0.015042589, -0.021633064, 0.01941812, 0.012141421, 0.027204392, 0.004891899, -0.0137177, 0.027204392, -0.029623166, 0.005992576, 0.007888187, -0.0022489147, 0.027775114, 0.026715204, 0.010531171, -0.006260951, 0.01166582, 0.022394026, 0.039705914, 0.026130894, -0.011767735, -0.002783966, 0.028481722, -0.008655943, -0.0068724384, 0.016564513, 0.028970912, 0.019173525, 0.019159937, 0.002243819, -0.033563863, 0.004508021, 0.013676934, 0.011326104, -0.0072766994, -0.019295823, -0.009824564, 0.028780673, 0.023209343, -0.01551819, -0.009437288, -0.006726361, -0.009987627, 0.023671355, -0.052968394, 0.013867174, -0.014702874, -0.0012637406, 0.00907719, 0.013473105, -0.019214291, -0.023304462, 0.011726969, 0.01815438, 0.015463836, 0.017556481, -0.018276678, -0.02899809, 0.019676305, 0.00043653403, 0.017692368, -0.0018259692, 0.019404532, 0.037042547, -0.010028393, -0.031906053, -0.6318159, -0.030465659, 0.02978623, -0.00422266, 0.022040723, 0.022013545, 0.0077930666, 0.017678779, -0.0011949482, 0.012025918, -0.03016671, -0.014594165, -0.0047526155, -0.013221716, 0.0006514039, -0.017447773, 0.02069545, -0.028780673, 0.011033949, 0.024663324, -0.008465703, 0.017991317, -0.025274811, -0.012080273, 0.0258863, 0.0060707107, -0.02011114, -0.011971564, -0.027000565, 0.022230962, -0.009722649, 0.03296596, 0.014526222, 0.013541048, 0.048864633, -0.010143896, -0.018765869, 0.038537294, 0.0019227881, 0.028536078, -0.039189547, -0.03171581, 0.007487323, 0.005187451, 0.0012391112, -0.004871516, 0.051881306, 0.01332363, -0.005071948, 0.012617023, -0.00020329832, -0.008601589, -0.009382934, 0.009743032, 0.022815272, -0.011027155, 0.0056732437, -0.017053703, 0.0167004, 0.018901754, -0.013873969, 0.011516346, -0.005812527, -0.03905366, -0.035221674, 0.023467526, -0.017705956, -0.008554028, 0.019309413, -0.017420596, -0.0013028078, 0.017787488, -0.01815438, -0.010850503, 0.0048647216, 0.03720561, 0.01786902, 0.010517582, 0.007242728, -0.011095098, 0.0087782405, 0.013901146, -0.0031066956, -0.01215501, 0.013839997, 0.0033343048, -0.02225814, 0.0047696014, -0.004796779, -0.0055917124, -0.0012824249, -0.019445298, 0.00017898745, -0.008275462, -0.0040392135, 0.00059195375, -0.025709646, -0.0010463229, 0.021741772, -0.0030302596, -0.025723236, 0.028916558, 0.013731289, 0.0033767691, 0.008316228, -0.0053301314, -0.035629332, -0.016931405, 0.03331927, -0.0028077462, 0.014322393, -0.0126917595, -0.002680353, -0.032667015, -0.002303269, -0.029514456, 0.017393418, 0.008859772, 0.015531779, 0.008268668, -0.00427022, 0.00022591061, 0.011047538, 0.0016994253, 0.0036519384, 0.024921507, 0.017746722, 0.0042294543, -0.009729443, -0.0036485412, -0.0061726253, -0.0126781715, -0.0024340595, -0.009410111, 0.0031440642, -0.01000801, -0.0054456345, 0.00082465867, 0.025369931, -0.04715247, -0.01600738, -0.015993793, 0.0037504558, -0.030927671, -0.0011898525, 0.014553399, 0.0034073435, -0.0015193763, -0.012637406, 0.0062915254, 0.017230354, -0.004915679, -0.027992534, 0.01706729, -0.0057072155, -0.007888187, -0.022040723, -0.019567596, -0.0055033863, 0.00009872973, 0.013500283, 0.011101893, -0.024228489, -0.000120174256, -0.015654076, -0.018670747, 0.017012937, 0.016985761, 0.006947176, -0.037504558, -0.013425545, -0.014499045, -0.019377355, 0.030601546, 0.009539203, 0.013357602, -0.015232829, 0.008927716, -0.014186507, -0.012141421, -0.007575649, -0.01024581, -0.012712142, 0.003093107, 0.023589823, -0.0029979867, 0.014335982, 0.016822698, -0.009403317, 0.012080273, 0.0112989275, 0.0034701908, -0.0072291396, 0.0101778675, -0.0067637297, -0.008295845, -0.008255079, -0.006390043, 0.013636168, 0.0028756892, 0.014702874, -0.016931405, 0.0132353045, -0.014037032, 0.020138318, -0.034324825, 0.015953027, -0.014050621, 0.018643571, 0.03878189, 0.03171581, -0.010857298, -0.022095077, -0.008125988, 0.013310041, 0.017529305, -0.0014446389, 0.039108016, -0.025261223, -0.0013444229, -0.0077658896, -0.011115481, 0.0134799, -0.019241469, -0.021130286, 0.039026484, 0.015558956, 0.030601546, 0.014893115, -0.007854216, -0.0006390892, 0.027299514, 0.0014318996, 0.009539203, 0.019173525, -0.048348267, 0.0370969, -0.019880133, 0.032585483, 0.015667666, -0.0052655856, 0.028943736, 0.020124728, 0.0066754036, 0.015246418, 0.007011722, 0.010205044, 0.014037032, -0.011190219, 0.014499045, -0.034868367, 0.010035187, -0.03497708, -0.018860988, -0.0022726946, -0.037993748, -0.0013851888, 0.007392203, 0.023250109, 0.019078406, 0.011054332, 0.0058057327, -0.0018327635, -0.01689064, 0.01621121, 0.018032083, -0.013534253, -0.027245158, -0.018793045, -0.009749826, -0.014961057, 0.0028111434, -0.02888938, -0.017705956, 0.0015278691, -0.0069981334, -0.0033937548, 0.009043219, 0.0044740494, 0.01845333, -0.026701614, -0.0033105246, 0.016863463, -0.009185899, 0.0052214228, -0.0026718602, -0.0061964053, -0.031172266, -0.028101241, 0.0011261558, -0.0076707695, 0.01493388, -0.014648519, 0.0076707695, -0.016442215, 0.013608991, 0.012474342, -0.013676934, 0.009050013, 0.0005066003, 0.015925849, -0.016632456, -0.025995007, 0.00902963, 0.02470409, -0.0029877953, -0.013337219, 0.013853586, -0.013072241, -0.005163671, 0.009206282, -0.0066754036, -0.036662064, -0.024839975, 0.015029, -0.006434206, -0.01815438, -0.010483611, 0.01952683, -0.005411663, -0.031987585, -0.019594774, -0.016292742, 0.013079035, 0.0895761, 0.014879526, -0.0008628766, 0.018208735, 0.01406421, -0.0060605193, -0.028481722, -0.009016042, 0.006770524, 0.0018480507, -0.018765869, 0.002323652, -0.0068996157, 0.00888695, 0.011638643, -0.02020626, 0.0005983234, -0.00970906, 0.015069766, -0.003998448, 0.005432046, 0.03552062, -0.0134799, 0.028671963, 0.014648519, 0.03497708, 0.014118563, 0.03337362, 0.017991317, -0.019187115, 0.010789355, -0.0040731854, -0.0035262438, 0.003927108, -0.020342147, 0.027652817, 0.026524963, 0.02000243, -0.023983894, 0.00018461398, 0.0017478347, 0.025954241, 0.008037662, -0.014961057, -0.010286576, -0.040684294, -0.012277307, 0.010918447, 0.001232317, -0.010300165, 0.03103638, 0.010707824, -0.009117956, -0.019010462, 0.033536684, 0.00018408317, -0.00068749866, 0.013106213, 0.0074533517, -0.025261223, -0.006128462, -0.023290874, -0.003927108, -0.006909807, -0.033944342, -0.009185899, -0.015789963, -0.006991339, -0.0151920635, 0.013595402, 0.005095728, 0.0011516345, -0.020885691, 0.0020773585, 0.025546582, 0.0107417945, 0.019241469, 0.0025070983, 0.008920921, 0.012623817, 0.0004072336, -0.008017279, -0.011203808, -0.0093285795, -0.0030761212, 0.0024068821, 0.02888938, -0.009858536, -0.0071611963, 0.00085395906, 0.007528089, 0.021442823, -0.008594794, 0.0038387817, 0.04361943, -0.0018752279, 0.00683507, 0.01513771, -0.00082083687, -0.008880155, 0.010497199, 0.012793674, -0.013608991, 0.00025053998, 0.017991317, 0.008968482, -0.00034396164, -0.017447773, 0.0023066662, 0.01444469, 0.011754146, -0.0060401363, 0.0013265879, 0.01254908, -0.023562646, 0.026402665, -0.009430494, 0.019975254, -0.0053063515, -0.01619762, 0.010768972, -0.024146957, 0.0021486985, -0.0016798917, -0.00020648315, 0.019159937, -0.018956108, -0.016781932, 0.0026056156, 0.0013605594, -0.010470022, 0.021021577, -0.034814015, -0.01941812, -0.021999957, 0.016917817, -0.018711513, 0.0052893655, -0.0079357475, -0.0138060255, -0.033210557, -0.008227902, -0.0041920855, -0.027272336, -0.024812799, -0.02861761, -0.017692368, -0.0004777245, -0.006084299, 0.012555874, -0.007018516, -0.019119171, 0.0024323608, -0.004718644, 0.012134627, -0.04851133, -0.042994358, -0.0010981294, 0.016836286, 0.025342753, 0.029731875, -0.005156877, 0.016985761, 0.016374273, -0.0036994985, -0.01367014, -0.010646675, -0.0071544023, -0.020872101, -0.007263111, 0.0071204305, 0.011659026, -0.00629832, 0.011455197, -0.013941912, 0.029161153, -0.014240861, 0.0044570635, -0.004562375, -0.02342676, 0.04598385, -0.004154717, -0.026796736, 0.0075145, 0.026280368, -0.0061352565, -0.0040324195, 0.024269255, 0.02568247, -0.0031729399, 0.035004254, -0.023114223, 0.0121210385, -0.015599722, -0.010891269, -0.0101846615, 0.008255079, -0.018820222, -0.013969089, 0.015885083, 0.028454546, 0.011088304, 0.008458909, -0.0054218546, -0.0035602152, 0.0022862833, -0.01000801, -0.010945624, 0.020736216, -0.015545367, -0.038673177, -0.019024052, -0.014499045, -0.006570092, -0.005353912, 0.007528089, -0.012521902, 0.0031831313, -0.006610858, -0.011720175, 0.00003901417, -0.011271751, 0.025505817, 0.015015412, 0.02363059, 0.015450248, 0.0037708387, 0.008764653, -0.0049564447, -0.0027347074, -0.001999224, 0.011047538, 0.028318658, -0.013744877, -0.022475557, 0.004562375, 0.0039203134, -0.046146914, -0.025723236, 0.034732483, 0.01952683, 0.014539811, -0.013384779, 0.012365634, 0.0006416371, 0.009192693, -0.015980203, 0.013445928, -0.012386017, -0.0063119084, -0.023902362, 0.034243293, 0.016088912, 0.008914127, 0.017012937, 0.0031593514, -0.025356343, 0.0055917124, -0.016428627, -0.002167383, 0.008526851, 0.031688634, -0.025560172, 0.0067603327, 0.0090636015, 0.009267431, 0.003329209, -0.0029589194, 0.0041445256, 0.03242242, -0.003913519, -0.014648519, -0.010395285, -0.008995659, -0.007643592, -0.016564513, -0.010069159, 0.0090636015, -0.015110532, -0.008125988, 0.01425445, 0.015096944, -0.0031270785, -0.012053096, 0.0031151883, -0.021551533, -0.015694842, 0.0013656551, 0.005411663, -0.026715204, -0.013826408, -0.014988234, -0.03247677, 0.015667666, 0.006454589, -0.012936355, 0.0020247025, 0.0149202915, -0.0067875097, -0.0066957865, 0.0058227186, 0.0029011678, -0.021320526, 0.012650994, -0.01963554, -0.03712408, 0.014648519, 0.006502149, -0.027068507, -0.026334722, 0.018752279, 0.015042589, -0.007847421, 0.0019924296, 0.030248241, -0.011672614, 0.006685595, 0.0146213425, -0.039108016, -0.0056494637, 0.011468785, 0.019336589, 0.010816532, -0.029949293, 0.013201333, 0.011584288, 0.022489147, -0.015029, -0.025913475, -0.02050521, -0.0034922722, 0.006254157, -0.0055985064, 0.0045895525, -0.026226014, -0.015083355, -0.025247633, -0.0035432295, 0.0069369846, 0.00047220412, 0.01600738, 0.045168534, 0.018398976, 0.033210557, -0.0031474615, 0.004215866, -0.02840019, -0.014091386, -0.015395893, -0.0057106125, -0.010646675, 0.054218546, -0.0018633379, -0.021402057, -0.03796657, -0.0029181535, -0.02918833, -0.010306959, -0.012236541, 0.03329209, 0.028780673, -0.0077387122, 0.0003862137, 0.026633672, -0.019880133, 0.0047899843, -0.02566888, -0.012576257, 0.018317444, -0.0013614086, 0.026008597, 0.013316836, -0.032585483, -0.018575627, 0.03668924, -0.012848029, 0.012800469, 0.051038813, -0.005163671, -0.01737983, 0.026891856, 0.0063322913, 0.0035466268, -0.0020128125, 0.017053703, -0.012032713, 0.0073242597, 0.0035398323, 0.013194539, -0.0018072849, -0.0030965041, 0.023888772, 0.004868119, 0.03386281, -0.017026525, 0.005697024, -0.012807263, 0.02391595, 0.025016628, -0.0087714465, 0.008323022, 0.026565729, 0.009165516, -0.02801971, -0.024676912, 0.031226622, -0.01640145, -0.011149453, 0.021116696, -0.008533645, 0.0016094007, -0.022611443, 0.0051704654, 0.0019465681, -0.0073174653, -0.011115481, -0.008649149, -0.025859121, 0.021823304, 0.027639229, -0.015694842, -0.0021419043, 0.0026429843, 0.00795613, 0.015953027, -0.018276678, 0.011258162, -0.016863463, 0.010164279, 0.00021210968, -0.014961057, -0.024364375, -0.0061726253, -0.0014132152, -0.042912826, -0.033129025, 0.22524476, -0.00485453, 0.015110532, 0.05457185, 0.003385262, -0.0055101807, -0.00005711462, 0.0028637992, -0.014689285, 0.014566988, 0.009362551, 0.0018140791, 0.0033139219, -0.003910122, 0.01117663, -0.035873927, -0.047777545, -0.029731875, 0.0023542263, 0.006260951, -0.0062269797, -0.0055373576, -0.010239016, -0.0048409416, -0.0013079036, 0.027462577, 0.0031627484, -0.009525614, 0.028101241, 0.018697925, -0.01786902, -0.0044129007, -0.004888502, -0.021714596, -0.025519406, 0.008384171, 0.022720153, 0.009376139, 0.030628722, 0.013303247, 0.0016569609, 0.010646675, -0.010959213, 0.00093846326, -0.030492837, -0.008785035, -0.004423092, -0.00874427, -0.00693019, 0.013982678, -0.029242685, -0.004029022, 0.02713645, 0.022108665, 0.015300773, -0.0124063995, 0.008649149, 0.0020450854, -0.030873317, -0.0022421204, -0.008785035, 0.035194494, -0.028970912, 0.049544066, 0.000033228393, -0.0060231504, 0.005564535, -0.01425445, 0.021633064, -0.0048375446, 0.004358546, -0.014580577, 0.0048171617, -0.018643571, 0.0002471428, -0.009219871, 0.02840019, 0.02812842, 0.02235326, 0.020056786, -0.00898207, 0.0067535383, 0.00052358606, 0.00483075, 0.0073106713, -0.033726927, 0.018100025, 0.003341099, 0.012236541, -0.029541634, -0.0151920635, -0.0143631585, -0.006970956, -0.023780065, -0.0065565035, 0.0024085809, 0.0002817513, 0.026497785, 0.009512026, -0.014662108, -0.008662738, -0.014716462, 0.006301717, 0.02978623, -0.005601904, -0.017936964, -0.019975254, 0.0071136365, 0.0032391844, -0.00076648244, 0.0035907896, -0.036770772, -0.0029657136, -0.007990101, -0.004202277, 0.035085786, -0.023725709, -0.007127225, 0.030465659, -0.030818963, -0.0007507706, -0.026919033, -0.0028468133, 0.0057343924, -0.015885083, -0.010748589, 0.0077455067, 0.006352674, 0.0039237104, -0.036281582, 0.036662064, 0.013364396, 0.015803551, -0.006186214, 0.0024663324, -0.014335982, -0.011101893, -0.015300773, 0.0053471173, -0.002872292, -0.016374273, 0.0068996157, 0.013982678, -0.0053437203, 0.0050821393, -0.03152557, 0.0052655856, 0.009980832, -0.008200725, 0.0022506132, -0.005279174, -0.0090568075, -0.02431002, -0.021592299, 0.024839975, 0.0037470586, -0.027054919, -0.025913475, 0.02429643, -0.007711535, -0.028563254, 0.0044162977, 0.03239524, -0.02214943, -0.024133367, -0.0038319875, -0.17349935, 0.044652168, 0.02020626, -0.0306559, 0.009450877, -0.0076096207, 0.006430809, -0.005792144, -0.0026412858, 0.0026259986, 0.017719544, 0.019105583, -0.00039916535, -0.021918425, 0.017678779, -0.012168598, -0.013996267, 0.0064002345, 0.040140748, 0.02734028, 0.030003646, -0.0028145404, 0.0026412858, 0.016754754, 0.018466918, 0.0040935683, 0.013873969, -0.015219241, 0.013038269, 0.0023848007, 0.011957975, -0.018086437, -0.00096139405, -0.001660358, 0.0084928805, 0.0038591647, -0.00060256984, 0.0030506426, 0.011679409, 0.015749197, 0.0035228466, -0.0107417945, -0.0034124393, 0.011237779, 0.014186507, -0.0014854047, 0.018385386, 0.0005983234, -0.018195147, -0.023752887, 0.01583073, -0.008404554, 0.013357602, 0.0025767398, 0.008064839, 0.015708432, 0.009036425, 0.008044456, -0.0057140095, 0.0067603327, 0.006301717, -0.023929538, -0.0026412858, -0.0039203134, -0.004579361, -0.009838153, -0.0074601457, 0.009165516, -0.020287791, 0.010558348, 0.014730051, 0.029731875, 0.0203965, 0.009756621, -0.016034558, -0.006933587, -0.024962272, -0.0015652378, 0.03054719, 0.0024119779, -0.021809716, -0.000038377202, -0.030818963, 0.0069369846, 0.002243819, 0.0046608928, 0.009593558, 0.0021368086, -0.016020969, -0.01019825, 0.0015796757, 0.0066923895, 0.020437267, -0.017216766, 0.010082747, 0.022692975, -0.008132782, 0.0107282065, -0.004450269, -0.025016628, 0.002167383, -0.011428019, -0.017040115, 0.028074063, 0.03475966, 0.0024102794, 0.004372135, 0.033455152, 0.013140184, 0.00085395906, -0.03212347, 0.018983286, 0.02342676, 0.011095098, -0.016279152, 0.031579927, -0.01332363, -0.025560172, 0.030927671, -0.006658418, 0.026334722, -0.017339064, -0.032340888, -0.007439763, -0.00022527364, -0.00024841673, -0.10251246, 0.011441608, -0.0063662627, 0.019404532, -0.034732483, -0.009247048, 0.01483876, 0.039434142, 0.0011550317, 0.011645437, -0.012161804, -0.028101241, -0.009226665, 0.00075926346, -0.0015643885, -0.0057106125, 0.008424937, -0.008588, 0.010836915, 0.008554028, -0.023983894, -0.0050889337, -0.019159937, -0.00022527364, -0.01648298, -0.02840019, -0.014702874, 0.016374273, 0.027014153, 0.010408874, 0.025995007, -0.008547234, 0.007378614, -0.030356951, 0.0028077462, 0.024568204, 0.007779478, -0.025614526, 0.0030982026, -0.029161153, 0.0055951094, -0.008132782, 0.0085064685, -0.038482938, -0.012358839, 0.0072970823, -0.04394556, 0.014757228, 0.017176, -0.01757007, -0.022774506, -0.010510788, -0.03524885, -0.023562646, 0.0382927, 0.011244574, -0.01322851, -0.0060367393, -0.031770166, 0.002371212, -0.0036145698, 0.004426489, -0.005584918, 0.017447773, 0.019662715, 0.016347095, -0.016618868, 0.0004624373, 0.014335982, 0.005156877, -0.0060605193, 0.011095098, -0.010809738, 0.020029608, -0.014716462, -0.0258863, -0.014037032, -0.008139576, -0.006294923, -0.01532795, 0.0025003038, -0.011625054, -0.012569463, -0.032368064, -0.010503994, -0.007568855, 0.0040799794, 0.008730681, 0.0072495225, -0.06576886, 0.011400842, 0.0007363327, -0.0009393125, 0.0076775635, -0.0044400776, 0.0051296996, 0.009104367, 0.013466311, 0.027557697, -0.0059416187, -0.032205, -0.019594774, -0.05038656, 0.019445298, 0.015993793, -0.031688634, -0.0035432295, -0.022285318, -0.0010132006, 0.004310986, 0.019445298, 0.024921507, -0.019078406, 0.023657767, 0.009756621, -0.019350179, -0.010014804, -0.048484154, 0.019309413, -0.0019075009, 0.039298255, 0.025696058, -0.00035351614, 0.008839389, 0.031226622, 0.018480508, -0.03448789, 0.012630612, -0.04764166, 0.03239524, -0.0118492665, 0.0065191346, 0.022720153, -0.02107593, 0.0059076473, 0.023127811, -0.01619762, -0.011312516, -0.009552792, 0.013527459, 0.007820244, 0.0038183988, -0.013167361, -0.019798601, 0.0064274115, -0.0015270198, -0.033047494, -0.0012093862, -0.025152514, -0.0024119779, 0.032368064, 0.0024850166, 0.03231371, 0.01619762, -0.00573779, -0.028345836, -0.008791829, -0.0034718893, 0.044624988, 0.0043891203, -0.018616393, -0.02274733, 0.029568812, 0.006294923, 0.022326084, -0.009342168, -0.0036451442, -0.014594165, -0.019119171, -0.0033546877, -0.0067875097, -0.012922767, 0.0016272358, 0.007011722, 0.013534253, 0.021238994, 0.00520104, -0.0013325328, -0.022543501, -0.03130815, -0.04402709, 0.030058, 0.00781345, -0.008295845, -0.0093285795, 0.017243944, 0.0016824396, -0.009579969, 0.003084614, 0.012909178, -0.002155493, 0.0014072702, -0.02011114, -0.012562668, 0.028454546, -0.007303877, 0.0012824249, 0.030982027, 0.012494725, -0.030085178, 0.025736824, -0.0026786544, 0.0047526155, 0.003485478, 0.011108687, -0.008873361, -0.008085222, -0.005741187, -0.011679409, -0.05291404, 0.009668294, 0.002559754, 0.01444469, -0.018983286, 0.005697024, 0.010966007, -0.018820222, 0.02129335, -0.007222345, 0.006240568, -0.0109999785, 0.03367257, 0.0011066223, 0.01600738, 0.03720561, -0.014159329, 0.0046574953, -0.005099125, 0.024323609, -0.0057717613, 0.027707173, 0.02080416, 0.00419888, 0.0038251933, -0.01845333, 0.0028247319, -0.004742424, -0.014974646, 0.008424937, 0.03171581, -0.03133533, 0.07702023, 0.033455152, 0.0038082073, -0.002872292, 0.014376747, 0.030982027, 0.016360683, -0.0042838086, 0.023929538, -0.001698576, -0.01024581, -0.011964769, -0.019798601, -0.015586133, -0.031090735, 0.0016722481, -0.016741166, 0.012304485, -0.012583051, -0.015654076, 0.027476165, 0.0006514039, 0.016659634, 0.011047538, -0.010748589, 0.004331369, 0.021361291, -0.02118464, -0.02187766, -0.02186407, 0.009688677, 0.013432339, -0.04098324, -0.012304485, -0.01973066, -0.005313146, -0.015260007, 0.015708432, 0.0055339606, 0.0146349305, 0.009634323, 0.033563863, -0.020736216, -0.005469415, 0.009593558, -0.035004254, -0.009552792, -0.008560823, -0.02460897]
```

## Back to TikTok videos...

So getting back to TikTok videos I actaully skipped a step I should tell you about. I also built a classifier using GPT-3.5-turbo to roughly classify my video transcript text that looks something like this:

```
You are going to classify transcribed audio from TikTok data. I will pass you transcribed text that has been taken directly from tiktok videos and you will classify by categorizing using the rules defined below.
You will be passed text but you must always respond in JSON format using the following format (defined as a typescript type): {"classification":  string, "mentionedCompany": boolean, "potentialProductNames": Array<string>, "sentiment": 'POSITIVE' | 'NEUTRAL' | 'NEGATIVE', "summary": string, "topics": Array<string>}
where "classification" will be the code defined in the rules below. If the company name "${storeName}" was mentioned, you can flag "mentionedCompany" as true, otherwise default is false.
If you think you recognized specific nouns as product names this company might sell, you can include them as an array of strings in the "potentialProductNames" value.
Next, if you can detect specific positive or negative sentiments set the "sentiment" value to either "POSITIVE" or "NEGATIVE" accordingly, otherwise default to NEUTRAL.
Next, for each unique topic you detect (basically any noun that seem to be a focus) you can include it in the "topics" array, this must be limited to 10 at most.
Finally, in a condensed sentence or two, summarize the content into the "summary" field.

Rules to classify codes:
  1. If the text is not english, empty, or unrecognizable use code "NON_ENGLISH"
  3. If the text appears to be primarily repetitive words like song lyrics and makes no logical sense, use code "SONG_LYRICS"
  4. If it's very short like a single sentence and it does not seem to be descriptive of a product or an experience use code "SHORT_HOOK"
  5. If the text is description of a product or an experience use code "RECOGNIZED_DESCRIPTION"
  6. If the text is clearly specific product feedback that sounds like a review, as a complaint, a positive review or primarily some mixture of these use code "PRODUCT_FEEDBACK".
  7. If you can't classify into the above categories, use code "UNKNOWN"

Transcription: "${transcription}"
JSON Response:
```

This calssifier works quite well for my purposes here, and I can use the results to know if I should bother making vectors or not (I ignore the SONG_LYRICS & SHORT_HOOK videos), and I can also tag the videos in the dashboard of the brand showing postive and negative sentiment (and much more, but those are just examples).

The output for the above transcript from that classifier looks like this:

```
{
    "classification":"RECOGNIZED_DESCRIPTION",
    "sentiment":"POSITIVE",
    "mentionedCompany":true,
    "summary":"The speaker talks about their subscription to Bokksu, a company that delivers Japanese snacks. They describe the variety of snacks and the quality of the curation, as well as the cultural themes and support for small businesses. They express excitement for their next box and recommend the service.",

   "topics":[
      "subscription",
      "Bokksu",
      "Japanese snacks",
      "cultural themes",
      "small businesses",
      "quality curation",
      "variety of snacks"
   ],

   "potentialProductNames":[
      "Bokksu",
      "Japanese snacks",
      "white strawberry",
      "organic matcha tea",
      "vegetable apare tomato",
      "20th century pear biscuit",
      "handmade yuzu sake candy",
      "don don yaki",
      "seaweed tempura",
      "zawawa sabu",
      "sesame seed mochi",
      "matcha stick chocolate cake",
      "kinako azuki crunch",
      "soka senbei umazarabe"
   ]
}

```

## What else can you do with the vectors?

So going back to the vectors, I have classified the transcripts and I know which ones contain "PRODUCT_FEEDBACK" or "RECOGNIZED_DESCRIPTION" which are both useful to my analysis.

I can do now do what people are calling ["generative questioning and answering"](https://docs.pinecone.io/docs/examples) with my dataset. Meaning that I can ask a question, convert that to a vector and then semantically search for documents related to my question, and then feed the entire context into GPT to get some kind of analysis about my question from the relevant documents.

I will explain - the process looks like this in full:

1. Transcribe all videos
2. Classify all videos
3. Make vectors of all useful videos (e.g. not just song lyrics)
4. Insert the vectors to Pinecone
5. Ask a question in english
6. Make a vector of my question
7. Search the DB for similar vectors (e.g. top 10)
8. Write a promp to GPT to ask it to answer my question using the given context.

The prompt to GPT by the way looks like this:

```typescript
const promptParts: string[] = [];
promptParts.push("Answer the question based on the context below.");
for (const match of queryResponse.matches) {
  promptParts.push("Context: " + match.metadata?.text);
}
promptParts.push("Question: " + query);
promptParts.push("Answer:");
const prompt = promptParts.join("\n");
console.log("Prompt: ", prompt);
const gptResult = await callCompletion(prompt);

console.log("GPT result: ", gptResult);
```

## Example Generative Q & A

I built a little dashboard in Retool to make a rudimentary interface into our transcript data to run these kinds of tests.

Here is an example asking questions about Gfuel video transcript data:

![asking a question](/images/blog/saymore/asking-question-1.png)

![question response](/images/blog/saymore/question-response-1.png)

![transcript data](/images/blog/saymore/transcript-data-1.png)

## Product insights - from TikTok videos?

Something you might realize quite quickly here is that you can probably glean some product insights rather quickly doing this.

However, this is not the exactly right application of this...

Yes, these videos are about the companies, but the videos are not objective and they are not representative of a wide audience. These users are beign compensated & they are
likely big fans of the brand to begin with.

This was when we started to think about building a generalized product feedback tool.

## Saymore.ai - general product feedback.

[Saymore](https://saymore.ai) is meant to be a generalized product feedback tool, but it works like this:

1. A user is asked one single question
2. A user makes an audio recording
3. The same pipeline above is run and you can now semantically mine these feedback sessions for data.

Here it is in pictures:

![asking a question](/images/blog/saymore/saymore-question-1.png)

![recording response](/images/blog/saymore/saymore-recording-1.png)

![asking for insights](/images/blog/saymore/saymore-responses-1.png)

## Surfacing Trends

One of the very frustrating things observing users attempting to interact with generative to Q&A is that they will try to ask questions like:

1. What is the biggest complaint?
2. What the is the most important feature to work on?
3. What is the most frequently mentioned issue?

Now, these are perfectly reasonable questions to ask, however they are in fact to a large degree **quantitative** questions and not **qualitative** questions.

The problem here is that if you feed only a few relevant responses (snippets of text) into a system of this type you are not going to be able to answer a quantitive question in this manner, its just not the correct approach.

What you really want to do is surface trends like so:

![feedback trends](/images/blog/saymore/saymore-feedback-trend-mockup.png)

## Using unsupervised learning (clustering)

I will outline a process I have been doing to handle trying to surface trends in a more quantitive manner, which does help with the generative Q&A problem but it's just a start.

1. Pull out every vector withing a time range / filter range
2. Do PCA to reduce dimensionality on the vectors (I was trying like n=10)
3. Run K-means (pick a number of clusters like n / 4 but vary based on your data)
4. Do avg silhouette score of each cluster and rank by this (filter out low n clusters)
5. Take the text of each cluster and feed it into GPT for classification, and ask it to "summarize"
6. Display each summarized result with ranking of silhouette score descending

This gives you something pretty close to a "trending" result.

The iffy parts are the following: reducing dimensionality loses a lot of data, and picking the number of clusters for the data is very data dependent.

Fortunatly, I did some experiments with different clustering algorithms and I found that some density based algorithsm like [OPTICS](https://en.wikipedia.org/wiki/OPTICS_algorithm) yielded some better results.

Experimentally, they seem to be superior for this task because of the following reasons:

- the algorithm chooses the number clusters based on your tuning of the sensitivity
- they seem to tolerate high-dimensional data better so you dont need to do PCA.

Doing PCA on high dimensional semantic vectors means you are tossing the majority of the data out, and given that semantic vectors store many complex relationships in the high dimensional space, I don't know how well this will work in production (although the K-Means version did reasonably well in my limited testing).

## Looking at results of clustering

What I'll do next is show you some results at various points of the steps above.

### A K-Means cluster (using PCA & silhouette score)

First, I will show you a clustering of results at step 4 and show you that it appears that generally related results have been clustered together. We could call this cluster "suggestions or improvements around compensation".

![cluster of feedback improvements](/images/blog/saymore/saymore-pca-kmeans-cluster-improvements.png)

I think I should show you another one, which grouped all of the feedback about Blendjet together on here. Where did this data come from? We collected it as an experiment inside of the Bounty creators app. Many of our users were confused and thought we were asking about the e-com brand (who is **our** customer) but thats a whole other conversation.

The relevant parameters btw are:

```python
# 9 gives good results vs perf with a few hundred results.
pca = PCA(n_components=9)
embeddings = pca.fit_transform(embeddings)

# Decide on the number of clusters (you may need to adjust this)
num_clusters = math.floor(len(rows) / 5)

# Perform k-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(embeddings)

```

![cluster of blendjet people that are happy](/images/blog/saymore/pca-kmeans-blendjet-cluster.png)

### Some results using OPTICS

Next, I want to show you optics which does give interesting results.

I think you will see from the below screenshot that the clusters are quite good, and you can see 111 unclustered documents (which is high but you can tune the tolerance here). The algorithm choses the number of clusters based on the parameters:

```python
# Apply OPTICS
optics = OPTICS(min_samples=3, xi=0.0001, min_cluster_size=0.0001)
optics.fit(embeddings)
```

The clusters could be explained as followes:

1. complaints about returning products (Again, not our customers but 🤷)
2. people explainging why they didnt post
3. delivery issues (again we are running a platform so not much we can do 😢)
4. feedback about Bounty itself
5. people talking about running out of time to upload videos

![optics clusters of feedbacks](/images/blog/saymore/optics-clusters-feedback.png)

## What else can you do with the semantic vectors of product feedback?

[Saymore](https://saymore.ai), as a product is still in development. We are building an internal version now to dogfood and help us to improve Bounty, but I am so interested in applying this technology to different software applications.

If you want some help with some of these machine learning / AI applications feel free to reach out! My contact info / LinkedIn is on the footer of this page or you can use the form on the front page.
