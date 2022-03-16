import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewJournalForm from "./NewJournalForm";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPenToSquare} from "@fortawesome/free-solid-svg-icons";

class NewJournalModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Editing Journal";
    var button =         <FontAwesomeIcon icon={faPenToSquare} onClick={() => this.toggle()}/>
    if (create) {
      title = "Creating New Journal";

      button = (
        <Button
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "100px", marginLeft: "30px", marginRight: "20px"}}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewJournalForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              journal={this.props.journal}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewJournalModal;