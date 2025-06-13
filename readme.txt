Planteamiento del Problema -->Simular el funcionamiento real de un aplicativo de contratacion, enviando archivos a través del protocolo HTTP
    El plantel empresarial tiene una problematica mayor, la cual es la gestion de papel,
    esto debido a que la documentacion a firmar por los auxiliares es muy grande(aprox 20 paginas por persona)
    Lo cual representa un gran gasto problematicas en la gestion general del area "Talento Humano"

Solucion del Problema -- > Armar un Aplicativo que permita la transferencia de archivos, y a su vez contenga la logica para la firma automatica de los mismo
    Se establecieorn las tecnologias a utilizar ->(Python-FLASK, JavaScript-REACT, MySQL)

    GUI -> Se inicio con Tkinter(Se hizo el avance,pero el alcance del proyecto era muy grande para una app escritorio)

    GUIv2-> En react se desarrolaron 2 vistas para la gestion del aplicativo, se renderizan segun el cargo del usuario,
        Maneja States y Effects que gestionan el SaaS y los datos a renderizar segun el cargo
        Uso el .env para el enlace de mi Backend esto debido a que al ser local en una red inestable; ese valor es muy cambiante, y cuando  
    
    Backend -> Toda la logica a excepcion del modulo encargado de firmar los archivos está contenido en un Controller FLASK
        Se implementan los endpoints con metodos HTTP, tambien se aplica el SaaS Al Backend

    El sistema maneja ciertas valdiaciones y excepciones para amarrarnos al lado legal del sistema,
        entre ellas está la firma, los estados, y el almacenamiento de metadatos para el registro de aceptacion el politica de datos



