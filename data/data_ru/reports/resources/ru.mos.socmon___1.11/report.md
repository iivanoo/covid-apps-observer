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

> Сколько дней длиться карантин ? Я с 07 мая и с вчерашнего дня нет уведомление и ни каких смс .что мне делать. Никто мне не говорить ничего<br> :date: __2021-05-21 12:15:27__

> Нормально все работает<br> :date: __2021-05-17 12:47:23__

> Удобно. Справедливо! Современно.<br> :date: __2021-05-15 15:51:31__

> Чудо-приложение. При регистрации сообщило, что данные будут на проверке от двух дней. В итоге за 2 недели так обо мне и не вспомнило. В общем рекомендую и с удовольствием удаляю.<br> :date: __2021-05-14 18:19:41__

> Приложение огонь! Не даёт расслабляться! Приучает к внимательности! ))) Но всё равно удаляю его )<br> :date: __2021-05-11 23:19:19__

> У меня работает отлично. Единственный минус после самоизоляции, не приходит никакое оповещение, мол все, спасибо вы свободны. Подумайте над этим, это важно.<br> :date: __2021-05-11 23:11:54__

> Нормально работает.<br> :date: __2021-05-08 14:16:17__

> Работает все отлично, приходит смс три раза в день с напоминанием сделать фото, никаких проблем нет. На все уходит меньше минуты. Не знаю откуда столько плохих отзывов.<br> :date: __2021-05-06 17:21:29__

> Что нужно делать я таки не понял. Не могу включать тихий час.<br> :date: __2021-04-28 21:45:26__

> Прикольное приложение, мне очень нравится функция "тихий час", такие милые картинки, будто в сказке.<br> :date: __2021-04-22 00:53:19__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ru.mos.socmon 4 reviews"/>
</p>

> Добавьте информацию о сроке действий карантина и контактные телефоны для получения справочной информации<br> :date: __2021-05-19 08:16:58__

> Само приложение работало хорошо. Беспокоило 3-4 раза в день. Есть тихий час. Фотографии распозновало нормально. Из улучшений хотелось бы скачать в конце все свои фото. Ну и чтобы даты мониторинга отображались. А сама концепция мониторинга, конечно, ничего кроме раздражения не вызывает.<br> :date: __2021-05-17 23:00:54__

> Приложение у меня работает хорошо, уведомления приходят в среднем по 4 раза в день, мне не напряжно им пользоваться, если учесть тот факт, что у меня никаких симптомом нет и я чувствую себя хорошо...а вот для больного человека, которому хочется спать большую часть дня, это наверное пытка....за это и сняла одну звезду....<br> :date: __2021-05-16 14:02:09__

> Приложение работает хорошо, правда не всегда с первого раза проходит проверка геопозиции.<br> :date: __2021-05-13 11:07:23__

> Всё классно<br> :date: __2021-05-05 11:54:48__

> Присылали запрос на фото 3-4 раза в день с 11.00 до 19.00, смс плюс пуш-уведомление. Есть режим тихого часа на 2 часа. Геопозицию не включал. Вообщем, проблем не было.<br> :date: __2021-04-29 13:43:10__

> Начитавшись негатива не хотел ставить. Но сейчас, после изоляции ничего плохого не скажу. Удобно, тихий час есть, проверка в интервале не менее 2часов. То есть смело можно "заняться своими делами"). Но это при условии, если вы болеете не в тяжёлой форме!!! Ставлю 4ку, т.к. сам факт изоляции под наблюдением не по мне.<br> :date: __2021-04-26 08:08:51__

> Периодически случались сбои<br> :date: __2021-03-03 09:16:47__

> Upd 22.02.2021 По итогу использования. Приложение наконец доработали более-менее. Действительно, несмотря на то, что приходят оповещения, даже когда в больнице, санкции не наступают. Кроме того, после того, как выписали, ещё некоторое время приходили оповещения, но без последствий (метки уже не ставила) . Видимо, ещё из-за большого наплыва больных осенью ответы поддержки были вообще не по теме, никто не вчитывался, о чем вопрос, автоматически выбирался ответ. Ну да ладно, пережили.<br> :date: __2021-02-22 08:13:26__

> Нормальная программа, но вот с оповещениями у неё плохо. Тот пилик, что она выдаёт часто просто не замечаешь. Как и приход смски. Приходится постоянно смотреть в телефон, чтобы не пропустить фотографирование. Сделали ли бы они возможность ставить на оповещение разные мелодии, цены бы им не было.<br> :date: __2021-02-18 20:04:26__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ru.mos.socmon 3 reviews"/>
</p>

> Сегодня какието глюки с сетью, явно проблемы связи через вайфай, не отражается запрос на фото, только после отключения вайфая запрос появился. В предыдущей версии такого не было. История запросов то появляется, то исчезает. Вообще программа странно работает со связью, в прошлой версии после установки напрочь отрубилась доставка смс, не мог даже зарегиться спасался перезагрузками телефона. В этой версии одновременно мобильный интернет и вайфай не работают. Может от телефона зависит конечно.<br> :date: __2021-05-22 12:04:14__

