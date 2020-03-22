import React, {Component} from 'react';

import Paper from "@material-ui/core/Paper";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';

function createData(name, peakDate, peakInfections, overallInfected) {
    return { name, peakDate, peakInfections, overallInfected };
}
const rows = [
    createData('Scenario A', "12-05-2020", 13000, 234000),
    createData('Scenario B', "12-05-2020", 33000, 123456),
];

class DataView extends Component {


    render() {
        if (this.props.store.bundeslaender) {
            return (
                <div>
                    {this.props.store.infizierte != null &&
                    <Paper style={{padding: 10, margin: 20}}>
                        <p>Possible scenarios for <span>{this.props.store.selected_landkreis_name}</span></p>
                        <TableContainer component={Paper}>
                            <Table aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Scenario</TableCell>
                                        <TableCell align="right">Peak date</TableCell>
                                        <TableCell align="right">Infection peak</TableCell>
                                        <TableCell align="right">Overall infected</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {rows.map(row => (
                                        <TableRow key={row.name}>
                                            <TableCell component="th" scope="row">
                                                {row.name}
                                            </TableCell>
                                            <TableCell align="right">{row.peakDate}</TableCell>
                                            <TableCell align="right">{row.peakInfections}</TableCell>
                                            <TableCell align="right">{row.overallInfected}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </TableContainer>
                        <p>Scenario details:</p>
                        <ExpansionPanel>
                            <ExpansionPanelSummary
                                aria-controls="panel1a-content"
                                id="panel1a-header"
                            >
                                <Typography>Scenario A</Typography>
                            </ExpansionPanelSummary>
                            <ExpansionPanelDetails>
                                <Typography>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                                    sit amet blandit leo lobortis eget.
                                </Typography>
                            </ExpansionPanelDetails>
                        </ExpansionPanel>
                        <ExpansionPanel>
                            <ExpansionPanelSummary
                                aria-controls="panel2a-content"
                                id="panel2a-header"
                            >
                                <Typography>Scenario B</Typography>
                            </ExpansionPanelSummary>
                            <ExpansionPanelDetails>
                                <Typography>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                                    sit amet blandit leo lobortis eget.
                                </Typography>
                            </ExpansionPanelDetails>
                        </ExpansionPanel>
                    </Paper>
                    }
                </div>
            );
        } else {
            return (<span/>);
        }
    }
}

export default DataView;