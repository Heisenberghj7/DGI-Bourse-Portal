import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import Dashboard from "./Dashboard";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
      </div>
    );
  }
}


const appDiv = document.getElementById("app");
render(<App />, appDiv);

// const HomePageDiv = document.getElementById("HomePage");
// render(<App />, HomePageDiv);