import React, { Component } from "react";

class Header extends Component {
    render() {
        const mystyle = {
            color: "blue",
            padding: "20px",
            fontFamily: "Arial",
            margin: "50px"
          };
        return (
            <div className="text-center">
                <h1 style = {mystyle}>Journals Web App</h1>
            </div>
        );
    }
}

export default Header;