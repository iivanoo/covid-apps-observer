# StopCovid France
App version ``1.1.3``

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
| **Latest version** | 1.1.3 |
| **Last update** | 2020-08-07 10:56:14 |
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

The StopCovid France app has been installed by more than **1000000** times. At this time, **9182** rated the app and its average score is **2.878821**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3017

:star::star::star::star:: 932

:star::star::star:: 801

:star::star:: 781

:star:: 3648

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 5 reviews"/>
</p>

> StopCovid France est très efficace.<br> :date: __2020-08-22 21:19:51__

> Très bien je n'ai pas rencontré aucun Covid..pour vu que ça dure.<br> :date: __2020-08-22 13:02:16__

> Bonjour, Suite aux nombreux commentaires au sujet de dysfonctionnements, je vous adresse ma candidature pour un contrat en alternance en développement démarrant en octobre 2020. Cordialement<br> :date: __2020-08-21 09:09:30__

> Ça devrait être obligatoire sur tout les téléphones je sais pas pourquoi c'est pas le cas 😕<br> :date: __2020-08-20 17:44:33__

> Pour ne pas mourir d'une petite grippette Trumpette ou Bolsonarotte.<br> :date: __2020-08-20 13:50:18__

> Appli fonctionne si elle ne fonctionne pas allez vide le cache de l'application et effacer les données... Cela fait cela depuis la mise a jour, cela devrai résoudre votre problème<br> :date: __2020-08-20 12:31:26__

> Parfait<br> :date: __2020-08-20 12:24:23__

> L'idée est bonne et civique. Malheureusement certains politiciens ont rendu cette app inefficace sous le prétexte de défendre une soit disant liberté ! Le pire est qu'ils seront capables de la critiquer sans réaliser qu'ils en sont la cause !<br> :date: __2020-08-19 19:43:55__

> un des outils nécessaires parmi tous les moyens à notre disposition<br> :date: __2020-08-19 16:09:46__

> superbe application. je la recommande. Il serait bien que tout le monde l'a télécharge comme ça on pourrait enfin lutter contre cette cochonnerie et s'en sortir s'il vous plaît téléchargez-la<br> :date: __2020-08-19 02:13:55__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Après avoir réinstaller le téléphone. Cela semble fonctionner. L application reste active Après avec le nombre d'utilisateur j'ai un doute que cela permet de détecter rapidement épidémie.<br> :date: __2020-08-22 13:33:05__

> Marche à partir du moment où on fait attention si bluetooh en fonction. Se vérifie facilement<br> :date: __2020-08-22 09:59:00__

> Dommage que si peux de gens l'utilisent...<br> :date: __2020-08-20 12:58:10__

> Idée sur le principe très efficace. Malheureusement, la stupidité humaine fait que chacun pense à ça petite personne sans penser au collectif...<br> :date: __2020-08-20 02:20:59__

> Cette appli part d une bonne initiative, mais il serait peut être bien d avoir une option/application pour savoir dans quelle rue mettre le masque.<br> :date: __2020-08-15 12:03:23__

> Consommé beaucoup de batterie. Sinon, l'idée est bonne.<br> :date: __2020-08-14 08:10:14__

> Pas de retour techniquement negatif. Le travail est bien fait. Les avertissements sont clairs. Neanmoins, il y a deux axes d'amélioration significatifs car je desactive l'application en revenant chez moi ou dans la voiture. - Activation programmée par plages horaires - Widget d'activation et de desactivation pour activer plus spontanément l'application.<br> :date: __2020-08-14 07:46:59__

> Aucun pb de fonctionnement sur moto z2 force. Pas de pb de consommation de batterie, pas de pb d'arrêt/relance intempestif, pas de pb de confidentialité, très facile d'installation... Ah si un gros pb: c'est français. D'où très certainement le french bashing des commentaires un peu trop systématique ci dessous. En fait le seul vrai pb , c'est l'égoïsme de certains qui rejoint celui de ceux qui ne veulent pas porter de masque.<br> :date: __2020-08-13 09:04:14__

> Bie<br> :date: __2020-08-12 22:40:54__

> POUR L'INSTANT pas recu d'alerte et tant 😉😷<br> :date: __2020-08-11 21:55:29__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Trop peu d'utilisateurs<br> :date: __2020-08-23 10:21:23__

> L'appli semble enfin fonctionner avec le dernière version. Elle ne se ferme plus toute seule. Il aura fallut du temps.<br> :date: __2020-08-22 12:31:59__

> Le bluetooth consomme beaucoup la batterie. Je ne l'utilise que dans les transports. Dommage, l'idée de cette application est bonne mais pas suffisamment de personnes ne l'utilise pour qu'elle soit efficace<br> :date: __2020-08-22 01:29:19__

> Je l utilise lorsque je vais dans un magasin et des que je sort je l arrête car il consomme de la batterie.<br> :date: __2020-08-21 21:26:11__

> L'application se deconnecte. On s'aperçoit à un moment donné qu'on n'est plus connecté. Du coup, cela perd de son intérêt.<br> :date: __2020-08-21 05:53:28__

> L'installer d'office et sans bluetooth serait une bonne idée<br> :date: __2020-08-20 22:43:56__

> Pénible ! Une appli qui se désactive toute seule. Il suffit de mettre en mode avion ou de couper le bluetooth pour que l'appli se désactive. Il faut penser ensuite à la réactiver. Bilan : une appli qui sert quand on y pense alors quelle devrait être activé 100% du temps. A CORRIGER D'URGENCE<br> :date: __2020-08-19 18:10:13__