> Поставил приложение во вторник. Сегодня пятница и номер до сих пор на проверке. Техподдержка на телефоне не доступна. Специалист не знает почему не проверен телефон. Если придёт штраф пойду в суд. Разговоры записаны.<br> :date: __2021-05-22 11:12:59__

> Зарядка сильно садится....<br> :date: __2021-05-12 16:02:33__

> Нет настройки громкости и мелодии уведомлений конкретно для приложения. Телефон надо все время носить с собой иначе штраф. У меня уведомления отключены, т.к. других приложений много. Нужна настройка именно для данного приложения, а не телефона вообще - нет желания бежать к телефону на каждое уведомление от других приложений. Срочный ответ требует только Ваше приложение, поэтому и уведомление должно быть индивидуально<br> :date: __2021-05-04 12:07:01__

> Нельзя заставить приложение проигрывать свой сигнал. Функция тихий час работает лишь однажды. Нет информации о окончании периода самоизоляции.<br> :date: __2021-05-03 08:17:01__

> Обычно запросы были 4-5 раз в день с 10 до 19, пару тройку раз пропустил запрос - спал днем, санкций не было. Телефон с МТС интернетом выдали и после отрицательного теста забрали. Для китайских телефонов, сделали дублирующий запрос по смс.<br> :date: __2021-04-24 03:09:48__

> Пишет приложение не работает на устройствах с root доступом<br> :date: __2021-04-20 16:45:23__

> можно обмануть приложение<br> :date: __2021-04-08 08:26:51__

> Даже при очень громком звуке, сигнализирующем, что пришло смс и нужно отправить фото, на него не реагируешь, если уснул. А когда болеешь, то спишь много и в любое время. Как результат, пропущенная отправка фото. Это самая большая недоработка приложения. Возможно было бы правильнее не смс отправлять, а звонить на телефон. Больше шансов , что человек услышит и проснется. Если, конечно, целью приложения является контроль за распространением болезни, а не сбор денег.<br> :date: __2021-03-25 22:46:52__

> Это самое ужасное. Заболел 9-го марта, анализ результата пришёл 12-го марта, у меня взяли анализ 12-го марта, результат отрицательный. Почему же меня посадили на карантин до 26-го марта, если переболевший может выходить на улицу, а я сижу дома на карантине, где логика?<br> :date: __2021-03-25 11:04:22__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ru.mos.socmon 2 reviews"/>
</p>

> Приложение работает отвратительно,первые несколько дней после установки все было нормально, а сейчас не важно с первого раза ответить на запрос, Приложение зависает и не даёт ничего сделать<br> :date: __2021-05-22 12:50:44__

> Те кто сделал заказ этого приложения они явно не выполнили свою работу разьве что пункты 1содрать денег 2замучить граждан 3 не у всех есть дорогие мобильники и не все усеют пользоваться им. Дальше к обращение к команде всех кто причастен к этому приложению: 1ребята вы либо выполнили то что от вас просили и вообще не думали что делали. 2 вам что трудно было сделать более развернутый интерфейс? Вот что трудного поставить начало и конец карантина? 3 у приложения проблема с уведомлением.<br> :date: __2021-05-22 00:41:03__

> После обновления начались одни лаги, каждый раз теперь запрашивается геолокация,которая вроде как постоянно отслеживается, предыдущих фотографий нет, пришел запрос по смс,но в самом приложении его нет. Дозвониться по горячей линии тоже еще надо суметь. А теперь главный вопрос: человек лежит с температурой, ему теперь еще и об этом глючном приложении беспокоиться надо?<br> :date: __2021-05-21 18:22:50__

> Добавьте информацию о нарушениях! Прилетают штрафы ХЗ за что. И не понятно как программа видит мое местоположение.<br> :date: __2021-05-18 05:40:05__

> При написании вопроса в техподдержку ответ шаблоном, да и если позвонить операторы ничего не знают кроме "14 дней" и если они вам скажут можно удалить вас не мониторят, вы получите штраф 4000₽. Сам мониторинг не навящив 3-4 раза в день. НО, когда приходит время выписки с больничного и общения с поликлиникой и мониторингом это Ж. Сегодня последний день и никаких запросов нет, поликлиника требует прийти и закрыть больничный. Оператор техподдержки говорит, что нельзя штраф.<br> :date: __2021-05-13 15:09:06__

> Оповещения иногда отсутствуют, приходится постоянно мониторить экран, а вдруг что-то пришло, везёт что проверяю постоянно, иначе бы раза 3 штраф схватил<br> :date: __2021-04-27 15:33:11__

> Не принимает фотографии, геоданные отображает с ошибками.<br> :date: __2021-04-25 11:28:47__

