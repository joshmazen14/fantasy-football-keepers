# fantasy-football-keepers
A way to determine your keepers in Fantasy football

This is my first project in Python, which I made using the Yahoo! Fantasy API.

The Problem: In keeper fantasy leagues, if you didn't immediately store the results of your draft, it becomes very confusing to figure out who your keepers should be for the next year.

The Solution: This little script I wrote over a weekend.

The Rules: While the rules between different leagues are different, and I plan on extend it so the rules are customizable, our rules were simple:
- You get to pick 3 keepers in your league from the previous year.
- The round in which you forfeit to keep that player is one round earlier than they were drafted.
  - So for instance, I (somehow) drafted Jay Ajayi in the 14th round in 2016, so this year I was able to keep him in 2017.
  - This means should I keep him next year, I will have him in the 12th.
  - Undrafted free agents are kept in the 8th round.
  - As a result of these rules, you cannot keep a first round draft pick.
  
As of version 1.0.0, it simply returns the list of all potential keepers.

In order to run:
1. Fork this repository and navigate into the repository.
2. Make sure you have pip, Python 2.7, and virtualenv installed on your machine.
3. Activate the virtual environment by running `source venv/bin/activate`.
4. You'll need to create two config files.
  - `/keepers/oauth.json`: your oauth2 credentials, eg: 
  ```
    {
      "consumer_key": "<YOUR_YAHOO_FANTASY_CONSUMER_KEY>",
      "consumer_secret": "<YOUR_YAHOO_FANTASY_CONSUMER_SECRET>"
    }
  ```
  - `/keepers/league_config.py`: your specific league config. As of right now, you just need a league id. Eg:
  ```
  config = {
    'league_id': '371.l.1234567;
  }
  ```
  (Note: League ID is determined by the game id (so for instance, 371 was fantasy football for 2017) followed by 'l', followed by league ID, which can be found in your Yahoo! Fantasy settings.)
5. Run `python keepers/keepers.py`, sit back, and enjoy gloating about the fact that you picked up Dion Lewis as a Free Agent when nobody else would :)
