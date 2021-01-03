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

> Сколько же полоумных клоунов в комментариях, огромное спасибо государству и разработчикам,если бы не это приложение, эти клоуны шароебились бы по улицам<br> :date: __2021-01-03 13:15:33__

> После перехода на версию 1.9 стало отличным приложением.<br> :date: __2021-01-02 11:14:42__

> Вроде норм работает, без косяков. Пришлось последовать совету техподдержки, перезагрузить телефон, тогда приложение запустилась. Подтверждение номера пришло в течении суток, хотя сначала думал, что не придет. Каждый день стабильно приходят запросы на селфи и по смс и в приложение, с фитнес браслетом удобно, ниразу не пропускал, в течении минуты двух отсылаю и минуты 2-3 подтверждается. Субъективно мое мнение, болезнь проходит в лёгкой форме. Нету вкуса и запаха...<br> :date: __2020-12-31 15:26:46__

> а мне приложение понравилось, ничего лишнего + дублируют по смс оповещения синхронизация с будильником или настройка мелодий оповещения из приложения была бы не лишней<br> :date: __2020-12-29 11:34:24__

> Замечательно, не понимаю только почему это приложение занимает 7.5 мбайт а Емиас больше чем полгига. Сделали бы Емиас.лайт, хотя к этому оно и не относится.<br> :date: __2020-12-27 15:33:28__

> 14 числа,в 19ч ,у меня почему то не прошла проверку фотография,я сделала фото и отправила,не смотрела прошла она не прошла,только после больницы и было плохо.А в остальные дни,делала повторные снимки на такие вопросы.Что же делать мне,придет штраф?Но это ваша вина,одно и то же лицо и не прошло.Я была 2 дня после больницы.18 дней в больнице провела с 60% поражения,до этотго 9 дней дома.Что мне делать?Вчера 26.12 закончился карантин и только сегодня, я первый раз буду выходить.<br> :date: __2020-12-27 06:50:02__

> Я конечно ,понимаю и разделяю волну негатива к идейной составляющей приложения, но программная часть проблем не создает. Рано утром и ночью запросы не прилетают, фотки определяются оперативно. Стабильно по 3 запроса в день, нет бесконечного спама, рекламы и глюков. Если б добавили идентификацию не по фото, а по отпечатку, было бы еще лучше. Пускай программисты на стороне зла, но работу сделали хорошо<br> :date: __2020-12-26 15:11:37__

> Приложение после изменения стало очень удобным и понятным . Спасибо разработчику.<br> :date: __2020-12-25 12:58:51__

> Я подключилась, зарегестрировалась. Меня удивляет, что прислали угрозе о штрафе 4000 р. Я болею. Сплю. Хочу, что бы приложение само отслеживало мое местонахождение. Есть и другие дела Как поделиться? На что нажать? Сложно.<br> :date: __2020-12-23 17:49:11__

> Не могу скачать приложение крутится подождите и все.Получилось после перезагрузки приложения гугл плэй маркет.<br> :date: __2020-12-23 11:31:48__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ru.mos.socmon 4 reviews"/>
</p>

> Спасибо разрабам всё работает хорошо,по крайней мере у меня.<br> :date: __2020-12-27 20:16:17__

> К приложению вопросов нет. Простое и интуитивно понятно. Проверка вмеру адекватно.<br> :date: __2020-12-27 18:49:17__

> Хорошее приложение. Жаль только, что не уведомляет каждые 5-10 минут о том, что надо пройти идентификацию. За это звезду снимаю. Но на телефоне можно отдельно настроить повторяющееся уведомление об смс. И кто пишет, что проспал и штраф пришел - это не так. У меня несколько знакомых пропустили один раз и ничего им не было за это. Ерунда только со снятием с карантина. Телефоны какую-то ерунду в основном говорят. Но это вопрос не к разработчикам.<br> :date: __2020-12-27 09:14:37__

> Вчера были врачи, после прочитала бумагу и сразу скачивала приложение, но мой номер сутки уже висит на подтверждении данных.<br> :date: __2020-12-27 08:50:42__

> Теперь, после обновления приложения определение местоположения заработало корректно. Минус одна звезда за то, что приложение не учитывает самочувствие человека, что он может спать и не среагировать на смс, а спать может и три часа подряд, при этом больному человеку нужно отсыпаться и восстанавливаться, а не дёргаться, что проспал смс. В общем по это проблема не разработчика, а скорее правительства Моаквы.<br> :date: __2020-12-25 14:51:22__

> Сразу хочу отметить, что отзыв оставляю о работе самого приложения, а не системы отслеживания) поначалу было менее информативно, приложение я поставила 10.12. Приходит смс и в течение часа надо отправить свое фото. Отметок о том, что фото прошло, не было. С обновлением стало удобнее: видно, во сколько пришел запрос, во сколько отправила фото и прошла ли фотл идентификацию. Следила конечно за смс, потому что раз пиликнет и всё, можно пропустить. Было бы удобнее реализовать дозвон. Всем здоровья.<br> :date: __2020-12-25 10:51:44__

> Нет данных о том, что изоляция окончена<br> :date: __2020-12-24 05:27:08__

