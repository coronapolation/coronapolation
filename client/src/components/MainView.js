import React, {Component} from 'react';

import Paper from "@material-ui/core/Paper";
import XAxis from "recharts/lib/cartesian/XAxis";
import YAxis from "recharts/lib/cartesian/YAxis";
import CartesianGrid from "recharts/lib/cartesian/CartesianGrid";
import Tooltip from "recharts/lib/component/Tooltip";
import Legend from "recharts/lib/component/Legend";
import Line from "recharts/lib/cartesian/Line";
import ResponsiveContainer from "recharts/lib/component/ResponsiveContainer"
import Bar from "recharts/lib/cartesian/Bar";
import ComposedChart from "recharts/lib/chart/ComposedChart";

class MainView extends Component {
    render() {
        if (this.props.store.bundeslaender) {
            return (
                <div>
                    {this.props.store.infizierte != null && this.props.store.neuinfizierte != null && this.props.store.graphData != null &&
                    <Paper style={{padding: 10, margin: 20}}>
                        <p>Fallzahlen in <span>{this.props.store.selected_bundesland}</span> im <span>{this.props.store.selected_landkreis_name}</span></p>
                        <ResponsiveContainer width="100%" height={500}>
                            <ComposedChart data={this.props.store.graphData}
                                   margin={{top: 50, right: 50, left: 50, bottom: 50}}>
                                <XAxis dataKey="name"/>
                                <YAxis/>
                                <CartesianGrid strokeDasharray="1 1"/>
                                <Tooltip/>
                                <Legend/>
                                <Line type="monotone" dataKey={this.props.store.selected_landkreis_name + ' SUMME'} stroke="#8884d8" activeDot={{ r: 8 }}/>
                                <Bar type="monotone" dataKey={this.props.store.selected_landkreis_name + ' NEU'} fill="#82ca9d"/>
                            </ComposedChart>
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
