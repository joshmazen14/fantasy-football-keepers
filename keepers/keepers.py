from api_calls import hit_api, get_teams, get_roster, get_draft_results
import pprint
draft_results = get_draft_results()
draft_result_elems = draft_results.getElementsByTagName('draft_result')

def determine_keeper_round (round):
  int_round = int(round)
  if int_round == 1:
    return 'N/A'
  elif int_round > 1:
    return int(round) - 1

get_element_text = lambda e, t: e.getElementsByTagName(t)[0].childNodes[0].nodeValue.encode('ascii', 'replace')

def create_player_dict (player):
  player_key = get_element_text(player, 'player_key')
  player_dict = {
    'name': get_element_text(player, 'full'),
    'position': get_element_text(player, 'position'),
    'team': get_element_text(player, 'editorial_team_full_name')
  }
  for elem in draft_result_elems:
    if player_key == get_element_text(elem, 'player_key'):
      player_dict['round'] = determine_keeper_round(get_element_text(elem, 'round'))
      return player_dict
  player_dict['round'] = '8 (UFA)'
  return player_dict

def create_players_dict (players_dom):
  return map(create_player_dict, players_dom)

def create_team_dict (team_dom):
  team_key = get_element_text(team_dom, 'team_key')
  team_dict = {
    'team': team_key,
    'owner': get_element_text(team_dom, 'nickname'),
  }
  roster_dom = get_roster(team_dict)
  players_dom = roster_dom.getElementsByTagName('player')
  team_dict['players'] = create_players_dict(players_dom)
  return team_dict

def create_team_dicts ():
  team_dom = get_teams()
  team_elems = team_dom.getElementsByTagName('team')
  return map(create_team_dict, team_elems)


if __name__ == "__main__":
  pp = pprint.PrettyPrinter(indent=1)
  teams = create_team_dicts()
  pp.pprint(teams)