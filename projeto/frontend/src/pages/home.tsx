import React, { useState } from 'react';
import { Box, Typography, Tabs, Tab } from '@mui/material';
import Portfolio from "./portfolio.tsx";


type ViewType = 'portfolio' | 'planejamento' | 'tecnico';


const Planejamento: React.FC = () => <Typography>Conteúdo da página de Planejamento.</Typography>;
const Tecnico: React.FC = () => <Typography>Conteúdo da página Técnica.</Typography>;


const Home: React.FC = () => {
    const [activeView, setActiveView] = useState<ViewType>('portfolio');


    const handleTabChange = (_event: React.SyntheticEvent, newValue: ViewType) => {
        setActiveView(newValue);
    };

    return (
        <Box sx={{ width: '100%', p: 3, textAlign: 'center' }}>
            <Typography variant="h6" sx={{ mb: 20 }}>
                Magaiver / FORUM Investimentos @ 2025
            </Typography>

            <Tabs value={activeView} onChange={handleTabChange} centered>
                <Tab label="PORTFOLIO" value="portfolio" />
                <Tab label="PLANEJAMENTO" value="planejamento" />
                <Tab label="TECNICO" value="tecnico" />
            </Tabs>

            <Box sx={{ mt: 4 }}>
                <Box style={{ display: activeView === 'portfolio' ? 'block' : 'none' }}>
                    <Portfolio />
                </Box>
                <Box style={{ display: activeView === 'planejamento' ? 'block' : 'none' }}>
                    <Planejamento />
                </Box>
                <Box style={{ display: activeView === 'tecnico' ? 'block' : 'none' }}>
                    <Tecnico />
                </Box>
            </Box>
        </Box>
    );
};

export default Home;