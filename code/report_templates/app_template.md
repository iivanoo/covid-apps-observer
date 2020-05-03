# <<<APP_NAME>>>

<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/icon.png" alt="<<<APP_NAME>>> icon" width="200"/>

|---|---|
| **Name**  | <<<APP_TITLE>> |
| **Unique identifier** | <<<APP_ID>>> |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=<<<APP_ID>>][https://play.google.com/store/apps/details?id=<<<APP_ID>>] |
| **Summary**  | <<<APP_SUMMARY>> |
| **Privacy policy** | [<<<APP_PRIVACY_POLICY>>>][<<<APP_PRIVACY_POLICY>>>] |
| **Latest version** | <<<APP_VERSION>>> |
| **Last update** | <<<APP_UPDATED>>> |
| **Recent changes** | <<<APP_RECENT_CHANGES>>> |
| **Installs**  | <<<APP_INSTALLS>> |
| **Category** | <<<APP_GENRE>>> |
| **First release** | <<<APP_RELEASE>>> |
| **Size**  | <<<APP_SIZE>> |
| **Supported Android version**  | <<<APP_ANDROID_VERSION>> |

## Developer

In the following we report the main information provided by the developer in the Google play store

|---|---|
| **Developer**  | <<<APP_DEVELOPER>> |
| **Website**  | [<<<DEVELOPER_WEBSITE>>][<<<DEVELOPER_WEBSITE>>>] |
| **Email** | [<<<mailto:DEV_EMAIL>>>][DEV_EMAIL] |
| **Physical address**  | [<<<APP_DEVELOPER_ADDRESS>>][https://www.google.com/maps/search/<<<DEVELOPER_WEBSITE>>>/] (Google Maps) 
| **Other developed apps**  | [<<<APP_TITLE>>][https://play.google.com/store/apps/developer?id=<<<APP_DEVELOPER_ID>>>] |

## Requested permissions

In the following we report the complete list of the permissions requested by the app. A detailed explanation of all the levels mentioned below is provided right after the table.

|---|---|---|
<<<PERMISSIONS_TABLE>>>

As you probably know, the Android operating system has a permission model which allows users to grant access to potentially sensitive information. We carefully analyzed the [official Android documentation (v. 29)][https://developer.android.com/reference/android/Manifest.permission], and it resulted that a permission requested by an Android app can belong to the following protection levels:
* **Dangerous**: higher-risk permissions that would give a requesting app access to private user data or control over the device that can negatively impact the user. Because this type of permission introduces potential risk, the system usually does not automatically grant it to the requesting app. For example, any dangerous permissions requested by an app may be displayed to the user and require confirmation before proceeding.
* **Normal**: this is the default and most common level in Android; normal permissions are lower-risk and give access to isolated app-level features, with minimal risk to other apps, the system, or the user. 
* **Signature**: permissions granted only if the requesting app is signed with the same certificate as the app that declared the permission
* **Appop**: old permission level, a reminiscence of the App Ops tool that Google introduced in Android 4.3.
* **Development**: optional permissions which can be granted to development-oriented apps.
* **Privileged**: permissions who give higher power to mobile apps w.r.t. other apps, such as binding to incoming calls, interacting via bluetooth with other devices without user interaction, etc.
* **Preinstalled**: reserved only for preinstalled apps
* **Installer**: allow the holder to start the permission usage screen for an app
* **RetailDemo**: permissions related to devices used in demonstrations in shops.
* **Pre23**: permissions automatically granted to apps targeting devices running pre-6.0 Android.
* **Upcoming**: permissions which will be released in the next version of the Android platform. 
* **Deprecated**: permissions belonging to old releases of the Android platform, they should not be used by developers since they will not be supported in the near future.
* **Not for use by third-party applications**: permissions which can be requested only by apps developed by Google.
* **Undefined**: this protection level is not documented by Google.

## Mentioned servers

We analyzed the app in order to look for all possible mentions of remote URLs. The mentioned URLs can refer to remote servers the the app is using for either sending or receiving information, web addresses for directing the user to an information website, and so on. It is important to note that this analysis is not meant to be complete and it is very prone to obfuscation. The servers reported here are simply _mentioned_ somewhere in the code of the app and are meant to just give an indication about the "hooks" of the app towards external resources. For example, for an Android app it is normal to contact Google services in order to send/receive push notifictions, or to contact the servers of analytics services for having real-time diagnostics about crashes of the app or bugs.

|---|---|---|
<<<SERVERS_TABLE>>>

## Androiwarn analysis 

TODO

## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The <<<APP_NAME>>> app has been installed by more than **<<<APP_MIN_INSTALLS>>>** times. At this time, **<<<APP_RATINGS>>>** rated the app and its average score is ***<<<APP_SCORE>>>. Below we show the distribution of the ratings across the usual star-based rating of Google Play
* Five stars: <<<APP_5_STARS>>>
* Four stars: <<<APP_4_STARS>>>
* Three stars: <<<APP_3_STARS>>>
* Two stars: <<<APP_2_STARS>>>
* One star: <<<APP_1_STAR>>>

## Reviews

For each level of rating (5 stars, 4 stars, ..., 1 star) we show the main topics discussed by end users in their reviews in the Google Play store. Those topics are collected in a simple frequentist manner and are meant to help both future users and the developers of the app in understanding what are the main positive and negative points of the app under analysis. 

<p align="center">
<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/wordcloud_5_stars.png" alt="<<<APP_NAME>>> wordcloud" width="200"/>
<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/wordcloud_4_stars.png" alt="<<<APP_NAME>>> wordcloud" width="200"/>
</p>
<p align="center">
<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/wordcloud_3_stars.png" alt="<<<APP_NAME>>> wordcloud" width="200"/>
<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/wordcloud_2_stars.png" alt="<<<APP_NAME>>> wordcloud" width="200"/>
</p>
<p align="center">
<img src="resources/<<<APP_ID>>><<<SEPARATOR>>><<<APP_VERSION>>>/wordcloud_1_star.png" alt="<<<APP_NAME>>> wordcloud" width="200"/>
</p>