> L'application pourrait être utile peut-être si elle ne se fermait pas régulièrement. Il faut penser à la relancer. Je ne parle pas du message dans les notifications "Veuillez ouvrir Stop Covid" pour le réactiver, là dessus pas de souci. J'ai vérifié les autorisations et comparé par rapport à une autre appli qui fonctionne parfaitement en arrière plan, les autorisations sont pourtant les mêmes. Quant à l'utilité je ne suis pas sûr que beaucoup de gens se déclarent positifs via l'application ... mais si on n'essaie pas... D'autre-part, une question que je me pose ... je viens de changer de téléphone ; je n'ai rien trouvé qui permette de récupérer l'historique. L'application se base-t-elle sur le compte Google utilisé pour récupérer les données de l'historique ou ces données sont-elles perdues ?<br> :date: __2020-08-19 10:08:40__

> Trop energivore pour mon portable<br> :date: __2020-08-18 18:14:15__

> Pas de statistique disponible ( combien de personnes ayant l'appli ai je croisé ?) Et si peu de gens l'ont elle ne sert a rien. C'est étrange que tous le monde accepte des appli comme f...Book / twi.../ Snap../.... Qui nous espionne 24/24 sur des montagnes de parametres et que peu de gens activent stopcovid au prétexte que ça nous espionne sur 1 seul paramètre pour notre bien commun.<br> :date: __2020-08-15 10:50:07__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Obligé d'activer l'appli à chaque redémarrage du téléphone... Sniff!<br> :date: __2020-08-22 16:08:43__

> Tres bonne idee pour limiter la propagation de ce virus ! J'ai telecharge cette version debut juillet. Plantage de l'application avec necessite de la redemarrer. De plus elle semble entrainer un plantage du telephone : impossible d'utiliser le telephone apres un appel telephonique car perte de l'affichage. Ca revient quelques dizaines de minutes ou heures. Peut etre que la version paru en aout fonctionne mieux.<br> :date: __2020-08-20 20:13:57__

> Je c ps comment l'utiliser<br> :date: __2020-08-20 13:25:53__

> Se désactive tout le temps, je reçois régulièrement une notification pour activer le service, c'est plus que chiant...<br> :date: __2020-08-19 14:16:33__

> Contre virus sa protège aussi.<br> :date: __2020-08-18 22:04:09__

> On passe son temps à devoir réactiver l application après passage en mode avion ou la deactivation temporaire du bluetooth... résultat l appli et lancée mais elle ne sert souvent à rien puisque désactivée toute seule...<br> :date: __2020-08-18 11:16:58__

> S'arrête immédiatement C'est la troisième fois que je dois installer<br> :date: __2020-08-16 20:59:30__

> Ne fonctionne pas du tout sur mes 2 telephones qui n'ont pas le "BLE". j'aurai accepte de vider ma batterie plus vite. La sante n'a pas de prix et comme je sors tres peu, ce n'est vraiment pas genant que temporairement la batterie se vide plus vite. Parfois j'emmene ma tablette sur laquelle stopcovid fonctionne mais c'est lourd et encombrant. Je vais devoir acheter un new tel en esperant que ca fonctionne dessus... A quand la version qui ignore l'absence de " BLE" ?<br> :date: __2020-08-16 19:03:28__

> Ne fonctionne plus. Démarrage avec beaucoup d'avertissement a valider. Non convivial. N'averti pas de l'arrêt de l'appli si BT désactivé. Déçu. Un outil qui n'aura pas d'impact positif contre le Covid en France<br> :date: __2020-08-16 18:38:30__

> Je ne comprends pas pourquoi l'application ne peut pas d'elle-même activer le bluetooth lors alors qu'il est désactivé (permissions Android 10 ?)<br> :date: __2020-08-16 16:30:14__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Plus d'une semaine depuis la mise a jour qui empêche le fonctionnement et pas de correctif !! La mise a jour indique "amélioration et correction". La version précédente fonctionnait. Impossible d'activer celle ci. L'application se ferme après avoir cliqué sur "j'active". java.io.IOException: javax.crypto.AEADBadTagException Toujours pas de correctif alors que le virus sévit encore !!!<br> :date: __2020-08-24 08:06:09__

> Aucune solution toujours le meme problème cette application ne sert à rien elle arrête toute seule<br> :date: __2020-08-24 07:04:35__

> Inefficace<br> :date: __2020-08-23 20:53:28__

> Se désactive en permanence, mais aucune notification particulière ne le signale. Dommage l'idée est bonne<br> :date: __2020-08-23 20:14:12__

> Décharge rapidement la batterie.<br> :date: __2020-08-23 19:53:37__

> Je fonctionne pas sur Xiaomi redmi note 5<br> :date: __2020-08-23 11:24:49__

> Impossible de l'activer depuis la dernière mise à jour : s'éteint immédiatement<br> :date: __2020-08-23 09:09:40__

> Cela fait 3 fois que je dois la désinstaller / réinstaller car l'application se met à disfonctionner d'un coup... Elle de désactive toute seule. C'est pénible !<br> :date: __2020-08-23 09:05:17__

> Appli plante et impossible de redémarrer.<br> :date: __2020-08-22 15:18:55__

> l'App n'utilise le système de notification d'exposition officiel SNE (COVID-19) alors que tout les mobile ont reçu cette mise a jour il y a plusieurs mois et pour activer cette fonctionnalité de prévention COVID il faut une app SNE (COVID-19) officiel, donc sauf si les développeurs reconfigure l'App pour qu'elle fonctionne avec le SNE (COVID-19) officiel, je pense pas que cette app soit réellement efficace, la France devrait se basé sur l'App Canadienne Système de Notification d'Exposition<br> :date: __2020-08-22 13:05:52__


