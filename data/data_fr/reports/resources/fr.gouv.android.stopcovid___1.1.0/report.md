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

> Utilisation du BLE donc intéressant et code source clair, même sans commentaires. Si votre téléphone n'est pas d'une qualité minimale, il est évident que vous ne pouvez pas profiter du BLE. On a la qualité que l'on paye, cela va de soit<br> :date: __2020-08-04 10:32:43__

> Super application je vous la conseille vivement facile à comprendre et si tous le monde l avait sa stopperai le Covid<br> :date: __2020-08-04 10:15:54__

> Une super application très simple d'utilisation pour lutter contre la covid-19. Certains personnes disent que l'application se désactive toute seule. Ayant moi même remarqué que la barre me notifiant que StopCovid France était activé n'apparaissait plus,je suis allé dans l'application et j'ai constaté que l'application était toujours active. J'ai également remarqué que cela arrive pendant que j'utilise mon téléphone. Ensemble luttons tous contre le virus en téléchargant cette application !<br> :date: __2020-08-03 22:37:17__

> C'est miraculeux, à l'aide de cette appli, j'ai pu guérir de mon cancer et ma femme est sortie du coma dans lequel elle était plongée depuis des mois durant.. Je remerci le gouvernement pour l'apport d'une telle appli, si utile dans ce monde si sombre; que les âmes du Stux n'oseraient pas s' y perde. Merci Mr. Macron<br> :date: __2020-08-03 04:30:03__

> Très facile à maîtriser. Si vous laissez google vous suivre à la trace (ce qui est sûrement le cas) n'hésitez pas à indiquer votre position anonymement en permanence pour lutter contre le covid.<br> :date: __2020-08-02 20:44:13__

> Tres bonne initiative, merci le gouvernement. Je pense qu'au lieu de raler qu'elle n'est pas obligatoire, il faudrait raler que les français soient aussi peu responsables... En tout cas, ça serait vraiment pratique si on pouvait choisir des heures d'activation, genre de 8h à 20h, pour quand même economiser un peu la batterie!<br> :date: __2020-08-01 09:29:53__

> Simple, et pas de localisation, juste du positionnement par rapport au autres et seulement en Bluetooth. Je la conseille,<br> :date: __2020-07-30 13:42:27__

> Très bonne application soyont tous unis contre se virus cette applis et vraiment incroyable pour nous protéger<br> :date: __2020-07-28 20:11:48__

> Très facile d'utilisation ! Commencez à l'utiliser c'est très facile !<br> :date: __2020-07-27 23:13:38__

> Aucun problème avec l'application. Il ne vaut mieux pas écouter les avis négatifs de personnes qui sont juste opposés au gouvernement qui souhaite uniquement nous protéger avec cette application.<br> :date: __2020-07-27 20:10:46__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Super application<br> :date: __2020-08-04 15:00:40__

> Je préfèrerais pas<br> :date: __2020-08-04 06:58:35__

> Installée sur Pixel 3 et fonctionne parfaitement depuis le début. Ouverte en arrière plan, une notification permanente indique si l'appli est activée ou non. Consommation batterie faible grâce à l'utilisation du bluetooth low energy, je n'ai ressenti aucune différence à l'usage. Manque peut être un aspect ludique pour savoir combien d'identifiants ont été croisés dans une journée ou depuis le début de l'installation.<br> :date: __2020-08-03 23:44:11__

> Problème de plantage<br> :date: __2020-08-03 23:36:00__

> Bonjour, je ne comprends pas pourquoi à chaque fois que je tente de l'activer, il y a marqué erreur Robert inconnu. Merci de votre réponse.<br> :date: __2020-08-02 07:41:58__

> Très bien pour l'initiative... dommage cependant que l'application ne démarre pas toute seule, ni ne fasse pareil avec le bluetooth car il est facile d'oublier de la réactiver après un redemarrage/passage en mode avion... peut-être cependant que d'un point de vue légal vous ne soyez pas autorisés à le faire... Bon courage en tous cas car il est possible d'avoir bien besoin de l'appli un de ces jours...<br> :date: __2020-07-30 14:16:07__

> Je trouve que c'est une bonne idée d'avoir créé cette appli. Je ne sais pas si elle est efficace par contre ce qui est contraignant c'est qu'elle s'arrête souvent et il faut la relancer. L'autre problème est qu'elle affiche en permanence une notification indiquant qu'elle est activée. C'est dommage et je pense que c'est en partie pour cela qu'elle n'est pas utilisée plus que ça.<br> :date: __2020-07-29 15:59:59__

> Bon apparemment, désormais, l'appli se réactive automatiquement au redémarrage du Smartphone. donc correction de mon précédent commentaire qui était négatif à ce sujet.<br> :date: __2020-07-29 13:17:40__

> Neant pour le moment<br> :date: __2020-07-26 17:43:29__

> Application facile d'utilisation<br> :date: __2020-07-26 14:34:26__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Aplli certainement utile, simple et claire. Installée dès le 1et jour en 3 min chrono sur Samsung A6. MAIS: 1)Consomme trop de batterie.. 2) pourquoi les utilisateurs d'android n'ont pas de message quotidien comme sur Apple sur le fait d'avoir croisé ou non des personnes infectées? On a l'impression que l'appli ne fonctionne pas... 3) conflit avec les autres appareils bluetooth : notamment android auto (très désagréable en voiture). Obligé de la réactiver en sortant de la voiture (oubli)!<br> :date: __2020-08-04 11:06:20__

> Activation réussie après un re installation<br> :date: __2020-08-03 15:47:22__

