# MACETEROS INTELIGENTES
1. MOTIVACIÓN

Concienciación sobrelos objetivos de desarrollo sostenibleque se mencionan a continuación mediante el desarrollo de un sistema informático de calidad que los fomente.

+ Objetivo 7: Energía asequible y no contaminanteo
  + 7.1: Acceso universal a la energíao
  + 7.2:Energíasrenovableso
  + 7.3: Eficiencia energéticao
  + 7.B: Infraestructura y tecnología en países en desarrollo
+ Objetivo 11: Ciudades y comunidades sostenibleso
  + 11.3: Urbanización inclusiva y sostenibleo
  + 11.A: Vínculos zonas urbanas, periurbanas y rurales
+ Objetivo 12: Producción y consumo responsableso
  + 12.1: Planes de consumo y producción responsableo
  + 12.2: Uso eficiente de recursos naturaleso
  + 12.3: Desperdicios de alimentoso
  + 12.4: Gestión de desechos y productos químicoso
  + 12.5: Prevención, reducción, reciclado y reutilización de desechos
+ Objetivo 13: Acción por el climao
  + Educación y sensibilización

2. PROBLEMA

En ciertos ámbitos, se hace un mal uso de los recursos naturales. Por esta razón,se quiere afrontar el problema desarrollando un sistema informático que sea capaz de satisfacer las necesidades de un cierto tipo de planta, favoreciendo con estolas características de un desarrollo sostenible.

3. SOLUCIÓN

En este proyecto se implementará un sistemabasado en computador, bajo la arquitectura de Internet of Things(IoT), con el objetivo principal de concienciar a la civilización del impacto medioambiental que está desarrollando la actividad humana y ofrecerles posibles formas de mitigarlo.

4. DESCRIPCIÓN DEL SISTEMABASADO EN COMPUTADOR

El sistema tendrá las siguientes funcionalidades físicas y software:

SENSORES
+ Un subsistema que capture los aspectos relacionadoscon el entorno de la planta: temperatura, humedad y luz, principalmente.
+ Un subsistema que capture los aspectos más relevantes del estado interno de la planta: humedad del suelo, nutrientes y sales minerales, entre otros.

ACTUADORES
+ Un subsistema de iluminación para situaciones en las que se requiera de luz artificial.
+ Un subsistema de riego que actúe en función de los datos obtenidos.
+ Un subsistema de alimentación que actúe cuando la planta requiera nutrientes.

ALMACENAMIENTO Y VISUALIZACIÓN DE LA INFORMACIÓN
+ Un sistema IoT situado en la nube, llamado thingsboard.io, que se encargaráde integrar y almacenar las distintas características muestreadas de la planta para facilitar el acceso a estas y mostrarlas gráficamente a los usuarios.
+ Mostrar los datos recogidos y almacenados en la nube en paneles informativos del Campus de la Universidad Politécnica de Madrid (UPM). Para ello se utilizarán dashboards para ofrecer una interfaz gráfica más intuitiva y adaptada al usuario.

COMPUTADOR
+ Un sistema principal, el computador, que será el nexo entre el resto de los subsistemasy cuyo papel será recibir los datos capturados, realizar un tratamiento adecuado de estos y, en función de ello, enviar órdenes a los distintos actuadores (iluminación, riego, etc.)manteniendo así la planta en perfecto estado. El protocolo de comunicación entre el computador y los sensores y actuadores estará basado en I2C, es decir, todos los dispositivos compartirán una misma línea de comunicación conectada al computador para enviar o recibir datos.
+ También se encargará de almacenar los datos en la plataforma IoT para mantener una monitorización coherente.
+ Todas estas tareas se programarán utilizando el lenguaje Python.

La arquitectura seguirá el modelo esquemático mostrado a continuaciónen la figura 1.

![Esquema global del sistema](https://i.ibb.co/0jVjSTM/esquema.png)
