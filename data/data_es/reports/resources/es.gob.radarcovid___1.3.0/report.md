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

> Sale que no hay contactos porque los positivos no registran que lo son<br> :date: __2021-05-07 12:54:54__

> es la mejor aplicacion para el covid19<br> :date: __2021-05-05 19:16:57__

> Muy buena antes lo lo tenía con tanto campo como ahora<br> :date: __2021-05-05 19:03:41__

> Muy buena aplicación<br> :date: __2021-05-04 01:37:04__

> Sensacional y muy necesaria.<br> :date: __2021-05-03 18:17:41__

> Recomiendo...pero consume mucha batería.<br> :date: __2021-05-02 10:13:50__

> por esto es por que nunca me contagio<br> :date: __2021-05-02 08:21:02__

> Excelente App para avisarte cuando el Bluetooth de tu celular está apagado, le doy 5 estrellas porque no hay más y además soy fun de la Mahou 5 estrellas. Desde que la instalé no puedo vivir sin ella.<br> :date: __2021-04-28 21:34:38__

> Excelente<br> :date: __2021-04-28 05:13:00__

> Me ha encantado el juego me encanta que hayan sacado Plague Inc 2.0 tiene sistema de detección increíble y me encanta que ya venga una enfermedad gratis incluida porcierto me encanta que la cuarentena se tan efectiva que pena que la vacuna cueste tanto de sacar en España, Gracias<br> :date: __2021-04-27 11:13:30__



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

> No se pero si me gustaría saber si estoy al lado de un cobi9<br> :date: __2021-05-09 15:37:14__

> Me resulta chocante que en Euskadi que tengo alardeamos de muchas cosa estemos con respecto a otras comunidades n la cola d espera para vacunarnos tengo yo tengo 69 años y ni una sola notificacion para vacunarme<br> :date: __2021-05-07 01:32:52__

> Si se supone que usa el Bluetooth y no la localización, así que no debería de estar constantemente dando señales de alerta para activar localización. Si no quieres hacerlo. Incluso con modo avión, o de noche, molesta. Si no quiero activar localización, no debería de estar todo el tiempo avisando.<br> :date: __2021-05-06 09:05:40__

> Me parecería muy útil si desde sanidad se dieran los códigos a la gente positiva. No conozco a nadie a quien le hayan dado un código,; y algunos que han preguntado por el código, no sabían ni de qué les hablaban<br> :date: __2021-04-30 16:56:19__

> Nunca he debido de estar el tiempo suficiente con un positivo con la app para que me avisara. Si que es muy cansina, creo que su función era recordarte constantemente que te podías infectar.<br> :date: __2021-04-25 10:16:36__

> Esto habría q haberlo hecho obligatorio para que sirviese para algo. Si nos han obligado a confinarnos, cerrar empresas y luego a toque de queda podrían haber obligado a descargarse una app q es mucho menos problemático. Para eso estamos en estado d alarma.<br> :date: __2021-04-22 22:12:42__

> El numero de personas con covid - 19 dadas de alta en esta aplicacion es muy bajo, teniendo en cuenta el alto numero de contagiados que ha habido en el pasado y que hay en el presente en España, hacen de esta aplicacion que su accion de avisar de que uno este cerca o proximo a una persona contagiada de covid es muy limitada y su influencia para limitar los contagios es muy limitada y precaria. Es una buena idea pero depende de la capacidad social, empatica y sentido de la solidaridad de España<br> :date: __2021-04-21 15:22:42__

> Después de bastante tienpo usándolo me acaba de decir que ahora tengo que darle permiso de ubicación, que antes no era necesario ¿Ha habido algún cambio en la aplicación? ¿Por qué es necesario ahora si antes no lo era porque usaba el Bluetooth?<br> :date: __2021-04-20 17:36:00__

> Dudo que funcione, tengo mis dudas.<br> :date: __2021-04-19 13:41:32__

