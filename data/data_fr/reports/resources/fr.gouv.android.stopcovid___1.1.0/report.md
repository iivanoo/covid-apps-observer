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

> Pas de soucis avec cette application.<br> :date: __2020-06-28 18:27:29__

> Très bien<br> :date: __2020-06-28 18:22:40__

> Application fiable et transparente. Aucune interférence avec le fonctionnement de mon smartphone.<br> :date: __2020-06-28 18:06:48__

> Impérative application.<br> :date: __2020-06-28 17:34:58__

> J'essaie de la télécharger mais je n'y arrive pas<br> :date: __2020-06-28 16:35:54__

> Tout le monde devrait la télécharger !<br> :date: __2020-06-28 16:33:30__

> Parfait<br> :date: __2020-06-28 14:48:03__

> Simple et sur. Aucun pistage personnel.<br> :date: __2020-06-28 14:17:50__

> 👍<br> :date: __2020-06-28 13:49:34__

> Je l'active lorsque je sors , pas contraignant , ça me rassure, je n'oublie pas quand même mon masque et le gel hydroalcolique.<br> :date: __2020-06-28 12:50:40__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Très bien<br> :date: __2020-06-28 17:04:12__

> Bonjour Impossible à installer sur samsung SM-J600FN de mon épouse, alors qu'elle est sous androidone version 10. Avez-vous une solution ?. J'ai un Nokia, androidone version 10, et aucun problème. J'avais un windowsphone 10, que je quitte à regret (car plus facile à paramétrer et plus convivial), et l'application n'est pas disponible, alors qu'il y a encore des utilisateurs.<br> :date: __2020-06-28 16:58:40__

> Application simple et adaptée aux circonstances car il faut continuer à être vigilant.<br> :date: __2020-06-28 16:27:49__

> Dans tous les cas, il ne peux qu'être utile de participer à cette expérience quelle fasse progresser (c'est mieux) ou quelle échoue.<br> :date: __2020-06-28 13:18:41__

> ளபக்ஷக்ஷக்ஷிளணட டகஙஙஙணண<br> :date: __2020-06-28 11:00:03__

> Depuis la dernière MAJ, l'application s'arrête lors se son activation...<br> :date: __2020-06-28 09:58:17__

> Le bug qui faisait planter l'application au démarrage semble avoir été résolu donc je remonte ma note. L'application est très claire sur son fonctionnement et la confidentialité des données, dommage que trop peu de personnes l'utilise mais c'est de la responsabilité des citoyens.<br> :date: __2020-06-28 08:47:49__

> Très bien, mais ne pourrait on pas visualiser le trafic potentiellement à risque des zones traversées ? Cela permettrait d'inciter aux gestes barrières.<br> :date: __2020-06-28 08:45:28__

> Securisant<br> :date: __2020-06-28 08:08:50__

> Application utile et simple. Doit être réactivée de temps en temps, je ne sais pas pourquoi.<br> :date: __2020-06-28 07:36:43__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Principe est bon mais consomme beaucoup de batterie<br> :date: __2020-06-28 18:15:23__

> J'ai compris le principe de cette application. Ce qui me chiffonne un peu, c'est que si une personne positive au covid ne se déclare pas, j'aurai beau avoir l'application qui ne me servira à rien si je rencontre cette personne.<br> :date: __2020-06-28 17:01:18__

> Le bluetooth une technologie sur base de version toute différente.<br> :date: __2020-06-28 15:11:07__

> Cette applic se desactive trop souvent.<br> :date: __2020-06-28 14:06:36__

> Je débute pour l'instant ça va nous verrons plus tard<br> :date: __2020-06-28 13:39:56__

> L'Appli fonctionne sur mon A3 2016 (android 7.0). Pas eu le problème cité par un autre utilisateur d'A3 2016. La batterie ne semble pas souffrir visiblement. En revanche, il faut réactiver le fonctionnement de l'app une ou 2 fois par jour, car elle s'inhibe toute seule. A voir si la màj de l'app corrige ce problème.<br> :date: __2020-06-28 12:55:26__

