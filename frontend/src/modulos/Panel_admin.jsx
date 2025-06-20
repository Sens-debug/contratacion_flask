import { useState,useEffect } from "react";

const [cargoIdSolicitante,setCargoIdSolicitante] = useState()
const uri_flask = import.meta.env.VITE_URL_SERVIDOR

useEffect(()=>{
    const comprobacionCargo = async() =>{
        const response =await fetch(uri_flask+"/obtener_cargo_id",{
            method:'POST',
            credentials:'include',
            headers:{'Content-Type':'application/json'

            },
        }
        );
        const data = await response.json()
        setCargoIdSolicitante(data.cargo_id)
    }
    comprobacionCargo()
},[])

if(cargo_id==4){
      async function traerListaUsuarios(e) {
        e.preventDefault();
        fetch(uri_flask+"/traer_todos_usuarios")
        .then(response=>response.json())
        .then(data =>{set_lista_usuarios(data.usuarios);console.log(data.usuarios)})
        .catch(error=> console.log(error));
        
      }
    
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
          <div className="bg-gray-500 w-full h-full  ">
              {/*Formulario Creacion Usuario  */}
            <Form
            className="min-w-1/3 max-w-1/2  h-full flex flex-col gap-4 bg-white"
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

             {/* Empresa */}
            <Select
            className="border-2 mb-2"
            isRequired
            label="Empresa"
            labelPlacement="outside"
            name="empresa"
            placeholder="Seleccione Empresa"
            onSelectionChange={set_empresa}>
              <SelectItem className="bg-white w-1/2  border-2" key="1">IPS TID</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="2">SU ASESORIA</SelectItem>
            </Select>
            
            {/* CARGO */}         
            <Select
            className="border-2 mb-2 overflow-y-auto"
            isRequired
            label="Cargo"
            labelPlacement="outside"
            placeholder="Seleccione Cargo"
            name = "cargo"
            onSelectionChange={set_cargos_a_elegir}
            >
              <SelectItem className="bg-white  border-2" key="1">Antibiotico</SelectItem>
              <SelectItem className="bg-white  border-2" key ="2">Cuidador</SelectItem>
              <SelectItem className="bg-white  border-2" key="3">Permanente</SelectItem>
              <SelectItem className="bg-white  border-2" key="4">AuditorContatacion</SelectItem>
              <SelectItem className="bg-white  border-2" key="5">Nutricionista</SelectItem>
              <SelectItem className="bg-white  border-2" key="6">Psicologo</SelectItem>
              <SelectItem className="bg-white  border-2" key="7">Terapeuta Fisico</SelectItem>
              <SelectItem className="bg-white  border-2" key="8">Terapeuta Ocupacional</SelectItem>
              <SelectItem className="bg-white  border-2" key="9">Terapeuta Respiratorio</SelectItem>
              <SelectItem className="bg-white  border-2" key="10">Fonoaudiologo</SelectItem>
              <SelectItem className="bg-white  border-2" key="11">Medico General</SelectItem>

            </Select>
            
            {/* TIPO SANGRE */}
            <Select
            className="border-2 mb-2"
            isRequired
            label="Tipo de Sangre"
            labelPlacement="outside"
            name="tipo_sangre"
            placeholder="Seleccione Tipo Sangre"
            onSelectionChange={set_tipos_sangre_a_elegir}>
              <SelectItem className="bg-white w-1/2  border-2" key="1">0-</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="2">0+</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="3">A-</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="4">A+</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="5">B-</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="6">B+</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="7">AB-</SelectItem>
              <SelectItem className="bg-white w-1/2  border-2" key="8">AB+</SelectItem>
            </Select>
            
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

            <div className="min-w-2/3 max-w-full flex flex-col rounded-sm">
                <div className=" w-1/2 max-w-xs border-2 border-black " >
                      {/* Actualizar Estado Contratacion */}
                      <Form className="bg-white min-w-full max-w-1/2 flex flex-col px-4"
                      onSubmit={actualizar_estado_contratacion}
                      >      
                      <h1 className="bg-gray-300 w-full text-center font-medium">Actualizar Estado Contratacion</h1>

                      {/* Seleccionar ID usuario */}
                      <Select
                      className="border-2 mb-2"
                      isRequired
                      label="Usuario"
                      labelPlacement="outside"
                      name="id_usuario"
                      placeholder="Seleccione Usuario"
                      selectedKeys={[usuario_seleccionado]}
                      onSelectionChange={set_usuario_a_seleccionar}
                      >
                        {usuarios_en_sistema.map((item)=>(
                          <SelectItem 
                          className="bg-white border-2  overflow-y-auto" 
                          key={item[0]}
                          textValue={item[1]+ "  "+item[2]+" CC"+item[3]}>
                            {item[1]} {item[2]} CC{item[3]}
                            </SelectItem>
                        ))}

                      </Select>
                          
                      {/* Seleccionar estado de contratacion */}                          
                        <Select
                        className="border-2 mb-2 "
                        isRequired
                        label="Seleccione Estado Contratacion"
                        labelPlacement="outside"
                        onSelectionChange={set_estados_a_seleccionar}
                        >
                          {estados_contratacion.map((item)=>(
                            <SelectItem className="bg-white border-2 capitalize" key={item[0]}
                            textValue={item[1]}>{item[1]}</SelectItem>
                          ))}
                        </Select>
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
              
              {/* Seleccionar ID usuario */}
              <Select
              className="border-2 mb-2"
              isRequired
              label="Usuario"
              labelPlacement="outside"
              name="id_usuario"
              placeholder="Seleccione Usuario"
              selectedKeys={[usuario_seleccionado]}
              onSelectionChange={set_usuario_a_seleccionar}
              >
                {usuarios_en_sistema.map((item)=>(
                  <SelectItem 
                  className="bg-white border-2  overflow-y-auto" 
                  key={item[0]}
                  textValue={item[1]+ "  "+item[2]+" CC"+item[3]}>
                    {item[1]} {item[2]} CC{item[3]}
                    </SelectItem>
                ))}
                
              </Select>

              {/* Estado Firma */}
            <Select
            className="border-2 mb-2"
            isRequired
            label="Seleccione el Estado de Firma"
            labelPlacement="outside"
            name = "estado_firma"
            placeholder="---"
            onSelectionChange={set_estado_firma_a_elegir}>
              <SelectItem  className=" bg-white border-2 overflow-y-auto" key="0">Disponible Para La firma</SelectItem>
              <SelectItem  className=" bg-white border-2 overflow-y-auto" key="1">No Disponible Para La firma</SelectItem>
            </Select>
              
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

                <button
                onClick={traerListaUsuarios}>Traer Usuarios</button>

                <table className="bg-white border-2">
                  <thead>
                    <tr>
                      <th className="border-2">Nombre Completo</th>
                      <th className="border-2">Cedula</th>
                      <th className="border-2">Usuario</th>
                      <th className="border-2">Contraseña</th>
                      <th className="border-2">Empresa</th>
                      <th className="border-2">Firmó</th>
                    </tr>
                  </thead>
                  <tbody>
                  {lista_usuarios.map((usuario)=>(
                    <tr>
                      <td className="border-2 text-center" key="1">{usuario[0]}</td>
                      <td className="border-2 text-center" key="2">{usuario[1]}</td>
                      <td className="border-2 text-center" key="3">{usuario[2]}</td>
                      <td className="border-2 text-center" key="4">{usuario[3]}</td>
                      <td className="border-2 text-center" key="4">{usuario[4]}</td>
                      <td className="border-2 text-center" key="5">{usuario[5] ==0? 'No':'Si'}</td>
                    </tr>
                  ))}
                  </tbody>
                </table>
            </div>

            </div>
        )
    }