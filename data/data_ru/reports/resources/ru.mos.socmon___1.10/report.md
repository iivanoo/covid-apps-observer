# Социальный мониторинг
App version ``1.10``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Социальный мониторинг icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Социальный мониторинг |
| **Unique identifier** | ru.mos.socmon |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=ru.mos.socmon](https://play.google.com/store/apps/details?id=ru.mos.socmon) |
| **Summary**  | Приложение для контроля за соблюдением гражданами режима изоляции на дому |
| **Privacy policy** | [https://www.mos.ru/privacypolicy/socmon/](https://www.mos.ru/privacypolicy/socmon/) |
| **Latest version** | 1.10 |
| **Last update** | 2020-12-18 12:02:18 |
| **Recent changes** | Улучшение работы приложения по замечаниям пользователей. |
| **Installs**  | 100 000+ |
| **Category** | Медицина |
| **First release** | 22 апр. 2020 г. |
| **Size**  | 14M |
| **Supported Android version**  | 6.0 и выше |

### Description
> Приложение «Социальный мониторинг» создано для пациентов с подтвержденным диагнозом COVID-19 и граждан контактировавших с ними, проживающих в Москве и соблюдающих предписанный им режим изоляции. С его помощью пациент информирует город о добросовестном соблюдении карантина.
<br>При регистрации пользователь подтверждает номер телефона, делает фотографию, геолокация (местонахождение) отправляется автоматически. Это нужно для того, чтобы проверить, находится ли пользователь в той же локации, которую указал в согласии, выбирая лечение на дому.
<br>Чтобы у пользователя не было возможности оставить смартфон дома и выйти на улицу без него, приложение в случайное время присылает СМС-уведомления с запросом дополнительного подтверждения — для этого потребуется сделать селфи.
<br>Если пользователь покидает исходную геолокацию или не реагирует на уведомления, система предупреждает городские службы о возможном нарушении режима изоляции.
<br>Личные данные, которые пользователь передает сервису, определены в согласии на получение медицинской помощи на дому и соблюдение режима изоляции либо в постановлении главного санитарного врача города Москвы. Все данные, которые пользователь передает приложению, хранятся в защищенном виде на серверах Департамента информационных технологий и используются в строгом соответствии с федеральным законом № 152-ФЗ "О персональных данных".


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Информационный город ГКУ |
| **Website**  | [https://www.mos.ru/city/projects/monitoring/](https://www.mos.ru/city/projects/monitoring/) |
| **Email** | socialmonitoring@mos.ru |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4+%D0%93%D0%9A%D0%A3](https://play.google.com/store/apps/developer?id=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4+%D0%93%D0%9A%D0%A3) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>USE_FULL_SCREEN_INTENT** | Normal | Required for apps targeting Build.VERSION_CODES.Q that want to use notification full screen intents. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 
 **com.msk.socmon<br>PERMISSION** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | adobe.com | Adobe Inc. | :us: US | 1986-11-17 05:00:00 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | mos.ru | - | - | 1996-12-23 09:49:03 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lv/b/a/a/a;->w(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Method sendUrgentData() is not supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Method setHandshakeTimeout() is not supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Method setOOBInline() is not supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Method setSoWriteTimeout() is not supported.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Socket closed' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Socket is closed' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Socket is closed.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Socket is not connected.' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'socket is closed' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library: 'conscrypt_gmscore_jni'<br>
> - This application loads a native library: 'conscrypt_jni'<br>
> - This application loads a native library: 'tool-checker'<br>
> - This application executes a UNIX command<br>
> - This application executes a UNIX command containing this argument: 'getprop'<br>
> - This application executes a UNIX command containing this argument: 'mount'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Социальный мониторинг app has been installed by more than **100000** times. At this time, **9097** rated the app and its average score is **1.3493078**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 416

:star::star::star::star:: 232

:star::star::star:: 271

:star::star:: 271

:star:: 7907

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ru.mos.socmon 5 reviews"/>
</p>

> а мне приложение понравилось, ничего лишнего + дублируют по смс оповещения синхронизация с будильником или настройка мелодий оповещения из приложения была бы не лишней. сейчас что бы настроить длинную мелодию на оповещении, необходимо установить mp3 на сообщение и отключить оповещение в приложении т.к. звук приложения скидывает сигнал смс потому что приходит сразу после смс<br> :date: __2021-01-09 16:33:49__

> Спасибо<br> :date: __2021-01-09 09:03:14__

> Нормальное приложение! В день приходит 3-4 уведомления. Плюс запрос дублируется по СМС. Час на отправку фото. Всё просто и понятно. Те, кто жалуются, что не слышат звук уведомления, или короткий сигнал, ребята, изучайте свои смартфоны! Я сразу, в настройках телефона, выставила длинную мелодию конкретно для этого приложения и никаких проблем! Ну а уж отрегулировать громкость телефона и дитё малое сумеет....<br> :date: __2021-01-08 18:12:53__

> Отличное приложение!<br> :date: __2021-01-05 10:32:36__

> Господа разработчики, благодарю вас за отличную прогу! Спасибо!<br> :date: __2021-01-05 10:26:13__

> все что надо делает<br> :date: __2021-01-05 09:26:22__

> Очень понравилось! В карантине лучше чем на море! А с приложением нет чувства одиночества, знаешь что за тобой следят, волнуются! Спасибо!<br> :date: __2021-01-04 09:54:20__

> Сколько же полоумных клоунов в комментариях, огромное спасибо государству и разработчикам,если бы не это приложение, эти клоуны шароебились бы по улицам<br> :date: __2021-01-03 13:15:33__

> После перехода на версию 1.9 стало отличным приложением.<br> :date: __2021-01-02 11:14:42__

> Вроде норм работает, без косяков. Пришлось последовать совету техподдержки, перезагрузить телефон, тогда приложение запустилась. Подтверждение номера пришло в течении суток, хотя сначала думал, что не придет. Каждый день стабильно приходят запросы на селфи и по смс и в приложение, с фитнес браслетом удобно, ниразу не пропускал, в течении минуты двух отсылаю и минуты 2-3 подтверждается. Субъективно мое мнение, болезнь проходит в лёгкой форме. Нету вкуса и запаха...<br> :date: __2020-12-31 15:26:46__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ru.mos.socmon 4 reviews"/>
</p>

> Что касается уведомления (тихое или громкое) его можно выбрать в настройках звука уведомлений в телефоне (сделать громче и выбрать рингтон). Молодцы, что дублируют в смс запрос на идентификацию. Теперь пропустить реально проблематично. Что касается самой всей этой ситуации, то ощущение, что ты находишься под домашним арестом по уголовному делопроизводству и это пипец))) А по факту: берегите себя и окружающих, находитесь дома и не заражайте других. И, конечно же, скорейшего выздоровления всем!<br> :date: __2021-01-08 13:32:54__

> Со своей функцией справляется. Просидел на самоизоляции 2 недели, ни одной фотки не пропустил. ИМХО в приложении есть недостатков: 1. Самая идея, что вы мне смс, а я вам фотку за час- это бред, больные люди могут отдыхать, сам спал по 2 часа, но ИМХО это нормально. Нужен вариант, чтобы я предупредил вас, что прошу не беспокоить, я лечусь, а не вам информирую. 2. Громкость уведомления. Она должна быть адской 3. Добавить в приложение скан моего согласия и срок самоизоляции<br> :date: __2021-01-08 12:38:17__

> Спасибо разрабам всё работает хорошо,по крайней мере у меня.<br> :date: __2020-12-27 20:16:17__

> К приложению вопросов нет. Простое и интуитивно понятно. Проверка вмеру адекватно.<br> :date: __2020-12-27 18:49:17__

> Хорошее приложение. Жаль только, что не уведомляет каждые 5-10 минут о том, что надо пройти идентификацию. За это звезду снимаю. Но на телефоне можно отдельно настроить повторяющееся уведомление об смс. И кто пишет, что проспал и штраф пришел - это не так. У меня несколько знакомых пропустили один раз и ничего им не было за это. Ерунда только со снятием с карантина. Телефоны какую-то ерунду в основном говорят. Но это вопрос не к разработчикам.<br> :date: __2020-12-27 09:14:37__

> Вчера были врачи, после прочитала бумагу и сразу скачивала приложение, но мой номер сутки уже висит на подтверждении данных.<br> :date: __2020-12-27 08:50:42__

> Теперь, после обновления приложения определение местоположения заработало корректно. Минус одна звезда за то, что приложение не учитывает самочувствие человека, что он может спать и не среагировать на смс, а спать может и три часа подряд, при этом больному человеку нужно отсыпаться и восстанавливаться, а не дёргаться, что проспал смс. В общем по это проблема не разработчика, а скорее правительства Моаквы.<br> :date: __2020-12-25 14:51:22__

> Сразу хочу отметить, что отзыв оставляю о работе самого приложения, а не системы отслеживания) поначалу было менее информативно, приложение я поставила 10.12. Приходит смс и в течение часа надо отправить свое фото. Отметок о том, что фото прошло, не было. С обновлением стало удобнее: видно, во сколько пришел запрос, во сколько отправила фото и прошла ли фотл идентификацию. Следила конечно за смс, потому что раз пиликнет и всё, можно пропустить. Было бы удобнее реализовать дозвон. Всем здоровья.<br> :date: __2020-12-25 10:51:44__

