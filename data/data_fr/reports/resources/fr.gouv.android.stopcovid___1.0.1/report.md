# StopCovid France
App version ``1.0.1``

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
| **Latest version** | 1.0.1 |
| **Last update** | 2020-06-05 22:08:27 |
| **Recent changes** | Améliorations et corrections. |
| **Installs**  | 500 000+ |
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
> - This application opens a Socket and connects it to the remote address 'Lcom/android/tools/r8/GeneratedOutlineSupport;->outline17(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Socket;->isConnected()Z' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Only InetSocketAddress is supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Wrapped socket should already be bound' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Wrapped socket should already be connected' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The StopCovid France app has been installed by more than **500000** times. At this time, **4072** rated the app and its average score is **3.5807292**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 2163

:star::star::star::star:: 424

:star::star::star:: 180

:star::star:: 222

:star:: 1081

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 5 reviews"/>
</p>

> Toujours moins intrusif que Facebook, Google, Apple et Amazon contrairement à ce qu'affirme une publication Facebook... J'aurais du me méfier, l'avertissement était signé Albert Einstein...<br> :date: __2020-06-07 20:20:47__

> Acte citoyen, on sera pas plus traqués qu'on ne l'est déjà par Amazon Google et autres<br> :date: __2020-06-07 20:20:02__

> C'est super bien<br> :date: __2020-06-07 19:54:17__

> Bonjour, Comme souhaité dans un précédent commentaire, on peut choisir de lancer automatiquement StopCovid au démarrage de son téléphone. Avec Android 9 : appui long sur l'icône de l'application, puis menu informations et enfin l'option démarrage automatique.<br> :date: __2020-06-07 19:41:24__

> Excellent ! Rien à dire.<br> :date: __2020-06-07 19:38:44__

> Très satisfait<br> :date: __2020-06-07 19:17:54__

> Facile<br> :date: __2020-06-07 18:38:22__

> Simple et efficace<br> :date: __2020-06-07 18:29:04__

> Qui c'est peut être ça vole les données comme les FRANÇAIS son avec les USA et arrêter de dire que les truc chinois volent les données TOUS les entreprises volent les données (oui même Google et Google c'est quoi c États-Unis...Mes bon sa sert a rien de mettre un mauvaise note mais j'espère que se sera plus lu que dans un simple tweet ou une story.<br> :date: __2020-06-07 18:02:14__

> Très simple à utiliser. Très pratique de pouvoir activer ou désactiver l'application.<br> :date: __2020-06-07 17:55:52__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Activation impossible. Le truc n'arrive pas a me distinguer d'un robot. Comme un robot ne peut attraper le Covid je suis rassuré. Bon après de nombreuses tentatives infructueuses depuis ma petite commune alpine (malgré réussite des tests photos avec passages piétons, feux rouges et autres), j'ai réussi à me connecter lors d'un passage a Marseille.<br> :date: __2020-06-07 22:08:34__

> Application bien faite. Pas convaincu de l'intérêt sachant que tout le monde ne l'aura pas installé mais l'application en soi fonctionne bien. Rien à signaler.<br> :date: __2020-06-07 17:20:01__

> Parfait pour la transparence, Suggestions d'Amélioration : Un compteur indiquant le nombre de portables ayant été en relation serait intéressant. Ceci afin de le correler à notre perception du nombre de personnes côtoyées, et cela permettrait aussi d'améliorer le respect de la distanciation puisque l'on saurait avec combien de personnes nous sommes restés plus d'1/4 d'heure à moins de 1m Correctif technique : L'application ne se reactive pas en sortie du mode avion ou redémarrage (redmi note 7)<br> :date: __2020-06-07 17:01:56__

> Bien pensé, seulement, la plus part des smartphones avec surcouches l'empêche de s'exécuter en continu. Durant le processus d'activation, il faudrait ajouter la demande de permission concernant l'optimisation de batterie.<br> :date: __2020-06-07 15:52:57__

