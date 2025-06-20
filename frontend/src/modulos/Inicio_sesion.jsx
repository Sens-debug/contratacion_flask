import React, { useEffect, useState } from "react";
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
    const manejarEnvio = async(variableControl) => {
        variableControl.preventDefault();
       try{
        const response = await fetch(uri_flask+'/login',{ 
            method: 'POST',
            credentials:'include',//esto es crítico para que las cookies se envíen y reciban
            headers:{
                'Content-Type':'application/json'
            },     
            body: JSON.stringify({"usuario":usuario, "contraseña":contraseña}),
        });       
        const data = await response.json()
        setMensaje(data.mensaje)
        setTimeout(()=>{
            if (data.cargo_id==4){ navegacion('/panel_admin')}
        },0)     
        } catch(error) {
            console.error('ERROR:', error)
            setMensaje('Ocurrio un error durante el fetch');
        };
    };
       

        return(
            <div className=" bg-gray-700 justify-center min-h-screen flex items-center">               
                <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md flex items-center">
                <form onSubmit={manejarEnvio}className="space-y-4 ">
                <div>
                    <label className="block text-black font-medium" >Usuario:</label>
                    <input type="text"
                    className="mt-1 block rounded-md bg-gray-200 border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                    value={usuario}
                    onChange={(e)=> setUsuario(e.target.value)} 
                    required/>
                </div>
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