# Социальный мониторинг
App version ``1.11``

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
| **Latest version** | 1.11 |
| **Last update** | 2021-01-27 15:18:09 |
| **Recent changes** | Добавлена новая функция «Тихий час», которая позволяет отключить запрос идентификации один раз в день на 2 часа. |
| **Installs**  | 100 000+ |
| **Category** | Медицина |
| **First release** | 22 апр. 2020 г. |
| **Size**  | 15M |
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
> - This application opens a Socket and connects it to the remote address 'Lw/b/a/a/a;->w(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
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

The Социальный мониторинг app has been installed by more than **100000** times. At this time, **9680** rated the app and its average score is **1.4561404**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 699

:star::star::star::star:: 219

:star::star::star:: 349

:star::star:: 259

:star:: 8154

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ru.mos.socmon 5 reviews"/>
</p>

> Чтобы сделать фото дается целый час времени. Выражение лица не важно, состояние тоже. Достаточно включить уведомления и просто нажать одну кнопку в приложении, чтобы отправить фото. 3-4 раза в день и всё<br> :date: __2021-03-06 12:48:45__

> Супер<br> :date: __2021-02-27 17:29:48__

> Оооочень весёлая штука!!!😏👍, Самое лучшее, что могли придумать наши разработчики!!!🤭🤣🤣<br> :date: __2021-02-25 09:08:32__

> Фух, ну вот и я переболел ковидом. Приложение работает, отслеживает, отправляет запросы, проблем не выявлено. Правда батарейку жрёт, но я думаю это от постоянных запросов джипиэс. Наверное только это неудобство, которое решается зарядкой, ибо и так сидишь дома.<br> :date: __2021-02-22 19:48:20__

> Приложение работает нормально, хорошая и нужная функция «тихий час»<br> :date: __2021-02-22 06:43:37__

> 14 дней карантина и мониторингп позади... пишу только потому, что увидел здесь кучу странных отзывов, с которыми не сталкивался ни я ни мои знакомы, которые тоже прошли карантин. ни разу запро не приходил раньше 10 утра и позже 8 вечера... ни разу не было проблем с проверкой фото, на всю процедуру фото-отправка-подтверждение ни разу не ушло больше 2х минут. у меня самсунг а41, все работает замечательно.<br> :date: __2021-02-18 18:50:06__

> Спасибо за добавление в приложение Тихий час. Не мешает детям уведомление и можно самому лечь спать а не ждать смс.<br> :date: __2021-02-09 11:17:06__

> Исправились. Сообщения приходят и в виде СМС.<br> :date: __2021-02-09 11:14:20__

> Проблем не испытывал и не испытываю. Скачал, зарегистрировался, работает. P.s.: самое милое обновление, что я встречал в приложениях, функция "Тихий час"))))<br> :date: __2021-02-06 19:55:47__

> Приложение у меня работало отлично. К нему претензий нет, единственное, что горячая линия никогда ничего не знает))) фото 3-4 раза в день нужно было делать. Если фото светлое и нагрузка на сервера небольшая, то его в ту же минуту принимают. Однако болезнь тяжёлая, и приходилось в 9 будильник ставить , спать по полчаса... днем всегда рядом телефон и страх от того, что вдруг пропущу уведомление. Приложение не висло, с технической стороны все ОК. Отключилось само, соответственно предписанию.<br> :date: __2021-02-03 11:00:18__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ru.mos.socmon 4 reviews"/>
</p>

> Периодически случались сбои<br> :date: __2021-03-03 09:16:47__

> Upd 22.02.2021 По итогу использования. Приложение наконец доработали более-менее. Действительно, несмотря на то, что приходят оповещения, даже когда в больнице, санкции не наступают. Кроме того, после того, как выписали, ещё некоторое время приходили оповещения, но без последствий (метки уже не ставила) . Видимо, ещё из-за большого наплыва больных осенью ответы поддержки были вообще не по теме, никто не вчитывался, о чем вопрос, автоматически выбирался ответ. Ну да ладно, пережили.<br> :date: __2021-02-22 08:13:26__

