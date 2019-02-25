import React, { Component } from "react";
import { Fade, Grid, MuiThemeProvider, createMuiTheme } from "@material-ui/core/";
import { Layout } from "./components";
import 'typeface-roboto';



const theme = createMuiTheme({
  palette: {
    type: "dark"
  },
  typography: {
    useNextVariants: true,
    fontSize: 14
  }
});

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { is_in_game: false, teams: [] };
    this.connection = new WebSocket('ws://localhost:6110');

    // this.connection = new WebSocket("wss://echo.websocket.org");
    // this.connection.onopen = () => {
      // this.connection.send('{"type": "game_started"}');
      // this.connection.send(
      //   '{"type": "player_data", "data": [[{"id": 0, "is_me": true, "name": "philwashere123456", "race": "Orc", "solo_stats": {"wins": 1, "losses": 8, "win_percent": 11}, "team_stats": {"wins": 0, "losses": 2, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}], [{"id": 1, "is_me": false, "name": "OrcImbalancE", "race": "Orc", "solo_stats": {"wins": 82, "losses": 23, "win_percent": 78}, "team_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}]]}'
      //   '{"type": "player_data", "data": [[{"id": 0, "is_me": true, "name": "philwashere", "race": "Orc", "solo_stats": {"wins": 1, "losses": 9, "win_percent": 10}, "team_stats": {"wins": 0, "losses": 2, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}, {"id": 2, "is_me": false, "name": "a3s2d3as21", "race": "Random", "solo_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "team_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}], [{"id": 1, "is_me": false, "name": "3as2dda13a1", "race": "Undead", "solo_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "team_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}, {"id": 3, "is_me": false, "name": "as3d21da3211", "race": "Random", "solo_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "team_stats": {"wins": 0, "losses": 0, "win_percent": 0}, "ffa_stats": {"wins": 0, "losses": 0, "win_percent": 0}}]]}'
      //   '{"type": "player_data","data": [[{"id": 0,"name": "ILoveNecropolis","race": "Undead","solo_stats": {"wins": 1168,"losses": 19,"win_percent": 98},"team_stats": {"wins": 1168,"losses": 19,"win_percent": 98},"is_me": true,"ffa_stats": {"wins": 0,"losses": 0,"win_percent": 0}},{"id": 2,"name": "FollowGrubby","race": "Orc","solo_stats": {"wins": 484,"losses": 79,"win_percent": 86},"team_stats": {"wins": 484,"losses": 79,"win_percent": 86},"is_me": false,"ffa_stats": {"wins": 0,"losses": 0,"win_percent": 0}}],[{"id": 1,"is_me": false,"name": "RomanticHuman","race": "Human","solo_stats": {"wins": 2590,"losses": 378,"win_percent": 87},"team_stats": {"wins": 2590,"losses": 378,"win_percent": 87},"ffa_stats": {"wins": 0,"losses": 0,"win_percent": 0}},{"id": 3,"is_me": false,"name": 123456789012345,"race": "Night Elf","solo_stats": {"wins": 1493,"losses": 155,"win_percent": 91},"team_stats": {"wins": 1493,"losses": 155,"win_percent": 91},"ffa_stats": {"wins": 0,"losses": 0,"win_percent": 0}}]]}'
      // );
      // this.connection.send('{"type": "game_ended"}');
    // };

    this.connection.onmessage = evt => {
      const msg = JSON.parse(evt.data);
      this.msg_handler(msg);
    };
  }

  msg_handler(msg) {
    switch (msg.type) {
      case "player_data":
        this.setState((state, props) => ({
          is_in_game: state.is_in_game,
          teams: msg.data
        }));
        break;
      case "game_started":
        this.setState((state, props) => ({
          is_in_game: true,
          teams: state.teams
        }));        
        break;
      case "game_ended":
        this.setState((state, props) => ({
          is_in_game: false,
          teams: []
        })); 
        break;
      default:
        console.log("Unexpected Message");
        break;
    }
  }

  render() {
    const should_reder = this.state.is_in_game && (this.state.teams.length > 0);
    return (
      <MuiThemeProvider theme={theme}>
        <Fade in={should_reder}>
           <Grid><Layout teams={this.state.teams}/></Grid>
        </Fade>
      </MuiThemeProvider>
    );
  }
}

export default App;
