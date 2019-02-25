import React from "react";
import Paper from "@material-ui/core/Paper";
import Player from "./player";

function Team(props) {
  const use_solo_stats = props.team.length === 1;
  return (
    <Paper style={{ padding: 16, backgroundColor: "rgba(0,0,0,.7)" }}>
      {props.team.map(player => (
        <Player key={player.id} 
          {...{
            name: player.name,
            race: player.race,
            wins: use_solo_stats
              ? player.solo_stats.wins
              : player.team_stats.wins,
            losses: use_solo_stats
              ? player.solo_stats.losses
              : player.team_stats.losses,
            win_percentage: use_solo_stats
              ? player.solo_stats.win_percent
              : player.team_stats.win_percent
          }}
        />
      ))}
    </Paper>
  );
}

export default Team;