> Нет данных о том, что изоляция окончена<br> :date: __2020-12-24 05:27:08__

> Приложение как приложение. Ничего особенного. Больной постоянно должен быть на связи. Поспать особо не дадут. В любом состоянии делай фото, что ты дома, а то штраф.<br> :date: __2020-12-21 19:25:33__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ru.mos.socmon 3 reviews"/>
</p>

> Здорово , что вы контролируете заражённых и все такое . Но вот не понятно, когда я уже второй анализ сделала и у меня отрицательный, почему все ещё это приложение нужно снабжать моими фото? Ещё и дома сидеть, я ведь не заразна?<br> :date: __2021-01-09 16:11:20__

> 1. Долго сверяет данные. 2. В первый день оповещения не приходили. UPD: спасибо за малоинформативнвй ответ. Оповещения так и не приходят ни мне, ни членам моей семьи. Ответ техподдержки жду уже 20 минут. Весь день всё внимание теперь телефону. Это просто... Слов нет. 3. UPD: работает лучше, но всё равно раздражает боязнь пропустить оповещение. Это очень лецствует на нервы. Сегодня (09.01.2021) снова ни одного оповещения так и нет. Слишком часто приходится звонить в техподдержку.<br> :date: __2021-01-09 15:23:27__

> Идея любопытная, но вот теперь став пациентом и невольным пользователем этого чуда, я испытываю некоторые трудности. Дело в том что я сова и привык поздно ложиться. Было бы здорово сделать возможным указать свой режим когда можно слать уведомления, а то одно я просто проспал не услышав смс. И вторая идея которая сделала бы это приложение более востребованным, это вмонтировать в него и дистанционную консультацию с врачом в чате и по видео и аудио связи. Ну и экстренный вызов скорой одним нажатием<br> :date: __2021-01-09 02:03:47__

