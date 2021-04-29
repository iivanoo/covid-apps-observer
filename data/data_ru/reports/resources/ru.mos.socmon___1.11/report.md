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

> Что нужно делать я таки не понял. Не могу включать тихий час.<br> :date: __2021-04-28 21:45:26__

> Прикольное приложение, мне очень нравится функция "тихий час", такие милые картинки, будто в сказке.<br> :date: __2021-04-22 00:53:19__

> Когда пришлось установить приложение, начиталась отзывов, впечатлилась и ждала неприятностей, но мои ожидания не оправдались. Оно очень разумное, не напрягает.Времени, отведённого на отправку фотографии более чем достаточно. Каждое уведомление о необходимости сфотографироваться дублируется смс. "Сон час" работает исправно. За всё время самоизоляции ни разу запрос не пришел раньше 10.00. Всё прошло хорошо. Очень бы было здорово, если бы по окончании срока изоляции приходило уведомление. Спасибо<br> :date: __2021-04-20 22:06:01__

> Приложение хорошее, сбоев особых не было. Была бы ещё возможность делать фотографии с фронтальной камеры. Есть те кто болеют не по одному, а целыми семьями. Людям с пожилыми родителями приходится дергать их, будить, для того чтобы они посмотрели в фронталку, это доставляет определенное неудобство.<br> :date: __2021-04-14 14:11:36__

> Мне приходило смс 3 раза в день,в 11 часов это самое раннее,да не очень удобно,но спасибо онлайн врачам,поддерживали как могли,еслиб не они,с ума сошла бы. Благодарю вас за это от души.Не болейте,всем здоровья и удачи.<br> :date: __2021-04-14 01:22:35__

> Работало стабильно, но действительно необходимо несколько напоминаний в течение часа. Причём к концу периода фотографирования более часто. Upd: у меня приходило notification только один раз. Нужно более насточивое.<br> :date: __2021-04-13 09:56:18__

> В последний день совершенно не понятно, закончился мониторинг или нет. Былоб оповещение об окончании, тогда вообще замечательно.<br> :date: __2021-04-11 13:29:29__

> Работает без сбоев, несправедливых штрафов не начислили. Хороший способ проверять несознательных граждан. Ничего унизительного и страшного в отправлении селфи нет. Времени даётся достаточно, днём можно спокойно поспать. Инструкция по пользованию понятная, звук (если настроить правильно телефон) слышно всегда<br> :date: __2021-04-09 18:36:29__

> Нормальное приложение. Да хорошо что хоть кто то за этим следит и порядок наводит. Без этого заражения было бы намного больше. Да. Надо скидывать фотки. Все правильно. Все равно сидишь дома. Ночью не беспокоят. Хорошее нужное приложение. Молодцы!<br> :date: __2021-04-06 19:22:28__

> Поставлю 5, потому что мне досталась версия с тихим часом. Приложение не развлекательное и тут трудно что-то оценивать. Остальные критерии: загрузилось, открылось, прошла авторизация - без нареканий. В дальнейшем надо ловить уведомления и фоткаться. Предупреждаю инстаграмщиц и тиктокерш, что фотки без фильтров, потому что делаются для ботов, а не для подписчиков.<br> :date: __2021-04-02 07:40:41__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ru.mos.socmon 4 reviews"/>
</p>

> Присылали запрос на фото 3-4 раза в день с 11.00 до 19.00, смс плюс пуш-уведомление. Есть режим тихого часа на 2 часа. Геопозицию не включал. Вообщем, проблем не было.<br> :date: __2021-04-29 13:43:10__

> Начитавшись негатива не хотел ставить. Но сейчас, после изоляции ничего плохого не скажу. Удобно, тихий час есть, проверка в интервале не менее 2часов. То есть смело можно "заняться своими делами"). Но это при условии, если вы болеете не в тяжёлой форме!!! Ставлю 4ку, т.к. сам факт изоляции под наблюдением не по мне.<br> :date: __2021-04-26 08:08:51__

> Периодически случались сбои<br> :date: __2021-03-03 09:16:47__

> Upd 22.02.2021 По итогу использования. Приложение наконец доработали более-менее. Действительно, несмотря на то, что приходят оповещения, даже когда в больнице, санкции не наступают. Кроме того, после того, как выписали, ещё некоторое время приходили оповещения, но без последствий (метки уже не ставила) . Видимо, ещё из-за большого наплыва больных осенью ответы поддержки были вообще не по теме, никто не вчитывался, о чем вопрос, автоматически выбирался ответ. Ну да ладно, пережили.<br> :date: __2021-02-22 08:13:26__

