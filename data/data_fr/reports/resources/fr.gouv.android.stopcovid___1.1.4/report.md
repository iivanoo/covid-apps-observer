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

> De la vraie daube façon Macron<br> :date: __2020-10-17 22:08:06__

> Rien à signaler, c'est gratuit, ça peut sauver des vies. Pourquoi s'en priver ?<br> :date: __2020-10-16 01:17:27__

> Top de mon côté ça ne plantes pas<br> :date: __2020-10-15 12:55:04__

> Très bien<br> :date: __2020-10-15 07:32:12__

> Excellente idée d'appli ! Continuez vos efforts<br> :date: __2020-10-14 21:35:20__

> Installée, opérationnelle. Acte citoyen : check !<br> :date: __2020-10-14 20:48:43__

> Top j'ai vraiment aimer ce jeux de tir rpg qui s'appelle fortnite 😐<br> :date: __2020-10-14 20:35:09__

> Pour que ça fonctionne il aurait fallu qu'il y ai des pubs sur internet et surtout à la TV pour l'appli<br> :date: __2020-10-14 20:34:52__

> Merci au gouvernement de mettre en place des moyens d'actions<br> :date: __2020-10-14 20:33:39__

> Grosse amélioration sur cette version (1.1.4#48) : J'avais tenté par 2 fois l'installation depuis sa sortie, mais l'appli était inutilisable : il fallait la réactiver sans arrêt... Lorsque l'on se rend compte après une balade que l'appli a planté, on se dit que l'intérêt est limité. Bref, une horreur qui ne valait même pas son étoile. Cela ne semble plus être la cas. Enfin! L'appli est réinstallée depuis 1 semaine. Elle fait le job en ce qui me concerne. (Je me méfie quand même)<br> :date: __2020-10-14 19:51:59__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Appli pour avertir si on est atteint de l'épidémie<br> :date: __2020-10-15 17:53:52__

> Dans la prochaine version, il serait bien de pouvoir programmer à l'avance l'activation parce que parfois on oublie au moment même. Je m'en sers mais souvent je le désactive pour économiser la batterie.<br> :date: __2020-10-15 09:17:56__

> Utile<br> :date: __2020-10-14 20:36:00__

> Ça fait ce qu'on lui demande<br> :date: __2020-10-14 13:25:36__

> L'application s'arrête régulièrement toute seule au bout de qq semaines, il faut alors y penser pour la relancer lorsque sa notification de présence disparait<br> :date: __2020-10-13 06:50:37__

> L'appli utilise pas mal de batterie, c'est dommage. Mais contrairement aux autres avis que j'ai pu lire, je n'ai aucun problème d'arrêt inopinée de l'application. J'utilise un Samsung S7.<br> :date: __2020-10-12 11:24:07__

> Simple et tellement utile qu'elle devrait etre obligatoire !. Mais elle refuse de s'ouvrir regulierement: je suis obligee de la desinstaller puis de la reinstaller...<br> :date: __2020-10-10 07:51:35__

> Apparemment la mise à jour du 15 09 2020 a désactivé l'application ! Que ce soit un bug ou un choix volontaire, c'est scandaleux s'agissant de santé publique. Combien de personnes se sont rendu compte à ce jour qu'elles ont une application supposée les protéger qui est désactivée à leur insu ? Pas étonnant que peu de gens l'utilisent...<br> :date: __2020-10-06 14:29:53__

> Bonjour, Je retrouve parfois l'application arrêtée ou "désactivée". Ill suffit de la réactiver, mais combien de temps a été perdu ? Il semble que cela soit arrivé après sortie du mode avion. J'espère aussi que la désactivation ne fait pas perdre l'historique des deux dernières semaines, sinon, tout cela devient assez inutile. Et cette interrogation n'aide pas à avoir confiance. Il manque drastiquement un affichage statistique, par exemple un histogramme du nombre de contacts par jour. Merci<br> :date: __2020-10-04 15:39:17__

> Je peux enfin l'activer..... Elle n'était même pas opérationnelle à son lancement.... Mieux vaut tard que jamais.<br> :date: __2020-10-03 09:50:53__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Il manque une notification à chaque fois qu'on quitte notre domicile par ex pour penser à la lancer<br> :date: __2020-10-15 09:10:59__

> Ma batterie meirt trop vite avec l appli malheureusement (15min -60%)<br> :date: __2020-10-14 21:24:52__

> Ce qui serait plus simple serait de généralisé dans chaque établissement, restaurants etc... Un flash code contenant les coordonnées de l'établissement dans lequel on se trouve. Ces flash code pourrait être apposé sur un coin de table ou de comptoir ou à l'entrée pour des tabacs et chaque client pourrait d'un geste flasher celui-ci afin de déclarer sa position ainsi que l'heure et la date etc.... Merci aux devs pour votre Taf... Nous battrons ensemble ce microbe.<br> :date: __2020-10-14 20:48:19__

> Pendant la configuration de l'application celle-ci est passée en anglais au moment où les gestes sanitaires sont expliqués. Depuis impossible de la repasser en français. Une idée de comment faire ?<br> :date: __2020-10-14 20:46:34__

> Mais pourquoi ne pas avoir utilisé l'API de traçage de Google & Apple comme dans les autres pays de l'UE ? Leur devise : Pourquoi faire simple quand on peut faire compliqué.<br> :date: __2020-10-12 22:10:52__

> J'ai installé cette application il y a plusieurs semaines et je me rends compte seulement aujourd'hui qu'elle n'était pas activée. Sur mon smartphone, un One+ 5T sous Android 10, le bouton d'aide pour l'activation ne renvoie pas vers le bon menu. Il faut aller dans paramètres > bluetooth > re-clicker sur bluetooth même si celui-ci est activé > activer option : "visible par appareils bluetooth à proximité"<br> :date: __2020-10-12 20:26:18__

> Je viens de l'installer sans aucun problème, mais je reçois des alertes fréquentes ( toutes les 2~3 min ) lorsque j'utilise mon smartphone pour me dire que StopCovid est activé, j'avoue c'est un peu usant à force. Y a t- il moyen de supprimer cette notification ? Mise à jour avis le 11/10/2020 Le défaut des alertes fréquentes avait été résolu, en revanche ces derniers jours il était impossible d'activer l 'appli. Le bouton était grisé. J'ai du désintaller puis réinstaller l'appli.<br> :date: __2020-10-11 09:14:23__

> De nouveau après MAJ 1.1.4 du 15/09 .. Se désactive seule en permanence malgré toutes les autorisations voulues. Version précédente le problème était déjà présent. Et version encore précédente le problème était résolu.. Le tout sur le même téléphone et installé depuis la première version dispo.<br> :date: __2020-10-10 22:34:56__

> Bizarre, l'application s'arrête sans crier gare, depuis plusieurs mois ce genre de Blague arrive régulièrement. Et là cette semaine, c'est le pompon : elle ne démarre plus du tout. J'ai du désinstaller puis réinstaller, je me demande si cette application est franchement utile...<br> :date: __2020-10-10 19:17:59__

> Je voulais savoir si l application fonctionne bien pour qu'il détecte si il y a une personne a le virus covid 19<br> :date: __2020-10-10 16:20:24__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Après des soucis de désactivation lors de mon 1er essai, nouvel essai 1h le temps d'un passage en ville. Impossible d'activer le bluetooth demandé par l'app, ok après avoir redémarré le téléphone. Batterie vidée en 5-6h dans ma poche alors que j'avais désactivé le suivi en rentrant. Je venais de le charger et j'ai habituellement 2 jours d'autonomie... Impossible de rallumer le bluetooth j'ai encore dû redémarrer le téléphone. Bref, des anomalies trop handicapantes, désinstallation.<br> :date: __2020-10-18 01:16:48__

> Personne de mes connaissances l'a téléchargé<br> :date: __2020-10-16 13:07:30__

> Ca mange toute la batterie<br> :date: __2020-10-16 10:26:47__

> Incompatibilité avec le système Google sur les téléphones Google Pixel 4a. Que fait l'état ?<br> :date: __2020-10-14 15:22:48__

> L'application Stop Covid se désactive toute seule... Quel intérêt ?<br> :date: __2020-10-14 11:25:00__

> L'application n'est jamais active, je suis obligé de vérifier si elle est activée. Un icône est affiché en permanence sur l'écran de mon téléphone. Ce fonctionnement n'est pas très clair ...<br> :date: __2020-10-14 08:37:50__

> Bluetooth obligatoire trop gourmand en énergie<br> :date: __2020-10-14 00:07:31__

> Se désactive sans arrêt et sans raison apparente<br> :date: __2020-10-12 23:25:17__

> Des que le téléphone est en mode avion l application doit être réactivée à l allumage du portable. C'est vraiment dommage.<br> :date: __2020-10-12 20:11:21__

> Après un fonctionnement erratique les premiers jours avec des désactivations sans raison évidente et plantages lors de la réactivation, l'application semble plus stable. Manque une alerte plus claire lorsqu'elle est désactivée : je m'aperçois régulièrement qu'elle n'est plus activée, sans savoir depuis combien de temps (remplacer la notification d'activation par une une notification de désactivation ?). Et comment ça se passe en avion, où le Bluetooth est censé être désactivé ?<br> :date: __2020-10-12 17:00:41__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Nul elle ne sert à rien car inefficace<br> :date: __2020-10-17 23:31:36__

