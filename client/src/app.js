import React, { Component } from "react";
import { Fade, MuiThemeProvider, createMuiTheme } from "@material-ui/core/";
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
    this.connect();
  }

  connect() {
    var ws = new WebSocket('ws://localhost:6110');

    ws.onmessage = e => {
      const msg = JSON.parse(e.data);
      this.msg_handler(msg);
    };

    ws.onclose = e =>  {
      console.log('Socket is closed. Reconnect will be attempted in 5 seconds.', e.reason);
      setTimeout(() => this.connect(), 5000);
    };

    ws.onerror = e =>  {
      console.error('Socket encountered error: ', e.message, 'Closing socket');
      ws.close();
    };
  }

  msg_handler(msg) {
    switch (msg.type) {
      case "player_data":
        this.setState({ teams: msg.data })
        break;
      case "game_started":
        this.setState({ is_in_game: true });
        break;
      case "game_ended":
        this.setState({
          is_in_game: false,
          teams: []
        });
        break;
      default:
        console.log("Unexpected Message");
        break;
    }
  }

  render() {
    const should_render = this.state.is_in_game && (this.state.teams.length > 0);

    return (
      <MuiThemeProvider theme={theme}>
        <Fade in={should_render}>
           <div><Layout teams={this.state.teams}/></div>
        </Fade>
      </MuiThemeProvider>
    );
  }
}

export default App;
