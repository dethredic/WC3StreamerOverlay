import React from "react";
import { Paper, Typography } from "@material-ui/core/";
import Team from "./team";


function Layout(props) {
  if (props.teams.length > 0) {
    return (
      <Paper style={{ maxWidth: 248, padding: 16, backgroundColor: "rgba(0,0,0,.7)" }}>
        <Team team={props.teams[0]} />
        <Typography color="textSecondary" variant="subtitle1" align="center">- vs -</Typography>
        <Team team={props.teams[1]} />
      </Paper>
    );
  } else {
    return null;
  }
}

export default Layout;
