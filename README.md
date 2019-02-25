# WC3 Stat and Race Bot
A simple tool for wc3 streamers to display their opponent's race and stats

## Summary
Only 1v1 games on bnet are supported. Custom games, local games and team games are all unsupported

[Twitch Clip](https://clips.twitch.tv/SassyBeautifulFlamingoHassanChop)

![screenshot example](/screenshots/screenshot.png)


- The Warcraft III Observer API (War3StatsObserverSharedMemory) is used to determine if a game is in progress
- A packet sniffer is used to obtain the opponent's name and race
- Stats are scrapped directly from (classic.battle.net/war3/ladder)
- The gathered information is broadcast via a websocket
- A very basic client was implemented which displays the information

## Requirements
- Warcraft III
- [Python 3](https://www.python.org/)
- [Npcap](https://nmap.org/npcap/#download)
- `pip install -r requirements.txt`

## Usage
- `python src/main.py`
- In OBS add a new browser source:
  - Local file: `client/index.html`
  - Width / Height: stream resolution
  - FPS: 1
  - Resize / move as desired

## Development
### Requirements
- Warcraft III
- [Python 3](https://www.python.org/)
- [Npcap](https://nmap.org/npcap/#download)
- npm (or yarn)
- `pip install -r requirements.txt`
- `cd client && npm install`
- Follow the direction in `client/README.md`

## Future Ideas
- Create an executable for easy use
- Improve the UI of the client
- Support a custom port via an argument or config file
- Look up player alias' from something like (warcraft3.info)