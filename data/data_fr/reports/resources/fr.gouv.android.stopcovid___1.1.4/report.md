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

> Idée bonne<br> :date: __2020-10-10 22:59:58__

> Il faut télécharger, cette application Arreter d imaginer des scénarios complotiste... Nous sommes déjà fichés, suivi, espionnés... Par nos réseaux sociaux, application de communication gratuite, Banque, achat en ligne... Le bémol de cette application est la connection qu'il faut penser à réactivité des que l'on coupe son tel, mode avion par exemple... C'est sûrement pour rassurer et éviter de se sentir trop épié, mais pour le coup, ca pourrait nous rassurer. Prenez soins de vous<br> :date: __2020-10-10 09:46:36__

> J'ai enfin réussi à activer l'application merci d'avoir corriger le problème<br> :date: __2020-10-10 08:22:05__

> Le coronavirus ne craint rien avec cette application même si l'étiquette StopCovid veut suggerer autre chose. Le virus profite de la négligence et ignorance à tous les niveaux et il a un allié avec cette application si cela continue comme cela... Bravo encore ... Après, je suis d'accord avec les avis qui demandent des statistiques. Le nombre de personnes détectés, combien de temps l'application fonctionne etc - il n'y a aucun contrôle sur cette application possible depuis 5 mois ...<br> :date: __2020-10-10 01:20:51__

> L'application a besoin d'être désinstaller et réinstaller depuis la dernière mise à jour...<br> :date: __2020-10-09 23:29:22__

> Bien mais manque d'activité, je n'ai croisé personne ayant que le COVID19 ! l0l ^^<br> :date: __2020-10-09 20:34:37__

> Application pertinante et espère ne pas avoir à l utiliser pour valider cette avis<br> :date: __2020-10-07 16:09:56__

> De l'amélioration a faire<br> :date: __2020-10-07 01:02:37__

> Très bonne idée très pratique et intuitifs<br> :date: __2020-10-05 22:02:05__

> Gonla rendre compatible avec les notifications d'exposition de Google...<br> :date: __2020-10-04 22:14:58__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Simple et tellement utile qu'elle devrait etre obligatoire !. Mais elle refuse de s'ouvrir regulierement: je suis obligee de la desinstaller puis de la reinstaller...<br> :date: __2020-10-10 07:51:35__

> Apparemment la mise à jour du 15 09 2020 a désactivé l'application ! Que ce soit un bug ou un choix volontaire, c'est scandaleux s'agissant de santé publique. Combien de personnes se sont rendu compte à ce jour qu'elles ont une application supposée les protéger qui est désactivée à leur insu ? Pas étonnant que peu de gens l'utilisent...<br> :date: __2020-10-06 14:29:53__

> Bonjour, Je retrouve parfois l'application arrêtée ou "désactivée". Ill suffit de la réactiver, mais combien de temps a été perdu ? Il semble que cela soit arrivé après sortie du mode avion. J'espère aussi que la désactivation ne fait pas perdre l'historique des deux dernières semaines, sinon, tout cela devient assez inutile. Et cette interrogation n'aide pas à avoir confiance. Il manque drastiquement un affichage statistique, par exemple un histogramme du nombre de contacts par jour. Merci<br> :date: __2020-10-04 15:39:17__

> Je peux enfin l'activer..... Elle n'était même pas opérationnelle à son lancement.... Mieux vaut tard que jamais.<br> :date: __2020-10-03 09:50:53__

> Demander à Google et Facebook qui fréquente qui, serait plus efficace, car 90% de la population leurs donnent déjà les informations de localisation et bien d'autres.m informations personnelles.<br> :date: __2020-10-03 09:32:51__

> Comme à Hong Kong, les consignes sanitaires doivent être respectées par l'ensemble des français.Le traçage est une bonne chose, pour isoler rapidement les cas covid déclarés. Bon courage à toutes et tous, nous finirons à voir bientôt le bout du tunnel.<br> :date: __2020-10-02 11:46:24__

> Depuis la maj on sait que l'appli est actif et c'est mieux, je regrette que l'appli consomment trop de batterie.<br> :date: __2020-10-02 08:40:26__

> Le principal avantage de stopcovid est d'utiliser la technologie bluetooth. En revanche la notification qui s'affiche en permanence est exaspérante.<br> :date: __2020-09-30 22:26:18__

> Plus de plantages, bravo pour la correction et merci<br> :date: __2020-09-29 18:39:10__

> Depuis quelques jours stopcovid plantait sur mon téléphone. J'ai fini par la désinstaller et la réinstaller. Depuis elle refonctionne. Par contre j'ai noté qu'il y avait eu une MAJ le 15 septembre, mais je n'ai pas souvenir de l'avoir vu s'installer sur mon téléphone.<br> :date: __2020-09-27 10:32:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Je viens de l'installer sans aucun problème, mais je reçois des alertes fréquentes ( toutes les 2~3 min ) lorsque j'utilise mon smartphone pour me dire que StopCovid est activé, j'avoue c'est un peu usant à force. Y a t- il moyen de supprimer cette notification ? Mise à jour avis le 11/10/2020 Le défaut des alertes fréquentes avait été résolu, en revanche ces derniers jours il était impossible d'activer l 'appli. Le bouton était grisé. J'ai du désintaller puis réinstaller l'appli.<br> :date: __2020-10-11 09:14:23__

> De nouveau après MAJ 1.1.4 du 15/09 .. Se désactive seule en permanence malgré toutes les autorisations voulues. Version précédente le problème était déjà présent. Et version encore précédente le problème était résolu.. Le tout sur le même téléphone et installé depuis la première version dispo.<br> :date: __2020-10-10 22:34:56__

