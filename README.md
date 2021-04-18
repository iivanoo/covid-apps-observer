# COVID Android apps observer
Web scraper and analyzer of COVID-related Android apps

![GitHub release (latest by date)](https://img.shields.io/github/v/release/iivanoo/covid-apps-observer)
[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)
![GitHub last commit](https://img.shields.io/github/last-commit/iivanoo/covid-apps-observer)

# What is it about?
Several mobile apps are being developed and released to the public in order to ease the tracking of COVID-19 and to inform people about key facts and procedures related to this virus.   

With this project we aim at providing useful insights about COVID-related mobile apps available to the public, ranging from the privacy-related permissions they request, contacted servers, users' perceptions, security-related issues, and so on. In order to extract those insights, we setup a dedicated analysis tool and we are running it **weekly** and on a **nation-by-nation** basis.

The slide deck below gives an overview about the project, including its goal, motivation, target audience, and the collected data. 

<p align="center">
<a href="https://docs.google.com/presentation/d/1O6vBbqjbI7X6ApTSspc9D-YpG_3xwugGgwXJ9SN0nIk" target="_blank"><img src="./slide_deck_cover.png" alt="Slide deck about the project" width="400"/></a>
</p>

The inspection of each mobile app is structured around five main dimensions:

:card_index_dividers: App and developer's information

:key: User permissions requested by the app

:globe_with_meridians: External servers mentioned in the code of the app

:closed_lock_with_key: Security issues in the code of the app

:speaking_head: User ratings and reviews

<p align="center">
<img src="https://media.giphy.com/media/lOxJZCPqVvVTVH5q2d/giphy.gif" alt="Report preview" width="600"/>
</p>

As you can imagine, we collect several data points for each dimension so the best way to get an idea about the information we provide is to directly look at one of our reports (see the table below).  

# Latest analyses

| **Nation** | **Report** | **Analysed apps** | **Updated at** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
:rainbow: By the community | :chart_with_upwards_trend: [Results](data/data_community/reports/report_2021_4_18.md) | 2 apps ([suggest new apps!](https://github.com/iivanoo/covid-apps-observer/issues/new)!) | :calendar: 18/04/2021
:australia: Australia | :chart_with_upwards_trend: [Results](data/data_au/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=au) (Links to Google Play) | :calendar: 18/04/2021
:austria: Austria | :chart_with_upwards_trend: [Results](data/data_at/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=at) (Links to Google Play) | :calendar: 18/04/2021
:canada: Canada | :chart_with_upwards_trend: [Results](data/data_ca/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=ca) (Links to Google Play) | :calendar: 18/04/2021
:cn: China | :chart_with_upwards_trend: [Results](data/data_cn/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=cn) (Links to Google Play) | :calendar: 18/04/2021
:denmark: Denmark | [:chart_with_upwards_trend: Results](data/data_dk/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=dk) (Links to Google Play) | :calendar: 18/04/2021
:fr: France | :chart_with_upwards_trend: [Results](data/data_fr/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=fr) (Links to Google Play) | :calendar: 18/04/2021
:de: Germany | :chart_with_upwards_trend: [Results](data/data_de/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=de) (Links to Google Play) | :calendar: 18/04/2021
:greece: Greece | :chart_with_upwards_trend: [Results](data/data_gr/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=gr) (Links to Google Play) | :calendar: 18/04/2021
:iceland: Iceland | [:chart_with_upwards_trend: Results](data/data_ic/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=ic) (Links to Google Play) | :calendar: 18/04/2021
:it: Italy | [:chart_with_upwards_trend: Results](data/data_it/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=it) (Links to Google Play) | :calendar: 18/04/2021
:jp: Japan | [:chart_with_upwards_trend: Results](data/data_jp/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=jp) (Links to Google Play) | :calendar: 18/04/2021
:netherlands: The Netherlands | [:chart_with_upwards_trend: Results](data/data_nl/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=nl) (Links to Google Play) | :calendar: 18/04/2021
:netherlands: The Netherlands (custom) | [:chart_with_upwards_trend: Results](data/data_nl_custom/reports/report_2020_10_7.md) | 9 apps | :calendar: 07/10/2020
:norway: Norway | [:chart_with_upwards_trend: Results](data/data_no/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=no) (Links to Google Play) | :calendar: 18/04/2021
:portugal: Portugal | [:chart_with_upwards_trend: Results](data/data_pt/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=pt) (Links to Google Play) | :calendar: 18/04/2021
:ru: Russia | [:chart_with_upwards_trend: Results](data/data_ru/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=ru) (Links to Google Play) | :calendar: 18/04/2021
:es: Spain | :chart_with_upwards_trend: [Results](data/data_es/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=es) (Links to Google Play) | :calendar: 18/04/2021
:sweden: Sweden | [:chart_with_upwards_trend: Results](data/data_se/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=se) (Links to Google Play) | :calendar: 18/04/2021
:uk: United Kindom | [:chart_with_upwards_trend: Results](data/data_uk/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=uk) (Links to Google Play) | :calendar: 18/04/2021
:us: United States | [:chart_with_upwards_trend: Results](data/data_us/reports/report_2021_4_18.md) | [Apps](https://play.google.com/store/search?q=covid&c=apps&gl=us) (Links to Google Play) | :calendar: 18/04/2021


> Do you want your nation listed here? You can [create an issue](https://github.com/iivanoo/covid-apps-observer/issues/new) in this repository and we will take care of it!

For transparency, the complete reports and raw data of _all_ the previous inspections are available in this GitHub repository and grouped by nation. For example, the ``data-it`` folder contains all the reports and raw data of our inspections in the previous weeks.

# Is this project for you?

This project is aimed at helping several actors:

:white_check_mark: **Citizens** can use our reports to easily compare COVID-related apps and identify which one fits their needs in terms of usability, trustworthiness, and privacy.

:white_check_mark: **Content creators and press** can use our reports as the basis for articles, blog posts, statistical analyses, further investigations, etc.

:white_check_mark: **Decision makers** can use our report to estimate the current landscape about COVID-related apps in their country, for example in terms of app's quality, provided services, etc.

:white_check_mark: **App developers** can use our report to assess how their own app compares against other COVID-related apps (both within their own nation and worldwide), whether some security-oriented improvements can be done in their own app, and how users perceive it (for example by using our analysis of app reviews in the Google Play store).

:white_check_mark: **Project contributors** can help in improving this project by:
  - running the analysis tool for countries which are not covered yet
  - implementing additional analyses
    * for example: detection of used 3rd-party libraries, deeper URL detection, detection of usability antipatterns, etc.
  - fixing bugs or improving the current analysis tool

## Contributions :rainbow:

Any feedback, questions, and improvements about the project are very welcome, feel free to create an issue or pull request directly in this GitHub repository. 

For independent verification, the raw data and the source code of the project is publicly available in this repository and its source code has been thoroughly commented in order to provide all the details about how the information provided in our reports has been extracted. 

Installation and usage guide of the analysis tool are available [here](code/).

## License

This software is licensed under the MIT License.
