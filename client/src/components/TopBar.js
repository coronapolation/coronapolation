import React from 'react';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const TopBar = () => {
    let title = 'Coronapolation';
    return (
        <AppBar color="default">
            <Toolbar>
                <Typography variant="h5" color="inherit" style={{flex: 1}}>
                    {title}
                </Typography>
            </Toolbar>
        </AppBar>
    );
};

export default TopBar;