> Приложение как приложение. Ничего особенного. Больной постоянно должен быть на связи. Поспать особо не дадут. В любом состоянии делай фото, что ты дома, а то штраф.<br> :date: __2020-12-21 19:25:33__

> Приложение закачал, через сутки проверили. И пошло... Смс уведомления сделать фото и отослать. Ни 1 сбоя. Фото делаю и отсылаю. В день 3-4 запроса. Только неправильно определяет место. Типа Я по дороге бегаю... Не дома сижу. GPS +- . Слава КПСС закончилось наблюдение!<br> :date: __2020-12-21 13:05:34__

> Нет возможности установить на телефон с root доступом. Полагаю, на этом проблемы не заканчиваются (симка в новом телефоне, Google аккаунт и т.п.). Пока это только предположение, как привезут новый аппарат - дополню отзыв. Дополнение: телефон привезли быстро, с СИМкой, инструкцией по установке приложения. Установил без проблем. Приложение свою функцию выполняет.<br> :date: __2020-12-21 11:22:35__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ru.mos.socmon 3 reviews"/>
</p>

> Приложение доработано по отзывам: приходит сообщение о времени, когда необходимо отправить фото, о том, что фото отправлено и проверено.Доработайте и в плане сообщений, когда приложение можно удалить (окончание изоляции): у мужа закрыли больничный, врач сказал, что сообщения больше не будут в этот день приходить.В итоге сообщения пришли, только началось не с утра, как обычно, а во второй половине дня.Наводит на мысль, что у вас ждут, когда удалят приложение, чтобы выписать штраф<br> :date: __2021-01-03 15:47:42__

> Приложение стабильно работало неделю. Соглашусь, что уведомления приходят очень тихо, постоянно напрягаешься пропустить смс. Из плюсов:понятный режим оповещения с 9 до 22,нет ночных смс (с другой стороны и спать я, например, рано могу лечь, но по факту последнее смс позже 20 ч не приходило), после отправки фото, приходит отбивка, что фото прошло проверку, ранее говорят такой опции не было. Косяк- со второй недели самоизоляции прекратили приходить пуш-уведомления,надеюсь штрафы не получу.<br> :date: __2021-01-02 06:07:48__

> Вцелом, приложение рабочее. Главный его косяк - тихое, невнятное уведомление. Невозможно настроить его звук, громкость, нет мигания вспышки, свечения экрана, и пр. Его легко пропустить за игрой, фильмом или сном. Обычный будильник это может делать, а уберприложение от мэрии Москвы - нет. Т.е. полностью забили на главную задачу - уведомить пользователя о необходимости сделать фото. Если исправят, то будет на четверочку. Для пятерки потребуется более читабельный текст, т.к. пенсионерам это мелко.<br> :date: __2021-01-01 08:22:26__

> Периодически не работает камера. Лечится остановкой приложения через диспетчер.<br> :date: __2020-12-30 15:22:40__

> Третий день не открывается приложение,как же я буду фото отсылать<br> :date: __2020-12-28 09:35:11__

> Плдвисло в один день и пришел штраф!<br> :date: __2020-12-28 07:18:54__

> Срок самоизоляции 14 дней закончился вчера. Позвонила в тех поддержку, что бы уточнить, мне подтвердили, что 27ого могу удалить прилодение. Удалила. Вышла из дома. Сегодня все ещё идут смс для подтверждения. Мне ждать штрафы????<br> :date: __2020-12-27 14:17:48__

> Не знаю,что ставить...прошли сутки,а мой номер всё ещё на проверке...указал я его верно. Или всё в систему заносят..или мне придут штрафы..<br> :date: __2020-12-25 16:19:55__

> Очень легко пропустить запрос. Добавьте возможность непрерывного звукового уведомления (как звонок), я не могу постоянно смотреть в телефон.<br> :date: __2020-12-25 16:17:13__

> Ладно, это все понятно. Но я сплю утром а днем делаю домашние дела. Телефоном почти не пользуюсь. У меня двое маленьких детей. Я просто не знаю как отслеживать. Так глаз задергается на нервах.. Одно вылечишь другое заболит. Реально звонили бы.. А не смс. Или время определенное, будильник бы ставила. А то от телефона вообще не отойти. БРЕД<br> :date: __2020-12-23 20:27:35__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ru.mos.socmon 2 reviews"/>
</p>

> Нет никакой техподдержки с оператором.<br> :date: __2020-12-31 13:04:37__

> При плохом самочувствии еще и с приложениями разбираться приходиться. Сложно. Почему- то пишет, что мое местонахождение не определяется.<br> :date: __2020-12-29 12:10:46__

> Регистрация не проходит. Удаляю приложение, устанавливаю и опять не проходит....<br> :date: __2020-12-29 11:23:04__

> Тупит. Не реагирует на нажатие кнопок<br> :date: __2020-12-28 10:20:30__

