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

> IMPRESCINDIBLE<br> :date: __2021-03-28 13:13:47__

> De momento ninguna experiencia, gracias a Dios<br> :date: __2021-03-27 12:15:16__

> Muy buena las explicaciones gracias saludos<br> :date: __2021-03-26 15:44:16__

> HOLA BUENOS DÍAS MEA GUDTADO ESTOY CONFORME CONTODO LO QUE ABIS PUESTO PER DONAR QUE NO OSPONGA MAS COSAS NO MESE ESPLICAR MUY 👍PERO LO E ENTENDIDO GRACIAS POR TODO 💜😉<br> :date: __2021-03-26 12:32:55__

> Eletricien<br> :date: __2021-03-25 13:24:56__

> I gracias pero no me hace falta soy de otra galaxia Mas avanzada<br> :date: __2021-03-25 12:59:53__

> Bueno<br> :date: __2021-03-25 12:31:34__

> Bien<br> :date: __2021-03-23 12:12:05__

> Bájatela ya !!!!!!!<br> :date: __2021-03-23 00:31:40__

> Es la mejor aplicación que he tenido y tendré jamás. Una gran experiencia que sin duda le recomiendo que viva España<br> :date: __2021-03-22 17:20:23__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Buena aplicación, como la mayoría de las dedicadas al fin del control de la epidemia. Su problema, la dejadez e ineptitud de una gran mayoría de la población.<br> :date: __2021-03-28 15:04:45__

> es intere sante<br> :date: __2021-03-26 04:33:17__

> Muy útil como idea, la pega, la escasa implantación... por tanto, dudoso resultado<br> :date: __2021-03-24 09:17:28__

> La APP muy bien. Di positivo y lo puse. Tardaron un par de días en mandarme el código. Eso debería ser más rápido. Al día siguiente les avisaron a mis contactos. Pero ahora ya no soy positivo y no se como quitarlo para que no me salga en rojo como si siguiera dando positivo. No es mala idea, pero debería ser más rápida y sencilla. Gracias<br> :date: __2021-03-22 09:03:26__

> Es muy util<br> :date: __2021-03-21 00:46:23__

> Muy buena<br> :date: __2021-03-19 13:53:17__

> Bien<br> :date: __2021-03-17 15:52:21__

> Viajo en transporte público y trabajo en un centro administrativo. La duración del transporte es de más de una hora. Tengo 64 años.<br> :date: __2021-03-13 07:48:05__

> Falla mucho<br> :date: __2021-03-09 19:08:42__

> Acabo de descargármela. Me parece estupendo la iniciativa, así podremos detectar más casos y de forma más rápida.<br> :date: __2021-03-06 04:58:49__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> La idea es buena pero si el infectado no lo informa en la aplicación no vale para nada.Despues de meses y haber estado cerca de positivos nunca me ha alertado<br> :date: __2021-03-24 07:20:06__

> La app funciona bien, pero en el momento que está activo el modo ahorro de batería en mi Xperia me empieza a decir que no funciona por los datos en segundo plano.<br> :date: __2021-03-19 23:42:12__

> Con la cegurida<br> :date: __2021-03-18 21:04:14__

> muy sitifactoria.<br> :date: __2021-03-11 15:42:58__

> No se por que la gente no lo usa. Media poblacion contagiada y nunca ha saltado. Funciona realmente????<br> :date: __2021-03-09 13:58:43__

> Creo que es una buena idea veremos como es de efectiva<br> :date: __2021-03-08 22:04:51__

> LA APP TIENE UN VIRUS NO LA DESCARGUES Y SI LA TIENES DESINSTALALA YA ES MUY PELIGROSO PUEDEN RASTREARTE ATENCIÓN TIENE UN VIRUS<br> :date: __2021-03-04 04:33:13__

> No tengo experiencia<br> :date: __2021-03-03 23:53:27__

> Eso de que no te pide ubicacion... A mi si me pide activarla, por lo visto porque el bluetooh se lo exige, creo que en iphones no. Seguramente no use datos de ubicacion ni otroas datoa, pero es que son ya entonces dos funciones que hay que tener activas, y funde la bateria que no veas<br> :date: __2021-03-03 11:41:32__

> Al final es un problema si no se notifican los positivos y todo eso...yo creo que con el código que te dan cuando te hacen los pcr... Ellos deberían notificar el positivo y hasta que no se obtenga un negativo no se cambiaría en la app pero bueno<br> :date: __2021-03-03 01:03:15__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> No me deja activar el radar covid<br> :date: __2021-03-25 21:41:01__

> Depende de que alguien positivo que se salta las normas saliendo a la calle lo confirme en la aplicación?<br> :date: __2021-03-25 17:49:02__

> Estuve usándola días parecía que estaba buscando poquemons<br> :date: __2021-03-24 18:50:22__

> Muy mala<br> :date: __2021-03-20 21:01:15__

> Lleva días que no funciona la activación de alerta. Da error.<br> :date: __2021-03-15 14:30:58__

> Poco útil<br> :date: __2021-03-13 07:07:11__

> La aplicación está bien, pero la veo algo limitada para la situación actual, sería conveniente añadir una opción para declarar si tienes síntomas, ya que la aplicación solo sirve si oficialmente has dado positivo (cosa que está perfecto) pero hay muchas personas que aún no se han hecho una pcr y padecen síntomas de covid, pues opino que por prevención, sería útil añadir esta opción<br> :date: __2021-03-12 10:34:52__

> Desinstalando... La idea es buena la verdad, pero no está teniendo mucho éxito, ya que el covid me ha rozado ya varias veces, hemos estado hasta arriba de casos en Alicante y me dice que nunca he tenido contacto con ningún infectado y eso es porque la gente no conoce la app y/o porque a la gente no le interesa.<br> :date: __2021-03-12 02:34:54__

> No hace más que darme alertas de que no funciona correctamente<br> :date: __2021-03-09 17:42:02__

> No le han hecho la publicidad que está aplicación necesita, para que sea efectiva.<br> :date: __2021-03-07 18:29:09__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Desinstalada hasta que inventen un test pcr que no haga tanto daño, me da tanto miedo que me metan semejante baston por la nariz que prefiero ni saber si he estado en riesgo. Lo mejor es tener siempre cuidado y actuar con responsabilidad.<br> :date: __2021-03-28 09:54:06__

> Se nota que la han hecho con prisa.<br> :date: __2021-03-27 23:14:20__

> Inútil<br> :date: __2021-03-27 19:27:09__

> No vale para nada. Información complementamente obsoleta e inútil.<br> :date: __2021-03-27 17:55:29__

> Malisimaaaaaaaaaaaa. Desinstalarla no sirve para nadaaaaaaaaaa.<br> :date: __2021-03-27 13:14:52__

> No se ve nada<br> :date: __2021-03-27 10:29:26__

> No funciona. El registro de positivos no puede recaer en la buena voluntad del usuario.<br> :date: __2021-03-27 08:09:34__

> Una basura, mi mujer positivo lo avisa en la app y a mi jamas me ha saltado, mas de lo mismo con mi madre. Que se haya gastado dinero publico en esto es para que lo estudie un juez.<br> :date: __2021-03-27 01:00:29__

> Gobierno comunista, que entre al gobierno vox y verás como se acaban las tonterias<br> :date: __2021-03-26 17:32:55__

> Mala no sirve para nada<br> :date: __2021-03-26 14:36:45__


