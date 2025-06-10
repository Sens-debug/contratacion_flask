import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {BrowserRouter as Router , Routes, Route} from 'react-router-dom'
// import './index.css'
// import '../src/index.css'

import Panel_usuario from './modulos/Panel_usuario.jsx'
import { Formulario_login } from './modulos/Inicio_sesion.jsx'

function App(){
  return(
      <Routes>
        <Route path='/' element={<Formulario_login/>}></Route>
        <Route path='/app' element={<Panel_usuario/>}></Route>
        {/* <Route path='/'></Route> */}
      </Routes>    
  )
}

export default App