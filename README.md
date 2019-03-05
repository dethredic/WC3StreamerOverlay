# WC3 Streamer Overlay
A simple tool for WC3 streamers to display their opponent's race and stats

## Summary
Only bnet games are supported (ROC and TFT). Custom games and local games are unsupported

[Twitch Example (Old UI)](https://www.twitch.tv/videos/387166497)

![1v1](/screenshots/1v1.png)
![2v2](/screenshots/2v2.png)


- The Warcraft III Observer API (War3StatsObserverSharedMemory) is used to determine if a game is in progress
- A packet sniffer is used to obtain the opponent's name and race
- Stats are scrapped directly from (classic.battle.net/war3/ladder)
- The gathered information is broadcast via a websocket
- A basic client written in React/Material-UI displays the information

## Usage
- Install [Npcap](https://nmap.org/npcap/#download)
- [Download the latest release](https://github.com/dethredic/WC3StreamerOverlay/releases)
- Run the executable
- In OBS add a new browser source:
  - Local file: `client/index.html`
  - Width: 280
  - Height: ~300 (use more for team games)
  - Move/resize as desired
- Look for the `Client connected` log. If you don't see that then `Refresh cache of current page` under the source settings

## Development
### Requirements
- [Python 3](https://www.python.org/)
- [Npcap](https://nmap.org/npcap/#download)
- npm (or yarn)

### Tool
- `pip install -r requirements.txt`
- python src/main.py

### Client
- `cd client`
- `npm install`
- `npm start`
- See `client/README.md`

## Future Ideas
- Support a custom port via an argument or config file
- Look up player alias' from something like (warcraft3.info)
