El principal objetivo del proyecto es simular el funcionamiento real de un aplicativo de contratacion, enviando archivos a través del protocolo HTTP

Se creó una carpeta Flask la cual contiene la logica del servidor, permitiendo así el flujo de archivos
Tambien se establecio una interfaz tkinter que permite la seleccion y subida de un archivo a través de su PATH, conectandose a la URI del servidor Flask

*   -Se requiere correr ambos scripts en consolas separadas para su correcto funcionamiento-*

Se modifico el parametro 'host' a = '0.0.0.0' esto para permitir el intercambiar paquetes dentro de la misma red,
puesto que esto me crea una IPPRIVADA más allá del LocalHost, lo cual me permite trabajar en la red

Se deja un archivo .BD que constituye la query de inicializacion de la estructura de tablas -> Donde se manejara una estructura que permita ampliacion