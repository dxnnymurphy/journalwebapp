import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import Select from "react-select";
import axios from "axios";

import { API_URL } from "../constants";

const options = [
  {value: "python", label: "Python"},
  {value: "django", label: "Django"},
  {value: "javascript", label: "Javascript"},
  {value: "react", label: "React"},
  {value: "css", label: "Css"},
]

class NewJournalForm extends React.Component {
  constructor() {
    super();
    this.state = {
      id: 0,
      title: "",
      url: "",
      software: "",
      notes: "",
      technologies: [],
      technologiesList: [],
    };

    this.handleMultiChange = this.handleMultiChange.bind(this);
  }

  componentDidMount() {
    if (this.props.journal) {
      const { id, title, url, software, notes, technologies, technologiesList } = this.props.journal;
      this.setState({ id, title, url, software, notes, technologies, technologiesList });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleMultiChange(option) {
    this.setState(state => {
      return {
        technologies: option
      };
    });
  }

  createJournal = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editJournal = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.id + '/', this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };




  render() {
    return (
      <Form onSubmit={this.props.journal ? this.editJournal : this.createJournal}>
        <FormGroup>
          <Label for="title">Title:</Label>
          <Input
            type="text"
            name="title"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.title)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="url">URL:</Label>
          <Input
            type="url"
            name="url"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.url)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="notes">Notes:</Label>
          <Input
            type="text"
            name="notes"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.notes)}
          />
        </FormGroup>
        <Select
          name="filters"
          placeholder="Softwares"
          value={this.state.technologies}
          options= {options}
          defaultValue={options[1]}
          onChange={this.handleMultiChange}
          isMulti
        />

        <Button style={{marginTop: "20px"}} >Send</Button>
      </Form>
    );
  }
}

export default NewJournalForm;