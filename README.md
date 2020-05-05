# COVID Android apps observers
Web scraper and analyzer of COVID-related Android apps

![GitHub All Releases](https://img.shields.io/github/downloads/iivanoo/covid-apps-observer/total)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/iivanoo/covid-apps-observer)
[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)
![GitHub last commit](https://img.shields.io/github/last-commit/iivanoo/covid-apps-observer)

# What is it about?
Several mobile apps are being developed and released to the public in order to ease the tracking of COVID-19 and to inform people about key facts and procedures related to this virus.   

With this project we aim at providing useful insights about COVID-related mobile apps available to the public, ranging from the privacy-related permissions they request, contacted servers, users' perceptions, security-related issues, and so on. In order to extract those insights, we setup a dedicated analysis tool and we are running it **weekly** and on a **nation-by-nation** basis. 

The inspection of each mobile app is structured around five main dimensions:

:card_index_dividers: App and developer's information

:key: User permissions requested by the app

:globe_with_meridians: External servers mentioned in the code of the app

:closed_lock_with_key: Security issues in the code of the app

:speaking_head: User ratings and reviews

As you can imagine, we collect several data points for each dimension so the best way to get an idea about the information we provide is to directly look at one of our reports (see the table below).  

# Latest analyses

| **Nation** | **Report** | **Analysed apps** | **Updated at** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
:it: Italy | [:chart_with_upwards_trend: Results](data_it/reports/report_2020_5_5.md) | [7 apps](https://play.google.com/store/search?q=covid&c=apps&gl=it) (Links to Google Play) | :calendar: 05/05/2020
:netherlands: The Netherlands | [:chart_with_upwards_trend: Results](data_nl/reports/report_2020_5_5.md) | [4 apps](https://play.google.com/store/search?q=covid&c=apps&gl=nl) (Links to Google Play) | :calendar: 05/05/2020
:us: United States | [:chart_with_upwards_trend: Results](data_us/reports/report_2020_5_5.md) | [3 apps](https://play.google.com/store/search?q=covid&c=apps&gl=us) (Links to Google Play) | :calendar: 05/05/2020

> Do you want your nation listed here? You can [create an issue](https://github.com/iivanoo/covid-apps-observer/issues/new) in this repository and we will take care of it!

For transparency, the complete reports and raw data of _all_ the previous inspections are available in this GitHub repository and grouped by nation. For example, the ``data-it`` folder contains all the reports and raw data of our inspections in the previous weeks.

# Is this project for you?

This project is aimed at helping several actors:

:white_check_mark: **Citizens** can use our reports to easily compare COVID-related apps and identify which one fits their needs in terms of usability, trustworthiness, and privacy.

:white_check_mark: **Content creators** can use our reports as the basis for articles, blog posts, statistical analyses, further investigations, etc.

:white_check_mark: **Decision makers** can use our report to estimate the current landscape about COVID-related apps in their country, for example in terms of app's quality, provided services, etc.

:white_check_mark: **App developers** can use our report to assess how their own app compares against other COVID-related apps (both within their own nation and worldwide), whether some security-oriented improvements can be done, and how users perceive their own app (for example by seeing our analysis of app reviews in the Google Play store).

:white_check_mark: **Project contributors** can help in improving this project by:
  - running the analysis tool for countries which are covered yet
  - implementing additional analyses
  - fixing bugs or improving the current analysis tool

## Contributions :rainbow:

Any feedback, questions, and improvements about the project are very welcome, feel free to create an issue or pull request directly in this GitHub repository. 

For independent verification, the raw data and the source code of the project is publicly available in this repository and its source code has been thoroughly commented in order to provide all the details about how the information provided in our reports has been extracted. Further information about how to contribute to the project is available [here](code/).

## License

This software is licensed under the MIT License.

