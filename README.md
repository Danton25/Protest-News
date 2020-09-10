### Protest News
The goal of this project is to gain hands-on experience in developing practical solutions to
societal problems based on web/text/social media mining. The specific event classes of
interest are: global social unrest events, such as demonstrations, marches, and protests
from 2019; and the countries to be focused on are:India and South Africa. This project
seeks innovative solutions and approaches for discovering and combining multiple data
sources.
#Benchmark Dataset:
Your system should be evaluated against the benchmark dataset. The Armed Conflict
Location & Event Data Project (ACLED) is a disaggregated conflict analysis and crisis
mapping project. ACLED is the highest quality, most widely used, real-time data and
analysis source on political violence and protest in the developing world. Practitioners,
researchers and governments depend on ACLED for the latest reliable information on current
conflict and disorder patterns. Refer to https://www.acleddata.com for more information and
access to the data.
The project involves three major tasks:
#Task 1: Data collection
As a first step, you are required to collect data on protests, marches and demonstrations that
happened in 2019 in India and South Africa. For this task, you can make use of ACLED
entries to find the related news articles for each event. Some of the libraries that you can use
to scrape news articles are news-please, spacy, scrapy, newspaper. Please note that all the
data should be in JSON format. Each group will be assigned a time span for data collection
(say Jan-Mar, 2019 for group 1), hence all the groups are required to meet the instructors
before starting the project (date and time to meet will be posted on Piazza).
#Task 2: Event extraction and summarization
Your system should give detailed information about the events so that your users could
understand the events by reading the summary. The following information should be
provided for each event: event date, location, event type, parties involved, data sources, and a
brief description. Daily based summarization should be generated on a timely manner, i.e. the
delay of your system should be at most 24 hours.
#Task 3: Live Demonstration of the end-to-end system
You are required to build a website to demonstrate your end-to-end system in the class. Your
website must contain multiple dashboards showing insights into your data and visualizing
events in both countries. The website should also show all the information related to the
event: event date, location, event type, parties involved, data sources, and a brief description.
Students are encouraged to make use of online tools and technologies to come up with
detailed and insightful visualizations.
