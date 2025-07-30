import React from 'react'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Layout from "./layout.tsx";
import Portfolio from "./pages/portfolio.tsx"
import Planejamento from "./pages/planejamento.tsx"
import Tecnico from './pages/tecnico.tsx'
import Test from './pages/test.tsx'


const AppRoutes: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index element={<Portfolio/>}/>
                    <Route path={"portfolio"} element={<Portfolio/>}/>
                    <Route path={"test"} element={<Test/>}/>
                    <Route path={"planejamento"} element={<Planejamento/>}/>
                    <Route path={"tecnico"} element={<Tecnico/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default AppRoutes