> sans plus !<br> :date: __2020-06-28 10:42:54__

> Raz le bol de la notification sonore tous les matins à 8h pour me rappeler que l'application fonctionne ! Si la mise à jour modifie cela, je continue, sinon je supprime l'application.<br> :date: __2020-06-28 08:58:05__

> Je pense qu'elle fonctionne. Mais je n'aurais un retour que si je suis en contact. Pour l'instant je n'ai pas eu de retour<br> :date: __2020-06-28 07:39:10__

> Je ne crois pas à stopcovid malheureusement bien trop peu d utilisateurs ont mis stopcovid dans leur téléphone et donc peu de réactivité.... Il aurait du être obligatoire...<br> :date: __2020-06-28 06:38:23__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Volontaire je l'ai installé, et hop on ne pense pas chaque jour à mettre le bluettooth. Aprés encore ce weekends je vois les 3/4 des gens sans masques, magasins, restaus, rues, bisous et serrages de mains etc... donc si 75% des gens se moquent de cette hygiène qui est primordiale, je suppose que 75% se moquent litteralement de cette application. Il faudrait que toutes les déclarations Covid 19 soit déclarées en toute transparence sur une carte nationale IGN. Plus de sensibilisation !!! Pas dur !<br> :date: __2020-06-28 17:13:21__

> 1/Se déconnecte tout seul 2/ Conso batterie trop portante.<br> :date: __2020-06-28 14:54:59__

> Garder le bluetooth ouvert peut permettre a des personnes mal intentionnées de recuperer nos données. Ce n est pas une bonne idee d avoir choisi cettetechbisue<br> :date: __2020-06-28 12:48:23__

> Jamais averti<br> :date: __2020-06-28 12:27:05__

> Ne fonctionne pas hors reseau<br> :date: __2020-06-28 11:00:46__

> Nul il marche pas sur Android Mais il marche sur iphone (Apple) Je suis vraiment déçu<br> :date: __2020-06-28 10:49:10__

> Le Bluetooth est très énergivore .<br> :date: __2020-06-28 10:43:00__

> Simpliste sommaire non intuitif aucune certitude quant à son fonctionnement<br> :date: __2020-06-28 10:30:48__

> Malheureusement trop peu de personnes ont du télécharger cette appli. Donc aucun résultat. Pourtant je bosse dans des endroits où il y a eu des cas de CORONAVIRUS et certains qu'il y en a encore.<br> :date: __2020-06-28 10:18:44__

> Consomme énormément de batterie du téléphone<br> :date: __2020-06-27 23:55:38__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Se désactivé sans arrêt<br> :date: __2020-06-28 16:54:49__

> Autoriser le gouvernement à vous suivre à la trace : toujours une bonne idée... Ça se saurait si le gouvernement avait l'habitude d'espionner les citoyens sans autorisation et aussi voler les données privées sans contrepartie ni contrôle ...<br> :date: __2020-06-28 16:18:16__

> La mise a jour ne se fait pas<br> :date: __2020-06-28 16:03:04__

> Impossible de l'activer..<br> :date: __2020-06-28 14:35:33__

> Je la télécharge juste pour mettre une étoile et critiquer alors que je ne l'utiliserai jamais et même pire je la desinstalle directement. Halte au flicage, au traçage des personnes ici c'est la France pas la Chine.<br> :date: __2020-06-28 14:30:52__

> L'application ne peut pas fonctionner avec mon Samsung Galaxy J7. Système Bluetooth non compatible...aucune possibilité de le télécharger. Extrêmement déçue...<br> :date: __2020-06-28 14:18:26__

> Non téléchargeable sur Samsung J6 c'est dommage Une de mes connaissances souhaitait l'installer sur son Samsung Android J6 mais cela n'est pas possible<br> :date: __2020-06-28 12:06:31__

> Inutile<br> :date: __2020-06-28 11:54:10__

> Impossible à télécharger<br> :date: __2020-06-28 11:34:25__

> Cette application ne sert à rien, je l'ai installée dès les premiers jours. Elle se déconnecte très souvent.<br> :date: __2020-06-28 11:03:59__


