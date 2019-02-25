function set_me(player) {
  console.log(player.name)
  document.getElementById('my_name').innerHTML = player.name;
  document.getElementById('my_race').innerHTML = player.race;
  document.getElementById('my_stats').innerHTML =  "W:" + player.solo_stats.wins + "   L:" + player.solo_stats.losses + "  (" + player.solo_stats.win_percent + "%)";
}

function set_opponent(player) {
  document.getElementById('opponent_name').innerHTML = player.name;
  document.getElementById('opponent_race').innerHTML = player.race;
  document.getElementById('opponent_stats').innerHTML =  "W:" + player.solo_stats.wins + "   L:" + player.solo_stats.losses + "  (" + player.solo_stats.win_percent + "%)";
}

function handle_msg(msg) {
  console.log(msg);

  switch(msg.type) {
    case 'player_data':
      if (msg.data[0].is_me) {
        set_me(msg.data[0]);
        set_opponent(msg.data[1]);
      } else {
        set_me(msg.data[1]);
        set_opponent(msg.data[0]);
      }
      break;
    case 'game_started':
      document.getElementById('main_div').style.display = 'block';
      break;
    case 'game_ended':
      document.getElementById('main_div').style.display = 'none';
      break;
  }
}

const socket = new WebSocket('ws://localhost:6110');

socket.addEventListener('message', function (event) {
  console.log(event.data)
  var msg = JSON.parse(event.data);
  handle_msg(msg)
});