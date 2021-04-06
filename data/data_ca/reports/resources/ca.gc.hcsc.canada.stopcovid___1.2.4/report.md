# COVID Alert - Let’s protect each other
App version ``1.2.4``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Alert - Let’s protect each other icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Alert - Let’s protect each other |
| **Unique identifier** | ca.gc.hcsc.canada.stopcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid](https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid) |
| **Summary**  | Health Canada Exposure Notification |
| **Privacy policy** | [https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html) |
| **Latest version** | 1.2.4 |
| **Last update** | 2021-03-25 21:30:59 |
| **Recent changes** | - Improved accessibility of the Menu button when using zoom features.<br>- Maintenance updates. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Jul 29, 2020 |
| **Size**  | 52M |
| **Supported Android version**  | 6.0 and up |

### Description
> Together, let’s slow the spread of COVID-19. Canada's COVID Alert app notifies you if someone you were near in the past 14 days tells the app they tested positive.
<br>COVID Alert uses Bluetooth to exchange random codes with nearby phones. It does not use or access any location data. COVID Alert works by determining how far away other phones are by the strength of their Bluetooth signal. 
<br>Several times a day, COVID Alert checks a list of codes from people who tell the app they tested positive. You’ll get a notification if a code you received matches one of the positive codes.
<br>If you test positive for COVID-19 you’ll receive a one-time key with your diagnosis to enter into COVID Alert. The app asks permission to share your random codes from the last 14 days with a central server.
<br>Other phones using COVID Alert check the central server periodically throughout the day. If they recorded any codes that match the codes in the central server, their user will be notified that they were exposed.
<br>COVID Alert has no way of knowing:
<br>-your location - COVID Alert does not use GPS or location services
<br>-your name or address
<br>-the place or time you were near someone
<br>-if you're currently near someone who was previously diagnosed
<br>Provincial and territorial governments are working to support COVID Alert across Canada. In some places, people cannot yet report a COVID-19 diagnosis through this app.
<br>It’s still helpful to keep COVID Alert on, no matter where you are.  That way, when people are able to report a diagnosis, you’ll find out if you were near them.
<br>COVID Alert was built by Health Canada with the Canadian Digital Service on the private exposure notification framework by Apple and Google.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Health Canada | Santé Canada |
| **Website**  | [https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/help.html](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/help.html) |
| **Email** | hc.AlerteCOVIDAlert.sc@canada.ca |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Health+Canada+%7C+Sant%C3%A9+Canada](https://play.google.com/store/apps/developer?id=Health+Canada+%7C+Sant%C3%A9+Canada) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>GET_TASKS** | Deprecated | This constant was deprecated in API level 21. No longer enforced. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Alert - Let’s protect each other app has been installed by more than **1000000** times. At this time, **7946** rated the app and its average score is **3.5705445**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3964

:star::star::star::star:: 895

:star::star::star:: 698

:star::star:: 491

:star:: 1898

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 5 reviews"/>
</p>

> A simple app does what it says it does<br> :date: __2021-04-02 07:46:53__

> As human beings we have to work TOGETHER, to get thing under control. And STOP ALL THIS HATE CRIMES. Can't WE JUST ALL GET ALONG.<br> :date: __2021-04-02 07:37:58__

> App works well and takes your privacy seriously. I wish that more people used it.<br> :date: __2021-04-02 03:25:27__

> Awesome app makes me feel more safe when I'm out shopping<br> :date: __2021-04-01 22:20:18__

> If I won't those gamers do you want it to be careful about your grace uncle's Love you now that sokay me know how much Rhonda Brisebois for sure I can not talk about it to the real thing is yours uncle Duc Tong Ottawa Ont you now so very true to me any time now and you're beautiful grill friend happy birthday to you 🎂🎈🎈🎈 hello everybody I don't need some you don't have it all right happy dog anyway I'm happy and even and I promise I<br> :date: __2021-04-01 00:12:15__

> Good<br> :date: __2021-03-31 10:47:18__

> This app worked and reported an exposure. Update your app to dismiss an alert of an exposure and confirm that you got tested.<br> :date: __2021-03-26 21:34:17__

> I love it and encourage everyone to get it! (the latest update was annoying but it was solved)<br> :date: __2021-03-25 02:53:11__

> The Application itself is fine, it works in the background and does what it needs to do without you ever knowing that it was on. The downside to this whole thing is that the roll out and the execution of making this app an essential part of daily life for people during the pandemic was a flop so you don't really need it. Also at some point the app stopped "updating" you on the week that just happened.<br> :date: __2021-03-25 01:59:34__

> Great<br> :date: __2021-03-20 22:48:20__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 4 reviews"/>
</p>

> Seems like a great idea, if only it worked for people from provinces that have not yet agreed to support it. It doesn't make sense that because my Provincial Government thinks it's not a good idea, that I can't use it anyways, and possibly be warned if others like myself have the app running and get sick.<br> :date: __2021-03-31 06:10:19__

> Learning but not good at this<br> :date: __2021-03-30 19:50:19__

> Still hasn't trickled down to notifications within my city<br> :date: __2021-03-29 15:21:55__

> It does exactly what it says on the tin (it's literally a random number generator). Only docking a star for the nags to turn Bluetooth back on, since my conventional wisdom would be to turn it on when I'm actually in public. Though I've seen a lot of reviews mention this already so that's fair.<br> :date: __2021-03-29 07:43:21__

> I assume it's working properly, but it would be reassuring to have a visible counter that shows how many contact codes have been exchanged. I don't care where or when, but a running count would at least let me know that I'm not the only person in town that has this installed. Edit: it will tell me how many times it's checked for exposures, but how effective will that be if none of the people I've been in contact with have this app installed?<br> :date: __2021-03-23 21:18:14__

> Not complicated;informative, has updates on the virus (s)<br> :date: __2021-03-08 17:11:05__

> cool<br> :date: __2021-03-01 12:09:51__

> No problems to report<br> :date: __2021-03-01 10:58:30__

> Stay home and be safe<br> :date: __2021-02-28 04:26:50__

> It's a good option to have<br> :date: __2021-02-21 03:52:48__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 3 reviews"/>
</p>

> It seems fantastic but it would be nice to know that it ONLY works in Ontario or around infected people from Ontario who have logged their exposure and left the province, for whatever extremely unlikely reason, before you install and finish the tutorial.<br> :date: __2021-04-02 22:06:41__

> Waste of Time, This app is a good concept but you have 2 major problems that you will be unable to overcome. First you are relying on the average person to download the app(which they aren't) and second you are again relying on them to input a code(which they aren't).<br> :date: __2021-03-29 17:13:31__

> As someone working in the healthcare field, I strongly recommend this app for everyone to use. There is however an issue with the app recently where it always sends a reminder notification that "bluetooth is off, unable to check for exposure" multiple times a day. It ends up being very annoying since I only turn off bluetooth at home, with no one else going out.<br> :date: __2021-03-20 18:17:29__

> Why does this app slow my phone down so much? It drains the battery twice as fast, and my phone is about half as fast. Everything lags while this app is running. I love the idea for the app, but this needs to be improved so as to discourage people from uninstalling it.<br> :date: __2021-03-20 01:25:15__

> decent<br> :date: __2021-03-16 04:50:19__

> Does this app give me updates on Tableau for my area. I have it on my computer but can't get it on my phone.<br> :date: __2021-03-14 16:26:52__

> Keeps asking to switch on the phone Bluetooth even though it is always on. Uninstalling as not working but just annoying.<br> :date: __2021-03-14 08:08:52__

> It is 100% voluntary COVID reporting which means that infected people will have to notify the app of their infection. What if they don't?<br> :date: __2021-03-13 21:01:17__

> Does this app work in alberta yet? Specifically jasper ab?<br> :date: __2021-03-11 16:33:37__

> Still not available for Alberta, it's been half a year<br> :date: __2021-03-07 20:07:25__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 2 reviews"/>
</p>

> I think we should be treating covid-19 as if it were a serial killer. I don't want to be told that I've been shot after the fact. If someone receives a positive diagnosis along with the one-time key it should be mandatory to put that key into the app. If that person does not stay at home and I am near them in public places I should receive an immediate buzz on my phone so that I can increase my distance from that person. The Play store screen shows only 1 million plus downloads.<br> :date: __2021-04-01 00:17:41__

> Wakes up my phone every hour and shows a heart attack inducing notification saying it's checking for exposures. Can't disable that without disabling all notifications. Makes no sense. This app makes you live in constant fear. Good idea but poor usability.<br> :date: __2021-03-31 19:52:05__

> Often didn't update or work even when Bluetooth was on<br> :date: __2021-03-26 06:09:51__

> It says that a one time key is not available for my area? But I live in one of the most populated places in BC?<br> :date: __2021-03-23 22:58:23__

> Great idea but poor execution. It's not useful if persons with Covid are not given the codes to report it.<br> :date: __2021-03-19 12:17:13__

> Needs A Lot of Work. The concept is fine but a lot of flaws. I tested positive for Covid and about 3 times every day it tells me to get a new code to share my new exposures. I'm in quarantine for at least 10 days and not going anywhere. I had to turn it off because it was so annoying.<br> :date: __2021-03-18 19:47:09__

> Just hope no one forgets their phone!<br> :date: __2021-03-06 11:38:26__

> I have had this App on my phone since 08/20. Do to the nature of my job I frequent Toronto and Ottawa, both hot spots. Here we are in March, 6 months of using this app, yet not one single notification. I highly doubt it's effectiveness.<br> :date: __2021-03-01 16:19:06__

> Great idea, but only 5 people in Canada are using it. Canada doesn't know how to reach out to its masses and connect with them on a personal level<br> :date: __2021-02-23 01:23:19__

> Not sure how useful this app is... This app is like the notorious pet rock - either does nothing or appears to do nothing. It would give a better sense of reliability if it reported to me how many other unique devices my phone came in the vicinity of and how many devices are reporting in the preceeding 24h period in my province / city. This app is worse than useless if I am the only one using it in all of Ontario. I'd rather free up space & release the processing power that this app is wasting.<br> :date: __2021-02-18 18:06:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 1 reviews"/>
</p>

> It doesn't work in my province. So definitely useless to me right now. I guess I'll try again whenever it expands<br> :date: __2021-04-04 04:56:42__

> What is the point of this app if it doesn't do what it's designed to do?? I was sitting right next to someone who was covid positive and got no alert. Now I'm covid positive, and still no alert. What a joke. Deleting this garbage<br> :date: __2021-04-02 21:48:12__

> Useless requires location, data to track... Concept is there not intetesting enough or enough users to make affective<br> :date: __2021-04-02 05:07:25__

> Doesn't even work!!! I've been in contact. And got covid. The person even put in the app code!!! It still shows I haven't been exposed. Realllllyyyyy?!?!? I'M COVID POSTIVE LOL I also know they did it because I made them get the app and enter their code....<br> :date: __2021-04-02 04:59:17__

> I don't know of anyone who has gotten an alert on this yet. and some should have.<br> :date: __2021-04-02 01:45:35__

> COVID has been a thing for over a year and this still doesn't work in my area? So it's health some parts of Canada?<br> :date: __2021-03-31 10:27:17__

> Useless<br> :date: __2021-03-30 00:20:51__

> Non functional for B.C. .Good idea though.<br> :date: __2021-03-26 16:53:41__

> My roommate got covid and he lives in the next room. But the app says "no exposure"!!<br> :date: __2021-03-25 23:09:09__

> What's the point of this app if it's not being used correctly ..... BTW it only takes a second to get COVID ...<br> :date: __2021-03-25 16:44:15__


