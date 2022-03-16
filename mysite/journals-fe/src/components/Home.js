import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import JournalList from "./JournalList";
import LoginModal from "./LoginModal";
import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    journals: [],
    login: false
  };
  loginSuccess = () => {
    this.setState({login: true});
  };
  getJournals = (data) => {
    if (data) {
      this.setState({journals: data})
    }
    else {
      axios.get(API_URL).then(res => this.setState({ journals: res.data }));
    }
  }

  componentDidMount() {
    this.resetState();
  }


  

  resetState = () => {
    this.getJournals();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <LoginModal 
          resetState={this.resetState}
          loginSuccess={this.loginSuccess} />
        <Row>
          <Col>
            <JournalList
              journals={this.state.journals}
              login={this.state.login}
              resetState={this.resetState}
              getJournals={this.getJournals}
            />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;