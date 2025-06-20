import React,{ useEffect, useState } from "react";
import {  data, useLocation, useNavigate} from "react-router-dom";
import "../index.css"

import {DateInput,Form,Button,Input,Select,SelectItem} from "@heroui/react";
import {Dropdown,DropdownItem,DropdownMenu,DropdownTrigger} from "@heroui/react";



function Panel_usuario(){
    const location = useLocation();
    const datos = location.state||{}; //<-- Acá accedo al state del anterior, pero no puedo trabajar bien con él
    const datos_recibidos_login = datos.datos || {};  // <--- acá extraigo "datos"
    //ESTE ESTADO ES PARA MANEJAR LOS ARCHIVOS QUE VAMOS A ENVIAR
    console.log(datos_recibidos_login)
    const [archivo, setArchivo] = useState({})
    const [estado_subida, set_estado_subida] = useState('')
    const navegacion = useNavigate();
    const uri_flask = import.meta.env.VITE_URL_SERVIDOR
    const [documentos_necesarios, set_documentos_necesarios]= useState([])
    const [usuarios_en_sistema, set_usuarios_en_sistema] = useState([])
    const [estados_contratacion, set_estados_contratacion] = useState([])
    const [lista_usuarios,set_lista_usuarios] = useState([])
      const [estados_a_seleccionar, set_estados_a_seleccionar] = React.useState(["Seleccione estado Contratacion"]);
      const estado_seleccionado = React.useMemo(
      () => Array.from(estados_a_seleccionar).join(", ").replace(/_/g, ""),
      [estados_a_seleccionar],
      );

      const [usuarios_a_seleccionar, set_usuario_a_seleccionar] = React.useState(["Seleccione Usuario"]);
      const usuario_seleccionado = React.useMemo(
      () => Array.from(usuarios_a_seleccionar).join(", ").replace(/_/g, ""),
      [usuarios_a_seleccionar],
      );

      const [cargos_a_elegir, set_cargos_a_elegir] = React.useState(["Cargo"]);
      const cargo_seleccionado = React.useMemo(
      () => Array.from(cargos_a_elegir).join(", ").replaceAll("_", " "),
      [cargos_a_elegir],);

      const [tipos_sangre_a_elegir, set_tipos_sangre_a_elegir] = React.useState(["Tipo Sangre"]);
      const tipo_sangre_seleccionado = React.useMemo(
      () => Array.from(tipos_sangre_a_elegir).join(", ").replaceAll("_", " "),
      [tipos_sangre_a_elegir],);

      const [estado_firma_a_elegir, set_estado_firma_a_elegir] = React.useState(["Estado Firma"]);
      const estado_firma_seleccionado = React.useMemo(
      () => Array.from(estado_firma_a_elegir).join(", ").replaceAll("_", " "),
      [estado_firma_a_elegir],);
      const [mensaje_back, set_mensaje_back] = useState("");
      const [cedula_a_buscar, set_cedula_a_buscar] = useState("");

      const [fecha_nacimiento, set_fecha_nacimiento] = useState();
      const [valido, setValido] = useState()
      const [aceptoPolitica, setAceptoPolitica] = useState();

      const [empresa,set_empresa] = useState()
      
    useEffect(()=>{
        fetch(uri_flask+"/comprobacion")
        .then(response => response.json())
        .then(data => setValido(data.estado))

        if(datos_recibidos_login.cargo_id!=4){
          fetch(`${uri_flask}/obtener_aceptacion_tratamiento_datos`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({"id_usuario":datos_recibidos_login.id_usuario})
          })
          .then(res => res.json())
          .then(data => {setAceptoPolitica(data.acepta)})
          .catch(error => console.error("Error al enviar:", error));

        fetch(uri_flask+'/obtener_cantidad_archivos',{
            method :'POST',
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({"id_usuario":datos_recibidos_login.id_usuario}),
        })
        .then(respuesta => respuesta.json())
        .then(data=> {set_documentos_necesarios(data.respuesta||[])})
      }
        if(datos_recibidos_login.cargo_id==4){
        fetch(uri_flask+'/obtener_usuarios')
        .then( response => response.json())
        .then(data => set_usuarios_en_sistema(data.usuarios))
        .catch(error=> console.log("error"+error))
        
        fetch(uri_flask+'/obtener_estados_contratacion')
        .then(response=> response.json())
        .then(data => set_estados_contratacion(data.estados))
        .catch(error=> console.log("error"+error))

        }
    },[]);
      
        console.log(documentos_necesarios)
        console.log(usuarios_en_sistema)
        console.log(estados_contratacion)

    function cerrar_sesion(){
        navegacion("/")
    }

    function envio_creacion_usuario(e){
                e.preventDefault();
                if (cargo_seleccionado === "Cargo" || tipo_sangre_seleccionado === ('Tipo Sangre')) {
                       alert("Debe llenar todos los campos obligarios '*'");
                       return;
                     }
                 
                     const datos = Object.fromEntries(new FormData(e.currentTarget));
                     datos["cargo_seleccionado"] = cargo_seleccionado;
                     datos["tipo_sangre_seleccionado"] =tipo_sangre_seleccionado
                     datos["fecha_nacimiento"] = fecha_nacimiento
                     datos["empresa"] = empresa
                 
                     // Enviar datos aquí directamente si necesitas
                     console.log("Datos a enviar:", datos);
                 
                     // Si quieres hacer un fetch aquí, hazlo directamente
                     fetch(`${uri_flask}/crear_usuario`, {
                       method: "POST",
                       headers: {
                         "Content-Type": "application/json"
                       },
                       body: JSON.stringify(datos)
                     })
                     .then(res => res.json())
                     .then(data => {
                       console.log("Respuesta del servidor:", data);
                     })
                     .catch(error => console.error("Error al enviar:", error));
                     alert("Se creo el usuario exitosamente")
                     window.location.reload()
                               
    }

   
    
    
    const manejar_cambio_archivo =(v_control_cambio,nombre_documento)=>{
        const archivo_seleccionado =(v_control_cambio.target.files[0])
        setArchivo(prev => ({...prev,[nombre_documento]:archivo_seleccionado}));
    }

    const manejarEnvio =(v_control) =>{
        v_control.preventDefault();
         if (!aceptoPolitica) {
        alert("Debes aceptar la política de tratamiento de datos.");
        return;
      }
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
    

    if(datos_recibidos_login.cargo_id!=4){ 
      
      
        console.log(aceptoPolitica)
        
         return(
        <div className="min-h-screen w-screen bg-gray-900">
            <div className="bg-gray-800 w-full text-white font-semibold  px-6 px-y-4 shadow-md flex justify-between items-center top-0 w-fill h-fill z-10">
                <h2>{datos_recibidos_login.cargo}</h2>
                <h2>|||</h2>
                <h2>{datos_recibidos_login.nombre_completo}</h2>
            
            </div>

            <div className="pt-2 px-6 flex flex-col items-center gap-8 ">
                {/* Vamos a usar un map para iterar sobre nuestro JSON, el map nos pide un oarametro item, y se expresa una funcion flecha */}
                <form onSubmit={manejarEnvio}
                className="border-4 border-blue-300 max-w-screen"
                >
                  <div className="bg-white">
                     <label className=" gap-2 text-sm text-gray-700">
                          <input
                            type="checkbox"
                            checked={aceptoPolitica}
                            onChange={(e) => setAceptoPolitica(e.target.checked)}
                            className="form-checkbox text-blue-600"
                          />
                          He leído y acepto la política de tratamiento de datos
                        </label>
                        <br />
                        <a  className ='text-blue-500 hover:text-blue-600' target ="_blank" href="https://drive.google.com/file/d/1D8oa0i422lA4sTEHhNoxGI4zJETDv_iU/view?usp=sharing">Ver politica tratamiento Datos</a>
                      
                      <br />
                      <p className="border-b p-2"></p>
                      
                    </div>
                    {documentos_necesarios.map((item)=> ( 
                        <div className="bg-white">
                            <label className="">{item}</label>
                            <input 
                            type="file"
                            onChange={(e) =>manejar_cambio_archivo(e,item)}
                            className="flex  w-full text-sm text-gray-600
                       file:mr-4 file:py-2 file:px-4
                       file:rounded-md file:border-0
                       file:text-sm file:font-semibold
                       file:bg-blue-50 file:text-blue-700
                       hover:file:bg-blue-100" />
                        </div>
                    ))}
                    
                    <div className="bg-white flex place-content-center">
                    <button type="submit"
                    className=" w-1/3  bg-blue-400 rounded-md  text-white  py-2 px-1  hover:bg-blue-900 transition">Subir</button>
                    </div>
                    <p className="text-black bg-amber-50">{estado_subida}</p>
                </form>
            </div>
            <br />
            <div  className="flex place-content-center ">
            <button onClick={cerrar_sesion}
            className="w-1/4 bg-blue-400  text-white py-2 px-4 rounded-md hover:bg-blue-900 transition">Cerrar Sesion</button>
            </div>
        </div>
    )
        
    }

   
}


export default Panel_usuario