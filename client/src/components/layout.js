import React from "react";
import PropTypes from 'prop-types';
import { Paper, Typography } from "@material-ui/core/";
import Team from "./team";


function Layout(props) {
  if (props.teams.length === 0) {
    return null;
  }

  return (
    <Paper style={{ maxWidth: 248, padding: 16, backgroundColor: "rgba(0,0,0,.7)" }}>
      <Team team={props.teams[0]} />
      <Typography color="textSecondary" variant="subtitle1" align="center">- vs -</Typography>
      <Team team={props.teams[1]} />
    </Paper>
  );
}

Layout.propTypes = {
  teams: PropTypes.arrayOf(
    PropTypes.arrayOf(PropTypes.shape({
      alias: PropTypes.string,
      id: PropTypes.number,
      is_me: PropTypes.bool,
      name: PropTypes.string,
      race: PropTypes.string,
      solo_stats: PropTypes.shape({
        level: PropTypes.number,
        wins: PropTypes.number,
        losses: PropTypes.number,
        win_percent: PropTypes.number,
      }),
      team_stats: PropTypes.shape({
        level: PropTypes.number,
        wins: PropTypes.number,
        losses: PropTypes.number,
        win_percent: PropTypes.number,
      }),
      ffa_stats: PropTypes.shape({
        level: PropTypes.number,
        wins: PropTypes.number,
        losses: PropTypes.number,
        win_percent: PropTypes.number,
      })}),
    )
  )
}

export default Layout;
