import React, { useState } from "react";
//Con el hook de la siguiente importacion podemos maneajr las redirecciones
import { useNavigate } from "react-router-dom";


export function Formulario_login(){
    //Seteamos las variables 'reactivas' con las que vamos a trabaj en este modulo
    const [usuario, setUsuario] = useState('');
    const [contraseña, setContraseña] = useState('');
    const [mensaje, setMensaje] = useState('');
    //Con este hook manejamos la navegacion por el sistema
    const navegacion = useNavigate();

    //Creamos una funcion que nos haga el manejo de envio de datos desde ellogin hasta el backend
    const manejarEnvio =(variableControl) => {
        variableControl.preventDefault();
        //Hace un fetch a la url del backend
        fetch('http://127.0.0.1:5000/inicio_sesion',{
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
            <div>
                <h1>CONTRATACION</h1>
                <h2>Iniciar Sesion</h2>
                {/* Creamos la etiqueta Formulario donde crearemos toda la estructura del mismo */}
                <form onSubmit={manejarEnvio}>
                {/* Div del usuario */}
                <div>
                    {/* Creamos la etiqueta Usuario del formulario */}
                    <label >Usuario:</label>
                    {/* Creamos un input y asiganos sus valores clave
                    -tipo-
                    -valor{muestra el valor actual contenido en la variable citada}
                    -onchange-{'actualiza el estado cuando el usuario escribe (on change)
                    -requerido : Especifica campo obligatorio} */}
                    <input type="text"
                    value={usuario}
                    onChange={(e)=> setUsuario(e.target.value)} 
                    required/>
                </div>
                {/* DIV de la contraseña */}
                <div>
                    <label>Contraseña:</label>
                    <input type="password"
                        value={contraseña}
                        onChange={(e)=>setContraseña(e.target.value)}
                        required 
                    />
                </div>
                <button type="submit">Ingresar</button>
                </form>
                <p>{mensaje}</p>
            </div>
            
        )   
    
}