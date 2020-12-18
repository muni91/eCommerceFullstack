import React from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import PrivateRoute from './components/auth/helper.js/PrivateRoute';
import Home from './components/core/Home';
import Signup from './components/user/Signup';

const Routes = () => {
    return(
        <Router>
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/signup" exact component={Signup} />
                {/* <PrivateRoute path="/user/dashboard" exact component ={} /> */}
            </Switch>
        </Router>
    );
};

export default Routes;