> Нормальная программа, но вот с оповещениями у неё плохо. Тот пилик, что она выдаёт часто просто не замечаешь. Как и приход смски. Приходится постоянно смотреть в телефон, чтобы не пропустить фотографирование. Сделали ли бы они возможность ставить на оповещение разные мелодии, цены бы им не было.<br> :date: __2021-02-18 20:04:26__

> Функционирует отлично, единственное пожелание- наличие статуса об активности ограничений, типа "Наблюдается/Не наблюдается"<br> :date: __2021-02-10 12:21:19__

> После регистрации в приложении с удивлением для себя заметил, что мое отчесво написано с ошибками, да и адрес не совсем тот. Позвонил в поддержку. Через неделю все исправили.<br> :date: __2021-02-09 10:15:14__

> Мдэмс...вот тебе и мониторинг)<br> :date: __2021-02-05 15:02:20__

> Не имеющая вес организация. Собрав информацию, не влияет на социум.<br> :date: __2021-02-03 11:03:21__

> Приложение работает. Зарегистрироваться удалось с первого раза. Предложение к разработчикам. По возможности сделайте отображение статуса пациента, например: на карантине, снят с карантина.<br> :date: __2021-02-01 03:03:07__

> В целом приложение работает хорошо, нареканий нет. Иногда, правда, бывают задержки с проверкой и проблемы при отправке фотографии по запросу. Но это за время моего использования было всего лишь один раз.<br> :date: __2021-01-30 12:56:06__

> Странно, что я это пишу, но надо отдать должное. На Андроиде программа работает нормально. Единственное пожелание - надо было сделать опцию выбора звука для уведомления, поскольку сейчас пришлось поменять звук сообщений от мессенджеров, чтобы не пропустить запросы из приложения. Раньше 10 запросы не шлют, можно спать утром.<br> :date: __2021-01-17 12:14:02__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ru.mos.socmon 3 reviews"/>
</p>

> Если у Вас бессонница или Вы любитель поспать до обеда,будьте морально готовы к постоянному недосыпу,помимо болезни,либо заплатить штраф за просрочку. Небольшой лайфхак для сов и страдающих бессонницей, как я. Ставите будильник на 9.55-просыпаетесь. Если фото не надо,то ставите режим "тихий час" и следующий будильник на 12.55.<br> :date: __2021-02-28 11:29:43__

> Если у вас техсбой( нет возможности сделать фото в приложении) и уже пришло на телефон уведомление о необходимости отправить фото, то почему тосле исправления техсбоя, не приходит повторное уведомление. Очень не удобно больному человеку сидеть и мониторить, когда заработает, что бы фото отправить. Делайте повторную рассылку после исправления техсбоя. И прежде, чем устанавливать см, позвоните и расскажите как это сделать и как он работает, люди за 70+ плохо в этом разбираются<br> :date: __2021-02-27 10:12:19__

> Сделайте возможность сфотографировать больного другому человеку. С температурой под 40 сфотографировать самого себя весьма не просто.<br> :date: __2021-02-24 14:59:48__

> Всем фото делать 6р/день или мне 1му?<br> :date: __2021-02-23 16:20:43__

> Сегодня перестали приходить запросы на идентификацию ... посмотрим может придёт теперь штраф 🤔<br> :date: __2021-02-23 12:23:30__

> В плане работы приложение работает нормально. Но для болеющего человека - оно является стрессом. Потому что не можешь нормально отключить телефон и звук и боишься пропустить требование о фото. Я очень советую разработчикам сделать возможность болеющему выбирать время когда он бодрствует, а когда спит. Делать под одну гребёнку с 9 до 22 - не вариант. При бессоннице я до 4 утра не сплю и приходится вставать в 9 включать звук чтобы ничего не пропустить. Очень морально тяжело.<br> :date: __2021-02-16 11:19:08__

