import React, {Component} from 'react';

import Actions from '../actions';
import Paper from "@material-ui/core/Paper";
import Select from "@material-ui/core/Select";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import LineChart from "recharts/lib/chart/LineChart";
import XAxis from "recharts/lib/cartesian/XAxis";
import YAxis from "recharts/lib/cartesian/YAxis";
import CartesianGrid from "recharts/lib/cartesian/CartesianGrid";
import Tooltip from "@material-ui/core/Tooltip";
import Legend from "recharts/lib/component/Legend";
import Line from "recharts/lib/cartesian/Line";

const selectStyle = {
    margin: 20,
    minWidth: 120,
};

class MainView extends Component {
    componentDidMount() {
        Actions.loadBundeslaender(this.props.store);
    }

    changedBundesland = event => {
        Actions.loadLandkreise(this.props.store, event.target.value);
    };

    changedLandkreis = event => {
        Actions.loadInfizierte(this.props.store, event.target.value);
    };

    render() {
        if (this.props.store.bundeslaender) {
            return (
                <div>
                    <Paper style={{padding: 10, margin: 20}}>
                        <FormControl style={selectStyle}>
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
                        {this.props.store.landkreise != null &&
                        <FormControl style={selectStyle}>
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
                    </Paper>
                    {this.props.store.infizierte != null &&
                    <Paper style={{padding: 10, margin: 20}}>
                        <LineChart width={800} height={600} data={this.props.store.infizierte}
                                   margin={{top: 50, right: 50, left: 50, bottom: 50}}>
                            <XAxis dataKey="name"/>
                            <YAxis/>
                            <CartesianGrid strokeDasharray="3 3"/>
                            <Tooltip/>
                            <Legend/>
                            <Line type="monotone" dataKey={this.props.store.selected_landkreis_id} stroke="#46467d"/>
                        </LineChart>
                    </Paper>
                    }
                </div>
            );
        } else {
            return (<span/>);
        }
    }
}

export default MainView;
