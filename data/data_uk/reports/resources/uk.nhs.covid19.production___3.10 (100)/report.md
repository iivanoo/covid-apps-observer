# NHS COVID-19
App version ``3.10 (100)``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="NHS COVID-19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | NHS COVID-19 |
| **Unique identifier** | uk.nhs.covid19.production |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=uk.nhs.covid19.production](https://play.google.com/store/apps/details?id=uk.nhs.covid19.production) |
| **Summary**  | Protect your loved ones with the NHS contact tracing app for England and Wales. |
| **Privacy policy** | [https://covid19.nhs.uk/our-policies.html](https://covid19.nhs.uk/our-policies.html) |
| **Latest version** | 3.10 (100) |
| **Last update** | 2020-11-05 22:05:26 |
| **Recent changes** | App can be used across UK borders in England, Wales, Scotland, Northern Ireland, Jersey and Gibraltar, detecting all relevant contact tracing app users (regardless of them using different official apps), alerting them if they have been in contact with coronavirus. Alerts users to new versions of the app when available to ensure access to the latest features, guidance, new tier information and advice. Feature enhancements when ordering a test. Overall UI, language and accessibility optimisations. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 8.0M |
| **Supported Android version**  | 6.0 and up |

### Description
> The new NHS COVID-19 app is the Official NHS contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from Coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>- Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>- Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>- Check-in: Get alerted if you have visited a venue where you may have come into contact with coronavirus, using a simple QR code scanner. No more form filling. 
<br>- Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>- Test: Helps you order a test if you need to.
<br>- Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Arabic (Modern Standard), Bengali, Chinese (Simplified), Gujarati, Polish, Punjabi (Gurmukhi script), Romanian, Somali, Turkish, Urdu and Welsh.
<br>The app has been built in collaboration with some of the most innovative organisations in the world. We have worked with medical experts, privacy groups, at-risk communities and we’ve shared knowledge with the teams working on similar apps in many countries.
<br>Protect your loved ones. Please download the app. 
<br>The App is CE marked as a class I medical device in the United Kingdom and developed in compliance with European Commission Directive 93/42/EEC for class I devices.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Department of Health and Social Care |
| **Website**  | [https://covid19.nhs.uk/](https://covid19.nhs.uk/) |
| **Email** | NHSCovid-19AppStoreSupport@nhsbsa.nhs.uk |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care](https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | apache.org | The Apache Software Foundation | :us: US | 1995-04-11 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **89069** rated the app and its average score is **4.0075464**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 53168

:star::star::star::star:: 12694

:star::star::star:: 6894

:star::star:: 3341

:star:: 12972

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> Easy to use app, keeping the UK safe!<br> :date: __2020-11-30 00:26:29__

> I belive in this app<br> :date: __2020-11-29 19:12:09__

> I love this app because you don't have to go to the hospital for a test.It even tells you if you have the virus.It also informs you what you should do if you have the virus and it tells you how many days to spend in isolation.<br> :date: __2020-11-29 15:44:46__

> Fantastic track and trace service 👍👍<br> :date: __2020-11-29 14:53:20__

> Very good<br> :date: __2020-11-29 11:57:17__

> excellent service<br> :date: __2020-11-29 06:19:20__

> EXCELLENT!!!<br> :date: __2020-11-29 06:15:28__

> Works well just needs a few things adding like away of knowing the app is working with a small icon adding 2 the top of phones so people know its working but apart from that its works ok<br> :date: __2020-11-28 16:22:40__

> Does what it says it does<br> :date: __2020-11-28 16:04:24__

> Excellent services...<br> :date: __2020-11-28 09:13:56__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> Hi how do I find my 8 digit code I've been told self isolate and I want to apply for some help and form needs it<br> :date: __2020-11-29 14:04:55__

> This application is clearly very important right now i have a few things that feel could be better if you use Contact tracing via Bluetooth it eats up your battery 🔋 shame enables when required only<br> :date: __2020-11-28 20:58:03__

> Definitely improved since the beginning. Well at least seems like that 😅<br> :date: __2020-11-28 17:12:26__

> THANKS NHS❤🌈<br> :date: __2020-11-28 09:34:37__

> Good<br> :date: __2020-11-28 01:36:04__

> Good enough under the circumstances. Takes a while to update, and kind of makes me feel a little more protected.<br> :date: __2020-11-27 22:02:39__

> it seems to do what it is set to do<br> :date: __2020-11-27 09:03:01__

> I got a pixel 5 with android 11. I got about 4 notifications a day that app stopped working. Now after reinstalling, I can't open it. On the feedback send to Google, I see "crash" and keystoreexception with a source code linenumber. Update: after restarting the pixel5 and reinstalling the app , it is up and running again.<br> :date: __2020-11-26 14:27:28__

> After reinstalling app it now works. Still things to develop but that comes with time. All in all happy it does what it sets out to do and helpful to have the feedback if any issues. Just needs more downloads for it to be efficient<br> :date: __2020-11-25 20:26:59__

> My 12 year old has tested positive and I've tried to put this app on his phone but you need to be over 16?? This app should be available for 11 year old going into secondary school. Would like more details of exposure such as date and time. And for alerts to stay on the app not just a notification that dissappears<br> :date: __2020-11-24 17:39:59__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> Heajlth<br> :date: __2020-11-30 03:20:18__

> The app is great and I'm always using it. Pity all businesses are not using qr code to allow us to check in. It should be compulsory for all retail shops and postoffices.<br> :date: __2020-11-29 10:03:03__

> I'd been using the app regularly and everything was fine, but last week the app wouldn't open for me to check-in at my office and still won't open.<br> :date: __2020-11-29 08:34:49__

> Seems useful but takes too much battery<br> :date: __2020-11-29 03:18:15__

> Seems to have stopped working in the last few days. Can't open the app and I'm periodically alerted to the fact that it "keeps stopping".<br> :date: __2020-11-29 01:44:00__

> Well I hope it works<br> :date: __2020-11-28 14:44:13__

> It seemed to interfere with me recieving text messages and phone calls. I fon't know why. My fix uninstall it. I got a back log of messages after.<br> :date: __2020-11-27 23:39:56__

> I've been using the NHS app to report how I'm feeling on a daily basis,with no problems until last week when it suddenly crashed. I logged out & back in again & it was still the same?? I even deleted it from my Xperia XA2 - then added it again, but it stayed the same - it used to ask me to put my details in every morning. But now it does nothing?? I've tried everything but it still won't respond. I've recently bought a new Google phone & it's working fine on that. 🤔<br> :date: __2020-11-27 20:50:07__

> On the whole good and easy to use, but I get far too many random exposure alerts, especially in the middle of the night!<br> :date: __2020-11-27 09:41:46__

> So far so good, I don't go to many places at the moment but the automatic visual log in is good but not many places have got this at present, like say petrol stations or even supermarkets don't seem to have it. Mostly coffee places! Haven't used it any other way yet like for test or the other features but I do put the local search on when I go out if a lot of people about.<br> :date: __2020-11-27 09:40:48__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> Doesn't link to Track and Trace so I effectively have two different profiles. Uninstalling this and sticking to the Track and Trace that has my details and user ID. UPDATE. No it doesn't. Reinstalled, entered test result, got completely different isolation date in the App.<br> :date: __2020-11-30 12:30:54__

> Have downloaded for 3 time now on my pixel 3 and it keeps stopping working<br> :date: __2020-11-30 11:45:39__

> The app was ok for a while but the last month I can't even open the app, it just crashes whenever I try.<br> :date: __2020-11-30 10:13:10__

> Asks for your postcode and then reports the risk level based on your local authority. Postcodes are a fairly arbitrary geo-tagging mechanism used by the post office and have little connection to most authorities. Mine is not even in the right county! So far from being informative, it's misleading. It appears that the isolation instructions given in the app are DIFFERENT to those given by the NHS. Sadly, this is just one of several contradictions in advice and instructions given.<br> :date: __2020-11-29 17:42:56__

> Not sure how this protects anyone from covid. Location is not accurate enough to pin someone to a exposure. Impossible to define the exposed or be exposed.<br> :date: __2020-11-29 13:15:05__

> Rubbish<br> :date: __2020-11-28 17:39:05__

> This app used to scan Qr codes in a flash. Now it doesn't control the camera, it no longer sees the code<br> :date: __2020-11-28 09:30:33__

> I'm confused by this app, if I turn Bluetooth off I am able to look into the exposure checks. One of them has shown up that I've had one match but there's been no messege to Isolate or anything. I keep hearing that these apps aren't great on Huawei which is what I have. If someone could explain to me what the match means that would be great<br> :date: __2020-11-27 18:28:36__

> I was happily using this app and then in following with this governments performance it goes down for some Android users and just like this government this app isn't fit for purpose when many people have fallen out of the loop. I won't bother to reinstall the updated app as I no longer have any trust in this government and its handling of the pandemic as well as usual Tory hatred for the working class.<br> :date: __2020-11-27 18:28:08__

> App Is stupid, said I had to isolate as I apparently came into contact wirh someone who tested posative, but working out the day I came into contact with them I was not around anyone for longer than 15mins which it days you have to be in contact with the person for. Only person close to me was a guy who was sat in another lorry next to me for over 30 mins he was in his lorry and I was in mine so how is that close contact?? Deleted the app as can't afford for this to happen again<br> :date: __2020-11-27 15:08:13__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> Doesn't work- we tested positive and yet my app didn't notify my husband. His 2 phones took over 24 hours to notify each other and my friend has been told to isolate even though she hasn't left the house for 4 days! Edit to add that mine and my husband's phones sit next to each ither to charge overnight. If the app worked our phones would have pinged each other but they didn't. I've been supportive of all covid measures throughout, but track and trace isn't effective.<br> :date: __2020-11-30 11:53:41__

> App no longer launches on Pixel 3A. Been unable to launch for several days now and a reinstall hasn't fixed it. For something as vital as this, there should really be a better process for making sure this is working reliably.<br> :date: __2020-11-30 11:44:12__

> Aload of rubbish<br> :date: __2020-11-30 06:48:54__

> Persistently refusing to open on pixel 5.<br> :date: __2020-11-29 21:26:37__

> Absolute shambles the government should be ashamed of themselves<br> :date: __2020-11-29 19:02:19__

> I knew someone near me had covid the app does not inform you so complete waste of time<br> :date: __2020-11-29 14:51:42__

> Junk. Gave me a fake positive and I have not left my house. It's detached too so it's not like a flatmate got me through the wall. They also lie and say they don't need location on... try it without - go on.<br> :date: __2020-11-29 14:13:38__

> Unable to download help!<br> :date: __2020-11-29 14:09:38__

> Doesn't recognise official nhs qr codes. I've reinstalled app twice to get it to work- it worked when I first downloaded but just stopped. The QR codes i am scanning are nhs official - other people are able to scan codes with their android device, but it just keeps saying the code isn't recognised on mine. Worked originally when I first installed it, but just stopped working. Very poor track and trace system - very disappointed.<br> :date: __2020-11-29 11:32:50__

> This app is useless. Doesn't tell me the correct information. I have got covid but this doesn't have the symptoms I've got on it. It has barely any useful information on it and it still hasn't told my partner to isolate even tho I put into it that I have had a positive test. Its the biggest waste of money that I've ever been spent. A chocolate teapot comes to mind...<br> :date: __2020-11-29 10:20:10__


