import React, { Component } from 'react';
import '../index.css';
import axios from 'axios';

class Landing extends Component {
    constructor() {
        super();
        this.state = {
            students: []
        }
    }

    componentDidMount() {
        axios.get('http://localhost:8000/api/students/')
            .then(res => this.setState({ students: res.data }))

    }

    renderTable() {
        return this.state.students.map((student, key) => {
            const { id, name, subj1, subj2, subj3 } = student;
            return (
                <tr key={id}>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{subj1}</td>
                    <td>{subj2}</td>
                    <td>{subj3}</td>
                </tr>
            )
        })
    }

    render() {
        return (
            <div className="wrapper ">
                <div className="heading">
                    <p>Attendence</p>
                </div>
                <div className="table">
                    <table className="centered striped">
                        <thead>
                            <tr>
                                <th>Roll No</th>
                                <th>Name</th>
                                <th>Subj-1</th>
                                <th>Subj-2</th>
                                <th>Subj-3</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.renderTable()}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}

export default Landing;