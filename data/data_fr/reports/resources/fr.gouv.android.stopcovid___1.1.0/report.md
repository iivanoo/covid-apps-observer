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

> Très bien<br> :date: __2020-07-20 09:14:20__

> Tb<br> :date: __2020-07-20 09:11:29__

> Si toute les applications été aussi clair quand on les installés<br> :date: __2020-07-20 07:28:05__

> Bonjour à tous cela fait un peu près 4 jours que j'ai installé sur mes deux portable S9 Samsung et S10 et l'application fonctionne très bien il y a pas de déconnexion du bluetooth en tout cas jusqu'à ce jour comme j'ai vues sur certains messages. Dimanche 19 juillet 20 je viens confirmer ce que disait les internautes effectivement il se déconnecte. C'est quand la mise à jour les développeurs<br> :date: __2020-07-19 14:54:08__

> Je me sens en toute sécurité. Cette application est formidable<br> :date: __2020-07-18 16:40:18__

> Fonctionne parfaitement, se désactive automatiquement lorsque je passe en mode avion et se réactive automatiquement lorsque je l'enlève.<br> :date: __2020-07-18 09:15:34__

> L'application pour ma part ne se désactive pas tout le temps comme certains peuvent le dire. Je la recommande donc car c'est bien et bon pour la société !<br> :date: __2020-07-18 00:11:12__

