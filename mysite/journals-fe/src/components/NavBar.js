import { Component } from "react";
import Navbar from 'react-bootstrap/Navbar';
import NewJournalModal from "./NewJournalModal";
import { Nav, Container } from "react-bootstrap";
import axios from "axios";
import { API_URL } from "../constants";

class NavBar extends Component {
    resetState = () => {
        axios.get(API_URL).then(res => this.setState({ journals: res.data }));
    };
    loginSuccess = () => {
        axios.get(API_URL + 'loginsuccess/').then(res => this.setState({ journals: res.data }))
    }
    render() {
        return (
            <div className="navbar">
                <Navbar bg="light" expand="lg" fixed="top">
                    <Container fluid>
                        <img
                            src="https://www.solirius.com/img/logo.png"
                            alt="soliriuslogo"
                            width="125"
                            className="img-thumbnail"
                        />
                        <Navbar.Toggle aria-controls="navbarScroll" />
                        <Navbar.Collapse id="navbarScroll">
                            <Nav
                                className="me-auto my-2 my-lg-0"
                                style={{ maxHeight: '100px' }}
                                navbarScroll
                            >
                                <Nav.Link href=""></Nav.Link>
                                <NewJournalModal create={true} resetState={this.resetState} />
                                <Nav.Link href="/home/">Logout</Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
            </div>
        );
    }
}

export default NavBar;