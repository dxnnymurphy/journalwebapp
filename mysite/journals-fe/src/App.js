import React, { Component, Fragment } from "react";
import './App.css';
import Header from "./components/Header";
import Home from "./components/Home";
import NavBar from "./components/NavBar"
class App extends Component {
  render() {
    return (
      <Fragment>
        <NavBar/>
        <Header />
        <Home/>
      </Fragment>
    );
  }
}

export default App;