> Иногда уведомления даже и не слышала ибо была занята своими делами, могла уснуть в послеобеденное время или же проспать все утро. Я не нарушитель, но система может запросто посчитать меня таковым ибо я не слышу уведомления. Это огромный стресс, я не могу уснуть не подумав о том что я пропущу идентификацию. Я понимаю необходимость проверок, но нельзя ли сделать отслеживание геолокации+звонки на телефон например. Звонок по крайней мере будет услышан, ты на него ответишь и будешь дальше отдыхать.<br> :date: __2020-12-26 15:11:32__

> Было б здорово уменьшить частоту проверок: 2-3 в день мне кажется будет более чем достаточно чтобы пациент не сбежал далеко. Судите сами, сижу на удалёнке на электронной почте, плюс звонки из департамента здравоохранения, штаба Ковид, поликлиники, коллеги, мессенджеры... Ещё можно увеличить интервал отправки фото с часа до двух часов, а то и так невничаешь что болеешь, а теперь ещё и 4000 штрафа над тобой маячат домокловым мечом. Карантин-карантином, но надо помнить и про удобство для людей)<br> :date: __2020-12-21 15:41:30__

> Плохо работает<br> :date: __2020-12-21 07:24:41__

> Нужно приложение звонило, а не отправляло смс, или издавало длинный звуковой сигнал как будильник. Я, как и многие, от смс не просыпаюсь, сегодня уже проспала одну(<br> :date: __2020-12-19 10:49:27__

> Создатели не учитывают режим мамы с новорожденным ребенком. У мам часто нет времени помыть голову или покушать, а здесь добавляется стресс разбудить ребенка из-за сообщений. Плюс ко всему, что ребенок, который не гуляет, больше плачет. Делала фото с орущим на руках ребенком..разве это нормально? Отличная поддержка матерей. Матери и так почти на изоляции с детками. Зато к тем, кто меня заразил врач вообще не пришёл, хотя мазок был положительный, и соц.мониторинг им устанавливать было не нужно.<br> :date: __2020-12-18 06:31:31__

> Все конечно замечательно. Но больше похоже на тюремное заключение. После лечения на 11 день взяли повторно мазок, результат отрицательный. Почему после отрицательного результата я должен сидеть дома еще 4 дня и отсылать фото по запросу ? Ваша тех.поддержка предложила позвонить врачу, только не уточнила как его найти и как до него дозвониться чтоб сняли с мониторинга. И второй момент поспать с этим приложением не возможно, особенно тяжко было в первые дни болезни, это издевательство а не забота.<br> :date: __2020-12-17 21:09:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ru.mos.socmon 1 reviews"/>
</p>

> Маме 81 год поставили ей приложение, она и так никуда в течение 3х месяцев не выходит.и плохо слышит ,пришла смска и она не услышала и пропустила фото..и что теперь штраф..вы какие нибудь уж скидки делайте людям преклонного возраста а то мне стыдно за ваше приложение...<br> :date: __2021-01-03 14:30:01__

> Нам начисляют штраф, якобы за то, что мы не используем эту программу...видимо через суд будем решать и с разработчиками программы, и с теми, кто нам выписывают эти штрафы...программа просто не даёт мне выполнить условия, чтобы дальше пользоваться данным приложением..<br> :date: __2021-01-03 13:50:40__

> Нет настройки оповещения! Должен быть и громкий звук и световая индикация. + приложение жрет батарейку.<br> :date: __2021-01-03 13:45:21__

> Зарегился, а там ФИО чужое. Поддержка 50 минут не берет трубку. Фашисты.<br> :date: __2021-01-03 13:23:12__

> Насильно заставляют пользоваться данным приложением. А если отсутствует интернет или телефон не поддерживает данное приложение? Бесит<br> :date: __2021-01-03 13:23:01__

> Во-первых, приложение бесполезное: можно оставлять телефон дома и каждый раз выходить на 50минут в магазин/погулять и никак оно это не отследит. Во-вторых, приложение вредное: первый инстинкт при болезни — много спать, восстанавливая силы организма. Здесь же больным людям предлагается бодрствовать не менее 13 часов в сутки, залипать в телефон и нервничать, дабы ничего не пропустить. Если SIM была занята, смс может опоздать на час. И всё. +постоянная работа с GPS убивает батарею телефона.<br> :date: __2021-01-03 12:13:49__

> Сложилось впечатление, что приложение написано специально, что бы никто не ушёл с карантина без штрафов. Нет ни какой возможности настроить оповещение. Уснул - оповещение проморгал. А как быть людям с плохим слухом, которые звук оповещения не слышат<br> :date: __2021-01-03 11:13:42__

> Офигенное приложение. Даже не открывается. Просто сразу вылетает. Не даёт зарегистрироваться<br> :date: __2021-01-03 10:28:12__

> Мой отзыв был удален! 👏 браво...<br> :date: __2021-01-03 08:04:58__

> Безобразное приложение. Оповещений не слышно. Вынуждает все время контролировать смс, лечь поспать просто невозможно. Для больного человека сон- главное лекарство, но нет, ты как идиот, должен залипать в телефон в течении 14 дней. Где тут здоровье? Только невроз разовьётся. Про работу самого приложения промолчу. Ничего не работает. Служба поддержки молчит, дозвониться туда нереально. Так ненавидеть своих граждан могут только у нас.<br> :date: __2021-01-03 07:46:13__


