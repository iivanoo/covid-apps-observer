# StopCovid France
App version ``1.1.4``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="StopCovid France icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | StopCovid France |
| **Unique identifier** | fr.gouv.android.stopcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=fr.gouv.android.stopcovid](https://play.google.com/store/apps/details?id=fr.gouv.android.stopcovid) |
| **Summary**  | Protégeons nos proches, protégeons-nous et protégeons les autres |
| **Privacy policy** | [https://bonjour.stopcovid.gouv.fr/privacy.html](https://bonjour.stopcovid.gouv.fr/privacy.html) |
| **Latest version** | 1.1.4 |
| **Last update** | 2020-09-15 15:47:01 |
| **Recent changes** | Améliorations et corrections. |
| **Installs**  | 1 000 000+ |
| **Category** | Médecine |
| **First release** | 29 mai 2020 |
| **Size**  | 20M |
| **Supported Android version**  | 5.0 ou version ultérieure |

### Description
> L'application StopCovid est destinée au territoire français.
<br>Avec StopCovid, participez à la protection de vos proches, de vous-même et de tous en étant alerté si vous avez été à proximité d’un utilisateur testé positif.
<br>Protégeons nos proches, protégeons-nous et protégeons les autres. 
<br>StopCovid, c’est simple :
<br># J'active l'application
<br>En utilisant le Bluetooth de votre téléphone, StopCovid détecte les téléphones des autres utilisateurs qui restent à proximité du vôtre.
<br># Je reste informé
<br>Vous serez informé si vous avez été à proximité d’un utilisateur testé positif au COVID-19.
<br># Je protège mes proches et les autres
<br>Si vous effectuez un test COVID-19 et qu’il est positif, votre laboratoire vous donnera un code à scanner ou à saisir pour avertir anonymement les utilisateurs que vous avez rencontrés.
<br>#  Mes données sont protégées
<br>L’application n’utilise à aucun moment la localisation des personnes, et il est impossible de connaître l’identité des utilisateurs.
<br>Cette application de suivi de chaîne de transmission de la Covid-19 a été réalisée par l'équipe StopCovid, sous la supervision du Ministère des Solidarités et de la Santé et du Secrétariat d'Etat chargé du Numérique.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Gouvernement |
| **Website**  | [https://stopcovid.gouv.fr](https://stopcovid.gouv.fr) |
| **Email** | contact@stopcovid.gouv.fr |
| **Physical address**  | [20 avenue de Ségur 75007 Paris](https://www.google.com/maps/search/20%20avenue%20de%20Ségur%2075007%20Paris) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Gouvernement](https://play.google.com/store/apps/developer?id=Gouvernement) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | stopcovid.gouv.fr | Etat francais represente par le Ministere de l Economie et des Finances de l Action et des Comptes publics | - | 2020-04-15 12:02:42 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lcom/android/tools/r8/GeneratedOutlineSupport;->outline18(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Only InetSocketAddress is supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Wrapped socket should already be bound' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Wrapped socket should already be connected' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The StopCovid France app has been installed by more than **1000000** times. At this time, **9728** rated the app and its average score is **2.7793815**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 2999

:star::star::star::star:: 832

:star::star::star:: 842

:star::star:: 1133

:star:: 3922

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 5 reviews"/>
</p>

> Ses intéressant pour savoir pour le covid ses important télécharger le pour votre sécurité<br> :date: __2020-10-02 09:29:23__

> De nouveau fonctionnel après plusieurs mois dommage que la réactivité ne soit pas de mise sur les corrections, ça aurait aidé l'application à mieux percer.<br> :date: __2020-10-02 08:29:41__

> Peu importe si oui ou non l'appli fonctionne correctement, elle a le mérite d'exister. Les màj arriveront au fur et à mesure. 5 étoiles car en dessous ça ne doit pas décourager de la télécharger. Elle est à partager car cette appli doit être propagée beaucoup plus vite que ce put\*\*n de virus.<br> :date: __2020-10-01 23:02:40__

> Simple et respectueuse de la vie privée, un outil nécessaire au principe de précaution afin de lutter contre le COVID et ses conséquences tant sur la santé que sur l'économie.<br> :date: __2020-10-01 10:35:54__

> Ne semble pas bien fonctionner sans WIFI.(mais marche bien à la maison)<br> :date: __2020-10-01 04:36:20__

> Facile à démarrer<br> :date: __2020-09-30 13:17:15__

> La notification est présente pour que l'application puisse tourner en tâche de fond.<br> :date: __2020-09-29 13:47:49__

> Soyez responsable et citoyen<br> :date: __2020-09-29 10:37:14__

> Genial<br> :date: __2020-09-28 16:08:56__

> Version 1.1.4 #49 : stupéfiant, l'activation a fonctionné sans erreur ROBERT. Cette application serait devenue opérationnelle ? On croise les doigts... Update : 5 jours après, fonctionne toujours parfaitement bien<br> :date: __2020-09-28 10:58:33__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Comme à Hong Kong, les consignes sanitaires doivent être respectées par l'ensemble des français.Le traçage est une bonne chose, pour isoler rapidement les cas covid déclarés. Bon courage à toutes et tous, nous finirons à voir bientôt le bout du tunnel.<br> :date: __2020-10-02 11:46:24__

> Depuis la maj on sait que l'appli est actif et c'est mieux, je regrette que l'appli consomment trop de batterie.<br> :date: __2020-10-02 08:40:26__

> Le principal avantage de stopcovid est d'utiliser la technologie bluetooth. En revanche la notification qui s'affiche en permanence est exaspérante.<br> :date: __2020-09-30 22:26:18__

> Plus de plantages, bravo pour la correction et merci<br> :date: __2020-09-29 18:39:10__

> Depuis quelques jours stopcovid plantait sur mon téléphone. J'ai fini par la désinstaller et la réinstaller. Depuis elle refonctionne. Par contre j'ai noté qu'il y avait eu une MAJ le 15 septembre, mais je n'ai pas souvenir de l'avoir vu s'installer sur mon téléphone.<br> :date: __2020-09-27 10:32:54__

> Pas de plantage. pas de désactivation intempestive. ca semble fonctionner.<br> :date: __2020-09-25 13:25:39__

> Très bonne appli mais se désactive parfois. L'utilisateur devait en être informé. Et corriger ce beug pour que sa se désactive plus.<br> :date: __2020-09-23 21:43:10__

> Ai pas mis 5 étoiles à cause du bug lors des mises à jour, j'ai un message "stopcovid s'arrête automatiquement". Solution : désinstaller et réinstaller. Fastidieux mais bon, l'essentiel est d'avoir un truc qui contribue à nous protéger du Covid.<br> :date: __2020-09-23 18:00:08__

> Une application bien dans l'ensemble, simple d'utilisation. Néanmoins, l'application ce désactive beaucoup de fois et des oublies de réactivation sont faits.<br> :date: __2020-09-22 21:51:21__

> Pour l'instant je trouve que ça consomme beaucoup trop de batterie, vraiment beaucoup. Par contre côté protection des données, on peut difficilement faire mieux ! Et les quatre étoiles sont pour ça. J'attends de voir si beaucoup de gens la téléchargent, il y aura un réel intérêt pour cette appli<br> :date: __2020-09-22 17:43:47__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Pour l'instant aucun écho<br> :date: __2020-10-01 12:36:35__

> Fonctionne bien sans problème sur mon téléphone mais aucun signalement depuis que je l'ai activée (2 mois déjà) alors que Rennes est en zone rouge...suis-je le seul à utiliser cette appli?<br> :date: __2020-10-01 08:56:27__

> L'application dans le contexte du covid19 était fondamentale, mais pour qu'elle puisse fonctionner faut-il qu'elle soit chargée par l'ensemble de la population. Dommage une fois de plus que les français baissent les bras !<br> :date: __2020-10-01 07:44:05__

> Application des plus simples à utiliser. Hormis le fait qu'il faut bien penser à réactiver l'application tous les jours, je n'ai pas trop à me plaindre, je l'utilise depuis le début. Par contre, je m'interroge vraiment sur son utilité... Je doute qu'il y ait beaucoup de personnes que je croise qu'il l'ait téléchargé... 😟<br> :date: __2020-09-30 07:27:10__

> Malheureusement, l'application se désactive souvent.<br> :date: __2020-09-29 19:58:42__

> Validé par la CNIL et l'ANSSI : j'ai confiance 👍 Mais se désactive très souvent tte seule.. dommage MAJ : il faut retirer TOUTES les optimisations de batterie pour cette appli dans les parametres du téléphone pour éviter qu'elle ne plante ou se désactive..<br> :date: __2020-09-29 01:28:19__

> Application qui se désactive à chaque désactivation du bluetooth et qui ne se réactive pas quand on le remet (ce que j'oublie régulièrement)...<br> :date: __2020-09-28 16:52:13__

> Je viens de télécharger la mise a jour et je ne peux plus activer stop covid. Dommage !!!<br> :date: __2020-09-28 09:28:21__

> Gros impact sur consommation, au eu d'avoir 90% le matin sur Samsung Galaxy s7 (système de pause), on a 1% au milieu de la nuit. Lié au Bluetooth ou à l'application. Plantages.<br> :date: __2020-09-27 03:58:14__

> Ne sert à rien,nul<br> :date: __2020-09-26 16:49:22__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Se désactive inopinément sans cesse. Impossible de l'activer plusieurs heures de suite... Inutile..<br> :date: __2020-10-01 20:09:46__

> Consomme la batterie à la vitesse grand V. Il me reste 25% après 12h00. Obligation de recharger tous les jours.<br> :date: __2020-10-01 19:40:19__

> Elle se désinstalle souvent<br> :date: __2020-10-01 08:49:50__

> L'application se désactive toute seule et après quelques semaines d'utilisation ne veut plus s'ouvrir... Je suis tout à fait d'accord avec le fait que le plus grand nombre de français doit l'utiliser pour qu'elle soit efficace, mais si ça devient quelque chose qu'il faut vérifier continuellement, c'est plus une contrainte qu'un bénéfice<br> :date: __2020-09-29 12:09:02__

> Voulant participer à l'effort contre ce virus je l'ai chargé des la première heure mais j'ai des doutes importants quant à son efficacité quand je sais que: * j'en suis rendu au moins à la vingtième fois où je dois réactiver l'application qui s'est coupée sans crier gare * le traçage a du être amoindri en efficacité pour ménager les susceptibilités alors que google nous trace au quotidien. * peu de monde le charge faute d'obligation et de conviction. Allez on y croit quand même et on continue<br> :date: __2020-09-29 06:25:16__

> Déception. Mon téléphone n'est pas compatible avec Stop Covid car il ne dispose pas du Bluetooth Low Energy. Faute d'avoir accès au BLE, les personnes qui ont des vieux portables ou des mobiles bas de gamme ne peuvent utiliser StopCovid. L'application doit être améliorée pour qu'une grande partie de la population ne se trouve plus exclue du contact-tracing.<br> :date: __2020-09-29 03:23:52__

> Pourquoi ne peut-on pas désactiver la notification permanente qui indique seulement que l'application est active ? Cela pollue l'écran.<br> :date: __2020-09-28 11:16:05__

> Tellement utile mais l'application bouffe ma batterie en une matinée.. Dommage<br> :date: __2020-09-27 12:57:28__

> Application utile mais ne fonctionne pas sur mon téléphone, elle s'arrête aussitôt que je l'ouvre. Pourriez-vous la rendre fonctionnelle sur tous les appareils ? Merci.<br> :date: __2020-09-27 11:24:20__

> Inutile d'après mr Castex alors, pourquoi devrions nous l'utiliser?<br> :date: __2020-09-26 19:28:51__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> En fait, elle ne fonctionne que si les personnes l'ont téléchargées et que s'il laisse activé leurs bluetooth. Donc en fait, c'est quasiment impossible qu'elle nous protège car rien qu'autour de moi, personne ne l'a téléchargée.... Pourquoi pas utiliser le wifi que tous le monde laisse allumé au lieu du bluetooth ? Ça ferait une condition en moins.... Màj de l'avis : l'application se désactive toute seule donc niveau protection c'est nul !<br> :date: __2020-10-02 12:42:32__

> Je n'ai pas utilisé l'application, je veux juste contribuer à l'améliorer par certaines idées. Le principe de base est top, le vrai problème, c'est la forme de l'appli : le bluetooth ? Sérieusement ? Il fallait localiser les téléphones en fonction de leurs distances aux bornes 2G/3G/4G ! Ça évite d'avoir le BT constamment activé (piratage, batterie..)... C'est un peu la base, ou même par GPS à défaut ! C'est plutôt précis.<br> :date: __2020-10-02 10:13:42__

> Application qui s'arrête automatiquement, et aléatoirement. Ce qui pose la question de sont utilité. Je la remets à chaque fois que je le vois. Mais au bout de combien de temps d'arrêt...? Je continuerai malgré tous à l'activité a chaque fois pour ma famille, mon épouse qui n'a plus de défenses immunitaires...et les personnes que je croise.<br> :date: __2020-10-02 07:53:03__

> Impossible de faire fonctionner l'application... "Stopcovid a cessé de fonctionner"<br> :date: __2020-10-02 00:23:21__

> Pourri<br> :date: __2020-10-02 00:07:34__

> Ne marche pas dès la première fois<br> :date: __2020-10-01 22:30:17__

> Ne fonctionne pas ... ( Xiaomi redmi note 7 )<br> :date: __2020-10-01 22:27:36__

> J'ai l'application, et j'ai le covid19 en ce moment. Donc c'est que ça ne marche pas.<br> :date: __2020-10-01 22:26:49__

> À chaque fois que je regarde l'applucation n'est pas activée alors qu'à aucun moment je ne suis intervenue pour la stopper<br> :date: __2020-10-01 20:14:52__

> Cela ne marche pas.cela se désactive sans arrêt<br> :date: __2020-10-01 10:39:24__


