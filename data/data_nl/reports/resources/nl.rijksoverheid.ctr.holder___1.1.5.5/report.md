# CoronaCheck
App version ``1.1.5.5``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="CoronaCheck icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | CoronaCheck |
| **Unique identifier** | nl.rijksoverheid.ctr.holder |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=nl.rijksoverheid.ctr.holder](https://play.google.com/store/apps/details?id=nl.rijksoverheid.ctr.holder) |
| **Summary**  | Krijg toegang na testen |
| **Privacy policy** | [https://coronacheck.nl/nl/privacy](https://coronacheck.nl/nl/privacy) |
| **Latest version** | 1.1.5.5 |
| **Last update** | 2021-04-24 19:40:44 |
| **Recent changes** | * Bij het kopiëren/plakken van een code vanuit e-mail worden extra spaties nu automatisch eruit gehaald.<br>* Een mogelijke crash is opgelost.  |
| **Installs**  | 10.000+ |
| **Category** | Tools |
| **First release** | 17 mrt. 2021 |
| **Size**  | 37M |
| **Supported Android version**  | 6.0 en hoger |

### Description
> CoronaCheck is de officiële testbewijs-app van Nederland, ontwikkeld door het Ministerie van Volksgezondheid, Welzijn en Sport. Het is een digitaal hulpmiddel om toegang te krijgen tot bepaalde sociale, culturele of sportieve locaties in Nederland. Dat kan alleen als je op het moment van testen geen corona had.
<br>CoronaCheck kan worden gebruikt bij vooraf aangekondigde evenementen, zoals de interland Nederland - Letland op 27 maart.
<br> 
<br>Hoe werkt de app?
<br>Belangrijk: maak eerst een afspraak voor een coronatest bij een testlocatie.
<br> 
<br>- Haal je testresultaat op in de app
<br>Als het resultaat van jouw coronatest bekend is, haal je het testresultaat op in de app. Je vult daarvoor een code in die je van de testlocatie hebt gekregen.
<br> 
<br>- Maak van je testresultaat een QR-code
<br>De app maakt van jouw negatieve testresultaat een QR-code. In deze QR-code staat alleen of en wanneer je negatief getest bent.
<br> 
<br>- Laat jouw QR-code zien bij de ingang
<br>Bij de ingang wordt deze QR-code gescand - als bewijs dat je geen corona had op het moment van de test.
<br> 
<br>- Testresultaat is 40 uur geldig
<br>Een negatief testresultaat is geldig tot 40 uur na het moment van testen. Zorg dus dat jouw QR-code binnen die tijd gescand is aan de deur. Als je testbewijs verloopt verdwijnt de QR-code uit de app. Nieuwe QR-code nodig? Laat je opnieuw testen.


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
| **Developer**  | Rijksoverheid |
| **Website**  | [https://coronacheck.nl](https://coronacheck.nl) |
| **Email** | helpdesk@coronacheck.nl |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Rijksoverheid](https://play.google.com/store/apps/developer?id=Rijksoverheid) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | ggdghor.nl | - | - | 2014-03-06 00:00:00 |
 | coronacheck.nl | - | - | 2020-02-25 00:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>

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
> - This application loads a native library: 'barhopper_v2'<br>
> - This application loads a native library: 'gojni'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The CoronaCheck app has been installed by more than **10000** times. At this time, **63** rated the app and its average score is **2.9047618**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 23

:star::star::star::star:: 7

:star::star::star:: 2

:star::star:: 3

:star:: 28

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="nl.rijksoverheid.ctr.holder 5 reviews"/>
</p>

> Bevestigde testafspraak is niet terug te vinden in de app. Gelukkig had ik een screenshot gemaakt. Edit: Bevesting testafspraak kreeg ik alsnog na mijn review via de mail. Test uitslag omzetten naar QR en inchecken voor het pilot evenement ging vlekkeloos, prima app.<br> :date: __2021-04-27 09:33:27__

> Goed<br> :date: __2021-04-24 14:26:11__

> Slecht!!!!! Hoe krijg ik het testbewijs met coronachek. Waar de code invullen?<br> :date: __2021-04-24 11:12:47__

> App werkte soepel. Eenvoudig in gebruik. En lijkt ook aandacht voor privacy.<br> :date: __2021-04-23 17:11:49__

> Prima app. Zonder problemen code uit de mail gekopieerd en bevestigingscode uit sms kunnen invoeren. Simpel en doeltreffend. Heerlijk om er op deze manier weer op uit te kunnen.<br> :date: __2021-04-16 16:06:36__

> Zeer makkelijk te gebruiken. De stappen worden duidelijk uitgelegd, kan bijna niet mis gaan.<br> :date: __2021-04-14 19:04:07__

> Meteen vanaf de eerste poging werkt alles perfect.<br> :date: __2021-04-14 15:57:18__

> Geweldig dat het zo makkelijk gaat<br> :date: __2021-04-07 17:18:39__

> App werkt niet. Iedere keer als ik de SMS code invul en submit crasht de app... [edit: werkt nu wel!]<br> :date: __2021-03-27 12:24:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="nl.rijksoverheid.ctr.holder 4 reviews"/>
</p>

> Was een beetje angstig na het lezen van wat slechte reviews. Maar eigenlijk ging alles zoals het hoort. Heel vlot, geen problemen met scannen. Top!<br> :date: __2021-04-25 20:09:22__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="nl.rijksoverheid.ctr.holder 3 reviews"/>
</p>

> Wanneer geldt een vaccinatie ook om events te bezoeken en wanneer komt deze in de app.<br> :date: __2021-04-28 18:25:50__

> Jammer dat er maar voor 1 persoon een QR code kan worden aangemaakt. Zou handig zijn als een heel gezin erin gezet kan worden. Dan hoeft niet iedereen de app te hebben en te tonen. En kan ook een mobielloze partner gewoon een code krijgen.<br> :date: __2021-04-19 15:55:14__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="nl.rijksoverheid.ctr.holder 2 reviews"/>
</p>

> Werkt één keer goed, daarna niet meer. Donderdag negatieve test, omgezet in qr code, vrijdag verdwenen. Gister negatieve test, vanochtend omgezet in qr code, vanavond verdwenen en niet opnieuw om te zetten. Gelukkig werd de email ook geaccepteerd<br> :date: __2021-04-19 23:29:00__

> Werkt dus weer niet op Android 10 met tablet samsung galaxy tab 9.helaas maar waar.<br> :date: __2021-04-10 08:56:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="nl.rijksoverheid.ctr.holder 1 reviews"/>
</p>

> Door mee te werken aan de testsamenleving krijg je niet meer vrijheden maar je levert ze juist in, de eerste stap naar vrijheid is burgerlijkeongehoorzaamheid. Binnenkort punten systeem<br> :date: __2021-04-28 01:53:41__

> Omhandig<br> :date: __2021-04-27 11:43:55__

> Waardeloos, liet de app open staan nadat ik mijn code had laten zien. Binnen 2 uur was mijn telefoon leeg. Daarnaast een waardeloze manier om het gepeuppel in bedwang te houden.<br> :date: __2021-04-26 18:34:43__

> ben de hele dag bezig en geeft telkens aan app sluiten enz<br> :date: __2021-04-25 00:56:44__

> Van de 3 keer dat ik getest ben heb ik alleen de eerste keer 40 uur lang een bruikbare QR-code gehad. De keren daarna was die eenmalig te zien na het importeren en vervolgens verdwenen (melding: QR code verlopen). En omdat ie maar 1 keer te importeren is zit je vervolgens zonder! Als dit de toekomst wordt hoop ik wel dat de app nog wat verbeterd wordt.<br> :date: __2021-04-25 00:41:31__

> nou ik heb wel internet vul mijn code in die ik van de test locatie heb gehad nu wil ik mij unieke code opgeven die ik per sms heb ontvangen maar dat schrijft het apparaat dat de code verkeerd is dus idd het werkt totaal niet<br> :date: __2021-04-24 17:24:08__

> Deze versie crashed! Na update laatste versie<br> :date: __2021-04-24 16:12:17__

> App en site volstrekt onbereikbaar, schiet dus het doel voorbij. Praktisch nut zero.<br> :date: __2021-04-24 16:05:09__

> Net getest, negatief, heb de code nou al 10 keer ingevuld. Iedere keer " u heeft geen internet verbinding". Werkt dus totaal niet! Nou maar hopen dat ze bij evenement coulant zijn en de email accepteren. Eens maar NOOIT meer! Mijn hele dag is door dit gezeik verpest! Waardeloze app direct weer verwijderd!<br> :date: __2021-04-24 15:44:10__

> Code invullen maar inloggen lukt niet<br> :date: __2021-04-24 15:37:03__


