import winreg

GameVersionStrMap = {
  0: 'war3',
  1: 'w3xp'
}

class GameInfo:
  def get_game_version_str():
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Blizzard Entertainment\\Warcraft III') 
    value, regtype = winreg.QueryValueEx(reg_key, "Preferred Game Version")
    winreg.CloseKey(reg_key)
    return GameVersionStrMap[value]