> Ну такое, очень тихое уведомление, сделайте как будильник, ибо человек будет спать и не услышит , а потом лови штраф на 4 тыс<br> :date: __2021-01-08 23:12:07__

> Приложение иногда даёт сбой. Первые пару дней идёт проверка номера. В принципе, нормально.<br> :date: __2021-01-06 12:04:55__

> Нет возможности настроить на громкий звонок, а смс не слышно. У пожилых людей часто ослаблен слух. Больные люди часто днём спят. Простуда часто сопровождается отитом.<br> :date: __2021-01-05 07:43:19__

> С какого-то момента стало ОЧЕНЬ ТИХИМ. Я рядом с телефоном - не слышал что был запрос. Напропускал в итоге. Не знаю, подстава прям какая-то.<br> :date: __2021-01-03 17:23:22__

> Приложение доработано по отзывам: приходит сообщение о времени, когда необходимо отправить фото, о том, что фото отправлено и проверено.Доработайте и в плане сообщений, когда приложение можно удалить (окончание изоляции): у мужа закрыли больничный, врач сказал, что сообщения больше не будут в этот день приходить.В итоге сообщения пришли, только началось не с утра, как обычно, а во второй половине дня.Наводит на мысль, что у вас ждут, когда удалят приложение, чтобы выписать штраф<br> :date: __2021-01-03 15:47:42__

> Приложение стабильно работало неделю. Соглашусь, что уведомления приходят очень тихо, постоянно напрягаешься пропустить смс. Из плюсов:понятный режим оповещения с 9 до 22,нет ночных смс (с другой стороны и спать я, например, рано могу лечь, но по факту последнее смс позже 20 ч не приходило), после отправки фото, приходит отбивка, что фото прошло проверку, ранее говорят такой опции не было. Косяк- со второй недели самоизоляции прекратили приходить пуш-уведомления,надеюсь штрафы не получу.<br> :date: __2021-01-02 06:07:48__

> Вцелом, приложение рабочее. Главный его косяк - тихое, невнятное уведомление. Невозможно настроить его звук, громкость, нет мигания вспышки, свечения экрана, и пр. Его легко пропустить за игрой, фильмом или сном. Обычный будильник это может делать, а уберприложение от мэрии Москвы - нет. Т.е. полностью забили на главную задачу - уведомить пользователя о необходимости сделать фото. Если исправят, то будет на четверочку. Для пятерки потребуется более читабельный текст, т.к. пенсионерам это мелко.<br> :date: __2021-01-01 08:22:26__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ru.mos.socmon 2 reviews"/>
</p>

> Приложение вроде не плохое, но уведомления никуда не годятся... Я себя плохо чувствую, сплю постоянно и просто иногда не могу услышать его. Лучше бы это было что то типо видиозвонка. Тем более в течении часа, данного на отправку фото, я могу быть где угодно<br> :date: __2021-01-09 13:57:05__

> Совершенно бестолковое приложение с точностью локализации около 10км.<br> :date: __2021-01-08 17:04:19__