> Доброго здоровья всем,кто читает этот отзыв!Поставили диагноз "Ковид".Прислали ссылку на приложение соцмониторинг.Поставила на свою голову🤦‍♂️ Лежу с закрытыми глазами.Сил-едва дойти до дамской комнаты,а тут...чпок...Соцмониторинг просит пройти обязательную идентификацию...и так сегодня,в 16.45,уже третий(!)раз. Вы сами-то болели коронавирусом???Тут не то,чтобы выйти,тут с кровати не встать лишний раз,хоть мне 34.. Уважаемые разработчиаи,побойтесь Бога!Сделайте эту миссию выполнимой:это 2р.в д<br> :date: __2021-04-21 15:55:39__

> Мне тяжело попасть во время, которое не совпадает с моим бодровствованием. У меня слабость, до туалета дойти еле еле, в основном дремлю. А тут фото надо так часто отсылать. Это глупо придумано. Людям болеющим зачем это издевательство. Итак дипрессия, слезы, нервы. А вы что творите своей программой, подумайте.<br> :date: __2021-04-16 18:44:35__

> Не устанавливается! Пишет, что установлено, но в телефоне приложения нет!<br> :date: __2021-04-16 17:57:44__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ru.mos.socmon 1 reviews"/>
</p>

> Ужасное приложение. Первую неделю пользования работало без проблем, со второй начались проблемы. То изчезают данные о индентификации, теперь отправленное фото не может проверить. Колл центр не работает, не днем, не вечером. За то есть возможность поймать штраф из за плохо работающего приложения.<br> :date: __2021-05-22 17:43:02__

> Отвратительное приложение,по сравнению с прошлым годом стало еще хуже.Фото проверку не проходит,адрес изоляции указан неверно,поэтому геопозицию передать тоже нельзя.В поддержку дозвонилась минут через 20,составили 2 обращения,жду ответа.Запросы на идентификацию приходят,а я их не могу пройти.Второй раз дозвонилась до поддержки,тупо сбросили.<br> :date: __2021-05-22 15:29:14__

> Мне нет 18 лет, Вы не имеете права за мной следить и выписывать штраф в размере 4000₽!!!!<br> :date: __2021-05-22 14:19:44__

> Здравствуйте, приложение работает с постоянными ошибками в определении местоположения, при идентификации и отчета, о том что находишься дома. Вечные "тормоза" при использовании данного ПО. Перед тем как запускать ПО в промышленную эксплуатацию, нужно лучше тестировать, а не выкладывать сырой продукт, из-за которого люди не могут пользоваться им нормально, в итоге чего попадают на штрафы<br> :date: __2021-05-22 13:09:40__

> Приложение не работает от слова СОВСЕМ. Пропадает история идентификаций то за весь период, то за текущий день. Невозможно отправить фото, в приложении эти функции неактивны, хотя поступают смс. Невозможно включить "тихий час" - "что-то пошло не так и мы об этом знаем", но судя по всему, ничего не делаем. Такая котовасия 3-й день! Так на секунду - я на 8м месяце беременности, и не имею возможности ни прилечь отдохнуть - вдруг усну. Поддержка трубку либо не берет, либо ничем помочь не может!!!<br> :date: __2021-05-22 12:58:17__

> Это просто нечто. Мало того, что приложение крайне редко правильно определяет геопозицию без танцев с бубном, так ещё и главная функция работает через раз – пришло сообщение, а запрос в приложении не отображается. И даже когда сделал фото и всё отправил, приложение умерло – данные о запросе пропали на полчаса, что делать – непонятно.<br> :date: __2021-05-22 12:46:54__

> Приложение работает не корректно, геопозиция лагает, я дома нахожусь, а приложение говорит, что моя геопозиция не соответствует адресу изоляции. Сплошная нервотрёпка!!!<br> :date: __2021-05-22 12:35:23__

> Приложение работает некорректно 2 день. Приходится делать скрины страниц, что пришло смс уведомление, но нет возможности отправить фото. Это просто издевательство над людьми, которым и так плохо. Вчера мне пришлось принимать препарат от сердца, и пережить плохую ночь, потому что нервничала. Ах да, как издевательство висит сообщение, что я не передала информацию вчера. Готовлю письмо на сайт мэра. Издевательство над больными. Сегодня оператор сказала, что это же техника... А люди? Не важны?<br> :date: __2021-05-22 12:14:49__

> Неуважаемые разработчики с руками из неизвестного места почему из-за ваших криворучек я должна буду оплачивать штрафы? Приложение висит второй день, до службы поддержки не дозвониться, приходят только смс, а в приложении, через которое надо отправлять фото- тупняк. Обязуюсь соблюдать изоляцию, но отказываюсь от использования программы "социальный мониторинг". Не даю согласие на использование и обработку своих персональных данных. В соответствии с п. 1 ст. 9 Федерального закона от 27.07.2006 № 1<br> :date: __2021-05-22 12:10:06__

> Работает нестабильно. Теряет историю успешных идентификаций. Есть претензия к правительстау москвы - нельзя на базе такого сырого продукта устанавливать "карательные" мероприятия.<br> :date: __2021-05-22 11:54:33__


