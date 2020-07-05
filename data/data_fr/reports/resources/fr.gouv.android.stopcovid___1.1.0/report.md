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

> Calme plat pour le moment, mais heureuse de participer à la prévention de cas de covid 19<br> :date: __2020-07-05 12:46:28__

> Top. Encourager la pratique chez les jeunes ( un djeunz de 55 ans!)<br> :date: __2020-07-04 21:24:47__

> Très bonne application. Elle devrait être obligatoire pour se battre contre le COVID19.<br> :date: __2020-07-04 21:15:53__

> Fonctionne en ar plan en toute discrétion et en toute transparence avec la notif d'exécution. Franchement si ça peut éviter de se reconfiner je signe. Côté confidentialité j'ai un compte Google, et facebook alors....<br> :date: __2020-07-04 21:02:52__

> Tout est parfait MERCI<br> :date: __2020-07-04 20:57:09__

> Super<br> :date: __2020-07-04 20:52:58__

> S arrêté souvent<br> :date: __2020-07-04 20:03:08__

> Aucun problème avec mon Samsung S8. Elle reste activée tout le temps. Je ne comprends pas les autres utilisateurs qui voudraient la désactiver selon des plages horaires. Complexité inutile. Mais j aimerais bien avoir un compteur qui me dise combien de personnes croisées avaient l appli. Ça aiderait à se sentir moins seul et à avoir l impression qu en utilisant l appli, on est utile<br> :date: __2020-07-04 19:04:38__

> Je pense que les messages gouvernementaux diffusés sans cesse sur toutes les chaînes et radio sont obsolètes. Il faudrait montrer comment mettre son masque et surtout comment ne PAS le mettre de plus en plus de personnes le mettent sous le nez. Également les conseils pour le retour de l extérieur, comment jeter son masque ou comment le laver. On entend tout et n importe quoi. Enfin profiter de ces sports pour inviter les personnes à télécharger ce site, car seulement 20 % l ont faitMerci<br> :date: __2020-07-04 09:35:18__

> Tres bonne application<br> :date: __2020-07-04 09:08:14__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Application simple à utiliser. Le seul problème, c'est que tous les soirs, je mets mon téléphone en mode avion et je le désactive tous les matins. Cela désactive automatiquement stopcovid et, du coup, il faut le réactiver tous jours. C'est un peu lourd...<br> :date: __2020-07-05 09:17:49__

> Bonne application, manque juste un compte rendu .<br> :date: __2020-07-04 19:45:18__

> Zoé a été très occupée par la<br> :date: __2020-07-04 15:30:37__

> est amène de<br> :date: __2020-07-03 19:03:32__

> Un bémol : l'application consomme beaucoup d'énergie, je recharge mon téléphone dans la journée<br> :date: __2020-07-03 12:18:07__

> J'ai une notification persistante pour m'informer que l'appli est active (inutile) et je reçois des notifications vides de l'application... Si l'appli fonctionnait bien au début, depuis plusieurs jours sur One Plus 5 (Android 9), elle se ferme toute seule dès l'ouverture.<br> :date: __2020-07-03 08:14:33__

> Il faut penser a la réactiver régulièrement<br> :date: __2020-07-02 08:20:12__

> Indispensable !<br> :date: __2020-07-02 07:56:49__

> Application discrète et finalement pas trop gourmande en batteries<br> :date: __2020-07-02 07:23:06__

> Bug et s'arrête depuis mise à jour, sur Xperia<br> :date: __2020-07-01 21:20:16__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> L'application en elle-même est utile, mais elle est inutilisable car elle s'arrête 2 à 3 secondes après. Si vous pourriez corriger cette erreur ce serait bien En vous souhaitant une bonne journée Cordialement Appareil utilisé actuellement : Wiko Harry 2<br> :date: __2020-07-05 13:18:32__

> Difficile d'avoir un avis sur l'efficacité de l'appli tant qu'on ne croise pas de malades... Mais elle envoie en permanence une notification d'activité (c'est pénible) ou de désactivation puisqu'elle se déconnecte seule 😥<br> :date: __2020-07-05 10:03:18__

> L'application n'autorise pas l'optimisation de la batterie. C'est vraiment handicapant car le téléphone se décharge trop vite. Merlin en usage normal.<br> :date: __2020-07-04 21:47:32__

> L appli se désactivé toute seule il l'a réactiver quand j y pense pas pratique<br> :date: __2020-07-04 21:27:35__

> J ai téléchargé cette appli dans le but de faire mon devoir civique (et oui tout le monde parle de DROITS mais nous avons aussi des DEVOIRS (beaucoup semble l oublier mais ce n est pas le sujet ici)). L aplli est très bien faite mais a un défaut majeur, celui de noups informer de personne positive qu une fois l avoir cotoyer 15 mn. Quel intérêt ??? C est " dans l instant " que nous devons savoir, afin de ne pas cotyer plus longuement la/les personnes concernées. Ceci dit, bravo pour le travail.<br> :date: __2020-07-04 18:58:28__

