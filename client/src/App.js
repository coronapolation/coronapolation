import React, {Component} from 'react';

import Store from './store';

import TopBar from './components/TopBar';
import MainView from "./components/MainView";
import Actions from "./actions";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            store: new Store()
        };
        this.state.store.subscribe(s => {
            this.setState({store: s});
        });
        this.state.store.subscribe(s => {
            console.log(s);
        });
    }

    componentDidMount() {
        Actions.loadBundeslaender(this.state.store);
    }

    render() {
        return (
            <div style={{width: '100%', minHeight: '100%', display: 'flex'}}>
                <TopBar store={this.state.store}/>
                <div style={{width: '100%', marginTop: 84, marginBottom: 20}}>
                    <MainView store={this.state.store}/>
                </div>
            </div>
        );
    }
}

export default App;