> Siempre está que no funciona bien<br> :date: __2021-04-13 22:50:42__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Excelente iniciativa para ayudar a combatir la pandemia. Lastima que no haya funcionado como debiera. No me refiero al molesto aviso de ahorro de batería que salía cada dos por tres. Sino al conjunto de factores que hacen que no funcione como proyecto. Por un lado la app no la usaba casi nadie porque muchos no sabían que existía o se creían que era intrusiva en cuanto a privacidad. Y por otro lado resulta que para indicara la app que tienes covid han de darte un código especial en el médico.<br> :date: __2021-05-06 07:56:05__

> Nunca he tenido nadie cerca desde que lo instalé, me parece muy raro<br> :date: __2021-05-05 17:52:53__

> Funcionaría mejor si todo el mundo la tuviera. No todos saben de su existencia<br> :date: __2021-05-02 18:19:27__

> No es muy buena app. No notifica NADA. Esto no va.<br> :date: __2021-05-01 13:18:25__

> Solo vale para ocupa espacio en el teléfono...Así q no merece la pena tenerla<br> :date: __2021-04-26 17:58:14__

> Si no tenemos todos la aplicacion,sirve poco<br> :date: __2021-04-24 16:50:52__

> No encuentro la forma de activarlo en POCO X3 PRO<br> :date: __2021-04-23 21:45:07__

> Cuando te pones a hacer las misiones finales es imposible conseguir el radar que te pone en la 5 fecha esque no es normal porfavor arreglen eso<br> :date: __2021-04-17 22:19:03__

> Lamentablemente no sirve para nada. Con tanta seguridad no hace su función ya que no es obligatoria tenerla instalada y menos aún activarla si alguien está infectado, además de que las personas asintomáticas no activarian el "modo infectado" al no saber su infección por lo que resta eficacia a la App. Deberían darle una solución más eficaz. La mejor protección es la prevención y sentido común.<br> :date: __2021-04-17 13:59:02__

> Poco útil<br> :date: __2021-04-15 10:36:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Voy a desinstalarla. Muy decepcionante, no funciona para nada. Una pena el dinero gastado.<br> :date: __2021-05-09 15:45:53__

> Penoso, los únicos mensajes son "la aplicación está funcionando mal" vaya desastre, ahora mismo lo desinstalo<br> :date: __2021-05-08 18:58:42__

> Horrible no sirve para nada, solo gasta batería<br> :date: __2021-05-08 10:11:12__

> De VERGÜENZA. La instalé en cuanto salió, incluso la envié a todos mis amigos y familiares recomendando que la instalaran... En la empresa donde trabaja mi mujer tuvieron un positivo, y ella por su trabajo trata con público a diario... jamás recibió ni un aviso. En otros países este tipo de apps han funcionado muy bien y han sido una herramienta vital contra el virus; aquí, ni funciona, ni es obligatorio instalarla, ni el Gobierno ha hecho NADA por promoverla. Un DESASTRE. Desinstalada 05/2021.<br> :date: __2021-05-07 18:17:14__

> Dinero público para el amiguito de turno...<br> :date: __2021-05-07 16:44:24__

> EL HOMBRE SIN MASCARILLA AQUEL QUE GUARDABA LOS DOS METROS DE DISTANCIA<br> :date: __2021-05-06 22:40:40__

> Es imposible notificar un positivo. Te piden un codigo que es imposible conseguir (al menoa en la comunidad valenciana).Llevo 1 semana intentando notificarlo, y lo doy por imposible. La idea es buena, pero tiene que ser accesible para que sea útil.<br> :date: __2021-05-06 09:41:24__

> "Radar Covid no funciona" Único mensaje que he recibido a lo largo de 5 meses. ¿Hay algún responsable?<br> :date: __2021-05-04 21:26:52__

> Aplicación de porquería, dejen de asustar a la gente😂😂<br> :date: __2021-05-04 20:27:43__

> Ahora sí podre jugar e tirarme un si, gracias, yo no lo descargo por qué ya lo tengo, yo escupirle a si corona y comer corona todas my House :(<br> :date: __2021-05-04 19:56:58__


