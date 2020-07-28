# StopCovid France
App version ``1.1.0``

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
| **Latest version** | 1.1.0 |
| **Last update** | 2020-06-26 14:13:47 |
| **Recent changes** | Améliorations et corrections. |
| **Installs**  | 1 000 000+ |
| **Category** | Médecine |
| **First release** | 29 mai 2020 |
| **Size**  | 17M |
| **Supported Android version**  | 5.0 ou version ultérieure |

### Description
> Avec StopCovid, participez à la protection de vos proches, de vous-même et de tous en étant alerté si vous avez été à proximité d’un utilisateur testé positif.
<br>Protégeons nos proches, protégeons-nous et protégeons les autres. 
<br>StopCovid, c’est simple :
<br># J'active l'application
<br>En utilisant le Bluetooth de votre téléphone, StopCovid détecte les téléphones des autres utilisateurs qui restent à proximité du vôtre.
<br># Je reste informé
<br>Vous serez informé si vous avez été à proximité d’un utilisateur testé positif au COVID-19.
<br># Je protège mes proches et les autres
<br>Si vous effectuez un test COVID-19 et qu’il est positif, votre laboratoire vous donnera un code à scanner ou à saisir pour avertir anonymement les utilisateurs que vous avez rencontrés.
<br>#  Mes données sont protégées
<br>L’application n’utilise à aucun moment la localisation des personnes, et il est impossible de connaître l’identité des utilisateurs
<br>.
<br>Cette application a été réalisée par l'équipe StopCovid, sous la supervision du Ministère des Solidarités et de la Santé et du Secrétariat d'Etat chargé du Numérique.


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

The StopCovid France app has been installed by more than **1000000** times. At this time, **7197** rated the app and its average score is **3.9713876**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4025

:star::star::star::star:: 1184

:star::star::star:: 607

:star::star:: 514

:star:: 864

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 5 reviews"/>
</p>

> Très facile d'utilisation ! Commencez à l'utiliser c'est très facile !<br> :date: __2020-07-27 23:13:38__

> Aucun problème avec l'application. Il ne vaut mieux pas écouter les avis négatifs de personnes qui sont juste opposés au gouvernement qui souhaite uniquement nous protéger avec cette application.<br> :date: __2020-07-27 20:10:46__

> Excellente application qui devrait être obligatoire pour lutter contre le virus. Elle devrait s'installer automatiquement sans que les gens le sachent. Tout le monde utilise Facebook sans se poser de questions.<br> :date: __2020-07-27 20:09:56__

> Plutôt que de devoir écrire nos coordonnées sur un petit bout de papier sur les plages et dans les cafés, obligeons à l'installation de StopCovid !<br> :date: __2020-07-27 08:44:13__

> OK, je conseille cette application<br> :date: __2020-07-26 22:19:22__

> Super<br> :date: __2020-07-26 20:30:21__

> Très bonne application<br> :date: __2020-07-26 19:39:56__

> Cliquez pauvre fous<br> :date: __2020-07-25 21:33:09__

> Efficace<br> :date: __2020-07-24 14:51:52__

> Bonsoir, merci pour les factures, je l'ai assuré mais je fais les démarches pour comparer les prix et changer d'assureur. La voiture va au garage debut de semaine pour la clim et normalement fin de semaine pour la distribution. Nous sommes contents que le restaurant vous ait plu. Merci, encore une fois, à vous d'être venu jusque chez nous. Loïc.<br> :date: __2020-07-24 13:38:48__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Neant pour le moment<br> :date: __2020-07-26 17:43:29__

> Application facile d'utilisation<br> :date: __2020-07-26 14:34:26__

> Utile mais un peu trop passive pour l'utisateur. L'appli serait l'endroit parfait pour pousser des stat quotidienne nationale concernant la situation.<br> :date: __2020-07-25 19:52:18__

> Je dois sans cesse vérifier que l'application est démarrée et bien souvent elle ne l'est pas. Je dois donc la rreactiver. J'imagine donc que le nombre d'utilisateurs est très faible en dépit du nombre de téléchargements.<br> :date: __2020-07-25 19:33:10__