> Application en service après les 1er test (j'ai attendu 2 semaines) pas de crash, après un reboot il a redémarré également seul. Pas de point négatif sauf la consommation qui augmente un peu. Utilisé sur galaxy note 9 . J'espère que plus de monde le chargera mais je doute fort que cela soit le cas. On préfère se faire "tracer" par Facebook, Tweeter, Google,... mais pour la sécurité nationale... ha ben non faut pas délirer man. Genre... non mais... bref c'est bien dommage... mais sinon ça marche<br> :date: __2020-07-18 00:01:57__

> Aucun problème d installation. L application est très stable.elle se désactive quelques secondes parfois mais se réactive toute seule.<br> :date: __2020-07-17 23:16:40__

> Je n'ai pas encore été testé positif, mais au niveau information sur la sécurité des données c'est un exemple a suivre !<br> :date: __2020-07-17 21:44:54__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> C'est une très bonne façon de lutter contre ceux virus il y a pas assez de gens qui l'on téléchargé<br> :date: __2020-07-19 21:33:33__

> Dommage qu il faille toujours réactiver l appli. A défaut elle est éteinte et n'e sert donc à rien. Il faudrait qu elle soit toujours active. Bin tu me diras il faudrait aussi qu il y est plus de gens qui s en servent... Mais ça c un autre sujet.<br> :date: __2020-07-19 12:31:12__

> J'ai l'impression que l'application perturbe le fonctionnement de mon kit mains libres, avez vous fait des essais sur ce point ?<br> :date: __2020-07-19 10:38:55__

> Je suis très fragile et je préfère faire attention<br> :date: __2020-07-17 13:14:23__

> Le choix d'activer ou non est libre et le Bluetooth est activé en même temps. Je trouve que la batterie tient très bien. La protection des données est parfaitement expliquée. Le seul problème c'est qu'il n'y a pas assez de personnes qui l'utilisent. Il faudrait la médiatiser en même temps que les gestes barrières pour que ce soit vraiment efficace.<br> :date: __2020-07-16 22:00:01__

> Après 3 bugs qui m'ont poussé à désinstaller l'App lors de sa sortie (et la noter 2/5), je l'ai réinstallée il y a 1 semaine et constate qu'elle s'est grandement améliorée depuis. Pour le moment pas de souci à remonter de mon côté donc j'édite mon avis !<br> :date: __2020-07-16 07:46:11__

> Bien pris en main<br> :date: __2020-07-15 17:17:35__

> Simple à mettre en place.<br> :date: __2020-07-14 21:53:59__

> C'était difficile de s'inscrire la dernière fois que j'ai essayé.<br> :date: __2020-07-13 19:07:45__

> Dommage d'avoir à relancer l'appli après un redémarrage du téléphone<br> :date: __2020-07-10 21:24:21__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Comme bp le disent, le fait qu'il faille réactiver manuellement l'appli après avoir été en mode avion est aberrant et fait que je suis resté plusieurs fois non protégé ( habitant en zone blanche, je passe en mode avion à la maison, sinon la batterie se vide très vite)<br> :date: __2020-07-20 15:31:42__

> Simple à utiliser. Il manque le nombre de contacts rencontrés. Car on ne sais pas si cela fonctionne.<br> :date: __2020-07-20 12:46:18__

> Se desactive souvent toute seule. Surconsommation batterie. Pour une meilleure acceptation des français, il manque le côté "ludique" de l'application : statistiques sur le nombre d'utilisateur croisé, le temps moyen de contact, etc<br> :date: __2020-07-20 08:40:38__

> La première fois que je l'ai installé ça marchait et depuis quelque temps il ne marche plus On me demande d'appuyer sur le bandeau orange pour l'activer ce que je fait Et j'ai un message en haut à gauche qui me dit de désinstaller l'application et de la réinstaller ce que j'ai fait plusieurs fois Mais ça ne marche pas Que faire !!! Annie LOCATELLI<br> :date: __2020-07-19 15:28:55__

> Stopcovid se désactive trop souvent, il faudrait peut-être mettre les développeurs de jeu sur cette application , leurs jeux sont plus coriaces !😉<br> :date: __2020-07-19 09:14:18__

> Le problème est que cette appli consomme bcp de batterie. 20% en une nuit (8h). Pas normal<br> :date: __2020-07-19 09:13:09__

> Se désactive toute seule tous les 2 ou 3 jours Pas vraiment fiable.<br> :date: __2020-07-18 21:37:51__

> Pas d'expérience<br> :date: __2020-07-18 12:07:08__

> Fonctionne bien pour le moment... Mais on après la mise à jour, il a fallu la désinstaller puis ré installer<br> :date: __2020-07-18 07:07:09__

> Elle fonctionnait en permanence jusqu'à hier. Depuis, elle se désactive toute seule. En espérant que le problème sera résolu rapidement.<br> :date: __2020-07-17 23:31:17__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Ne redémarre pas automatiquement après passage en mode avion 🙄 . Toutes les nuits, je mets mon téléphone en mode avion et le matin je suis obligée de relancer l'application. Il m'arrive d'oublier donc elle devient inutile à ce moment là. Pourquoi ne se relance-t-elle pas automatiquement ?<br> :date: __2020-07-20 07:55:38__

> aucun cas signalé alors que je me déplace sans cesse sur Paris et les hauts de France !!! c dingue non<br> :date: __2020-07-19 11:42:06__

> Se désactive tout seul...<br> :date: __2020-07-19 09:32:22__

> J ai une montre connecté Samsung et stopcovid me fait très souvent déconnecter ma montre, et après avoir désactivé puis activé stopcovid c est bien systématiquement quand stopcovid est activé que je rencontre ce problème. Merci de remédier au plus vite ce problème car je veux pouvoir l utiliser, en attendant je suis contraint de le désactiver<br> :date: __2020-07-18 20:33:59__

> L'application se cherche... s'ouvre puis disparaît. Si elle s'ouvre, à son activation un message"'erreur inconnue" s'affiche. Je désinstalle, réinstalle mais rien n'y fait. Pourtant lors de sa sortie elle a fonctionné au moins une journée avec une icône en haut de l'écran qui indiquait que l'application était opérationnelle. Idem avec le smartphone de ma femme, les deux sous Androïd 😕 Aujourd'hui 18 juillet je viens de désinstaller puis réinstaller, apparemment l'application fonctionne...<br> :date: __2020-07-18 18:57:19__

> J ai essaye d installer stopcovid sur mon Samsung . Pas de chance je reçois le message :téléphone incompatible !<br> :date: __2020-07-18 18:26:48__

> Elle se désactive tout le temps !<br> :date: __2020-07-18 17:37:02__

> Installé depuis hier après-midi j ai du réactive l appli une dizaine de fois du coup il faut être attentionné au portable, je pensais pas être aussi decuet vu le fonctionnement l appli n est pas au point, mais rien de surprenant vu les mensonges et l efficacité de l etat à gérer la crise Du coup je de s'installer l appli covid j espère que les personnes l ayant télécharger ça fonctionne mieux que pour moi!! Protegez vous bien<br> :date: __2020-07-17 16:09:33__

> Bon sur le principe, mais ne fonctionne plus après la saisie du cryptogramme pour ma part, et autres soucis techniques, merci de changer ça les développeurs<br> :date: __2020-07-17 11:10:24__

> 1. Très gourmand en batterie et empêche la connexion/reconnexion en Wi-Fi. Pour une raison inconnue, la connexion au Wi-Fi est parfois impossible sans désactiver le Bluetooth. 2. Impossible de réinstaller l'application, le capcha est systématiquement refusé donc pas de validation. L'application parle de vérifier la connexion internet qui par ailleurs fonctionne très bien donc impossible d'utiliser l'application.<br> :date: __2020-07-17 10:33:02__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Très compliqué à activiter car lorsque l'on appuie sur le bandeau d'activation l'appli disparaît et de ce fait on revient sur l'écran d'accueil vraiment pas terrible et au bout de x fois ça marche !!!!!<br> :date: __2020-07-20 15:28:05__

> Oneplus 5. Une vrai galère pour activer l'application car elle crash a chaque fois au niveau du captcha. Après une heure d'essai c'est tombé en marche mais après deux jours de fonctionnement l'application s'est arrêtée et ne veut plus se lancer même après reboot, elle crash direct au lancement. Dire que c'est une application gouvernementale payée avec de l'argent public....honte aux développeurs<br> :date: __2020-07-20 15:05:42__

> Je n'arrive plus a lancer l'application depuis la nouvelle version Android<br> :date: __2020-07-20 12:20:10__

> Ne fonctionne pas<br> :date: __2020-07-20 12:08:04__

> Pas de retour d'informations<br> :date: __2020-07-20 11:03:43__

> Depuis la dernière mise à jour, l'application crash lorsque je l'active. De plus, lorsqu'elle marchait avant, elle s'arrêtait toute seule de manière aléatoire et il fallait vérifier régulièrement pour la relancer. Et il faut la démarrer manuellement quand on rallume son téléphone. Bref, l'idée de départ était bonne, mais ce logiciel donne l'impression d'un codage à la vas-vite sans procédure de test par une bande d'amateurs.<br> :date: __2020-07-20 08:20:14__

> Ne fonctionne pas<br> :date: __2020-07-20 07:42:44__

> L'application fonctionnait très bien (à part une nécessité quelques fois de réactiver la connexion) jusqu'à hier, depuis, impossible de réactiver la connexion, l'application bugge et se ferme. Impossible d'envoyer quoi que ce soit comme rapport également, la fenêtre se ferme aussitôt.<br> :date: __2020-07-20 00:28:14__

> Le téléphone chauffe des l'activation et la batterie se vide ! Après désinstallation, tout redevient normal donc désinstalle, dommage<br> :date: __2020-07-19 22:34:07__

> Le gouvernement francais n'a pas adopte l'algorithme DP3T... Pourquoi etre aussi bete et arrogant?<br> :date: __2020-07-19 21:19:32__


