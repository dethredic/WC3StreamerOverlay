import React from "react";
import PropTypes from 'prop-types';
import { Grid, Typography } from "@material-ui/core/";

function GetRaceIcon(race) {
  if (race === "Human") {
    return require("../assets/human.png");
  } else if (race === "Orc") {
    return require("../assets/orc.png");
  } else if (race === "Night Elf") {
    return require("../assets/night_elf.png");
  } else if (race === "Undead") {
    return require("../assets/undead.png");
  } else {
    return require("../assets/random.png");
  }
}

function Player(player) {
  let name = <Typography noWrap variant="h6">{player.name}</Typography>;

  if (player.alias && player.name !== player.alias) {
    name = (
      <React.Fragment>
        <Typography noWrap variant="h6" style={{marginTop:-3, marginBottom:-6}}>{player.alias}</Typography>
        <Typography noWrap color="textSecondary" variant="subtitle2" style={{marginBottom:-2}}>as {player.name}</Typography>
      </React.Fragment>
    );
  }

  if (player.wins === -1) {
    return name;
  }

  return (
    <Grid container wrap="nowrap" alignItems="center" spacing={8}>
      <Grid item>
        <img width="64" alt="" src={GetRaceIcon(player.race)} />
      </Grid>
      <Grid item xs zeroMinWidth>
        <Grid container direction="column">
          <Grid item xs>
            {name}
          </Grid>
          <Grid item xs>
            <Grid container>
              <Grid item xs>
                <Typography variant="subtitle1">{`L:${player.level || 0}`}</Typography>
              </Grid>
              <Grid item xs>
                <Typography variant="subtitle1">{player.win_percentage}%</Typography>
              </Grid>
              <Grid item xs>
                <Typography variant="subtitle1" style={{ color: "#4caf50" }}>{player.wins}</Typography>
              </Grid>
              <Grid item xs>
                <Typography variant="subtitle1" style={{ color: "#f44336" }}>{player.losses}</Typography>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
}

Player.propTypes = {
  name: PropTypes.string,
  alias: PropTypes.string,
  race: PropTypes.string,
  level: PropTypes.number,
  wins: PropTypes.number,
  losses: PropTypes.number,
  win_percent: PropTypes.number,
}

export default Player;
