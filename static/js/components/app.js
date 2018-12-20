import React from 'react';
import { Container, Grid } from 'semantic-ui-react'
import { Category } from './category'

export class AppComponent extends React.Component {

    render() {

      const styles = {
        container: {
          backgroundColor: 'darkblue',
          minHeight: '-webkit-fill-available',
          width: '100%'
        },
      };
      
      return (
        <Grid style={styles.container}>
          <Category />
        </Grid>
      )
    }
}