> L'app arrete et redémarre la connexion Bluetooth de mon téléphone tous les quarts d'heure. Desinstaller stopcovid corrige le pb, preuve que c'est bien l'app. EDIT: même pb avec la dernière version.<br> :date: __2020-07-25 13:24:28__

> Galaxy S7. Pas de crash. Pas de surconsommation de batterie constatée. Sans doute ameliorable, un petit retour de temps en temps serait bien pour connaître son efficacité. Ex nombre de personnes croisées avec l'application dans la semaine.<br> :date: __2020-07-25 12:37:25__

> À part les notifications un peu trop fréquente pour signaler que l'application fonctionne, tout est ok. Ne consomme pas ma batterie. Rectification: depuis la mise à jour vers Android 10 je n'ai plus de notifications intempestives.<br> :date: __2020-07-24 20:14:33__

> J'ai l'impression que l'application perturbe le fonctionnement de mon kit mains libres, avez vous fait des essais sur ce point ?. En plus l'appli se désactive régulièrement , il faut la relancer ( quand on y pense). Finalement ce n'est pas fiable même si l'utilité est indéniable.<br> :date: __2020-07-24 13:06:31__

> Aucun souci apparent de fonctionnement. L'application reste active en arrière plan. Pas de consommation excessive de la batterie comme on peut le lire parfois. Seule réserve : rester au moins 15 minutes à moins d'un mètre d'une personne contaminée pour déclencher l'alerte auprès du serveur me paraît un peu irréel... A moins d'habiter dans une très grande ville et de voyager dans les transports en commun, cette probabilité est quand même très faible.<br> :date: __2020-07-23 18:20:44__

> J'aimerais bien que cette application puisse se réactiver automatiquement quand on reactive bluetooth.<br> :date: __2020-07-20 19:41:06__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Bof, s'arrête en permanence ! Et souvent ne s'ouvre plus et donc obligation de désinstaller et réinstaller.<br> :date: __2020-07-28 10:13:46__

> Dommage qu'il éteint souvent<br> :date: __2020-07-27 17:58:42__

> Cela marchait bien au début mais maintenant quand j'essaie de l'activer ça me demande d'être connecté à internet ! Sauf que quand je suis hors de chez moi je n'ai pas internet..<br> :date: __2020-07-26 20:42:33__

> Lp<br> :date: __2020-07-26 16:23:37__

> Ça marchait très bien et depuis aujourd'hui l'application ne marche plus ! Elle ne se lance plus du tout.<br> :date: __2020-07-24 21:36:15__

> Je trouve que 15 minutes à moins d'un mètre d'un contaminé pour déclencher une alerte, ce n'est pas très sensible. Il serait bien d'avoir des infos sur l'application : exemple nombre de contaminés détectés par l'application et dans quelles régions. Ça montrerait l'efficacité et inciterait les utilisateurs à en parler autour d'eux pour que d'autres personnes l'installent. Étant donné la recrudescence de nouveau cluster, pourquoi l'État n'incite pas à utiliser l'appli ? Ça marche réellement ?<br> :date: __2020-07-23 15:20:16__

> Bravo à ceux qui arrivent à "décrire cette expérience". Moi non. L'appli est installée, elle a l'air de fonctionner, comment s'en assurer...<br> :date: __2020-07-22 20:16:30__

> Bonne idée, mais application qu'il faut souvent désinstaller pour réinstaller car elle beugue. Dommage<br> :date: __2020-07-22 20:09:20__

> Comme bp le disent, le fait qu'il faille réactiver manuellement l'appli après avoir été en mode avion est aberrant et fait que je suis resté plusieurs fois non protégé ( habitant en zone blanche, je passe en mode avion à la maison, sinon la batterie se vide très vite)<br> :date: __2020-07-20 15:31:42__

> Simple à utiliser. Il manque le nombre de contacts rencontrés. Car on ne sais pas si cela fonctionne.<br> :date: __2020-07-20 12:46:18__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Je duid tred decu<br> :date: __2020-07-25 17:48:46__

