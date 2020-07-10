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

> Aucun problème de fonctionnement et pas de surconsommation de batterie remarquée.<br> :date: __2020-07-10 12:46:40__

> Tout a l'air de fonctionner (petite icone toujours présente en entête). Et pas encore d'annonce de contagion! Ouf<br> :date: __2020-07-09 22:18:25__

> Super<br> :date: __2020-07-09 22:10:31__

> Rassurante<br> :date: __2020-07-09 12:20:57__

> Aucune experience<br> :date: __2020-07-08 20:14:20__

> Très bien<br> :date: __2020-07-08 08:21:57__

> Bravo<br> :date: __2020-07-08 08:11:44__

> Ok, rien à redire pour l'instant. Je m'accorde avec d'autres commentaires sur l'idée d'avoir un peu plus d'infos ..... Carte des foyers épidémiques, évolution ..... Cela rendrait l'appli plus ludique ......<br> :date: __2020-07-08 06:18:07__

> Appli simple à télécharger, dommage quelle ne soit pas obligatoire ..<br> :date: __2020-07-08 03:31:08__

> Ok<br> :date: __2020-07-07 11:22:43__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Ce serait bien que l'icône dans la barre de notifications ne soit pas affiché en permanence !<br> :date: __2020-07-10 08:47:08__

> Le point faible est que l'on ne traîne pas forcément partout avec soi son smartphone... Il faudrait pouvoir conserver StopCovid actif avec soi sur d'autres supports moins volumineux, tels qu'un porte-clés, un manchon à branches de lunettes, etc.<br> :date: __2020-07-09 19:46:48__

> ca manque de statistiques a visualiser par l'utilisateur sur les données enregistrées<br> :date: __2020-07-09 08:29:17__

> Pour le moment pas d indication de cas covid fréquente.<br> :date: __2020-07-08 20:04:18__

> relevée 634a3 et 4<br> :date: __2020-07-06 16:26:14__

> Super pratique mais c'est dommage qu'il n'y ait pas de sonnerie spéciale pour cette application<br> :date: __2020-07-06 09:57:06__

> Sa peut vous aider<br> :date: __2020-07-05 16:39:03__

> Application simple à utiliser. Le seul problème, c'est que tous les soirs, je mets mon téléphone en mode avion et je le désactive tous les matins. Cela désactive automatiquement stopcovid et, du coup, il faut le réactiver tous jours. C'est un peu lourd...<br> :date: __2020-07-05 09:17:49__

> Bonne application, manque juste un compte rendu .<br> :date: __2020-07-04 19:45:18__

> Zoé a été très occupée par la<br> :date: __2020-07-04 15:30:37__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Se désactive tous le temps.... obligé d'ouvrir l'appli et de réactiver, pour être en marche<br> :date: __2020-07-10 07:52:01__

> L'application semblait fonctionner correctement depuis le début mais depuis la mise à jour, elle semble se désactiver toute seule, obligé de vérifier qu'elle tourne.<br> :date: __2020-07-09 20:52:33__

> Se désactive régulièrement et depuis la dernière mise à jour, ne s'active plus du tout<br> :date: __2020-07-09 19:04:21__

> Impossible de télécharger sur mon smartphone et impossible d'activer sur ma tablette... dommage pour moi (et pour les autres....)<br> :date: __2020-07-09 19:03:03__

> Tout allait bien jusqu'ici mais l'appli me demande de télécharger une nouvelle version ce que j'ai fait mais, même si la fenêtre indique maintenant "installée "et non plus "installer " le système continue à me dire qu'il y a un problème et qu'il faut que j'installe la nouvelle version....! Il doit y avoir un bug!<br> :date: __2020-07-09 18:52:07__

> Application qui se désactive sans raison apparente. Il faut alors relancer l'application manuellement (si/quand on s'en aperçoit) et impossible de savoir combien de temps l'application est restée inactive. Du coup, gros bémol sur son utilité.<br> :date: __2020-07-09 18:12:32__

> Cela serait mieux si l'activation et désactivation du bluetooth était automatique, lors de l'activation de l'appli.<br> :date: __2020-07-09 18:07:42__

> Utilité. Dommage, peu d'informations Les modifications de l'application sont très très longues à charger!!!<br> :date: __2020-07-09 09:41:42__

> Se désactive tout le temps et sans alerte. Du coup, je m'en rends compte beaucoup plus tard.... D'où une utilité limitée ! Sinon, pas de problème d'installation ou de bug.<br> :date: __2020-07-09 08:52:19__

