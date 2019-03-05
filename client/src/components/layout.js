import React from "react";
import { Grid, Paper, Typography } from "@material-ui/core/";
import Team from "./team";


function Layout(props) {
  if (props.teams.length > 0) {
    return (
      <Grid
        container
        direction="column"
        justify="space-between"
        alignItems="flex-start"
      >
        <Grid item style={{ width: 280 }}>
          <Paper style={{ padding: 16, backgroundColor: "rgba(0,0,0,.7)" }}>
            <Team team={props.teams[0]} />
            <Typography color="textSecondary" variant="subtitle1" align="center">- vs -</Typography>
            <Team team={props.teams[1]} />
          </Paper>
        </Grid>
      </Grid>
    );
  } else {
    return null;
  }
}

export default Layout;
