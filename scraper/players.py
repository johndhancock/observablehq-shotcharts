import requests
import time
import random
import json

master_list = []
years = ["1996-97", "1997-98", "1998-99", "1999-00", "2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06", "2006-07", "2007-08", "2008-09", "2009-10", "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19"]


headers = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'), # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('http://stats.nba.com')
}

def getPlayers(year):

    payload = {
        "LeagueID": "00",
        "Season": year,
        "IsOnlyCurrentSeason": "1"
    }

    r = requests.get("http://stats.nba.com/stats/commonallplayers", params=payload, headers=headers, timeout=15)
    r.raise_for_status()

    player_data = r.json()

    for player in player_data["resultSets"][0]["rowSet"]:
        playerDict = {
            "label": player[2],
            "value": player[0]
        }

        if not any(d['label'] == player[2] for d in master_list):
            master_list.append(playerDict)

for year in years:
    time.sleep(random.randint(3, 6))
    print(year)
    getPlayers(year)

sorted_master = sorted(master_list, key=lambda k: k['label'])

with open('../data/master-player-list.json', 'w') as output:
    json.dump(sorted_master, output)
