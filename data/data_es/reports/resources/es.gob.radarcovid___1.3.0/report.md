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

> Senecesita novedades Nuevas gracias por todo<br> :date: __2021-04-16 01:46:38__

> Estamos en ello. A ver si vence os al bicho<br> :date: __2021-04-15 19:53:24__

> Soy Nacho, ya yo estoy Bacunado con las dos dosis contra covid 19.<br> :date: __2021-04-15 16:43:13__

> Me gusta<br> :date: __2021-04-15 01:07:17__

> Buenos<br> :date: __2021-04-13 20:33:35__

> Más actividad<br> :date: __2021-04-13 15:21:02__

> Fácil de configurar<br> :date: __2021-04-13 09:48:53__

> Buena<br> :date: __2021-04-12 22:11:03__

> La creo muy conveniente dentro de lo qué estámos viviendo, 🙏🌛🌛🇪🇸🇪🇸🌛🌛<br> :date: __2021-04-12 19:20:35__

> No me ha avisado nunca pero y si sí?<br> :date: __2021-04-11 17:37:38__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Menudos sustos mete la "notificación semanal" de la última versión. Francamente ¿es necesario que avisen cada semana de que tienes las notificaciones de exposición activadadas? Eso ya lo sé, de hecho ¿para qué iba a quererlas desactivar si la finalidad de esta aplicación es que te notifique si has estado expuesto o notificar tú si has dado positivo? Francamente o el mensaje está equivocado o que te notifique de que la app funciona es no solamente innecesario sino alarmante. Por favor, revisenlo.<br> :date: __2021-04-15 12:58:24__

> Super<br> :date: __2021-04-13 15:10:01__

> Lo veo muy bien me gusta mucho estar informada<br> :date: __2021-04-11 16:24:14__

> Buena Si<br> :date: __2021-04-09 21:55:34__

> Esta muy bien<br> :date: __2021-03-29 10:06:36__

> Buena aplicación, como la mayoría de las dedicadas al fin del control de la epidemia. Su problema, la dejadez e ineptitud de una gran mayoría de la población.<br> :date: __2021-03-28 15:04:45__

> es intere sante<br> :date: __2021-03-26 04:33:17__

> Muy útil como idea, la pega, la escasa implantación... por tanto, dudoso resultado<br> :date: __2021-03-24 09:17:28__

> La APP muy bien. Di positivo y lo puse. Tardaron un par de días en mandarme el código. Eso debería ser más rápido. Al día siguiente les avisaron a mis contactos. Pero ahora ya no soy positivo y no se como quitarlo para que no me salga en rojo como si siguiera dando positivo. No es mala idea, pero debería ser más rápida y sencilla. Gracias<br> :date: __2021-03-22 09:03:26__

> Es muy util<br> :date: __2021-03-21 00:46:23__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Siempre está que no funciona bien<br> :date: __2021-04-13 22:50:42__

> Bb<br> :date: __2021-04-11 12:42:12__

> Soy nuevo o novato, y acabo de descubrir esta aplicación, incluso no sé si lo he activado bien, espero que sí, me gustaría que me contestaran.<br> :date: __2021-04-11 11:26:01__

> Regular o muy pobre. De casos.<br> :date: __2021-04-07 13:56:47__

> Buena<br> :date: __2021-04-06 09:52:10__

> ¿La usa la gente? El año pasado alguno hablaba de ella, ahora no oigo a la gente hablar de si la tiene instalada. Sigo con ella pero pienso en desinstalar.....<br> :date: __2021-04-02 21:24:50__

> no es muy útil pero buena idea<br> :date: __2021-04-02 17:14:10__

> Lo uso en caso de sospecha por bibliotecas. Nadie te cuenta su vida.<br> :date: __2021-03-30 17:46:34__

> Una vez q te Dan el alta. Y das negativo no puedes poner esa. Opción. Sales siempre como positiva. No entiendo.<br> :date: __2021-03-28 15:40:26__

> La idea es buena pero si el infectado no lo informa en la aplicación no vale para nada.Despues de meses y haber estado cerca de positivos nunca me ha alertado<br> :date: __2021-03-24 07:20:06__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Cuando te pones a hacer las misiones finales es imposible conseguir el radar que te pone en la 5 fecha esque no es normal porfavor arreglen eso<br> :date: __2021-04-17 22:19:03__

> Lamentablemente no sirve para nada. Con tanta seguridad no hace su función ya que no es obligatoria tenerla instalada y menos aún activarla si alguien está infectado, además de que las personas asintomáticas no activarian el "modo infectado" al no saber su infección por lo que resta eficacia a la App. Deberían darle una solución más eficaz. La mejor protección es la prevención y sentido común.<br> :date: __2021-04-17 13:59:02__

> Poco útil<br> :date: __2021-04-15 10:36:07__

> S.i pusieran todos los demás seria mejor que ahora<br> :date: __2021-04-09 11:08:50__

> Lleva unas semanas con "Error al cargar nuevos datos de contactos de infección (LOST)" o "... (AGAEN 10.-2)." Antes funcionaba bien aunque tira mucho de la batería por el bluetooth encendido continuamente.<br> :date: __2021-04-08 18:13:57__

> Se puede mejorar y mucho<br> :date: __2021-04-07 23:43:04__

> No se actualiza y siempre me dice que no funciona correctamente<br> :date: __2021-04-07 03:13:16__

> No lo sé<br> :date: __2021-04-02 14:13:33__

> Buena idea y diseño pero en mi zona hemos llegado a tener hasta 897 casos por cada 100.000 habitantes y nunca he tenido un aviso pese a tener el bluetooth permanentemente conectado.<br> :date: __2021-03-28 18:00:15__

> No me deja activar el radar covid<br> :date: __2021-03-25 21:41:01__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Mierdaseca<br> :date: __2021-04-18 05:37:03__

> La verdad no sé si aún es necesario está aplicación?? Porque el otro vi la noticia que la aplicación no sirvió de mucho 🤷 y ya dejaron de utilizarlos 😑 mejor dejaré de usar.<br> :date: __2021-04-17 23:37:04__

> No es útil en la forma actual<br> :date: __2021-04-17 22:19:23__

> Caca🤮🤮🤮🤮🤮<br> :date: __2021-04-17 17:55:46__

> Directamente no funciona. Por motivos de trabajo normalmente estoy en bastantes hospitales y por eso la instalé. Nunca he tenido un sólo aviso. Por no comentar que a los conocidos positivos que he tenido nunca se les ha facilitado el código para añadirlo en la aplicación.<br> :date: __2021-04-17 16:06:04__

> Malisimo<br> :date: __2021-04-17 15:45:36__

> No sirve para nada<br> :date: __2021-04-17 11:37:08__

> Después de tenerla instalada muchísimos meses y decirme siempre que no funciona correctamente, la desinstaló... Y no, no tengo ningún modo ahorro batería activado y siempre tengo el Bluetooth activado por el coche.<br> :date: __2021-04-17 10:47:11__

> No es práctica si su uso no es obligatorio<br> :date: __2021-04-16 21:54:05__

> No se puede actualizar, y no cumple con las espectativas de una plicación de el gobierno de España. Se podría poner un nombre con un aviso de que todas las personas con las que has estado más de 15 minutos podrán verte. He puesto 1 estrellas porque no está a la altura.<br> :date: __2021-04-16 20:50:57__


