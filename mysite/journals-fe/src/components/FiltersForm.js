import React from "react";
import { Button, Form, FormGroup, Input } from "reactstrap";
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

class FiltersForm extends React.Component {
  constructor() {
    super();
    this.state = {
      term: "",
      techDicts: [],
      techList: []
    };

    this.handleMultiChange = this.handleMultiChange.bind(this);
  }

  componentDidMount() {
    if (this.props.journal) {
      const { term } = this.props.journal;
      this.setState({ term });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createJournal = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  applyFilter = e => {
    e.preventDefault();
    axios.post(API_URL + 'filter/', this.state).then(res => {
      this.props.getJournals(res.data);
      this.props.toggle();
    });
  };

  handleMultiChange(option) {
    this.setState(state => {
      return {
        techList: option
      };
    });
  }


  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.applyFilter}>
         <FormGroup>
          <Input
            type="text"
            name="term"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.title)}
          />
        </FormGroup>
        <h6>Select Relevant Softwares:</h6>
        <Select
          name="filters"
          placeholder="Filters"
          value={this.state.techLixst}
          options= {options}
          onChange={this.handleMultiChange}
          isMulti
        />
        <Button style={{marginTop: "20px"}}  >Apply Filters</Button>
      </Form>
    );
  }
}

export default FiltersForm;