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

> Maintenant l'appli prévient quand il faut la réactiver 👍<br> :date: __2020-09-09 00:32:34__

> Desinstaller-réinstaller a fait refonctionner la chose<br> :date: __2020-09-08 21:33:42__

> Ok merci<br> :date: __2020-09-08 07:31:51__

> Hyper simple! 10 fois plus utile que TikTok, 10 fois moins invasif que Facebook.<br> :date: __2020-09-06 12:14:04__

> Bravo et merci. Point.<br> :date: __2020-09-06 11:29:05__

> N'hésitez pas à réinstaller cette appli, car elle a été améliorée, j'avais une version antérieure qui a été désactivée. Malheureusement, aucune pub ni information n'est faite dans ce sens... Même pas sur le site de santé publique France... Seul le gouvernement la recommande, ce qui est mal interprété. Pourtant ce devrait être un geste "barrière" supplémentaire.<br> :date: __2020-09-05 22:14:18__

> Les recentes correction on permis de réglé le problème de désactivation de l'application en tâche d'arrière-plan. L'application edt tres simple d'usage.<br> :date: __2020-09-04 12:19:42__

> Protection oblige..<br> :date: __2020-09-04 07:11:52__

> Cette application me rassure, c'est un bon outil de prévention.<br> :date: __2020-09-03 20:35:04__

> J'aime bien.<br> :date: __2020-09-03 14:00:07__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 4 reviews"/>
</p>

> Semble bien fonctionné<br> :date: __2020-09-09 00:21:35__

> L'appli est très chargée en messages destinés à rassurer les utilisateurs sur la protection de la vie privée. Il y en a même trop à mon goût, j'aimerais pouvoir oublier que cette application est installée, et ne pas avoir à la réactiver quand je sors du mode 'avion'. Les droits demandés sont normaux. Il n'y a pas de sur-utilisation de la batterie.<br> :date: __2020-09-07 06:34:05__

> Améliorée le 5 août. Se réactive bien après mode avion et après redémarrage.<br> :date: __2020-09-05 05:16:53__

> Le disign et les graphismes sont juste impressionnent j'ai été déçu par le gameplay qui devient untres peu palpitant au fil du temps j'ai fait top 1 que 4 fois en un semaine. Mais il reste très très jouable<br> :date: __2020-09-03 07:24:29__

> Fonctionne très bien. Une amélioration serait de connaître le nombre de téléphone utilisant l appli croisé dans la semaine, le mois, par jour. Ça aiderai chacun à percevoir l utilité de son action en installant cette appli<br> :date: __2020-08-31 01:18:42__

> Aucun prob elle fonctionne bien en fond.<br> :date: __2020-08-30 18:41:59__

> Quelles améliorations et fixes ?<br> :date: __2020-08-28 15:04:23__

> Pour saluer la démarche<br> :date: __2020-08-26 09:41:11__

> Dommage que si peu de gens l'utilisent donc compliqué que ce soit efficace mais ce n'est pas la faute de l'appli. Le bémol qui fait que je donnerai pas la 5e c'est que dès qu'on coupe le bluetooth ça désactive l'appli. C'est pénible parce qu'en plus j'ai pas de notif pour me dire que ça a été désactivé là où celle pour me dire qu'elle est activée en vrai je m'en moque, soit faut qu'elle arrête de se couper soit me prévenir quand elle est coupée plutôt<br> :date: __2020-08-25 13:03:36__

> Après avoir réinstaller le téléphone. Cela semble fonctionner. L application reste active Après avec le nombre d'utilisateur j'ai un doute que cela permet de détecter rapidement épidémie.<br> :date: __2020-08-22 13:33:05__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 3 reviews"/>
</p>

> Se désactive souvent. Il faut penser à le réactiver, sinon son utilité est faible.<br> :date: __2020-09-09 17:08:41__

> Se desactive régulièrement et souvent sans avertissements.<br> :date: __2020-09-09 07:55:49__

> L app se desactive par elle même après le mode avion...pas pratique...<br> :date: __2020-09-08 21:57:47__

> Je<br> :date: __2020-09-07 16:34:07__

> L. Application ne fonctionne plus<br> :date: __2020-09-07 15:40:12__

> Pourquoi était il désactivé ? Je viens de m'apercevoir que l'application était désactivée. Depuis quand ? Pourquoi ? Je n'en sais rien. Ce serait bien plus simple que l'application démarre en même temps que le téléphone et qu'elle reste active jusqu'à ce qu'on décide du contraire.<br> :date: __2020-09-07 12:24:50__

