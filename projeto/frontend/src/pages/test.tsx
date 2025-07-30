import React, { useState } from 'react';
import { Box, Typography, Tabs, Tab } from '@mui/material';
import Portfolio from "./portfolio.tsx"; // Assuming this is your component

// --- Type Definitions ---
type ViewType = 'portfolio' | 'planejamento' | 'tecnico';

// --- Dummy components for example ---
const Planejamento: React.FC = () => <Typography>Conteúdo da página de Planejamento.</Typography>;
const Tecnico: React.FC = () => <Typography>Conteúdo da página Técnica.</Typography>;

// --- Main Dashboard Component ---
const Test: React.FC = () => {
    const [activeView, setActiveView] = useState<ViewType>('portfolio');

    // Any state that needs to be shared between components lives here.
    // Let's assume Portfolio.tsx manages its own state for this example.

    const handleTabChange = (event: React.SyntheticEvent, newValue: ViewType) => {
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
                {/* Render all components, but use CSS to show/hide them */}
                {/* This preserves the state of each component */}
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

export default Test;