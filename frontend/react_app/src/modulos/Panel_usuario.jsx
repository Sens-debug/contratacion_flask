import { useEffect, useState } from "react";
import { data, useLocation } from "react-router-dom";

function Panel_usuario(){
    const location = useLocation();
    const datos = location.state||{}; //<-- Acá accedo al state del anterior, pero no puedo trabajar bien con él
    const datos_recibidos_login = datos.datos || {};  // <--- acá extraigo "datos"

    const [documentos_necesarios, set_documentos_necesarios] = useState([]) 

    console.log(datos_recibidos_login)

    useEffect(()=>{
        fetch('http://127.0.0.1:5000/obtener_cantidad_archivos',{
            method :'POST',
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({"id_usuario":datos_recibidos_login.id_usuario}),
        })
        .then(respuesta => respuesta.json())
        .then(data=> {set_documentos_necesarios(data.respuesta||[])})
    },[]);
    console.log(documentos_necesarios);
    
    return(
        <div>
            <h1>Prueba</h1>
            <div>{documentos_necesarios}</div>
        </div>
    )
}

export default Panel_usuario