> Malgré la communication catastrophique du gouvernement, par civisme j'ai installé cette appli.<br> :date: __2020-06-07 13:51:37__

> Malgré que je laisse le bluetooth activé, il faut que chaque jour lorsque j'allume mon téléphone que je pense à me connecter à l'application pour activer stopcovid. C'est pas très pratique.<br> :date: __2020-06-07 12:52:24__

> Très simple à installer. Une critique : la notification permanente "stopcovid est activé" est gênante<br> :date: __2020-06-07 11:33:17__

> Utile et facile d'utilisation malgré le fait qu'elle vide la batterie de n'importe quel téléphone ( si vous me croyez pas j'ai un S10)...<br> :date: __2020-06-07 11:28:32__

> 💜💜💜💜<br> :date: __2020-06-07 10:38:14__

> Semble fonctionner correction sir samsung s10<br> :date: __2020-06-07 10:36:14__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Obligé de mettre en route l'application après avoir démarré le téléphone, du coup quelques fois j'oublie de la mettre en route à quand une option de démarrage automatique ?<br> :date: __2020-06-07 20:10:48__

> Bof !!! Obligé de lancer l'application à chaque démarrage du téléphone. Aucun réglage pour la lancer au démarrage. Résultat une journée de courses sans l'application lancée. Grr !!!<br> :date: __2020-06-07 16:35:42__

> Personnellement mon téléphone est compatible, il est puissant donc c'est normal.<br> :date: __2020-06-07 12:42:15__

> J'ai l'impression qu'il se désactive lorsque j'éteins mon téléphone<br> :date: __2020-06-07 12:29:38__

> Fonctionne sans grand défaut me semble-t-il. Jusqu'à redémarrage du tel ou passage en mode avion. 😤🙄 Comment dire ça sans langue de bois. C'EST UNE BLAGUE ??? 😳😳😳 Mon tél fait une mise à jour une fois par mois, je le redémarre de temps en temps en dehors de sa pour diverses raisons. Ben imaginer l'utilité du truc. J'ose espérer que ça va être corrigé rapidement mais j'ai un doute vu qu'une mise à jour vient de passer (elle était du 04/06/2020) et que ce n'était pas dedans.<br> :date: __2020-06-07 12:21:16__

> Consomme trop de batterie.<br> :date: __2020-06-07 10:14:51__

> Les notifications toutes les demies heures pour dire que l'application fonctionne sont très pénibles Je pense à la désactiver alors que je suis convaincu de son utilité<br> :date: __2020-06-07 09:40:49__

> Super application, avec les potes on a enfin réussi à choper un infecté et à le tondre sur la place publique, mais on a même pas reçu de gratification. Il manque également une option pour dénoncer ses voisins. Et il faudrait pouvoir prendre en photo ceux qui ne mettent pas de masques sur cette appli (avec leur adresse bien sûr !) 🙄<br> :date: __2020-06-07 09:25:31__

> Entre en conflit avec min application de tracking d'activité de la montre connectée. Celle ci 'e fonctionne plus depuis l'installation de stopcovid et se remet en route des que l'autorisation d'utiliser le bluetooth est retirée a stopcovid (lors d'un redémarrage du smartphone par exemple)<br> :date: __2020-06-07 09:00:05__

> En cours d'utilisation sur Xiaomi, le démarrage automatique après un reboot serait apprécié. De plus, il manque un tableau statistiques du nombre de contact Covid-19 positif et négatif 🤔<br> :date: __2020-06-07 07:20:06__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> L application s arrête toute seule dès que le wifi s enlève ou que je le enlève pour basculer sur les données mobiles. L application perd de facto son intérêt puisque je dois la réactiver tout le temps et elle passe sont temps à se désactiver.<br> :date: __2020-06-07 19:17:45__

> Elle ne peut être installée sur des mobiles qui n'ont que 3 ans. S il faut changer c est dommage. Espérons une version utilisable sur des mobiles plus anciens<br> :date: __2020-06-07 16:51:08__

