import React from "react";
import Player from "./player";

function Team(props) {
  const use_solo_stats = props.team.length === 1;
  return (
    <React.Fragment>
      {props.team.map(player => (
        <Player key={player.id}
          {...{
            name: player.name,
            alias: player.alias,
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
    </React.Fragment>
  );
}

export default Team;