> L'application disparaît parfois et il faut la relancer, l'alerte par notification à disparu malheureusement. Dommage, ce problème avait été résolut dans une version antérieure. J'ai passé des journées entières sans me rendre compte, à résoudre d'urgence.<br> :date: __2020-07-25 17:38:32__

> Pas au point, marche au début et après plus moyen de l'activer. Il met sans cesse ouvrir l'application et activer, je le fais mais comme la 1ère fois ça ne marche pas, 2 fois que je la télécharge et toujours le même problème!!!<br> :date: __2020-07-25 12:26:54__

> Les commentaires négatifs sur l'application sont supprimés. Elle ne démarre pas sans redémarrage de l'appareil. Le captcha nécessite un redémarrage . Sinon pour le moment ça fonctionne sans intrusion dans la vie des autres. Plus qu'à voir si elle fait son job. Surchauffe du téléphone. Trop gourmand en énergie. ( désactivez la. On dirait un vieux codage de malware)<br> :date: __2020-07-23 23:19:53__

> L'appli se désactive tout le temps pourtant Bluetooth tout le temps actif. Très décevant pour une appli de santé publique, aussi visible médiatiquement et politiquement, qui ne fait pas le job.<br> :date: __2020-07-23 14:47:37__

> Je fais partie des gens qui voyagent. Depuis la fin du confinement,  j'en suis à mon 4ème voyage à l'étranger.   Avec avions et train entre les deux.  Le fait que l'appli ne se connecte pas toute seule au bluetooth après un passage au mode avion, ou ne se remette pas en route seule après un redémarrage est une erreure, car c'est facile d'oublier de réactiver l'App quand le tel est basculé plusieurs fois par jour en mode avion .  Une option pour une réactivation auto serait souhaitable.<br> :date: __2020-07-23 07:50:11__

> Le chemin est encore loin pour que çà fonctionne correctement...<br> :date: __2020-07-22 23:27:12__

> Impossible d'activer l'application !<br> :date: __2020-07-21 19:15:13__

> Bug au démarrage<br> :date: __2020-07-21 10:13:11__

> Malgré une facilité d'utilisation l'application reste pas terrible sur certains points comme le fait qu'il faut réactiver l'application car elle s'arrête tout le temps et qu'en plus de ça elle consomme beaucoup trop de batterie ( je pouvais presque une journée avec mon téléphone je ne tenais plus qu'une matinée à cause de l'application Conclusion il y a encore du boulot !<br> :date: __2020-07-21 00:15:02__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> bug pour l activation . cs ne marche pas!<br> :date: __2020-07-28 09:03:32__

> Impossible d'ouvrir<br> :date: __2020-07-28 09:02:52__

> Impossible de se connecter, erreur du protocole Robert ?? Dommage !<br> :date: __2020-07-28 08:37:58__

> Depuis la mise à jour de fin juin, l'application ne fonctionne plus sur mon téléphone. Je l'ai réinstallée aujourd'hui mais l'installation plante. Vu tous les commentaires négatifs et l'enjeu de santé public, je ne comprends pas pourquoi aucune amélioration a été faite récemment.<br> :date: __2020-07-27 22:06:38__

> Je me demande pourquoi on nous demande de télécharger cette appli si quand il faut qu'elle nous alerte, aucune info. Cas covid dans la boite depuis 8 jours pas même une info. Pfff<br> :date: __2020-07-27 21:28:50__

> Se ferme systématiquement au démarrage. Finalement, je désinstalle. En cas de besoin, je peux retrouver ma localisation.<br> :date: __2020-07-27 18:45:27__

> J'ai installé l'appli, mais elle bloque sur la page d'activation où il faut recopier le texte visuel...<br> :date: __2020-07-27 14:37:19__

> Jsp<br> :date: __2020-07-27 12:43:16__

> Je suis obligé de relancer l'application tous les jours ou presque... Ça en devient gênant de devoir vérifier avant chaque déplacement que l'application ne se soit pas arrêtée.<br> :date: __2020-07-27 11:21:38__

> Application qu'il faut réactiver chaque fois que le téléphone sort du mode avion, donc application totalement inutile.<br> :date: __2020-07-27 10:13:29__


