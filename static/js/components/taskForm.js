import React from 'react';
import { Button, Table, Form } from 'semantic-ui-react'
import { createTask } from '../services/taskService'
import DayPickerInput from 'react-day-picker/DayPickerInput';
import 'react-day-picker/lib/style.css';

export class TaskForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: '',
            description: '',
            deadline: new Date()
        };
    }

    formatDate = (date) => {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) month = '0' + month;
        if (day.length < 2) day = '0' + day;

        return [year, month, day].join('-');
    }

    handleChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    onDayChange = date => {
        this.setState({ deadline: date });
    }

    handleSubmit = event => {
        event.preventDefault();
        const task = {
            title: this.state.title,
            category: this.props.categoryID,
            description: this.state.description,
            deadline: this.formatDate(this.state.deadline)
        };
        createTask(task).then(t => {
            this.props.updateTasks();
        });
        this.setState({
            title: '',
            description: '',
            deadline: new Date()
        });
    }

    render() {
        const styles = {
            tableRow: { backgroundColor: 'lightgray' },
            button: { backgroundColor: 'darkblue', color: 'white' }
        };

        return (
            <Table.Row style={styles.tableRow}>
                <Table.Cell>
                    <Button type="action" style={styles.button} onClick={this.handleSubmit}>Add task</Button>
                </Table.Cell>
                <Table.Cell>
                    <Form onChange={this.handleChange} onSubmit={this.handleSubmit}>
                        <Form.Input label="Title" value={this.state.title} name="title" type="text" />
                        <Form.Input label="Description" value={this.state.description} name="description" type="text" />
                        <DayPickerInput label="Deadline" value={this.state.deadline} onDayChange={this.onDayChange} />
                    </Form>
                </Table.Cell>
                <Table.Cell />
                <Table.Cell />
            </Table.Row >
        )
    }
}