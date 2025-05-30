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
    const uri_flask = import.meta.env.VITE_URL_SERVIDOR

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
            fetch(uri_flask+'/campos_creacion_usuario').then(respuesta=>respuesta.json()).then(data =>set_elementos_creacion_usuario(data.retorno))
            
        })
        
        

        return (
            <div>
              {elementos_creacion_usuario}

            </div>
        )
    }
    
    

    useEffect(()=>{
        fetch(uri_flask+'/obtener_cantidad_archivos',{
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
        datos_formulario.append("nombre_completo",datos_recibidos_login.nombre_completo)
        datos_formulario.append("direccion",datos_recibidos_login.direccion)
        datos_formulario.append("cedula",datos_recibidos_login.cedula)
        datos_formulario.append("correo",datos_recibidos_login.correo)
        datos_formulario.append("cargo",datos_recibidos_login.cargo)
        datos_formulario.append("cargo_id",datos_recibidos_login.cargo_id)
        datos_formulario.append("area",datos_recibidos_login.area)
        datos_formulario.append("rh",datos_recibidos_login.rh)
        datos_formulario.append("f_nacimiento",datos_recibidos_login.f_nacimiento)
        datos_formulario.append("tel",datos_recibidos_login.tel)
        datos_formulario.append("id_usuario",datos_recibidos_login.id_usuario)
        
        try{
            fetch(uri_flask+"/upload",{
                method:'POST',
                body:datos_formulario,
            }).then(respuesta => respuesta.json())
            .then(data => {set_estado_subida(data.mensaje)});
            
        }catch (err){console.log(err)
        }
        
    }


    return(
        <div>
            <div>
                <h2>{datos_recibidos_login.cargo}</h2>
                <h2>{datos_recibidos_login.nombre_completo}</h2>
                <h2></h2>
            </div>

            <div>
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
                    <br />
                    
                    <button type="submit">Subir</button>
                    <p>{estado_subida}</p>
                </form>
            </div>
            <button onClick={cerrar_sesion}>Cerrar Sesion</button>
        </div>
    )
}

export default Panel_usuario