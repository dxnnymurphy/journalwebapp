import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, ModalBody } from "reactstrap";
import GoogleLogin from "react-google-login";

class LoginModal extends Component {
  state = {
    modal: true
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };
  fail = () => {

  }
  success = () => {
    this.props.loginSuccess();
    this.toggle();
  }


  render() {
    var title = "Please Login to View Journals";

    return (
      <Fragment>
        <Modal isOpen={this.state.modal} toggle={this.toggle} backdrop="static">
          <ModalHeader>{title}</ModalHeader>

          <ModalBody>
          <GoogleLogin
                                    clientId='742468814782-tuu4still9uush726lmavqig2bj1n75j.apps.googleusercontent.com'
                                    buttonText="LOGIN WITH GOOGLE"
                                    onSuccess={this.success}
                                    onFailure={this.fail}
                                />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default LoginModal;