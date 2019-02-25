import React from "react";
import Grid from "@material-ui/core/Grid";
import Team from "./team";


function Layout(props) {
  if (props.teams.length > 0) {
    return (
      <Grid
        container
        direction="row"
        justify="space-between"
        alignItems="flex-start"
      >
        <Grid item style={{ width: 280 }}>
          <Team team={props.teams[0]} />
        </Grid>
        <Grid item style={{ width: 280 }}>
          <Team team={props.teams[1]} />
        </Grid>
      </Grid>
    );
  } else {
    return null;
  }
}

export default Layout;
