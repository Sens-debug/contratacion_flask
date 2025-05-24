import { useState, useEffect } from "react";

export function Inicio_sesion() {
    //Establecemos un UseState el cual es un hook que se carga antes que el mismo componente en si, permitiendonos usar variables que resisten la "iteracion"
    //useState: Hook que permite usar estados (variables reactivas) en componentes funcionales.
    //    variable -- setterVariable -- ValorInicialVariable
    const [response, set_response] = useState([])

    //Procedemos a usa un useEffect, el cual es un hook que nos permite ejecutar codigo antes que el resto del modulo
    //UseEffect recibe como parametro una funcion, en este caso uso una flecha anonima
    //useEffect: Hook que permite ejecutar código cuando el componente se monta o actualiza.

    useEffect(()=>{
        //Realizamos un fetch a nuestra url 'servidor', esto antes de que corra cualquier otra logica
        fetch('http://127.0.0.1:5000/obtener_usuarios')
        //'entonces', recibe una respuesta que almacena en una variable {respuesta}, y la codificamos en formato json
        .then(respuesta => respuesta.json())
        //'entonces', esa respuesta del then anterior será almacenada en la variable de aquí
        .then(datos => set_response(datos.respuesta))
        .catch(e=> console.log(e))
        console.log(response)
    //La sintaxis array antes del cierre de parentesis es para especificar que solo va a hacer el effect 1 sola vez
    },[])
    return(
        <div>
            <h1>APP REACT+FLASK</h1>
                <p>{response}</p>

        </div>
    );
}