> Bizarre, l'application s'arrête sans crier gare, depuis plusieurs mois ce genre de Blague arrive régulièrement. Et là cette semaine, c'est le pompon : elle ne démarre plus du tout. J'ai du désinstaller puis réinstaller, je me demande si cette application est franchement utile...<br> :date: __2020-10-10 19:17:59__

> Je voulais savoir si l application fonctionne bien pour qu'il détecte si il y a une personne a le virus covid 19<br> :date: __2020-10-10 16:20:24__

> Comme tout le monde se désactive trop souvent. J'oublie de plus en plus souvent de la remettre.<br> :date: __2020-10-09 19:52:35__

> On voit malheureusement les limites de l'architecture technique choisie pour développer cette application. Celle-ci n'utilise pas le sdk spécifique mis à disposition par Google pour le contact tracing. Du coup, elle est considérée comme une application lambda et se retrouve dépendante des paramètres d'optimisation de la batterie mis en place par les constructeurs d'où les arrêts intempestifs de l'application remontés par de nombreux utilisateurs. Dommage, car cela rend l'application peu fiable.<br> :date: __2020-10-08 22:38:41__

> Avant ça plantait tout le temps, mais ça c'était avant...<br> :date: __2020-10-08 20:32:25__

> Cette appli est inutile, elle se désactive toute seule, au moins, à chaque démarrage du smartphone. Je désinstalle. Développer des programmes c'est un métier.<br> :date: __2020-10-06 17:03:03__

> Pour l'instant aucun écho<br> :date: __2020-10-01 12:36:35__

> Fonctionne bien sans problème sur mon téléphone mais aucun signalement depuis que je l'ai activée (2 mois déjà) alors que Rennes est en zone rouge...suis-je le seul à utiliser cette appli?<br> :date: __2020-10-01 08:56:27__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> C'était peut-être une bonne idée, mais l'application s'arrête toute seule... Donc elle ne sert à rien.<br> :date: __2020-10-10 23:55:11__

> Ces derniers jours, impossible d'ouvrir l'appli, elle s'arrête tout de suite après avoir affichée l'écran d'accueil. Vite une MAJ !<br> :date: __2020-10-10 10:04:25__

> L'application se stop tout les jours à un moment où l'autre dans la journée... Je m'en rend compte le soir en sortant du boulot depuis quand elle est arrêté aucune idee sûrement le matin vu qu'un jour je m'en suis rendu compte à 10h...<br> :date: __2020-10-09 20:41:26__

> Vide la batterie en moins d'une journée...<br> :date: __2020-10-09 17:57:25__

> L'application empêche mon téléphone de se connecter au kit mains libres bluetooth de mon véhicule<br> :date: __2020-10-08 19:28:48__

> L application a fonctionné au départ, mais maintenant, J ai toujours une demande de téléchargement de la nouvelle version ,mais rien ne se fait, dommage<br> :date: __2020-10-08 13:35:03__

> Jusqu'à présent l'application fonctionnait correctement mais aujourd'hui impossible de l'activer... je l'ai désinstallée et réinstallée mais rien ne se passe. Merci de me dépanner et de me donner une solution.<br> :date: __2020-10-08 12:48:50__

> Pourquoi est-ce que cette application doit être constamment réactivé ? A chaque fois que mon portable est en mode avion, il faut ensuite penser à réactiver l'application. Pénible...<br> :date: __2020-10-07 06:44:17__

> Plantages incessants non corrigés. J'ai été contraint de deinstaller l'application et la réinstaller à trois reprises ! Cela ne fonctionne pas.... J'abandonne... Très déçu alors que cette application à été conçue par les très grands du domaine.... 😕<br> :date: __2020-10-06 19:30:45__

> Comme beaucoup d'autres utilisateurs, l application s arrête seule. J ai essayé plusieurs fois de la redémarrer en vain. Donc pas efficace.<br> :date: __2020-10-06 17:20:06__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Ça nous a coûté combien pour une application qui n'est même pas capable de faire son job...<br> :date: __2020-10-11 13:06:33__

> Fonctionne pas très bien<br> :date: __2020-10-11 08:20:26__

> Se désactive en permanence. Du coup, desinstallée.<br> :date: __2020-10-10 23:56:35__

> Épuise la batterie Pas de communication, personne ne l'a installé donc c'est inutile. Honteux l'état n'est pas un chef de projet<br> :date: __2020-10-10 22:19:40__

> Application à la hauteur du gouvernement, une application de guignols, elle se ferme toute seule, elle ne mérite même pas une étoile.<br> :date: __2020-10-10 18:15:01__

> L'application est souvent récalcitrante à l'ouverture.<br> :date: __2020-10-10 13:51:38__

> Se mets hors service toute seule, bizarre. Et après on s'étonne que les gens l'utilise peu...Quelques fois en essayant de la relancer, elle affiche: "stop Clovis à cessé de fonctionner". Étonnant pour une appli qui a coûté des millions d euro.....<br> :date: __2020-10-10 10:23:39__

> Il faut utiliser cette application malgré sa conception pitoyable.<br> :date: __2020-10-10 00:31:12__

> Bonne idée mais ruine mon débit wifi. Du coup je n'utilise plus l'appli.<br> :date: __2020-10-09 21:29:32__

> Impossible de se declarer.... l'application rame puis finit en message d'erreur. Dommage et très décevant car c'était une bonne idée<br> :date: __2020-10-09 21:19:28__


