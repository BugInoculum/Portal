// frontend/src/App.js

import React, { Component } from "react";
import Root from "./Root"; // <------------- new import
import { Route, Switch } from "react-router-dom"; // <--- remove BrowserRouter
import Home from "./components/Home";
import Signup from "./components/signup/Signup";
import Login from "./components/login/Login";
import Dashboard from "./components/dashboard/Dashboard";
import { ToastContainer } from "react-toastify";
import axios from "axios";
import requireAuth from "./utils/RequireAuth";

axios.defaults.baseURL = "http://127.0.0.1:8000";



class App extends Component {
  render() {
    return (
      <div>
        <Root> {/* replace BrowserRouter with Root */}
          <Switch>
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <Route path="/dashboard" component={Dashboard} />
            <Route exact path="/" component={Home} />
            <Route path="*">Ups</Route>
            <Route path="/dashboard" component={requireAuth(Dashboard)} />
          </Switch>
        </Root> {/* replace BrowserRouter with Root */}
        <ToastContainer hideProgressBar={true} newestOnTop={true} />
      </div>
    );
  }
}




export default App;