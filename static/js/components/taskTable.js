import React from 'react';
import { Table, Form, Button } from 'semantic-ui-react'
import { deleteTask, editTask } from '../services/taskService'
import { TaskForm } from './taskForm'

export class TaskTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedCategory: null,
            tasks: [],
            editTask: null
        };
    }

    componentDidMount() {
        this.setState({
            tasks: this.props.tasks,
            selectedCategory: this.props.selectedCategory
        }, function () {
            this.props.updateTasks();
        });
    }

    componentWillReceiveProps(nextProps) {
        if (this.state.selectedCategory.id !== nextProps.selectedCategory.id) {
            this.closeEdit();
        }
        this.setState({
            selectedCategory: nextProps.selectedCategory,
            tasks: nextProps.tasks
        });
    }

    handleTaskCheck = (e, index) => {
        const id = index.value;
        if (id) {
            deleteTask(index.value)
                .then(res => {
                    this.props.updateTasks();
                })
                .catch(err => {
                    return err;
                })
        }
    }

    closeEdit = () => {
        this.setState({ editTask: null });
    }

    handleFormChange = e => {
        // causing deselection in input fields...
        let task = this.state.editTask;
        task[e.target.name] = e.target.value
        this.setState({
            editTask: task
        });
    }

    saveEdit = () => {
        const task = this.state.editTask;
        editTask(task)
            .then(res => {
                this.closeEdit();
                this.props.updateTasks();
            })
            .catch(err => {
                return err;
            })
    }

    onEditClick = (e, index) => {
        const id = index.value;
        if (id) {
            const task = this.state.tasks.find(t => t.id == id);
            this.setState({
                editTask: {
                    id: task.id,
                    title: task.title,
                    description: task.description,
                    category: task.category.id,
                    deadline: task.deadline
                }
            });
        }
    }

    render() {
        const styles = {
            table: { paddingTop: '1em' },
            tableHeading: { backgroundColor: 'silver' },
            checkButton: { backgroundColor: 'lightseagreen', color: 'white' },
            button: { backgroundColor: 'darkblue', color: 'white' },
            editRow: { backgroundColor: 'whitesmoke' }
        };

        const EditForm = () => (
            //Should be combined with taskForm-component but I dont have time...
            <Table.Row style={styles.editRow}>
                <Table.Cell>
                    <Button style={styles.button} onClick={this.saveEdit}>Save changes</Button>
                    <Button style={styles.button} onClick={this.closeEdit} icon="close" />
                </Table.Cell>
                <Table.Cell>
                    <Form onChange={this.handleFormChange}>
                        <Form.Input label="Title" value={this.state.editTask.title} name="title" type="text" />
                        <Form.Input label="Description" value={this.state.editTask.description} name="description" type="text" />
                    </Form>
                </Table.Cell>
                <Table.Cell />
                <Table.Cell />
            </Table.Row>
        )

        return (
            <Table color="violet" style={styles.table}>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Title</Table.HeaderCell>
                        <Table.HeaderCell>Description</Table.HeaderCell>
                        <Table.HeaderCell>Deadline</Table.HeaderCell>
                        <Table.HeaderCell />
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {this.state.tasks.map((task, index) => {
                        return (
                            <Table.Row key={index}>
                                <Table.Cell><b>{task.title}</b></Table.Cell>
                                <Table.Cell>{task.description}</Table.Cell>
                                <Table.Cell>{task.deadline}</Table.Cell>
                                <Table.Cell>
                                    <Button style={styles.checkButton} onClick={this.handleTaskCheck} value={task.id} icon="checkmark" />
                                    <Button style={styles.button} onClick={this.onEditClick} value={task.id} icon="edit" />
                                </Table.Cell>
                            </Table.Row>
                        );
                    })}
                    {
                        this.state.editTask ?
                            (<EditForm />)
                            : null
                    }
                    <TaskForm updateTasks={this.props.updateTasks} categoryID={this.props.selectedCategory.id} />
                </Table.Body>
            </Table>
        )
    }
}