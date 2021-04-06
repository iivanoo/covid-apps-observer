# Radar COVID
App version ``1.3.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Radar COVID icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Radar COVID |
| **Unique identifier** | es.gob.radarcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=es.gob.radarcovid](https://play.google.com/store/apps/details?id=es.gob.radarcovid) |
| **Summary**  | Radar COVID, app oficial de prevención del COVID-19 del Gobierno de España |
| **Privacy policy** | [https://radarcovid.covid19.gob.es/terms-of-service/privacy-policy.html](https://radarcovid.covid19.gob.es/terms-of-service/privacy-policy.html) |
| **Latest version** | 1.3.0 |
| **Last update** | 2021-02-17 13:20:51 |
| **Recent changes** | - Modificaciones en política de privacidad.<br>- Reporte de métrica anónima para medir eficiencia de la aplicación.<br>- Se añade idioma rumano.<br>- Corrección de errores.<br>- Mejoras de accesibilidad:<br>	--  Corregido encabezado de “Cambio de estado” en el pop up de 14 días que el lector de pantalla no leía.<br>	-- Incorporación de iconos de cierre en los ventanas emergentes. |
| **Installs**  | 5.000.000+ |
| **Category** | Medicina |
| **First release** | 7 ago 2020 |
| **Size**  | 22M |
| **Supported Android version**  | 6.0 y versiones posteriores |

### Description
> Radar COVID es la aplicación diseñada y dirigida por la Secretaría de Estado de Digitalización e Inteligencia Artificial del Gobierno de España para ayudar a evitar la propagación del coronavirus (COVID-19). 
<br>Radar COVID te avisa de manera anónima del posible contacto que has podido tener en los últimos 14 días con una persona que haya resultado infectada utilizando la tecnología Bluetooth de bajo consumo.
<br>Radar COVID además permite:
<br>-	Comunicar de forma anónima tu diagnóstico positivo.
<br>-	Comunicar la exposición de forma anónima a las personas con las que has estado en contacto 
<br>Radar COVID garantiza la seguridad y privacidad y es 100% anónimo. Por ello no solicitamos ni tu nombre, ni tu teléfono, ni tu correo electrónico. 
<br>Esta aplicación usa ilustraciones de licencia gratuita y que pertenecen a www.freepik.es


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Ministerio de Asuntos Económicos y Transf. Digital |
| **Website**  | - |
| **Email** | soporte.radarcovid@economia.gob.es |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Ministerio+de+Asuntos+Econ%C3%B3micos+y+Transf.+Digital](https://play.google.com/store/apps/developer?id=Ministerio+de+Asuntos+Econ%C3%B3micos+y+Transf.+Digital) |

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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lcom/android/tools/r8/GeneratedOutlineSupport;->outline15(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Radar COVID app has been installed by more than **5000000** times. At this time, **17370** rated the app and its average score is **2.716753**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5520

:star::star::star::star:: 1620

:star::star::star:: 1050

:star::star:: 780

:star:: 8400

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="es.gob.radarcovid 5 reviews"/>
</p>

> Pedazo juego, el mejor shooter del mundo<br> :date: __2021-04-01 13:31:54__

> Buena<br> :date: __2021-04-01 12:06:16__

> De momento no hay experiecia<br> :date: __2021-03-31 20:13:26__

> Hola lo unico q puedo decir es q no a saltado en mi caso alarma .<br> :date: __2021-03-31 12:25:10__

> Seguimiento más o menos estricto de personas contagiadas y asintomáticos<br> :date: __2021-03-31 08:32:18__

> Me encanto y ustedes tienen el movil solo una basura<br> :date: __2021-03-30 21:16:02__

> Muy buena para tu seguridad.<br> :date: __2021-03-29 23:51:11__

> Buenos<br> :date: __2021-03-29 20:17:47__

> muy buena<br> :date: __2021-03-29 19:31:24__

> Bueno<br> :date: __2021-03-29 01:09:52__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Esta muy bien<br> :date: __2021-03-29 10:06:36__

> Buena aplicación, como la mayoría de las dedicadas al fin del control de la epidemia. Su problema, la dejadez e ineptitud de una gran mayoría de la población.<br> :date: __2021-03-28 15:04:45__

> es intere sante<br> :date: __2021-03-26 04:33:17__

> Muy útil como idea, la pega, la escasa implantación... por tanto, dudoso resultado<br> :date: __2021-03-24 09:17:28__

> La APP muy bien. Di positivo y lo puse. Tardaron un par de días en mandarme el código. Eso debería ser más rápido. Al día siguiente les avisaron a mis contactos. Pero ahora ya no soy positivo y no se como quitarlo para que no me salga en rojo como si siguiera dando positivo. No es mala idea, pero debería ser más rápida y sencilla. Gracias<br> :date: __2021-03-22 09:03:26__

> Es muy util<br> :date: __2021-03-21 00:46:23__

> Muy buena<br> :date: __2021-03-19 13:53:17__

> Bien<br> :date: __2021-03-17 15:52:21__

> Viajo en transporte público y trabajo en un centro administrativo. La duración del transporte es de más de una hora. Tengo 64 años.<br> :date: __2021-03-13 07:48:05__

> Falla mucho<br> :date: __2021-03-09 19:08:42__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> ¿La usa la gente? El año pasado alguno hablaba de ella, ahora no oigo a la gente hablar de si la tiene instalada. Sigo con ella pero pienso en desinstalar.....<br> :date: __2021-04-02 21:24:50__

> no es muy útil pero buena idea<br> :date: __2021-04-02 17:14:10__

> Lo uso en caso de sospecha por bibliotecas. Nadie te cuenta su vida.<br> :date: __2021-03-30 17:46:34__

> Una vez q te Dan el alta. Y das negativo no puedes poner esa. Opción. Sales siempre como positiva. No entiendo.<br> :date: __2021-03-28 15:40:26__

> La idea es buena pero si el infectado no lo informa en la aplicación no vale para nada.Despues de meses y haber estado cerca de positivos nunca me ha alertado<br> :date: __2021-03-24 07:20:06__

> La app funciona bien, pero en el momento que está activo el modo ahorro de batería en mi Xperia me empieza a decir que no funciona por los datos en segundo plano.<br> :date: __2021-03-19 23:42:12__

> Con la cegurida<br> :date: __2021-03-18 21:04:14__

> muy sitifactoria.<br> :date: __2021-03-11 15:42:58__

> No se por que la gente no lo usa. Media poblacion contagiada y nunca ha saltado. Funciona realmente????<br> :date: __2021-03-09 13:58:43__

> Creo que es una buena idea veremos como es de efectiva<br> :date: __2021-03-08 22:04:51__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> No lo sé<br> :date: __2021-04-02 14:13:33__

> Buena idea y diseño pero en mi zona hemos llegado a tener hasta 897 casos por cada 100.000 habitantes y nunca he tenido un aviso pese a tener el bluetooth permanentemente conectado.<br> :date: __2021-03-28 18:00:15__

> No me deja activar el radar covid<br> :date: __2021-03-25 21:41:01__

> Depende de que alguien positivo que se salta las normas saliendo a la calle lo confirme en la aplicación?<br> :date: __2021-03-25 17:49:02__

> Estuve usándola días parecía que estaba buscando poquemons<br> :date: __2021-03-24 18:50:22__

> Muy mala<br> :date: __2021-03-20 21:01:15__

> Lleva días que no funciona la activación de alerta. Da error.<br> :date: __2021-03-15 14:30:58__

> Poco útil<br> :date: __2021-03-13 07:07:11__

> La aplicación está bien, pero la veo algo limitada para la situación actual, sería conveniente añadir una opción para declarar si tienes síntomas, ya que la aplicación solo sirve si oficialmente has dado positivo (cosa que está perfecto) pero hay muchas personas que aún no se han hecho una pcr y padecen síntomas de covid, pues opino que por prevención, sería útil añadir esta opción<br> :date: __2021-03-12 10:34:52__

> Desinstalando... La idea es buena la verdad, pero no está teniendo mucho éxito, ya que el covid me ha rozado ya varias veces, hemos estado hasta arriba de casos en Alicante y me dice que nunca he tenido contacto con ningún infectado y eso es porque la gente no conoce la app y/o porque a la gente no le interesa.<br> :date: __2021-03-12 02:34:54__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> No sé muy bien si funciona o no. Como idea es buena, como funcionamiento, es nulo. Yo la he desinstalado, harta ya de verla pulular por mi móvil...<br> :date: __2021-04-03 21:45:32__

> Esto es una patraña.. Como todo lo que está pasando😡😡😡😡<br> :date: __2021-04-03 18:53:50__

> Me pregunto si funciona realmente. No me ha saltado ningún aviso desde que la tengo puesta a pesar de haber estado en zonas confinadas de varias CC.AA. ¿Cuanto dinero público nos ha costado la App? Y lo que me aterra es por a gente que da positivo y pedir el código para comunicar su positivo y ni el sanitario ni el rastreador (si es que le llama) sabe nada del mismo.<br> :date: __2021-04-03 17:10:38__

> Aplicación que ha costado dos millones de euros. Va de pena. En esto tiran nuestro dinero público.<br> :date: __2021-04-03 16:14:59__

> No sirve<br> :date: __2021-04-03 13:45:00__

> No sirve para nada<br> :date: __2021-04-03 11:08:54__

> No sirve<br> :date: __2021-04-03 10:42:22__

> No sirve para nada<br> :date: __2021-04-02 19:44:11__

> Es una locura para ti mismo que no te preocupes de eso y te bendiga igualmente para ustedes que te lo digan y no me dejes que tal vez donde sea el tiempo de tu trabajo que te lo vas a decir a tu padre o en la tardes y te bendiga igualmente para ustedes<br> :date: __2021-04-02 18:13:04__

> Patética es poco<br> :date: __2021-04-02 03:30:49__


