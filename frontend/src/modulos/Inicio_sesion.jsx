import React, { useState } from "react";
//Con el hook de la siguiente importacion podemos maneajr las redirecciones
import { useNavigate } from "react-router-dom";
import "../index.css"


export function Formulario_login(){
    //Seteamos las variables 'reactivas' con las que vamos a trabaj en este modulo
    const [usuario, setUsuario] = useState('');
    const [contraseña, setContraseña] = useState('');
    const [mensaje, setMensaje] = useState('');
    //Con este hook manejamos la navegacion por el sistema
    const navegacion = useNavigate();
    const uri_flask = import.meta.env.VITE_URL_SERVIDOR


    //Creamos una funcion que nos haga el manejo de envio de datos desde ellogin hasta el backend
    const manejarEnvio =(variableControl) => {
        variableControl.preventDefault();
        //Hace un fetch a la url del backend
        fetch(uri_flask+'/inicio_sesion',{
            //Especifica el metodo del fetch 'post'
            method: 'POST',
            //Marca que se va a enviar un formato JSON
            headers:{
                'Content-Type':'application/json'
            },
            //Especificamos el JSON a enviar
            body: JSON.stringify({"usuario":usuario, "contraseña":contraseña}),
        })
        //Esta es la respuesta del servidor
        .then(respuesta => respuesta.json())
        
        //luego incrustamos en el estado mensaje, el valor de la clave estado en el return del server
        .then(data =>{setMensaje(data.estado)
            //Condicional ternario que verifica si el login fue exitoso, posterior a eso envia la data del fetch a traves de stados de React
            data.estado=='aprobado'?navegacion('/app',{state:{"datos":data}}):''
        })
        //Manejamos cualquier posible error en el fetch
        .catch(error => {
            console.error('ERROR:', error)
            setMensaje('Ocurrio un error durante el fetch')
        });
    };
        return(
            <div className=" bg-gray-700 justify-center min-h-screen flex items-center">
                

                <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md flex items-center">
                
                {/* Creamos la etiqueta Formulario donde crearemos toda la estructura del mismo */}
                <form onSubmit={manejarEnvio}className="space-y-4 ">
                {/* Div del usuario */}
                <div>
                    {/* Creamos la etiqueta Usuario del formulario */}
                    <label className="block text-black font-medium" >Usuario:</label>
                    {/* Creamos un input y asiganos sus valores clave
                    -tipo-
                    -valor{muestra el valor actual contenido en la variable citada}
                    -onchange-{'actualiza el estado cuando el usuario escribe (on change)
                    -requerido : Especifica campo obligatorio} */}
                    <input type="text"
                    className="mt-1 block rounded-md bg-gray-200 border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                    value={usuario}
                    onChange={(e)=> setUsuario(e.target.value)} 
                    required/>
                </div>
                {/* DIV de la contraseña */}
                <div>
                    <label className="block text-black font-medium">Contraseña:</label>
                    <input type="password"
                        value={contraseña}
                        onChange={(e)=>setContraseña(e.target.value)}
                        required
                        className="mt-1 block rounded-md bg-gray-200 border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500" 
                    />
                </div>
                <button className="w-full bg-blue-700 text-white py-2 px-4 rounded-md hover:bg-blue-900 transition" type="submit">Ingresar</button>
                <p className="text-m">{mensaje}</p>
                </form>
                
                </div>
            </div>
            
        )   
    
}