> Je suis d'accord pour participer à la lutte contre le covid mais si vous pouviez faire en sorte que je ne sois pas sans arrêt en train de réactiver l'application.....<br> :date: __2020-07-04 15:31:56__

> Tous contre le covid 19<br> :date: __2020-07-04 09:37:25__

> R A S<br> :date: __2020-07-03 15:37:48__

> En effet, l'application se ferme d'elle même régulièrement, et on ne s'en aperçoit pas tout de suite... donc des trous dans les mailles du filet. A améliorer.<br> :date: __2020-07-03 13:58:58__

> La dernière étape de l'installation est laborieuse, elle se bloque, il faut recommencer plusieurs fois, le capcha n'est pas lisible, etc<br> :date: __2020-07-03 10:43:24__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Il faut tout le temps réactiver l application mais il faut s en apercevoir, pas évident plus il manque quelques info pour savoir si l appli fonctionne correctement<br> :date: __2020-07-05 12:46:08__

> Désinstallee, Trop energivore .<br> :date: __2020-07-04 13:28:19__

> Impossible d'activer après la mise à jour car impossible d'écrire le texte. Dommage<br> :date: __2020-07-04 11:34:32__

> L'appli a sans arrêt besoin de mon intervention, elle s'arrête toute seule, etc.. Redmi Note 8 Pro<br> :date: __2020-07-03 19:13:09__

> Je l ai chargée. Mais inutile si personne ne le fait. Dommage<br> :date: __2020-07-03 17:28:44__

> Il faut réactiver à chaque fois l'application quand le téléphone est éteint, ce n'est pas pratique. J'oublie une fois sur deux de l'activer donc quelle efficacité ? Ce jour, impossible de l'activer, message d'erreur, trop de personnes l'ont téléchargé, dommage que cette appli ne soit pas prévue justement pour des millions de téléchargements...<br> :date: __2020-07-03 12:47:38__

> Démarrer sans internet me donne un crash et après ça ne marche plus. Je dois le désinstaller et encore installer.<br> :date: __2020-07-02 15:31:56__

> Aucune description sur le mode d'alerte. Comment cela se présente si on se trouve en présence prolongée d'un infecté ?<br> :date: __2020-07-02 15:31:29__

> Je ne veux pas activer la géo-localisation, même si stopcovid ne l'utilise pas.<br> :date: __2020-07-02 08:00:31__

> Ça fait 4 fois que j'installe et désinstalle cette application et l'on me demande d'activer la géolocalisation alors que je le fais....de plus ça se coupe toujours<br> :date: __2020-07-01 21:00:52__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Sollicite trop la batterie...<br> :date: __2020-07-05 10:33:27__

> Se désactive lorsque l'on éteint le téléphone<br> :date: __2020-07-05 07:23:58__

> Application à l'image de la société : Ça aurait pu le faire mais ça le fait pas. Embauchez des pro peut-être que l'application fonctionnera !<br> :date: __2020-07-05 06:56:25__

> Toujours une notification qui s'affiche sur le téléphone, enlever cette notification permanente<br> :date: __2020-07-04 23:08:48__

> C pas compatible avec mon téléphone du coup c'est pas très cool😞<br> :date: __2020-07-04 21:52:12__

> Comment cette app qui ne fait que de la tâche de fond peut elle consommer autant de batterie ?<br> :date: __2020-07-04 21:12:26__

> Ne fonctionne plus depuis quelques jours. Refuse de démarrer.<br> :date: __2020-07-04 21:11:40__

> Vu le peu d'utilisateur, j'ai un doute sur sa réelle efficacité, ...<br> :date: __2020-07-04 20:35:29__

> Non installé. Le big brother très peu pour moi. Seule la vaccination serait utile. Quid de ceux qui n'ont pas de portable ou qui ne l'allument que rarement. Réponse de technocrates à un problème de santé vitale.<br> :date: __2020-07-04 20:07:45__

> J'ai téléchargé l'application par "civisme " mais je pense que même pour moi qui suis médecin, la probabilité d'être 15 minutes à moins d'un mètre d'une personne contaminée est quasi nulle (je ne suis pas allé à la fête de la musique...). J'ai eu le Covid19 comme beaucoup de soignants et malgré des précautions draconiennes mais probablement prises trop tardivement par défaut de conseil de l'ARS. Je pense que ce dispositif ne peut être efficace que si on en augmente la sensibilité. Dr P Guibé<br> :date: __2020-07-04 19:51:33__


