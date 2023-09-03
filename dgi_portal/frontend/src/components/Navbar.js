import React, { Component } from "react";
import { render } from "react-dom";

export default class Navbar extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
                <nav id="navbar" className="navbar">
                        <ul>
                            <li><a class="active " href="index.html">Home</a></li>
                            <li><a href="Dashboard.html">Dashboard</a></li>
                            <li><a href="Actionnaire.html">Actionnaire</a></li>
                            <li><a href="Companies.html">Companies</a></li>
                            <li><a href="Publications.html">Publications</a></li>
                            <li class="dropdown"><a href="#"><span>Numbers</span> <i class="bi bi-chevron-down"></i></a>
                            <ul>
                                <li><a href="chiffresCle.html">Chiffres clés</a></li>
                                <li><a href="Ratio.html">Ratio</a></li>
                                <li><a href="Dividend.html">Dividend</a></li>
                                <li><a href="Retourner.html">Retourner</a></li>
                            </ul>
                            </li>
                            <li><a href="contact.html">Contact Us</a></li>
                        </ul>
                       <i className="bi bi-list mobile-nav-toggle"></i>
                </nav>
            </div>
    );
  }
}

ReactDOM.render(<Navbar />, document.getElementById("navbar_div"));