> 1.ОЧЕНЬ неудобно без индивидуального звукового оповещения, пропустить легко уведомление. От этого нервничаешь и постоянно залезаешь в телефон - жизнь вокруг него это нереально. 2.ОБРАТНАЯ СВЯЗЬ ОДНОСТОРОННЯЯ. Я писала в тех.поддержку дважды и дважды ничего не получила в качестве автореплая (ваше обращение получено, благодарим за ...) 3. Нам перестали приходить смски на 13ый день, воспринималос как сигнал к выходу.<br> :date: __2021-01-07 10:48:46__

> Было бы хорошо добавить возможность увидеть историю отправленных тобой обращений в техподдержку плюс отбивку на указанный электронный адрес о том, что твое обращение получено. А то пишешь, отправляешь - как в трубу. Ушло/не ушло, получено/не получено... Непонятно. Ну и хорошо бы, чтобы ответ по решению проблемы на электронную почту тоже приходил, как обещано в описании. Написала 2 обращения, прошло несколько дней - ни на одно ответа нет. Ошибок конечно, ранее описанных, очень много.<br> :date: __2021-01-06 12:13:52__

> А если я засну днём на два часа и пропущу ваше смс? Или мне надо целый день не спать сидеть ловить ваше смс?<br> :date: __2021-01-06 07:42:06__

> Нет никакой техподдержки с оператором.<br> :date: __2020-12-31 13:04:37__

> При плохом самочувствии еще и с приложениями разбираться приходиться. Сложно. Почему- то пишет, что мое местонахождение не определяется.<br> :date: __2020-12-29 12:10:46__

> Регистрация не проходит. Удаляю приложение, устанавливаю и опять не проходит....<br> :date: __2020-12-29 11:23:04__

> Тупит. Не реагирует на нажатие кнопок<br> :date: __2020-12-28 10:20:30__

> Иногда уведомления даже и не слышала ибо была занята своими делами, могла уснуть в послеобеденное время или же проспать все утро. Я не нарушитель, но система может запросто посчитать меня таковым ибо я не слышу уведомления. Это огромный стресс, я не могу уснуть не подумав о том что я пропущу идентификацию. Я понимаю необходимость проверок, но нельзя ли сделать отслеживание геолокации+звонки на телефон например. Звонок по крайней мере будет услышан, ты на него ответишь и будешь дальше отдыхать.<br> :date: __2020-12-26 15:11:32__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ru.mos.socmon 1 reviews"/>
</p>

> У меня вообще не работает. Установилось, но не запускается. Мучаюсь уже второй день. И что делать в такой ситуации?<br> :date: __2021-01-09 18:13:28__

> Не проходит подтверждение. И куда позвонить в случае если программа не работает🤦‍♀️<br> :date: __2021-01-09 17:45:24__

> Это дно ребята!<br> :date: __2021-01-09 17:45:21__

> Установила маме.На второй день смартфон начал жить своей жизнью: открывать, закрывать, включать, выключать, записывать....т.е. демонстрация вирусного поведения налицо.Антивирусное ПО ничего не обнаружило.Само приложение стало не работоспособным: оно просто не открывается.Кое как удалили эту дрянь со смартфона, ситуация не изменилась!!! Вывод: скачивание данного ПО вывело из строя рабочий смартфон!!! В ремонт не сдать,т.к.смартфон не самой актуальной версии, но он был исправен, а теперь нет!!!<br> :date: __2021-01-09 17:33:01__

> Пишу с юристом жалобу в прокуратуру на создателей этого приложения . Пожалуйста присоединяйтесь ко мне. Коллективно это эффективнее будет<br> :date: __2021-01-09 15:46:09__

> Установилось только 2 из 3.Дальше не даёт никаких действий. Обратилась в техническую поддержку. Написала обращение в Роспотребнадзор о плохо работающем приложении.. Врач не удосужился заполнить мой экземпляр постановления. На следующий день уточнял у вновь вызванного врача, сказали, что номер актуальный. о Оставляла заявка по обращению SD15373226<br> :date: __2021-01-09 14:49:53__

> Вообще не регистрирует<br> :date: __2021-01-09 14:40:38__

> Приложение не про людей, а про штрафы. Как и всё это конченное государство.<br> :date: __2021-01-09 14:07:33__

> Приложение уже три дня подтверждает номер телефона, при этом периодически запрашивает всякого рода разрешения. В итоге, непонятно мониторит кто нибудь что я дома или это просто пустышка. За три дня никаких оповещений, ничего, полная тишина. Я честно сижу дома на карантине, но приложение не активно так как все подтверждает мой номер телефона. Странно...<br> :date: __2021-01-09 10:04:06__

> Нифига не работает. Пишет, что приложение не работает на устройстве с root. Рута на телефоне нет.<br> :date: __2021-01-09 08:52:45__


