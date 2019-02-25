import React from "react";
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
  return (
    <Grid container spacing={16} wrap="nowrap" alignItems="center">
      <Grid item>
        <div>
          <img width="64"alt="" src={GetRaceIcon(player.race)} />
        </div>
      </Grid>
      <Grid item sm>
        <Grid item sm>
          <Typography variant="h6">{player.name}</Typography>
          <Grid container spacing={16} direction="row">
            <Grid item>
              <Typography variant="subtitle1">{player.win_percentage}%</Typography>
            </Grid>
            <Grid item>
              <Typography color="textSecondary" variant="subtitle1">W:{player.wins}</Typography>
            </Grid>
            <Grid item>
              <Typography color="textSecondary" variant="subtitle1">L:{player.losses}</Typography>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
}
export default Player;