> L'appli fait sûrement son boulot, mais ça n'est juste pas possible de demander systématiquement à l'utilisateur la réactivation après une mise en mode avion... 🥴<br> :date: __2020-09-06 08:11:32__

> L'application se désactive toute seule systématiquement au bout de quelques jours... C'est assez ennuyeux : peut elle vraiment servir à quelque chose dans ces circonstances ? En ce qui concerne l'icone d'application qui s'affiche dans la barre en haut, c'est indispensable sur un système android pour avoir la permission d'exécution en tâche de fond en permanence (je répond à une critique lue dans les commentaires).<br> :date: __2020-09-04 08:29:04__

> Pour suivre le fonctionnement de cette application il faudrait ajouter un simple compteur qui indique au porteur du mobile le nombre de personnes qu il a rencontré ou croisé et qui ont échangé des infos avec son mobile . Actuellement après 2 mois je me demande si l appli fonctionne car on a aucune indication .<br> :date: __2020-09-03 21:21:05__

> Dommage qu'il faut le Bluetooth, pas efficace<br> :date: __2020-09-01 23:58:16__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 2 reviews"/>
</p>

> Application inutile qui ne profite pas du protocole mis en place par Google et Apple utilisé dans d'autres pays. Très bonne idée de chacun développer une solution dans son coin pour faire face à un problème global...<br> :date: __2020-09-09 09:41:11__

> Les gens sont manipulable facilement mais ma femme n'a toujours pas compris les bienfaits du sperme 😢<br> :date: __2020-09-09 09:24:57__

> Problème de Batterie, l'application consomme beaucoup trop de batterie<br> :date: __2020-09-08 23:07:30__

> L'application plante systématiquement au bout de quelques semaines. Il faut la réinstaller de nouveau pour qu'elle fonctionne. C'est la seule appli de mon téléphone qui est dans ce cas.<br> :date: __2020-09-08 17:27:45__

> Se désactive constamment<br> :date: __2020-09-08 13:13:09__

> c'est la 3ème fois que l'application se désactive toute seule et ne prévient pas.<br> :date: __2020-09-08 09:57:13__

> Elle plante au bout de quelques jours et il faut la désinstaller pour la réinstaller ensuite. C'est pas au point du tout<br> :date: __2020-09-08 08:19:07__

> À revoir<br> :date: __2020-09-07 23:37:32__

> L'intention est louable... Mais alors ça perturbe tout. Ma batterie, ultra performante en temps normal prends un coup, dès que j'ai le malheur de me connecter à une enceinte portable la musique coupe régulièrement, voir l'application me coupe le Bluetooth au hasard (pourquoi ??🤷🏻‍♀️) de temps a autre et m'empêche de me reconnecter, enfin bref. Quelques points à améliorer je pense.<br> :date: __2020-09-06 14:03:25__

> j'ai eu aucune activation je suis étonné avec le nombre de personne que j'ai pu croiser<br> :date: __2020-09-05 09:15:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.gouv.android.stopcovid 1 reviews"/>
</p>

> Dommage que cette application ne fonctionne pas pour les anciens téléphone. J'ai un samsung S5 et l'application ne peux pas s'y installer. Elle me précise que mon téléphone est trop ancien. Vraiment dommage pour une telle application.<br> :date: __2020-09-09 17:13:54__

> Ne fonctionne plus et pas de mise à jour disponible.<br> :date: __2020-09-09 14:09:40__

> A fonctionné deux jours, depuis impossible de l'ouvrir ni même de le re-téléchargé, bravo, la on ce rend compte de l'implication des fonctionnaires qui sont sensé s'en occupé.<br> :date: __2020-09-09 10:13:22__

> Crash sans cesse... mais quelle indignité !<br> :date: __2020-09-09 09:38:48__

> Le service s'arrête de façon intempestif (ce qui revient à ne pas avoir installé l'application). Dommage, dans le contexte actuel, nous avions besoin d'une application fiable pour aider à la détection des cas contacts, c'est malheureusement un gros loupé.<br> :date: __2020-09-09 09:03:37__

> Pourquoi vous avez stopped de dire le nombre de cas en France<br> :date: __2020-09-08 21:54:23__

> J ai decide d d'installer l appli suite à la recrudescence annoncee du virus.j essaie depuis ce matin. Impossible de l installer. Tant pis.<br> :date: __2020-09-08 18:09:07__

> Plante systématiquement !<br> :date: __2020-09-08 13:13:27__

> J en suis a 3 activations application et ce matin il me redemande de l'activer. Normal que les gens decedent et que les cas augmentent avec une application ne fonctionnant pas.<br> :date: __2020-09-08 11:51:03__

> Plante trop fréquemment<br> :date: __2020-09-08 06:26:52__


