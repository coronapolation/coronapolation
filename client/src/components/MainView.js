import React, {Component} from 'react';

import Actions from '../actions';
import Paper from "@material-ui/core/Paper";

class MainView extends Component {
    componentDidMount() {
        Actions.loadBundeslaender(this.props.store);
    }

    render() {
        if (this.props.store.bundeslaender) {
            return (
                <Paper style={{padding: 40, margin: 40}}>
                    <pre>{JSON.stringify(this.props.store.bundeslaender, null, 4)}</pre>
                </Paper>
            );
        } else {
            return (<span/>);
        }
    }
}

export default MainView;
