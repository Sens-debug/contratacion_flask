import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { Inicio_sesion } from './inicio_sesion.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <App /> */}
  <Inicio_sesion/>
  </StrictMode>,
)