> Телефон ребенка (16 лет) уже 3 сутки на проверке. Нет возможности "мониторится", сегодня час потратила на выяснение причин. 122 - футболит меня в тех.поддержку, тех.поддержка рекомендует разбираться с 122!!!<br> :date: __2021-02-08 19:54:44__

> Было бы очень удобно если бы по окончании карантина приходило уведомление. "Ваш карантин закончен, можете удалить приложение. " не все открывают больничный, на сколько я поняла карантин заканчивается через 14 дней. И запрос на селфи просто перестаёт приходить.<br> :date: __2021-02-08 13:03:26__

> Добрый день. Устанавливала приложение с 02 на 03 февраля. До сих пор проверка данных. Что за проверка данных мне не понятно??? Сколько это может продолжаться? Не будут ли штрафы от от того, что не могу выслать фото? Можно как то продумать эти вопросы...<br> :date: __2021-02-06 12:34:51__

> Приложением пользоваться просто, и это плюс. Но уведомления приходят с задержкой. Т.е. вы только получили уведомление, а в приложении отмечено, что оно направлено 15 минут назад, и на фото у вас не один час, как вы думаете, а 45 минут. Однажды уведомление пришло уже просроченным. Благо штрафы предполагаются за "систематические нарушения" (цитата службы техподдержки приложения). Но вот большой вопрос кто виноват в долгой доставке уведомлений и как доказать свою невиновность в случае штрафа.<br> :date: __2021-02-04 12:15:20__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ru.mos.socmon 2 reviews"/>
</p>

> Нет возможности переключения в свой режим дня. Более 20 лет живу как сова, сплю днем. С этим приложением не сплю уже 10 дней! Могу позволить себе дремать между будильниками, которые стоят на каждый час, начиная с 9 утра! Издевательство! Я больше потеряла здоровья от этого контроля! Все хронические болячки повылазили! При этом у меня даже корону и не нашли, было превышение иммуноглобулинов на фоне отека Квинке! Тихий час не позволяет выспаться! 2часа это копейки<br> :date: __2021-03-03 07:50:55__

> Приложение присылает запрос на фотографию, а при переходе в само приложение функции фотографирования НЕТ. По истечении часа появляется информация, что ты пропустил фотографирование.<br> :date: __2021-02-27 10:03:15__

> Очень,часто делать фото,2-3 в день,в полне достаточно,а тут по 5 просят,<br> :date: __2021-02-25 23:02:21__

> не загружается<br> :date: __2021-02-25 14:16:59__

> Сегодня 25.02.2021 приложение не работает<br> :date: __2021-02-25 14:15:48__

> Что за дебилизм после каждой удачной проверки слать пуш-сообщения? Нахрена мне это знать? Я должен знать только когда проверка НЕ пройдена, и надо отправить фото повторно. Меня только это беспокоит. Что за дебилоид разрабатывал логику поведения программы? Вы, блин, ещё каждый час отправляйте подтверждение в виде пуша, что я действительно нахожусь по адресу! (сарказм) Я здоров, но живу с больным и тоже на карантине. У меня ночной график работы на удалёнке.Днём я сплю, а вы, твари, спать не даёте!<br> :date: __2021-02-20 16:40:43__

> Какое время требуется для проверки данных?Установила несколько часов прошло. Приложение не работает<br> :date: __2021-02-13 22:10:33__

> Разработчики, читайте! Из-за этого приложения меня оштрафуют за то, что я не услышал его звуковое оповещение, а не за то, что я нарушил самоизоляцию! Все дни таскал смартфон по квартире с собой, а потом вечером все равно не услышал "бульканье" от пришедшей СМС! Вам уже люди писали о тихом сигнале Вашего приложения! Почему не включить громкий сигнал как от входящего вызова, чтобы слышать даже в соседней комнате?! Можно за 10минут до истечения срока отправки фото. Можно выбрать галкой в настройках<br> :date: __2021-01-23 19:32:32__

