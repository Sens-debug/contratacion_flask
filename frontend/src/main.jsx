import React from 'react';
import ReactDOM from 'react-dom/client';
import { HeroUIProvider } from '@heroui/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <HeroUIProvider>
      <BrowserRouter>
        <App />  {/* App contiene las rutas */}
      </BrowserRouter>
    </HeroUIProvider>
  </React.StrictMode>
);