> Appli energivore, avec notif en permanence, et indicateur new toujours présent. Vous connaissez Pierre et Le Loup ? Ben c'est pareil !<br> :date: __2020-06-07 14:14:58__

> Une bonne idée à la base mais des impasses techniques rendent l'expérience totalement inutile et dans le meilleur des cas peu productive : la batterie est mise à rude épreuve (Bluetooth, fonctionnement en arrière plan) et la distance entre 2 utilisateurs est limitée...<br> :date: __2020-06-07 12:34:08__

> Pouvez vous me dire comment sa marche ?<br> :date: __2020-06-07 11:00:27__

> Il y a un bug. Obligé de supprimer l'app pour pouvoir la réinstaller tous les jours.<br> :date: __2020-06-07 08:38:12__

> Appli instable. Il faut la redémarrer tout le temps. Je doute de la qualité du traçage vu le nombre de redémarrage qu'il faut faire. Je viens de faire une màj... À voir...<br> :date: __2020-06-06 22:40:33__

> Ne fonctionne pas avec tous les smartphones. Domage<br> :date: __2020-06-06 20:24:07__

> Bonne application seulement il faut penser à réactiver l'application après chaque redémarrage du téléphone vraiment dommage car je n'y pense pas tout le temps Sur Samsung s10<br> :date: __2020-06-06 20:02:33__

> L'application s'arrête régulièrement et demande une réactivation. Un peu gênant lorsque cette application est censée fonctionner tout le temps afin d'être efficace. Je vais très certainement la désinstaller. Dommage.<br> :date: __2020-06-06 19:10:34__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> L application se désactive toute seule environ une fois par jour. Il faut constamment vérifier et la réactiver !<br> :date: __2020-06-07 23:32:45__

> Aucune utilité, je respecte les gestes barrières, pas besoin de ce genre d'application et en plus pour nous surveiller. Non merci<br> :date: __2020-06-07 23:30:53__

> Après deux jours d'activation, l'application c'est désactivé elle-même. Lors de la demande réactivation, elle indique que c'est impossible car Stopcovid est victime de son succès. C'est une bonne nouvelle ! C'est un peu le principe. Il faut qu'un maximum de personnes l'utilisent pour que ce soit utile. Mais encore faudrait-il pouvoir la conserver active. Cela fait donc trois jours que l'activation est impossible. Il faut la désinstaller et la réinstaller pour résoudre le problème.<br> :date: __2020-06-07 22:26:45__

> Facile à installer et à comprendre. Par contre au bout de quelques minutes: un premier message m'indiquant qu'elle s'est arrêtée. Je la redémarre. Et depuis, plusieurs notifications "pour rien". Si ce n'etait pas pour un sujet aussi important, je l'aurais desinstallé. Je baisse la note à la plus basse possible plusieurs jours après installation car elle s'arrête toute seule plusieurs fois par jour et m'envoie des notifications plusieurs fois également pour rien. Inutile....<br> :date: __2020-06-07 22:25:49__

> Nulle, dans le principe et dans la réalisation.<br> :date: __2020-06-07 22:05:26__

> Depuis la mise à jour, impossible d'activer l'application qui se désactivait toute seule avant... Une phrase dans un encadré rouge apparaît "victime de son succès, réessayez plus tard..."<br> :date: __2020-06-07 21:46:44__

> Ne fonctionne pas avec le Samsung Galaxy j5.<br> :date: __2020-06-07 20:51:47__

> La notification qui reste en permanence c'est insupportable et si on désactive les notifications ça ne fonctionne plus. En plus ça pompe la batterie.<br> :date: __2020-06-07 20:36:03__

> Décevant de croire le gouvernement, justement quand ils di que rien n'est collecté, c'est comme les masques mouai pas besoin. Croire touj le contraire d'un guouv<br> :date: __2020-06-07 20:03:58__

> Depuis la dernière mise à jour, je ne peux plus l'activer, j'ai du la supprimer et la réinstaller. Cela fausse les stats de téléchargements<br> :date: __2020-06-07 19:55:04__


