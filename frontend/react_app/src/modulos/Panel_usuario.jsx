import React,{ useEffect, useState } from "react";
import {  data, useLocation, useNavigate} from "react-router-dom";
import "../index.css"
import { Form } from "@heroui/form";
import {Button} from "@heroui/button"
import {Input} from "@heroui/input"
import {Dropdown, DropdownTrigger, DropdownMenu, DropdownItem, DateInputField} from "@heroui/react";
import {DateInput} from "@heroui/react";




function Panel_usuario(){
    const location = useLocation();
    const datos = location.state||{}; //<-- Acá accedo al state del anterior, pero no puedo trabajar bien con él
    const datos_recibidos_login = datos.datos || {};  // <--- acá extraigo "datos"
    //ESTE ESTADO ES PARA MANEJAR LOS ARCHIVOS QUE VAMOS A ENVIAR
    const [archivo, setArchivo] = useState({})
    const [estado_subida, set_estado_subida] = useState('')
    const navegacion = useNavigate();
    const uri_flask = import.meta.env.VITE_URL_SERVIDOR
    const [documentos_necesarios, set_documentos_necesarios]= useState([])
    const [usuarios_en_sistema, set_usuarios_en_sistema] = useState([])
    const [estados_contratacion, set_estados_contratacion] = useState([])

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
      const [mensaje_back, set_mensaje_back] = useState("")

      const [fecha_nacimiento, set_fecha_nacimiento] = useState()

    

    useEffect(()=>{
        if(datos_recibidos_login.cargo_id!=4){
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
                     window.location.reload()
                               
    }

    if(datos_recibidos_login.cargo_id==4){
      
    
      function actualizar_estado_contratacion(e){
        e.preventDefault();
        if(estado_seleccionado == "Seleccione estado Contratacion" || usuario_seleccionado == "Seleccione Usuario"){
        alert("Debe rellenar todos los campos del formulario");
        return;}
        
        const datos = Object.fromEntries(new FormData(e.currentTarget));
        datos["id_usuario"]= usuario_seleccionado
        datos["id_estado"] = estado_seleccionado
        console.log("datos a enviar",datos);

        fetch(uri_flask+"/actualizar_estadoxusuario",{
          method: 'POST',
          headers:{
            "Content-Type": "application/json"
          },
          body: JSON.stringify(datos)
        })
        .then(res => res.json())
        .then(data => set_mensaje_back(data.mensaje))
        .catch(error => console.log("error"+error));
        }
        
      function actualizar_estado_firma(e){
        e.preventDefault()
        if(estado_firma_seleccionado == "Estado Firma" || usuario_seleccionado == "Seleccione Usuario"){
            alert("Rellene los datos de su formulario")
            return
        }
        const datos = Object.fromEntries(new FormData(e.currentTarget));
        datos["estado_firma"] = estado_firma_seleccionado
        datos["id_usuario"] = usuario_seleccionado
        
        fetch(uri_flask+"/actualizar_estado_firma",{
          method: 'POST',
          headers:{
            "Content-Type": "application/json"
          },
          body: JSON.stringify(datos)
        })
        .then(res => res.json())
        .then(data => set_mensaje_back(data.mensaje))
        .catch(error => console.log("error"+error));
        }
      
        return (
            <div className="bg-gray-500 w-full  h-full flex flex-row  ">
              
            <Form
            className="w-1/2 max-w-xs  h-full flex flex-col gap-4 bg-white"
            onSubmit={envio_creacion_usuario}>
                <h1 className="text-center bg-gray-300 font-medium">Creacion Usuario</h1>
                <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="Ingrese el primer_nombre_del_usuario"
            label="Primer_nombre*"
            labelPlacement="outside"
            name="Primer_nombre"
            placeholder="Primer Nombre"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            errorMessage=""
            label="Segundo_nombre"
            labelPlacement="outside"
            name="Segundo_nombre"
            placeholder="Segundo Nombre"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="Ingrese el Primer Apellido"
            label="Primer_Apellido*"
            labelPlacement="outside"
            name="Primer_apellido"
            placeholder="Primer Apellido"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            errorMessage=""
            label="Segundo_apellido*"
            labelPlacement="outside"
            name="Segundo_apellido"
            placeholder="Segundo apellido"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            errorMessage=""
            label="Direccion_Residencia"
            labelPlacement="outside"
            name="Direccion_Residencia"
            placeholder="Direccion Residencia"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="Ingrese la cedula Ciudadania"
            label="Cedula_Ciudadania*"
            labelPlacement="outside"
            name="Cedula_ciudadania"
            placeholder="Cedula Ciudadania"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="Ingrese el correo Electronico"
            label="Correo_electronico*"
            labelPlacement="outside"
            name="Correo_electronico"
            placeholder="Correo Electronico"
            type="text"/>
            
            {/* CARGO */}
            <Dropdown >
              <DropdownTrigger>
                <Button className="capitalize bg-blue-500 text-white rounded-md hover:bg-blue-900 transition" variant="bordered">
                  {cargo_seleccionado}
                </Button>
              </DropdownTrigger>
              <DropdownMenu className="bg-gray-800  text-white border-2 border-black"
                disallowEmptySelection
                aria-label="Multiple selection example"
                closeOnSelect={true}
                selectedKeys={cargos_a_elegir}
                selectionMode="single"
                variant="flat"
                onSelectionChange={set_cargos_a_elegir}
              >
                <DropdownItem key="1">Antibiotico</DropdownItem>
                <DropdownItem key="2">Cuidador</DropdownItem>
                <DropdownItem key="3">Permanente</DropdownItem>
              </DropdownMenu>
            </Dropdown>
            
            {/* TIPO SANGRE */}
            <Dropdown >
              <DropdownTrigger>
                <Button className="capitalize bg-blue-500 text-white rounded-md hover:bg-blue-900 transition" variant="bordered">
                  {tipo_sangre_seleccionado}
                </Button>
              </DropdownTrigger>
              <DropdownMenu className="bg-gray-900  border-2 border-black text-white"
                disallowEmptySelection
                aria-label="Multiple selection example"
                closeOnSelect={true}
                selectedKeys={tipos_sangre_a_elegir}
                selectionMode="single"
                variant="flat"
                onSelectionChange={set_tipos_sangre_a_elegir}
              >
                <DropdownItem key="1">0-</DropdownItem>
                <DropdownItem key="2">0+</DropdownItem>
                <DropdownItem key="3">A-</DropdownItem>
                <DropdownItem key="4">A+</DropdownItem>
                <DropdownItem key="5">B-</DropdownItem>
                <DropdownItem key="6">B+</DropdownItem>
                <DropdownItem key="7">AB-</DropdownItem>
                <DropdownItem key="8">AB+</DropdownItem>
              </DropdownMenu>
            </Dropdown>
            
            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            errorMessage=""
            label="Telefono"
            labelPlacement="outside"
            name="Telefono"
            placeholder="Telefono"
            type="text"/>
            
            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="Ingrese Nombre_Usuario Con el que ingresará a la plataforma"
            label="Nombre_Usuario***"
            labelPlacement="outside"
            name="Nombre_Usuario"
            placeholder="CONTRASEÑA_USUARIO"
            type="text"/>

            <Input
            className="mt-1 border-2 rounded-md bg-gray-200 border-black shadow-sm focus:ring-blue-500 focus:border-blue-500"
            isRequired
            errorMessage="INGRESE LA CONTRASEÑA DEL USUARIO **"
            label="Contraseña_Usuario***"
            labelPlacement="outside"
            name="Contraseña_usuario"
            placeholder="CONTRASEÑA_USUARIO"
            type="text"/>
            
            <DateInput className="bg-gray-200 border-2 border-black"
            isRequired
            label={"Fecha_nacimiento (DD/MM/YYYY)"}
            value={fecha_nacimiento}
            onChange={set_fecha_nacimiento}
            
            />


            <div  className="flex gap-2 border-2  text-white bg-blue-400 rounded-md hover:bg-blue-900 transition
            py-2  px-2">
            <Button
            className="w-full text-center"
            type="submit">
                Crear
            </Button>
            
            </div>
             <p className="bg-gray-300 font-medium text-center">{mensaje_back}</p>

            </Form>

            <div className="px-10 "></div>

            <div className="w-1/2 max-w-m flex flex-col rounded-sm">
                <div className=" w-1/2 max-w-xs border-2 border-black " >
                      {/* Actualizar Estado Contratacion */}
                      <Form className="bg-white w-full max-w-xs flex flex-col px-4"
                      onSubmit={actualizar_estado_contratacion}
                      >      
                      <h1 className="bg-gray-300 w-full text-center font-medium">Actualizar Estado Contratacion</h1>

                      {/* Seleccionar ID usuario */}
                      <Dropdown>
                          <DropdownTrigger>
                            <Button className="capitalize rounded-xl border-2 border-black  bg-blue-500 hover:bg-blue-900 transition py-4" variant="bordered">
                              {usuario_seleccionado}
                            </Button>
                          </DropdownTrigger>
                          <DropdownMenu
                            className=" border-2 border-black"
                            disallowEmptySelection
                            aria-label="Single selection example"
                            selectedKeys={usuarios_a_seleccionar}
                            selectionMode="single"
                            variant="flat"
                            onSelectionChange={set_usuario_a_seleccionar}
                          >
                            {usuarios_en_sistema.map((item)=> (
                            <DropdownItem className="w-full bg-black text-white border-2 border-white"
                            key={item[0]}>{item[1]}-{item[2]}_{item[3]}</DropdownItem>
                            
                            
                            ))}

                          </DropdownMenu>
                      </Dropdown>
                          
                      {/* Seleccionar estado de contratacion */}
                      <Dropdown>
                          <DropdownTrigger>
                            <Button className="capitalize rounded-xl border-2 border-black  bg-blue-500 hover:bg-blue-900 transition py-4" variant="bordered">
                              {estado_seleccionado}
                            </Button>
                          </DropdownTrigger>
                          <DropdownMenu
                            className=" border-2 border-black"
                            disallowEmptySelection
                            aria-label="Single selection example"
                            selectedKeys={estados_a_seleccionar}
                            selectionMode="single"
                            variant="flat"
                            onSelectionChange={set_estados_a_seleccionar}
                          >
                            {estados_contratacion.map((item)=> (
                            <DropdownItem className="w-full bg-black text-white border-2 border-white"
                            key={item[0]}>{item[1]}</DropdownItem>
                            
                            
                            ))}

                          </DropdownMenu>
                      </Dropdown>
                          
                      <div  className="flex gap-2 border-2  text-white bg-blue-400 rounded-md hover:bg-blue-900 transition
                      py-2  px-2">
                          <Button
                          className="w-full text-center"
                          type="submit">
                              Actualizar
                          </Button>
                      </div>
                       <p className="bg-gray-300 font-medium text-center">{mensaje_back}</p>
                          
                      </Form>
                </div>
                              
            <div className="w-1/2 max-w-xs border-2 border-black ">

            {/* Actualizar Estado Firma */}
            <Form
            onSubmit={actualizar_estado_firma}
            className="bg-white w-full max-w-xs flex flex-col px-4 py-2"
            >
              <h1 className="w-full bg-gray-300 font-medium text-center">Establecer Estado de la Firma</h1>
               <Dropdown>
                <DropdownTrigger>
                  <Button className="capitalize rounded-xl border-2 border-black  bg-blue-500 hover:bg-blue-900 transition py-4" variant="bordered">
                    {usuario_seleccionado}
                  </Button>
                </DropdownTrigger>
                <DropdownMenu
                  className=" border-2 border-black"
                  disallowEmptySelection
                  aria-label="Single selection example"
                  selectedKeys={usuarios_a_seleccionar}
                  selectionMode="single"
                  variant="flat"
                  onSelectionChange={set_usuario_a_seleccionar}
                >
                  {usuarios_en_sistema.map((item)=> (
                  <DropdownItem className="w-full bg-black text-white border-2 border-white"
                  key={item[0]}>{item[1]}-{item[2]}_{item[3]}</DropdownItem>


                  ))}
                  
                </DropdownMenu>
            </Dropdown>

              {/* Estado Firma */}
              <Dropdown>
                <DropdownTrigger>
                  <Button className="capitalize rounded-xl border-2 border-black  bg-blue-500 hover:bg-blue-900 transition py-4" variant="bordered">
                    {estado_firma_seleccionado}
                  </Button>
                </DropdownTrigger>
                <DropdownMenu
                  className=" border-2 border-black"
                  disallowEmptySelection
                  aria-label="Single selection example"
                  selectedKeys={estado_firma_a_elegir}
                  selectionMode="single"
                  variant="flat"
                  onSelectionChange={set_estado_firma_a_elegir}
                >
                  
                  <DropdownItem className="w-full bg-black text-white border-2 border-white"
                  key='0'>Disponible para Firma</DropdownItem>

                  <DropdownItem className="w-full bg-black text-white border-2 border-white"
                  key='1'>No Disponible para Firma</DropdownItem>                  
                  
                </DropdownMenu>
            </Dropdown>
              
            <div className="flex gap-2 border-2  text-white bg-blue-400 rounded-md hover:bg-blue-900 transition
            py-2  px-2">
                <Button
                className="w-full text-center"
                type="submit">
                    Actualizar
                </Button>
            </div>
            <p className="bg-gray-300 font-medium text-center">{mensaje_back}</p>

            </Form>
            </div>

            </div>

            </div>
        )
    }
    
    
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
    

    if(datos_recibidos_login.cargo_id!=4){  
        
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