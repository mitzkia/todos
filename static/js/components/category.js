import React from 'react';
import { Grid, Header, Icon, Select, Button, Container } from 'semantic-ui-react'
import { getCategories, deleteCategory, getCategorysTasks } from '../services/categoryService'
import { CategoryForm } from './categoryForm'
import { TaskTable } from './taskTable'

export class Category extends React.Component {
  state = {
    categories: [],
    selectedCategory: null,
    tasks: []
  }

  componentDidMount() {
    this.updateCategories();
  }

  updateCategories() {
    getCategories().then(categories => {
      this.setState({ categories });
    });
  }

  updateTasks() {
    if (this.state.selectedCategory) {
      getCategorysTasks(this.state.selectedCategory.id)
        .then(tasks => {
          this.setState({ tasks });
        })
        .catch(error => {
          return error;
        })
    }
  }

  getOptions = () => {
    const options = this.state.categories.map(category => {
      return {
        key: category.id,
        value: category.id,
        text: category.name
      }
    });
    if (options.length) {
      return options;
    } else {
      return [{
        key: 0,
        value: 0,
        text: ''
      }]
    }
  }

  handleSelection = (event, data) => {
    var category = this.state.categories.find(function (c) {
      return c.id == data.value;
    });
    // this.setState({ selectedCategory: category });
    // this.setState({ selectedCategory: category }, this.updateTasks());
    this.setState({ selectedCategory: category }, function () {
      this.updateTasks();
    });
  }

  handleDelete = () => {
    deleteCategory(this.state.selectedCategory.id)
      .then(() => {
        this.updateCategories();
        this.setState({ selectedCategory: null })
      });
  }

  render() {
    const styles = {
      button: { marginLeft: '1em' },
      container: { padding: '2em', backgroundColor: 'white', width: '80%' },
      gridFields: { margin: '10px', paddingTop: '1em' },
      input: { width: '100%' }
    };

    const CategorySelection = () => (
      <div>
        <Select onChange={this.handleSelection} style={styles.input} placeholder="Select category" options={this.getOptions()}></Select>
      </div>
    )

    const Headering = () => (
      <Header as='h2' icon>
        <Icon name='checkmark' />
        TODOs
        <Header.Subheader>Manage your tasks</Header.Subheader>
      </Header>
    )

    const PageHeading = () => (
      <div>
        <Grid padded divided>
          <Grid.Row columns="equal">
            <Grid.Column width={3}>
              <Headering style={styles.gridHeader} />
            </Grid.Column>
            <Grid.Column width={6} style={styles.gridFields}>
              <CategorySelection />
              <CategoryForm updateCategories={this.updateCategories.bind(this)} />
            </Grid.Column>
          </Grid.Row>
        </Grid>
      </div>
    )

    if (this.state.selectedCategory) {
      return (
        <Container style={styles.container}>
          <PageHeading />
          <Grid padded divided>
            <Grid.Row>
              <h2>{this.state.selectedCategory.name}</h2>
              <Button style={styles.button} onClick={this.handleDelete} icon="trash alternate"></Button>
            </Grid.Row>
          </Grid>
          <TaskTable tasks={this.state.tasks} updateTasks={this.updateTasks.bind(this)} selectedCategory={this.state.selectedCategory} />
        </Container>
      )
    } else {
      return (
        <Container style={styles.container}>
          <PageHeading />
        </Container>
      )
    }

  }
}

//todo: fix task saving, fix purple background, task done 