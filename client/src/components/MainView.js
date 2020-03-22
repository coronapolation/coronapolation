import React, {Component} from 'react';

import Paper from "@material-ui/core/Paper";
import LineChart from "recharts/lib/chart/LineChart";
import XAxis from "recharts/lib/cartesian/XAxis";
import YAxis from "recharts/lib/cartesian/YAxis";
import CartesianGrid from "recharts/lib/cartesian/CartesianGrid";
import Tooltip from "@material-ui/core/Tooltip";
import Legend from "recharts/lib/component/Legend";
import Line from "recharts/lib/cartesian/Line";
import Bar from "recharts/lib/cartesian/Bar";

class MainView extends Component {
    render() {
        if (this.props.store.bundeslaender) {
            return (
                <div>
                    {this.props.store.infizierte != null && this.props.store.neuinfizierte != null && this.props.store.graphData != null &&
                    <Paper style={{padding: 10, margin: 20}}>
                        <LineChart width={800} height={600} data={this.props.store.graphData}
                                   margin={{top: 50, right: 50, left: 50, bottom: 50}}>
                            <XAxis dataKey="name"/>
                            <YAxis/>
                            <CartesianGrid strokeDasharray="5 3"/>
                            <Tooltip/>
                            <Legend/>
                            <Line dataKey={this.props.store.selected_landkreis_name + ' SUMME'} stroke="#46467d"/>
                            <Line dataKey={this.props.store.selected_landkreis_name + ' NEU'} fill="#46467d"/>
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