> Нормальная программа, но вот с оповещениями у неё плохо. Тот пилик, что она выдаёт часто просто не замечаешь. Как и приход смски. Приходится постоянно смотреть в телефон, чтобы не пропустить фотографирование. Сделали ли бы они возможность ставить на оповещение разные мелодии, цены бы им не было.<br> :date: __2021-02-18 20:04:26__

> Функционирует отлично, единственное пожелание- наличие статуса об активности ограничений, типа "Наблюдается/Не наблюдается"<br> :date: __2021-02-10 12:21:19__

> После регистрации в приложении с удивлением для себя заметил, что мое отчесво написано с ошибками, да и адрес не совсем тот. Позвонил в поддержку. Через неделю все исправили.<br> :date: __2021-02-09 10:15:14__

> Мдэмс...вот тебе и мониторинг)<br> :date: __2021-02-05 15:02:20__

> Не имеющая вес организация. Собрав информацию, не влияет на социум.<br> :date: __2021-02-03 11:03:21__

> Приложение работает. Зарегистрироваться удалось с первого раза. Предложение к разработчикам. По возможности сделайте отображение статуса пациента, например: на карантине, снят с карантина.<br> :date: __2021-02-01 03:03:07__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ru.mos.socmon 3 reviews"/>
</p>

> Обычно запросы были 4-5 раз в день с 10 до 19, пару тройку раз пропустил запрос - спал днем, санкций не было. Телефон с МТС интернетом выдали и после отрицательного теста забрали. Для китайских телефонов, сделали дублирующий запрос по смс.<br> :date: __2021-04-24 03:09:48__

> Пишет приложение не работает на устройствах с root доступом<br> :date: __2021-04-20 16:45:23__

> можно обмануть приложение<br> :date: __2021-04-08 08:26:51__

> Даже при очень громком звуке, сигнализирующем, что пришло смс и нужно отправить фото, на него не реагируешь, если уснул. А когда болеешь, то спишь много и в любое время. Как результат, пропущенная отправка фото. Это самая большая недоработка приложения. Возможно было бы правильнее не смс отправлять, а звонить на телефон. Больше шансов , что человек услышит и проснется. Если, конечно, целью приложения является контроль за распространением болезни, а не сбор денег.<br> :date: __2021-03-25 22:46:52__

> Это самое ужасное. Заболел 9-го марта, анализ результата пришёл 12-го марта, у меня взяли анализ 12-го марта, результат отрицательный. Почему же меня посадили на карантин до 26-го марта, если переболевший может выходить на улицу, а я сижу дома на карантине, где логика?<br> :date: __2021-03-25 11:04:22__

> Уже два дня не идут запросы на фотографии, специалист технической поддержки не знает - закончился карантин или нет<br> :date: __2021-03-21 17:31:49__

> Во–первых: ставьте индивидуальное уведомление — какую–ниб долгую мелодию, чтобы не провафльть запрос на фотографию, иначе легко встрять на 4к штрафа на ровном месте Во–вторых, если ваше состояние оставляет желать лучшего, то вы встряли, потому что дневной сон вам испортят этими запросами. Обычно 4–5 запросов в день, с 10 до 20, по крайней мере у меня было так... проспал запрос— 4к. Презумция невиновности не действует Еще в первый день штук 10 звонков получите, сверяющихся о вашем самочуствии...<br> :date: __2021-03-13 08:46:57__

> Оповещения из приложения приходят без звука! Спасает только дублирование запроса по смс через 20 минут. В остальном приложение функционирует нормально. Update: Уважаемые разработчики! Тогда что у вас за приложение такое, которое игнорит настройки моего телефона?! У меня даже сра*ый тетрис уведомления со звуком присылает!<br> :date: __2021-03-09 14:39:21__

> За время использования приложения особых проблем не возникло. Пару раз были технические сбои, когда приходил запрос на фото, а в программе не "горела" кнопка для фото, но быстро устранялись. Правильно люди пишут в отзывах, что когда болеешь, хочешь спать, а не следить за запросами фото. Увы, больному человеку 2 часов "тихого часа" мало. В послед.день карантина запросы не приходили. Хотелось бы, чтобы было оповещение об окончании карантина тоже.<br> :date: __2021-03-07 06:14:26__

> Если у Вас бессонница или Вы любитель поспать до обеда,будьте морально готовы к постоянному недосыпу,помимо болезни,либо заплатить штраф за просрочку. Небольшой лайфхак для сов и страдающих бессонницей, как я. Ставите будильник на 9.55-просыпаетесь. Если фото не надо,то ставите режим "тихий час" и следующий будильник на 12.55.<br> :date: __2021-02-28 11:29:43__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ru.mos.socmon 2 reviews"/>
</p>

> Оповещения иногда отсутствуют, приходится постоянно мониторить экран, а вдруг что-то пришло, везёт что проверяю постоянно, иначе бы раза 3 штраф схватил<br> :date: __2021-04-27 15:33:11__