> Où est l'UX dans cette application ????! Une application qui reste active quoi qu'il arrive, un peu de retour vers l'utilisateur courageux qui l'a téléchargée pour assumer la responsabilité collective (stat, contribution, ...), ... En 2020, comment peut-on ne pas profiter des nombreuses compétences françaises en la matière ??? 😉<br> :date: __2020-08-02 12:30:36__

> Consomme beaucoup de batterie<br> :date: __2020-08-02 10:39:59__

> Consomme beaucoup de batterie<br> :date: __2020-08-02 10:37:45__

> Dommage qu'il faille réactiver régulièrement l'appli....<br> :date: __2020-08-02 09:33:37__

> Dommage. L'application me dit que mon téléphone est incompatible... Un Samsung qui n'a "que" 4 ans...<br> :date: __2020-08-01 17:33:12__

> Il s agit d une veille. Difficile de savoir si elle fonctionne correctement. L application ne donne aucune information.<br> :date: __2020-08-01 13:40:18__

> L. Application ne fonctionne plus<br> :date: __2020-07-31 10:07:41__

> L'app arrete et redémarre la connexion Bluetooth de mon téléphone tous les quarts d'heure. Desinstaller stopcovid corrige le pb, preuve que c'est bien l'app. EDIT: même pb avec la dernière version.<br> :date: __2020-07-31 01:59:01__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Non compatible avec le suivi européen 🙄<br> :date: __2020-08-04 17:08:05__

> L'application c'est éteinte toute seule pendant.que je l'utilisais et je ne sais pas depuis combien de temps.<br> :date: __2020-08-03 20:26:25__

> Samsung A40. J'ai déjà hésité au début à installer cette application à cause des nombreux mauvais retours que je lisais. 2 jours après l'avoir installée, l'application s'est fermée toute seule. Je l'ai réactivé pour lui donner une deuxième chance. Elle est restée en place de nombreuses semaines sans aucun incident, bien que j'éteigne mon téléphone tous les soirs. Elle était toujours là le lendemain. Mais brusquement, il y a quelques jours, elle a carrément disparu du téléphone. Tant pis.<br> :date: __2020-08-03 19:59:18__

> Après un fonctionnement erratique les premiers jours avec des désactivations sans raison évidente et plantages lors de la réactivation, l'application semble plus stable. Manque une alerte plus claire lorsqu'elle est désactivée et le fonctionnement en avion, lorsque le Bluetooth doit être coupé, seules situations ces dernières semaines où j'ai côtoyé des inconnus plus de 15 minutes à moins d'1 mètre.<br> :date: __2020-08-03 16:35:28__

> Tombe en panne régulièrement. Il fait désinstaller puis réinstaller. Donc peu utile<br> :date: __2020-08-03 11:38:22__

> Intérêt très réduit sans interopérabilité avec les autres pays<br> :date: __2020-08-02 09:25:00__

> Il pourrais être mieux utiliser . Le fait d activité le bluetooth tout le temps rend l appli moins pratique. Activités une fois l appli, et la laissé en arrière plan serais mieux. Et pour le désactiver il faudrais que ce sois manuelle.<br> :date: __2020-07-30 17:18:10__

> Téléphone incompatible modèle j3 de Samsung<br> :date: __2020-07-30 16:30:21__

> Je la laisse toujours en fonctionnement. Mais au bout de quelques semaines, elle finit toujours par planter, et il n'est plus possible de la relancer. Je suis obligé de la désinstaller et de la réinstaller. Que deviennent les précédents contacts détecté pas l'application ? Aucune idée<br> :date: __2020-07-30 13:37:25__

> Ne fonctionne pas<br> :date: __2020-07-30 11:36:14__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Ne marche pas sur mon meizu MX4 L'application ne me permet pas d'interagir avec elle. Elle part en arrière plan immédiatement. Dommage pour une application essentielle...<br> :date: __2020-08-04 17:51:24__

> Impossible d'accéder à l'application, ça cherche quand il faut rentrer le code de sécurité...<br> :date: __2020-08-04 16:59:03__

> L'appli se déconnecte constamment malgré les bons paramétrages. C'est encore nos impôts qui ont payés cette M.. Un copain de sans doute !<br> :date: __2020-08-04 14:08:13__

> Se déconnecte régulièrement sur Huawei P30<br> :date: __2020-08-04 12:10:30__

> Ça ne fonctionne pas....<br> :date: __2020-08-04 11:24:30__

> L'application ne oeut pas être installée depuos un compte google étranger, pourquoi cette restriction aussi inutile que dangereuse ?<br> :date: __2020-08-04 11:19:08__

> Application qui ne fonctionne pas avec mon.téléphone(huawei ) .à croire que j ai un nokia 3210!!c est une honte de nous inviter à installer cette appli alors qu'elle est compatible qu avec les téléphones dernier cri. Du gros n importe quoi encore!!<br> :date: __2020-08-04 10:40:19__

> Malgré les nombreuses demandes des utilisateurs, l'application est toujours en attente d'activation lorsque le réseau est perdu, ou lorsqu'on sort du mode avion...L'appli peut donc ne pas tourner pendant des jours, sauf à revenir dessus régulièrement. Au total, application parfaitement inutile.<br> :date: __2020-08-04 10:24:50__

> L'application se déconnecte quotidiennement donc aucun intérêt. Si elle n'est pas axtive en permanence.<br> :date: __2020-08-04 08:28:08__

> L'app dit qu'elle ne peut pas fonctionner sans les autorisations de localisation Bluetooth, mais qui ne peuvent pas être activées en tache de fond. Android 10. Donc inutile...<br> :date: __2020-08-04 07:40:44__


