import React, {Component} from 'react';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Select from "@material-ui/core/Select";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Actions from "../actions";

const selectStyle = {
    marginLeft: 20,
    minWidth: 120,
};

class TopBar extends Component {
    changedBundesland = event => {
        Actions.loadLandkreise(this.props.store, event.target.value);
    };

    changedLandkreis = event => {
        Actions.loadInfizierte(this.props.store, event.target.value);
    };

    render() {
        return (
            <AppBar color="default" style={{height: 80}}>
                <Toolbar style={{flex: 1}}>
                    <Typography variant="h4" color="inherit" style={{marginRight: 40}}>
                        Coronapolation
                    </Typography>
                    {this.props.store.bundeslaender != null &&
                    <FormControl variant="filled" style={selectStyle}>
                        <InputLabel htmlFor="bundesland-selector">Bundesland</InputLabel>
                        <Select
                            native
                            onChange={this.changedBundesland}
                            inputProps={{
                                name: 'bundesland',
                                id: 'bundesland-selector',
                            }}
                        >
                            <option aria-label="None" value=""/>
                            {
                                this.props.store.bundeslaender.map(b => {
                                    return <option value={b.id} key={b.id}>{b.name}</option>
                                })
                            }
                        </Select>
                    </FormControl>
                    }
                    {this.props.store.landkreise != null &&
                    <FormControl variant="filled" style={selectStyle}>
                        <InputLabel htmlFor="landkreis-selector">Landkreis</InputLabel>
                        <Select
                            native
                            onChange={this.changedLandkreis}
                            inputProps={{
                                name: 'landkreis',
                                id: 'landkreis-selector',
                            }}
                        >
                            <option aria-label="None" value=""/>
                            {
                                this.props.store.landkreise.map(b => {
                                    return <option value={b.id} key={b.id}>{b.name}</option>
                                })
                            }
                        </Select>
                    </FormControl>
                    }
                </Toolbar>
            </AppBar>
        );
    }
}

export default TopBar;