> Extrêmement nul. Je veux être payer si j'utilise cette application<br> :date: __2020-10-17 23:09:01__

> La cpam ne vous donne même pas les elts pour vous déclarer dans stop covid quand vous êtes testés positif. A quoi sert donc cette application ?<br> :date: __2020-10-17 20:54:14__

> Trop nul elle ne fonctionne pas<br> :date: __2020-10-17 16:55:44__

> Bon, j'etais super motivé, mais il plante mon téléphone. Bref, ça marche pas. Je j'essaierai à nouveau plus tard.<br> :date: __2020-10-17 10:04:11__

> Inutile. J'ai eu le covid. Impossible de me déclarer sur l'application car il faut y saisir un code. Ni mon labo, ni mon médecin, ni la secsoc n'ont été en mesure de me donner ce numéro. Impossible donc d'activer LA fonctionnalité principale de l'application.<br> :date: __2020-10-17 09:32:32__

> Consomme trop de batterie Juste un conseil au développeur / gouvernement, pensez à placer un lien avec la position GPS et de définir une activation auto en cas de sortie de zone un peu comme en domotique...<br> :date: __2020-10-16 20:17:38__

> N'ai pas compatible avec tous les portables. C'est nul.<br> :date: __2020-10-16 14:36:09__

> NUL le gouvernement se sert de cette app pour ESPIONNER les gens : ouvrer les yeux, pour que l'app fonctionne, il faut que tout le monde aille se faire tester. Or ce n'est pas le cas. Donc arrêter de nous espionner !<br> :date: __2020-10-16 12:21:50__

> Ne se réactive pas automatiquement après une suspension du Bluetooth. Inutile si on ne pense pas à vérifier régulièrement l'état d'activation de l'appli.<br> :date: __2020-10-16 08:54:09__


