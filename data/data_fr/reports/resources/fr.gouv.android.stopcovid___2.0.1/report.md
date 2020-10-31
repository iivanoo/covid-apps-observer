# TousAntiCovid
App version ``2.0.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="TousAntiCovid icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | TousAntiCovid |
| **Unique identifier** | fr.gouv.android.stopcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=fr.gouv.android.stopcovid](https://play.google.com/store/apps/details?id=fr.gouv.android.stopcovid) |
| **Summary**  | Protégeons nos proches, protégeons-nous et protégeons les autres |
| **Privacy policy** | [https://bonjour.stopcovid.gouv.fr/privacy.html](https://bonjour.stopcovid.gouv.fr/privacy.html) |
| **Latest version** | 2.0.1 |
| **Last update** | 2020-10-22 13:00:24 |
| **Recent changes** | Améliorations et corrections. |
| **Installs**  | 1 000 000+ |
| **Category** | Médecine |
| **First release** | 29 mai 2020 |
| **Size**  | 21M |
| **Supported Android version**  | 5.0 ou version ultérieure |

### Description
> L'application TousAntiCovid est destinée au territoire français.
<br>Protégeons nos proches, protégeons-nous et protégeons les autres. 
<br>TousAntiCovid, c’est simple :
<br># J'active l'application
<br>En utilisant le Bluetooth de votre téléphone, TousAntiCovid détecte les téléphones des autres utilisateurs qui restent à proximité du vôtre.
<br># Je reste informé
<br>Vous serez informé si vous avez été à proximité d’un utilisateur testé positif à la COVID-19. Vous serez informés des derniers chiffres et de l’actualité sur l’épidémie. Vous aurez accès aux conseils personnalisés de Mes Conseils Covid.
<br># Je protège mes proches et les autres
<br>Si vous devez vous faire tester, vous pourrez trouver le laboratoire le plus proche. Si vous êtes diagnostiqué comme un cas de COVID-19, votre laboratoire ou votre médecin vous donneront un code à scanner ou à saisir pour avertir anonymement les utilisateurs que vous avez rencontrés.
<br># Mes données sont protégées
<br>L’application n’utilise à aucun moment la localisation des personnes, et il est impossible de connaître l’identité des utilisateurs.
<br>Cette application a été réalisée par l'équipe TousAntiCovid, sous la supervision du Ministère des Solidarités et de la Santé et du Secrétariat d'Etat chargé du Numérique.


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
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
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
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | stopcovid.gouv.fr | Etat francais represente par le Ministere des Solidarites et de la Sante | - | 2020-04-15 12:02:42 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lcom/android/tools/r8/GeneratedOutlineSupport;->outline19(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The TousAntiCovid app has been installed by more than **1000000** times. At this time, **15221** rated the app and its average score is **3.1827297**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 6530

:star::star::star::star:: 1560

:star::star::star:: 882

:star::star:: 661

:star:: 5588

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 5 reviews"/>
</p>

> Nickel fonctionne très bien<br> :date: __2020-10-31 10:47:14__

> L'application fonctionne très bien<br> :date: __2020-10-31 10:39:16__

> La nouvelle version est très bien. zéro problème !<br> :date: __2020-10-31 09:59:52__

> Super !<br> :date: __2020-10-31 09:59:18__

> Youpi<br> :date: __2020-10-31 09:59:12__

> Bien<br> :date: __2020-10-31 09:44:41__

> Bieb<br> :date: __2020-10-31 09:17:43__

> Très bien,préventif<br> :date: __2020-10-31 09:06:09__

> Trop bonne idée de gouvernement<br> :date: __2020-10-31 09:00:48__

> 👍👍👏👏<br> :date: __2020-10-31 08:58:11__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Enfin cette appli fonctionne. Après 2 jrs j'ai enfin pu faire ma première autorisation de sortie. Il était temps !<br> :date: __2020-10-31 11:02:59__

> L'ajout d'un lien vers la génération des attestations de déplacement est enfin sur l'application....<br> :date: __2020-10-31 10:36:10__

> So far so good. J'ai juste changé de navigateur web car Mi de Xiaomi ne fonctionnait pas pour télécharger l'attestation. Avec firefox ça marche, c'est très pratique et rapide.<br> :date: __2020-10-31 10:08:57__

> L'application est intéressante au niveau de l'information (dernière news, data par département, centre de dépistage de plus proche avec coordonnées, etc...) Le gros point positif est que vous avez un raccourci pour la demande d'attestation sur votre téléphone. Mais le problème, c'est de ne pas pouvoir l'activer. Code de validation non fonctionnel. A ressayer plus tard. Mise a jour : après une heure activation faite (pb serveur ?), Une net amélioration par rapport à Stopcovid<br> :date: __2020-10-31 09:41:22__

> Ayant déjà téléchargé Stopcovid, la mise à jour ne s'est pas faite correctement. Il a fallu la désinstaller pour ensuite installer TousantiCovid. Sinon la nouvelle application fonctionne bien et est plus complète.<br> :date: __2020-10-31 08:50:52__

> Bonjour, le lien pour l'attestation ne pointe pas vers la bonne page. Pourriez-vous corriger ça ? Merci [30/10 am : c'est corrigé !]<br> :date: __2020-10-31 08:50:09__

> Le minimum pour les attestations seraient d'enregistrer les informations de la personne propriétaire du téléphone.<br> :date: __2020-10-31 08:32:47__

> Tout va bien pour le moment<br> :date: __2020-10-31 07:52:55__

> En France il y a personne qui est capable de faire une application qui fonctionne c'est une honte et un vrai scandale et après ils vont s'étonner que personne l'installe le 31/10 je rajoute des étoiles l'application fonctionne enfin<br> :date: __2020-10-31 07:47:36__

> Fait largement le taff. Paramètrable en 2 minutes simple et efficasse.<br> :date: __2020-10-31 01:24:43__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Ça serait bien que l'attestation soit à jour...<br> :date: __2020-10-31 11:08:27__

> La création des attestations ne fonctionne pas sur mon téléphone.<br> :date: __2020-10-31 11:08:04__

> L'appli s'est mise en anglais ! Comment revenir au Français ?? Ce n'est pas dans les "Settings" =(<br> :date: __2020-10-31 10:58:28__

> Dommage qu'on puisse pas se déclarer cas contact direct<br> :date: __2020-10-31 10:51:22__

> Problème de Bluetooth (puissance) sur les ancien téléphone donc installation impossible<br> :date: __2020-10-31 10:19:24__

> Des choses à améliorer<br> :date: __2020-10-31 10:19:13__

> Cette deuxième version ne plante plus et reste toujours active, bon point ! Du coup elle consomme bien la batterie... 20% par jour sur un vieux téléphone... C'est trop !<br> :date: __2020-10-31 10:12:53__

> Dans l'appli le lien vers l'attestation pointe sur une attestation obsolète !<br> :date: __2020-10-31 10:12:09__

> L'attestation ne se telecharge pas correctement sur le téléphone, très dommage.<br> :date: __2020-10-31 09:57:16__

> Pourquoi la couleur bleue sur cette carte alors que le rouge est utilisé pour les cartes des médias. Une incohérence de plus.<br> :date: __2020-10-31 09:31:33__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Installé hier... mais ne parviens pas à s'activer aujourd'hui... Luttons plus efficacement !<br> :date: __2020-10-31 10:50:00__

> Application non compatible avec des smartphones Samsung datant un peu. Donc mon mari handicapé ne peux avoir d'attestation automatique !!! Encore une solution partielle. Le monde "En marche" marche sur la tête, comme pour tout.<br> :date: __2020-10-31 10:49:05__

> J'ai installé cette application sur mon Samsung J3 que j'utilise modérément. Au préalable la batterie tenait au minimum 2 jours depuis l'installation de cette application ma batterie ne tient plus la journée alors que je n'utilise pas plus le téléphone. Je me demandais ci cette application ne nécessite pas de changer de téléphone.<br> :date: __2020-10-31 10:39:32__

> Rien nest clair sur la migration de stopcovid a tousanticovid.<br> :date: __2020-10-31 10:30:34__

> Application téléchargée et installée. ça fait 1/2h que j'essaie de l'activer, impossible : vérifiez votre connexion internet !! la blague !!! honteux. qui ne désinstallerait pas après ça ? Enfin réussi après 1/2h ! il n'en reste pas moins que ce n'est pas acceptable pour une application de 1ère nécessité...<br> :date: __2020-10-31 10:26:12__

> Attestation réputée téléchargée sur appareil qui reste introuvable... (sous Android : ni dans Dowloads, ni dans Document). Comment pourra t-on justifier que l'on a fait une ?<br> :date: __2020-10-31 10:25:03__

> A voir dans le temps, mais attestation de sortie décevante car pas à jour. Le choix des courses de produits de 1ere nécessité n'est pas proposé<br> :date: __2020-10-31 10:19:26__

> On ne peut pas télécharger l attestation avec l application<br> :date: __2020-10-31 10:17:43__

> Tousanticovid à un endroit, anticovid à un autre, comment s'appelle l'appli ? Que de confusion! En plus elle ne reste pas active. //Par ailleurs, on ne peut pas obtenir le QR code attestation de déplacement depuis (tous)anticovid// MAJ des chiffres tous les 4 jours ?! J'en passe<br> :date: __2020-10-31 10:17:25__

> A chaque fois que j'active cette appli une notification sur mon Huawei P30 Pro s'affiche me disant que cette dernière est extrêmement energivore du coup je la ferme ! Si e c'est pour vider ma batterie aucun intérêt, dommage !<br> :date: __2020-10-31 10:02:57__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> L'application se ferme systématiquement impossible à lancer...merci de résoudre le bug. Et prenez soin de vous 🤞🏾🤞🏾🙏🏽<br> :date: __2020-10-31 11:08:47__

> Génération d'attestation de déplacement qu'il faut renseigner (nom, prénom, date et lieu de naissance et adresse) à chaque utilisation. La mise en place de cookies pour garder en mémoire les renseignements ne serait pas de trop !!!! Appmication au niveau de la gestion de la crise par le gouvernement !!!<br> :date: __2020-10-31 11:07:42__

> J'aurai bien mis 0 étoile car l'application ne fonctionne pas. Lorsque j'essaie d'activer tous Anti Covid (connecté au bluetooth et à la 4G) un chargement très long pour me dire finalement que je n'ai pas de réseau ce qui n'est pas le cas. Opération répétée plusieurs fois et rien n'y fait ça ne s'active pas. Application inutilisable en l'état.<br> :date: __2020-10-31 11:06:27__

> Application qui se déconnecte tout le temps et qui plante...<br> :date: __2020-10-31 10:57:13__

> L'application s'arrête systématiquement, elle s'ouvre puis se referme automatiquement sur mon téléphone doté de la version 8 d'Android (2017).<br> :date: __2020-10-31 10:53:48__

> Meme avec l'appli, l'attestation de deplacement n' est pas pré remplie. Il faut renseigner toutes les cases à chaque fois. Très long quand on est né a Nogent Le Retrout et quand on habite à Parfouru Sur Odon. D'autre part les notifications sont très invasives. Je désinstalle.<br> :date: __2020-10-31 10:53:19__

> Impossible d'activer l'appli ! Je renonce et la désinstalle... Quelques améliorations à faire<br> :date: __2020-10-31 10:53:16__

> Incompatible avec mon Samsung Galaxy<br> :date: __2020-10-31 10:53:10__

> Une fois activée, le texte est en anglais.<br> :date: __2020-10-31 10:48:38__

> Plante systématiquement depuis quelques semaines. Malgré la nouvelle version plante toujours autant<br> :date: __2020-10-31 10:48:01__


