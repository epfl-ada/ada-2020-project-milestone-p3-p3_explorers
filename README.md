# Team Explorers: ADA-P3

## Title: Long term chilling effect and other external factors

## Abstract
Though the results in the original article suggested a long-term chilling effect, this possibility can not be confirmed or denied with the used data. Additional research using more data could be an interesting extension to this study. We will try to investigate the long-term effects of the 2013 Snowden’s revelations, and more broadly, try to establish a bigger picture of the number of views’ evolution of “sensitive” wikipedia articles, and analyse it.
For that, we will be using the same list of wikipedia’s terrorism related articles of the study, and look at the views on a wider time range, from 2008 to 2018. The study’s dataset will be obtained with a web-scraping script.
We will consider other factors, like the evolution of internet traffic, that grows exponentially. We will also pay attention to events such as new privacy-related scandals, terrors attack or war, and outline them with the views’ evolution.

## Research Questions
1. Is there a persistent, long-term chilling effect related to Snowden’s revelation?
2. Can we highlight new chilling effects due to other scandals?
3. What may be the other factors governing the traffic and how are they affecting the article views?

## Proposed dataset
The data will be the Wikipedia traffic of the same articles used in the paper, for a longer time period. We will scrape the website [wikipediaviews](https://wikipediaviews.org), because it is one of the few providing per-article data for the period before 2015. 

For instance, we can get the pageviews for the Hamas article in June 2013 and July 2013 using [this link](https://wikipediaviews.org/displayviewsformultiplemonths.php?page=Hamas&months[0]=201306&months[1]=201307&language=en&drilldown=desktop).

The result is given in an HTML table, so we can process it with a python script and store it in a CSV file.
Note that the data of this website comes from stats.grok.se for the period before 2015, and from the Wikimedia REST API for the period after 2015. The main difference is that the Wikimedia API filters pageviews from bots. 

We can also use a data source like [Internet World Stats](https://www.internetworldstats.com/emarketing.htm) to find the number of internet users in the world to further understand the evolution of traffic. Even though it is hard to find precise values for each month from the given dataset, it will be enough to estimate an average value for each year, just to see the trend. 

## Methods
**Data Collection:** We will write an automated python script that will make a request for each article and write it into a CSV file. Then we can load the CSV file into a dataframe.

**Sanity check and pre process data:** First we will plot/ analyse the raw data and try to validate them. Then the data will be split into two time-series, one for the period before June 2013 and one for the period after. It is important to understand that there are spikes in page view count when there is an incident (eg. terror attack) happens related to the subject of the article (eg. terror attack by Hamas). We need to identify such spikes and exclude such anomalies from the dataset, preventing wrong conclusions derived from the experiment. 

**Data Analysis:** In this we are interested in answering the given research questions. Therefore we will try to plot the data and analyse the effect of Snowden revelation to the selected Wikipedia articles visit count. We will try to model the patterns before and after the event. Further we will also try to map other major scandals similar to Snowden revelation because we will be considering a broader time range. On top of all this we will try to understand other factors like overall increase of internet users which may be affecting the page view count.


## Proposed timeline
**Week 1:** Collecting the data and do the pre-processing

**Week 2:** Answer the research questions

**Week 3:** Agree on final deliverable, prepare the presentation materials including the video

## Organization within the team
- In week1,  Florian will write a script to download the data and share them with others while Carl can further research on incidents other than Snowden revelations which might cause a Chilling effect. Further Wenuka will work on downloading and pre-process other data that might affect the page views such as internet-users data evolution over the time.
- In week2 (or early if possible) Carl will work on the research question 1 by dividing the dataset and plotting the trend while Florian addresses the research question 2 and Wenuka will address the research question 3.
- In the beginning of week3, we will set up a meeting and with the experience so far, and will come up with the best way to visualize our results in the notebook. Further, we will decide what is the best way to present it, and will dedicate the week3 for the presentation (data story or report) in which Wenuka and Florian will take the responsibility. Carl will work on the video.


## Questions for TAs (optional)
1. Do we need to validate the datasource we are using? For example, for internet usage, even the [World Bank dataset](https://databank.worldbank.org/reports.aspx?source=2&series=IT.NET.USER.ZS) was not complete. But we found a more complete dataset in [Internet World Stats](https://www.internetworldstats.com/emarketing.htm ). In this case do we need to validate each datapoint?


## Contributions
- Florian: scraping of Wikipedia pageviews, research question 2, interactive plots, data story.


## Data Story
Available [here](https://wenuka.github.io/chillingeffect/)

