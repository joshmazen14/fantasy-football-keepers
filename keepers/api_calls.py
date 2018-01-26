from xml.dom import minidom
from yahoo_oauth import OAuth2
from league_config import config

oauth = OAuth2(None, None, from_file='keepers/oauth.json')
league = config['league_id']

if not oauth.token_is_valid():
  oauth.refresh_access_token()


def hit_api (url_path):
  base_url = 'https://fantasysports.yahooapis.com/fantasy/v2/'
  res = oauth.session.get(base_url + url_path)
  text = res.text

  xmltree = minidom.parseString(text)

  return xmltree

def get_draft_results ():
  print 'Getting draft results...'
  return hit_api('league/' + league + '/draftresults')

def get_teams ():
  print 'Gathering all teams...'
  return hit_api('league/' + league + '/teams')

def get_roster (team_dict):
  print 'Gathering roster for %s...' %(team_dict['owner'])
  return hit_api('team/' + team_dict['team'] + '/roster/players')