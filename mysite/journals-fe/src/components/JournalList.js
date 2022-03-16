import React, { Component } from "react";
import { Table, Button } from "reactstrap";
import NewJournalModal from "./NewJournalModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";
import FiltersModal from "./FiltersModal";

class JournalList extends Component {
  reset = () => {
    this.props.getJournals();
  }
  render() {
    const journals = this.props.journals;
    const login = this.props.login;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Title</th>
            <th>URL</th>
            <th>Software</th>
            <th>Notes</th>
            <th><FiltersModal
                    resetState={this.props.resetState}
                    getJournals={this.props.getJournals}
                  /></th>
            <th><Button onClick={this.reset} style={{marginLeft: '10px'}}>Reset</Button></th>
          </tr>
        </thead>
        <tbody>
          {!journals || journals.length <= 0 || login === false ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Oops, no one here yet</b>
              </td>
            </tr>
          ) : (
            journals.map(journal => (
              <tr key={journal.id}>
                <td>{journal.title}</td>
                <td>{journal.url}</td>
                <td>{journal.technologiesList.toString()}</td>
                <td>{journal.notes}</td>
                <td align="center">
                  <NewJournalModal
                    create={false}
                    journal={journal}
                    resetState={this.props.resetState}
                  />
                </td>
                <td align="center">
                <ConfirmRemovalModal
                    id={journal.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default JournalList;