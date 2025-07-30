import * as React from 'react';
import { useLocation } from 'react-router-dom';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';;
import Typography from '@mui/material/Typography';

interface LinkTabProps {
    label?: string;
    link?: string;
    selected?: boolean;
}

function LinkTab(props: LinkTabProps) {
    return (
        <Tab
            component="a"
            aria-current={props.selected && 'page'}
            {...props}
        />
    );
}

export default function NavTabs(): React.ReactElement {
    const location = useLocation();

    let currentTab = 0;
    if (location.pathname.startsWith('/planejamento')) {
        currentTab = 1;
    } else if (location.pathname.startsWith('/tecnico')) {
        currentTab = 2;
    }

    return (
        <h1>
        {/*    <Box sx={{ width: '100%', py: 2, textAlign: 'center', mt: 10 }}>*/}
        {/*        <Typography component="h2">*/}
        {/*            FORUM Investimentos @ 2025*/}
        {/*        </Typography>*/}
        {/*    </Box>*/}
        {/*<Box sx={{ width: '100%' }}>*/}
        {/*    <Tabs*/}
        {/*        value={currentTab}*/}
        {/*        // Add the centered prop here*/}
        {/*        centered*/}
        {/*        aria-label="nav tabs example"*/}
        {/*        role="navigation"*/}
        {/*        TabIndicatorProps={{*/}
        {/*            sx: {*/}
        {/*                bottom: 'auto',*/}
        {/*                top: 0,*/}
        {/*            },*/}
        {/*        }}*/}
        {/*    >*/}
        {/*        <LinkTab label="Portfolio" link="/portfolio" />*/}
        {/*        <LinkTab label="Planejamento" link="/planejamento" />*/}
        {/*        <LinkTab label="Tecnico" link="/tecnico" />*/}
        {/*    </Tabs>*/}
        {/*</Box>*/}
        {/*</h1>*/}
        </h1>
    );
}