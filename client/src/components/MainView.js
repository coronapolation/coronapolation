import React, {Component} from 'react';

import Paper from "@material-ui/core/Paper";
import LineChart from "recharts/lib/chart/LineChart";
import XAxis from "recharts/lib/cartesian/XAxis";
import YAxis from "recharts/lib/cartesian/YAxis";
import CartesianGrid from "recharts/lib/cartesian/CartesianGrid";
import Tooltip from "@material-ui/core/Tooltip";
import Legend from "recharts/lib/component/Legend";
import Line from "recharts/lib/cartesian/Line";
import ResponsiveContainer from "recharts/lib/component/ResponsiveContainer"

class MainView extends Component {
    render() {
        if (this.props.store.bundeslaender) {
            return (
                <div>
                    {this.props.store.infizierte != null &&
                    <Paper style={{margin: 20, padding: 10}}>
                        <p>Fallzahlen in <span>{this.props.store.selectedBundesland}</span> im <span>{this.props.store.selectedLandkreis}</span></p>
                        <ResponsiveContainer width="100%" height={500}>
                            <LineChart data={this.props.store.infizierte}
                                   margin={{top: 20, right: 20, left: 30, bottom: 20}}>
                                <XAxis dataKey="name"/>
                                <YAxis/>
                                <CartesianGrid strokeDasharray="5 3"/>
                                <Tooltip/>
                                <Legend/>
                                <Line type="monotone" dataKey={this.props.store.selected_landkreis_id} stroke="#46467d"/>
                            </LineChart>
                        </ResponsiveContainer>
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
