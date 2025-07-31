import React from 'react'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Layout from "./layout.tsx";
import Portfolio from "./pages/portfolio.tsx"
import Planejamento from "./pages/planejamento.tsx"
import Tecnico from './pages/tecnico.tsx'
import Home from './pages/home.tsx'


const AppRoutes: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index element={<Home/>}/>
                    <Route path={"portfolio"} element={<Portfolio/>}/>
                    <Route path={"planejamento"} element={<Planejamento/>}/>
                    <Route path={"tecnico"} element={<Tecnico/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default AppRoutes