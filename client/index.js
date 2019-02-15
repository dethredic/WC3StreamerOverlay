const socket = new WebSocket('ws://localhost:6110');

socket.addEventListener('message', function (event) {
  var msg = JSON.parse(event.data);
  console.log(msg);

  switch(msg.type) {
    case 'me_data':
    document.getElementById('my_name').innerHTML = msg.data.name;
    document.getElementById('my_race').innerHTML = msg.data.race;
    document.getElementById('my_stats').innerHTML =  "W:" + msg.data.wins + "   L:" + msg.data.losses + "  (" + msg.data.win_percent + "%)";
    break;
    case 'opponent_data':
      document.getElementById("opponent_name").innerHTML = msg.data.name;
    document.getElementById("opponent_race").innerHTML = msg.data.race;
    document.getElementById("opponent_stats").innerHTML = "W:" + msg.data.wins + "   L:" + msg.data.losses + "  (" + msg.data.win_percent + "%)";;
    break;
  case 'game_started':
    document.getElementById('main_div').style.display = 'block';
    break;
  case 'game_ended':
    document.getElementById('main_div').style.display = 'none';
    break;
  }
});