> Не принимает фотографии, геоданные отображает с ошибками.<br> :date: __2021-04-25 11:28:47__

> Доброго здоровья всем,кто читает этот отзыв!Поставили диагноз "Ковид".Прислали ссылку на приложение соцмониторинг.Поставила на свою голову🤦‍♂️ Лежу с закрытыми глазами.Сил-едва дойти до дамской комнаты,а тут...чпок...Соцмониторинг просит пройти обязательную идентификацию...и так сегодня,в 16.45,уже третий(!)раз. Вы сами-то болели коронавирусом???Тут не то,чтобы выйти,тут с кровати не встать лишний раз,хоть мне 34.. Уважаемые разработчиаи,побойтесь Бога!Сделайте эту миссию выполнимой:это 2р.в д<br> :date: __2021-04-21 15:55:39__

> Мне тяжело попасть во время, которое не совпадает с моим бодровствованием. У меня слабость, до туалета дойти еле еле, в основном дремлю. А тут фото надо так часто отсылать. Это глупо придумано. Людям болеющим зачем это издевательство. Итак дипрессия, слезы, нервы. А вы что творите своей программой, подумайте.<br> :date: __2021-04-16 18:44:35__

> Не устанавливается! Пишет, что установлено, но в телефоне приложения нет!<br> :date: __2021-04-16 17:57:44__

> Приложение отвечает только интересам контролирующей стороны с очевидными намерениями необоснованного обогащения. Для пользователей нет никакого удобства кроме возможности переснять фотографию. Нет самого простого: дат интервала карантина. Программа работает постоянно. Нет возможности контролировать геопозицию, чтобы пользователь мог заметить и исключить технические ошибки определения местоположения. В общем, эта программа - ошейник с электрошокером, который удаленно активирует каста продвинутых<br> :date: __2021-04-10 08:25:01__

> Да х.з. НИКТО НЕ ГОВОРИЛ УСТАНАВЛИВАТЬ. Жена в фотографии увидела говорит надо установить что как зачем нафига... Не понятно<br> :date: __2021-04-02 14:41:30__

> Приложение зависает при отправке фотографии.<br> :date: __2021-03-23 18:48:10__

> Ничего не понятно<br> :date: __2021-03-17 16:58:32__

> Вот мне надо забрать посылку, как поступить в этой ситуации?<br> :date: __2021-03-12 09:29:46__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ru.mos.socmon 1 reviews"/>
</p>

> Пусть бордюроукладчик свой электронный поводок сам носит<br> :date: __2021-04-28 16:58:10__

> Хуже вас людей уже нет)<br> :date: __2021-04-28 16:29:04__

> Учитывая стоимость пропущенных сообщений приложение должно работать по принципу будильника. Т.е. нарастающий сигнал уведомления, периодически повторяющийся до выполнения действия<br> :date: __2021-04-28 15:41:04__

> Лучшего способа отвернуть от себя людей власть ещё не придумала! Браво! Человек болеет, лежит без сил, а ему надо мониторить с 9 утра до 10 вечера приложение! Штраф за то, что ты болеешь! Фашисты!<br> :date: __2021-04-28 13:33:55__

> НЕ КАЧАЙТЕ. ЭТО сделает больному ещё большую головную боль и сворует у вас деньги. Человек болеет не соображает что делать ему приходят требования с трудоёмкими действиями. Дала СВОЙ телефон больному попользоваться, оказывается теперь его нельзя мне брать с собой. Лично больному телефон привезти забыли или долго. В поддержке звонить - все не знают что делать и никто не за что не отвечает. А штафы с радостью сразу начислят. Врача вызвали так и не приехал. Так и осталась с больным и БЕЗ ТЕЛЕФОНА<br> :date: __2021-04-27 18:16:45__

> Отвратительное приложение.Двойная индентификация,которая постоянно глючит.нужно два раза делать фото и отправлять. И так приложение работает в постоянной геопозиционной передачи,так ещё зачем то требует подтверждать свою геопозицию.<br> :date: __2021-04-26 15:53:36__

> Ваше приложение не работает. Даже зарегистрироваться не даёт! В чем смысл этого приложения.<br> :date: __2021-04-26 15:02:04__

> Не окрывыается даже<br> :date: __2021-04-26 14:22:06__

> я регулярно сплю, но благодаря вашему приложению приходится просыпаться и проверять запрос на фото..сами бы попробовали в таком режиме пожить<br> :date: __2021-04-25 18:33:30__

> Приложение должно быть запрещено на всех платформах, это нарушение конституционных прав и издевательство. Вместо того чтобы лечиться и спать, больные должны постоянно сидеть в приложении и отправлять свои фотографии, при этом уведомления в виде СМС доходят не всегда.<br> :date: __2021-04-25 16:42:25__


