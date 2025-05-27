import { useEffect, useState } from "react";
import { data, useLocation, useNavigate} from "react-router-dom";

function Panel_usuario(){
    const location = useLocation();
    const datos = location.state||{}; //<-- Acá accedo al state del anterior, pero no puedo trabajar bien con él
    const datos_recibidos_login = datos.datos || {};  // <--- acá extraigo "datos"
    //ESTE ESTADO ES PARA MANEJAR LOS ARCHIVOS QUE VAMOS A ENVIAR
    const [archivo, setArchivo] = useState({})
    const [documentos_necesarios, set_documentos_necesarios] = useState([])
    const [estado_subida, set_estado_subida] = useState('')
    const navegacion = useNavigate();


    function cerrar_sesion(){
        navegacion("/")
    }

    if(datos_recibidos_login.id_cargo==7){
        const [primer_nombre , set_primer_nombre] = useState('')
        const [segundo_nombre , set_segundo_nombre] = useState('')
        const [primer_apellido , set_primer_apellido] = useState('')
        const [segundo_apellido , set_segundo_apellido] = useState('')
        const [elementos_creacion_usuario,set_elementos_creacion_usuario] = useState({})
        useEffect (()=>{
            fetch('http://192.168.0.110:5000/campos_creacion_usuario').then(respuesta=>respuesta.json()).then(data =>set_elementos_creacion_usuario(data.retorno))
            
        })
        
        

        return (
            <div>
              {elementos_creacion_usuario}

            </div>
        )
    }
    
    

    useEffect(()=>{
        fetch('http://192.168.0.110:5000/obtener_cantidad_archivos',{
            method :'POST',
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({"id_usuario":datos_recibidos_login.id_usuario}),
        })
        .then(respuesta => respuesta.json())
        .then(data=> {set_documentos_necesarios(data.respuesta||[])})
    },[]);
       
    

    const manejar_cambio_archivo =(v_control_cambio,nombre_documento)=>{
        const archivo_seleccionado =(v_control_cambio.target.files[0])
        setArchivo(prev => ({...prev,[nombre_documento]:archivo_seleccionado}));
    }

    const manejarEnvio =(v_control) =>{
        v_control.preventDefault();
        //Trabajamos con el state {archivo}
        if (!archivo) return;

        const datos_formulario = new FormData();
        for (const nombre in archivo){
            datos_formulario.append(nombre,archivo[nombre]);
        }
        datos_formulario.append("nombre_usuario",datos_recibidos_login.primer_nombre+' '+datos_recibidos_login.primer_apellido)
        
        
        try{
            fetch("http://192.168.0.110:5000/upload",{
                method:'POST',
                body:datos_formulario,
            }).then(respuesta => respuesta.json())
            .then(data => {set_estado_subida(data.mensaje)});
            
        }catch (err){console.log(err)
        }
        
    }


    return(
        <div>
            <h2>{datos_recibidos_login.cargo}</h2>
            <h2>{datos_recibidos_login.primer_nombre+' '+datos_recibidos_login.primer_apellido}</h2>
            <h2></h2>

            {/* Vamos a usar un map para iterar sobre nuestro JSON, el map nos pide un oarametro item, y se expresa una funcion flecha */}
            <form onSubmit={manejarEnvio}>
                {documentos_necesarios.map((item)=> (
                    <div>
                        <label>{item}</label>
                        <input 
                        type="file"
                        onChange={(e) =>manejar_cambio_archivo(e,item)} />
                    </div>
                ))}
                <button type="submit">Subir</button>
                <p>{estado_subida}</p>
            </form>
            <button onClick={cerrar_sesion}>Cerrar Sesion</button>
        </div>
    )
}

export default Panel_usuario