import React from 'react';
import { Input, Button, Icon, Form } from 'semantic-ui-react'
import { createCategory } from '../services/categoryService'

export class CategoryForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: ''
    };
  }

  componentDidMount() {

  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const category = {
      name: this.state.name
    };
    createCategory(category).then(category => {
      this.props.updateCategories(category);
    });
    this.setState({ name: ''});
  }

  render() {
    const styles = {
      input: { paddingRight: '1em', paddingTop: '1em', width: '85%' },
      button: { backgroundColor: 'darkblue', color: 'white' }
    };

    return (
      <Form onSubmit={this.handleSubmit}>
        <Input onChange={this.handleChange} value={this.state.name} style={styles.input} type="text" placeholder='New category' />
        <Button type="submit" style={styles.button} icon="plus" />
      </Form>
    )
  }
}