> Bof, s'arrête en permanence ! En plus, vu le nombre de personnes qui ne mettent plus de masques dans les transports en commun, je ne crois qu'une personne contaminée activera l'appli !<br> :date: __2020-07-08 19:50:12__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Je suis partisan de ce genre d application, cependant l application ne fonctionne que si on lui laisse accès aux notifications. Celles-ci deviennent des spams !!!! Je l ai donc désactivé.<br> :date: __2020-07-10 11:19:59__

> Desactivation à chaque arrêt du téléphone, dommage, cela réduit l intérêt de l appli<br> :date: __2020-07-09 21:16:39__

> Bugs régulièrement et je n'arrive pas à me connecter car ferme l'appli automatiquement<br> :date: __2020-07-09 12:59:26__

> L'application fonctionnait parfaitement au début (installée le 2ieme jour), mais depuis 3 semaines, elle crashe constamment. J'ai effectué les différentes mise à jour, désinstallé puis réinstallé mais le problème persiste. Du coup cette appli pour moi perd complètement de son intérêt et de son utilité ! Mon Smartphone est un Lenovo Motorola 5GS à jour de ses updates. Je partage tout à fait l'avis des personnes qui disent qu'il est dommage que nous n'ayons pas plus de retour sur l'efficacité de ce dispositif public sanitaire, sur le nombre de personnes qui l'utilisent en même temps ...<br> :date: __2020-07-09 12:45:18__

> Se désactive tout seul et nécessite des actions complémentaires pour s'exécuter au démarrage<br> :date: __2020-07-08 14:51:30__

> Ce desactive toujours<br> :date: __2020-07-08 09:22:45__

> Ça marchait très bien depuis le 1er jour jusqu'à il y a quelques jours, mais depuis, elle me demande de mettre en fonction le Bluetooth et la géo-localisation, alors que c'est déjà fait. La seule solution que j'ai trouvé est d'autoriser tout, appareil photo, stockage etc... Sans, ça ne s'active pas. Autant dire que bien sûr je ne l'active plus, et si ce n'est pas corrigé je vais la desinstaller. C'est dommage car je pense, qu'elle pourrait servir en cas de 2rme vague..<br> :date: __2020-07-08 00:17:12__

> Cette version semble plus stable. Pas de plantage pour l instant. Maintenant je rejoins les avis pour la rendre plus fun et augmenter le nbre de téléchargement. +1 etoile avec cette version mais pas plus car je ne sais meme pas si elle fonctionne et combien de personnes j ai croisé.<br> :date: __2020-07-07 22:49:50__

> Se desactive tout le temps. Il me faut la réactiver plusieurs fois par jour et donc la protection est souvent inexistante.<br> :date: __2020-07-07 18:56:41__

> Elle se desactive constamment. Si on oublie de la réactiver et au même temps on croise une personne qui a le covid ou des personnes en général ça sert presque à rien<br> :date: __2020-07-07 18:19:06__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Depuis ce matin, l'application se desactive automatiquement toute seule. Impossible de la reactiver.<br> :date: __2020-07-10 13:13:36__

> Nul<br> :date: __2020-07-10 12:13:04__

> Ne fonctionne plus depuis quelques jours. Refuse de démarrer. Pas de réaction des développeurs, dommage car j'ai vu que je ne suis pas le seul... Déjà qu'il y a peu de monde qui la télécharge, ça n'aide pas.<br> :date: __2020-07-10 11:49:12__

> Sceptique sur l'utilisation centralisée des informations, même anonymisées<br> :date: __2020-07-10 10:30:26__

> Impossible d'activer stop covid, j'ai le spinner au moment d'entrer le code visuel et je peux plus rien faire, application inutilisable<br> :date: __2020-07-10 09:53:39__

> Impossible à télécharger donc inutile<br> :date: __2020-07-10 09:32:32__

> Ne fonctionne pas<br> :date: __2020-07-10 09:11:28__

> Pas utile car ne reste pas actif en permanence. Il faut penser a l'ouvrir a chaque déplacement. Google connait tout mon historique, mais pas stop Covid<br> :date: __2020-07-10 08:18:01__

> Impossible d'activer l'application je laisse tomber<br> :date: __2020-07-10 00:32:14__

> La vérification par code visuel ou audio ne marche pas pour activer l'appli, essayé au moins 20 fois...Et apparemment je ne suis pas le seul à avoir des problèmes au vue des commentaires. Incroyable, 1 appli gouvernementale censée freiner le covid, plus d'1 mois après sa sortie, qu'on ne peut même pas activer...<br> :date: __2020-07-10 00:30:28__


