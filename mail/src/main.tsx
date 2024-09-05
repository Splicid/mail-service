import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Navbar from './components/navbar.tsx'
import Main_Content from './components/main_content.tsx'
import Signup from './components/signup.tsx'
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import './index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Navbar />
    <Router>
      <Routes>
        <Route path="/" element={<Main_Content />} />
        {/* <Route path="/about" element={<About />} /> */}
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </Router>
  </StrictMode>,
)