> Ироды! Что б вам для получения зарплаты так каждый день прходилось отмечаться. Сделайте хотя бы повтор оповещений. Чтобы люди сами могли настроить напоминания, скажем, каждые 5 / 10 /15 мин.<br> :date: __2021-01-22 22:57:25__

> Приложение сырое, часто глючит. Один из основных багов: приложение даёт сделать фотографию, но не даёт её отправить, ХОТЯ ВЫДЕЛЕННОЕ НА ЭТО ВРЕМЯ - ЧАС, ещё не закончился!!!<br> :date: __2021-01-21 14:38:35__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ru.mos.socmon 1 reviews"/>
</p>

> К разработчикам притензий нет, приложение сделано более менее качественно. Root права не являюся особой помехой, геолокация меняется спокойно без них. Можно и убрать проверку root. У меня вопрос к людям, чей "гениальный" мозг додумался до такой концепции слежки за больными. Что делать в ситуации, если после бессонной ночи, вызванной вирусом, мне приходится терпеть сильнейшую боль в голове и ждать смс когда же попросят сделать фото. Ответьте на вопрос, гении профилактики болезни.<br> :date: __2021-03-06 14:23:49__

> Программа зависла на третьем шаге на весь день. Полный идиотизм эта программа. Что делать, неизвестно.<br> :date: __2021-03-06 09:02:24__

> Отвратительная идея! Почему на своем больничном, я могу спать только 2 часа днем? Почему меня сразу записали в преступники?<br> :date: __2021-03-05 19:30:04__

> Первые два дня запросы приложения синхронно дублировались в смс. На третий день смс перестали приходить или приходили спустя ровно час после информирования о запросе из приложения. В следующие дни стали пропадать и смс, и информирование от приложения. Открываешь приложение, а там висит запрос, но ни смс, ни сообщения от приложения не было, делаешь фото, спустя час приходит смс. Да уж, телефонные мошенники отдыхают в сравнении с этим.<br> :date: __2021-03-05 18:13:54__

> Не работают уведомления. Звука нет никакого. Ощущение, что это сделано специально для выписки штрафов. Приходится постоянно смотреть в телефон. Ужас.<br> :date: __2021-03-05 17:58:28__

> Ужасное предложение. Видимо людям нечем заняться. Как жаль что нельзя поставить 0 звёзд.<br> :date: __2021-03-05 17:10:25__

> Геноцид больных! Мало того, что состояние при болезни отвратительное, так ещё и постоянно дёргаешся, не пропустил ли очередную фотосессию. Да и непонятно как попасть теперь на КТ, хотя состояние ухудшилось. Я что, теперь должен платить ещё и штраф за посещение поликлиники, а потом его опротестовывать? Приложение, которое очень бы понравилось основателям Гестапо!<br> :date: __2021-03-05 11:00:14__

> Унылый гумус... Тех поддержка практический не работает, те на словах горазды, а на деле ничего не могут. Внесли не верные данные по адресу карантина, четыре дня так и не смогли поменять на верный. Не устанавливайте на свой смартфон, пусть вам привозят курьером казенный аппарат...<br> :date: __2021-03-05 08:26:47__

> За. 14 дней 2 раза подвисало.<br> :date: __2021-03-05 07:44:39__

> Я искренне не понимаю, почему я, не нарушая изоляции, должен платить штраф только за то, что на протяжении многих лет привык пользоваться телефоном раз в несколько дней. Для меня лично очень сложно следить за уведомлениями каждые пол часа в здоровом состоянии, тем более непонятно, как себя вести, если ты температуришь, пытаешься, например, заснуть весь день и не можешь этого сделать. Тихий час на два часа не помогает. Вероятно приложение - это просто еще один инструмент пополнения госбюджета.<br> :date: __2021-03-04 13:32:19__


