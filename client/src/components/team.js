import React from "react";
import PropTypes from 'prop-types';
import Player from "./player";

function Team(props) {
  const stats = props.team.length === 1 ? 'solo_stats' : 'team_stats';

  return (
    <React.Fragment>
      {props.team.map(player => (
        <Player key={player.id}
            name={player.name}
            alias={player.alias}
            race={player.race}
            level={player[stats].level}
            wins={player[stats].wins}
            losses={player[stats].losses}
            win_percentage={player[stats].win_percent}
        />
      ))}
    </React.Fragment>
  );
}

Team.propTypes = {
  team: PropTypes.arrayOf(PropTypes.shape({
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
}
export default Team;
