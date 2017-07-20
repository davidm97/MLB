import requests
import csv
from bs4 import BeautifulSoup
import os
from operator import itemgetter, attrgetter

print "Initializing..."
inputs = open('Scoring_Rules.csv', 'r')

hits = str(inputs.readline())
doubles = str(inputs.readline())
triples = str(inputs.readline())
homeruns = str(inputs.readline())
rbis = str(inputs.readline())

a = int(hits.strip()[-1])
b = int(doubles.strip()[-1])
c = int(triples.strip()[-1])
d = int(homeruns.strip()[-1])
e = int(rbis.strip()[-1])

inputs.close()

coach_names = []
roster = open('League_Rosters.csv', 'r')

coach1_name = str(roster.readline())
coach1_name = [coach1_name]
coach_names.append(coach1_name)
coach1 = []
team1_player1 = str(roster.readline())
team1_player2 = str(roster.readline())
team1_player3 = str(roster.readline())
team1_player4 = str(roster.readline())
team1_player5 = str(roster.readline())
team1_player6 = str(roster.readline())
team1_player7 = str(roster.readline())
team1_player8 = str(roster.readline())
team1_player9 = str(roster.readline())
coach1.append(team1_player1.strip())
coach1.append(team1_player2.strip())
coach1.append(team1_player3.strip())
coach1.append(team1_player4.strip())
coach1.append(team1_player5.strip())
coach1.append(team1_player6.strip())
coach1.append(team1_player7.strip())
coach1.append(team1_player8.strip())
coach1.append(team1_player9.strip())
final_coach1 = []

roster.readline()
coach2_name = str(roster.readline())
coach2_name = [coach2_name]
coach_names.append(coach2_name)
coach2 = []
team2_player1 = str(roster.readline())
team2_player2 = str(roster.readline())
team2_player3 = str(roster.readline())
team2_player4 = str(roster.readline())
team2_player5 = str(roster.readline())
team2_player6 = str(roster.readline())
team2_player7 = str(roster.readline())
team2_player8 = str(roster.readline())
team2_player9 = str(roster.readline())
coach2.append(team2_player1.strip())
coach2.append(team2_player2.strip())
coach2.append(team2_player3.strip())
coach2.append(team2_player4.strip())
coach2.append(team2_player5.strip())
coach2.append(team2_player6.strip())
coach2.append(team2_player7.strip())
coach2.append(team2_player8.strip())
coach2.append(team2_player9.strip())
final_coach2 = []

roster.readline()
coach3_name = str(roster.readline())
coach3_name = [coach3_name]
coach_names.append(coach3_name)
coach3 = []
team3_player1 = str(roster.readline())
team3_player2 = str(roster.readline())
team3_player3 = str(roster.readline())
team3_player4 = str(roster.readline())
team3_player5 = str(roster.readline())
team3_player6 = str(roster.readline())
team3_player7 = str(roster.readline())
team3_player8 = str(roster.readline())
team3_player9 = str(roster.readline())
coach3.append(team3_player1.strip())
coach3.append(team3_player2.strip())
coach3.append(team3_player3.strip())
coach3.append(team3_player4.strip())
coach3.append(team3_player5.strip())
coach3.append(team3_player6.strip())
coach3.append(team3_player7.strip())
coach3.append(team3_player8.strip())
coach3.append(team3_player9.strip())
final_coach3 = []

roster.readline()
coach4_name = str(roster.readline())
coach4_name = [coach4_name]
coach_names.append(coach4_name)
coach4 = []
team4_player1 = str(roster.readline())
team4_player2 = str(roster.readline())
team4_player3 = str(roster.readline())
team4_player4 = str(roster.readline())
team4_player5 = str(roster.readline())
team4_player6 = str(roster.readline())
team4_player7 = str(roster.readline())
team4_player8 = str(roster.readline())
team4_player9 = str(roster.readline())
coach4.append(team4_player1.strip())
coach4.append(team4_player2.strip())
coach4.append(team4_player3.strip())
coach4.append(team4_player4.strip())
coach4.append(team4_player5.strip())
coach4.append(team4_player6.strip())
coach4.append(team4_player7.strip())
coach4.append(team4_player8.strip())
coach4.append(team4_player9.strip())
final_coach4 = []

roster.readline()
coach5_name = str(roster.readline())
coach5_name = [coach5_name]
coach_names.append(coach5_name)
coach5 = []
team5_player1 = str(roster.readline())
team5_player2 = str(roster.readline())
team5_player3 = str(roster.readline())
team5_player4 = str(roster.readline())
team5_player5 = str(roster.readline())
team5_player6 = str(roster.readline())
team5_player7 = str(roster.readline())
team5_player8 = str(roster.readline())
team5_player9 = str(roster.readline())
coach5.append(team5_player1.strip())
coach5.append(team5_player2.strip())
coach5.append(team5_player3.strip())
coach5.append(team5_player4.strip())
coach5.append(team5_player5.strip())
coach5.append(team5_player6.strip())
coach5.append(team5_player7.strip())
coach5.append(team5_player8.strip())
coach5.append(team5_player9.strip())
final_coach5 = []

roster.readline()
coach6_name = str(roster.readline())
coach6_name = [coach6_name]
coach_names.append(coach6_name)
coach6 = []
team6_player1 = str(roster.readline())
team6_player2 = str(roster.readline())
team6_player3 = str(roster.readline())
team6_player4 = str(roster.readline())
team6_player5 = str(roster.readline())
team6_player6 = str(roster.readline())
team6_player7 = str(roster.readline())
team6_player8 = str(roster.readline())
team6_player9 = str(roster.readline())
coach6.append(team6_player1.strip())
coach6.append(team6_player2.strip())
coach6.append(team6_player3.strip())
coach6.append(team6_player4.strip())
coach6.append(team6_player5.strip())
coach6.append(team6_player6.strip())
coach6.append(team6_player7.strip())
coach6.append(team6_player8.strip())
coach6.append(team6_player9.strip())
final_coach6 = []

roster.readline()
coach7_name = str(roster.readline())
coach7_name = [coach7_name]
coach_names.append(coach7_name)
coach7 = []
team7_player1 = str(roster.readline())
team7_player2 = str(roster.readline())
team7_player3 = str(roster.readline())
team7_player4 = str(roster.readline())
team7_player5 = str(roster.readline())
team7_player6 = str(roster.readline())
team7_player7 = str(roster.readline())
team7_player8 = str(roster.readline())
team7_player9 = str(roster.readline())
coach7.append(team7_player1.strip())
coach7.append(team7_player2.strip())
coach7.append(team7_player3.strip())
coach7.append(team7_player4.strip())
coach7.append(team7_player5.strip())
coach7.append(team7_player6.strip())
coach7.append(team7_player7.strip())
coach7.append(team7_player8.strip())
coach7.append(team7_player9.strip())
final_coach7 = []

roster.readline()
coach8_name = str(roster.readline())
coach8_name = [coach8_name]
coach_names.append(coach8_name)
coach8 = []
team8_player1 = str(roster.readline())
team8_player2 = str(roster.readline())
team8_player3 = str(roster.readline())
team8_player4 = str(roster.readline())
team8_player5 = str(roster.readline())
team8_player6 = str(roster.readline())
team8_player7 = str(roster.readline())
team8_player8 = str(roster.readline())
team8_player9 = str(roster.readline())
coach8.append(team8_player1.strip())
coach8.append(team8_player2.strip())
coach8.append(team8_player3.strip())
coach8.append(team8_player4.strip())
coach8.append(team8_player5.strip())
coach8.append(team8_player6.strip())
coach8.append(team8_player7.strip())
coach8.append(team8_player8.strip())
coach8.append(team8_player9.strip())
final_coach8 = []

roster.readline()
coach9_name = str(roster.readline())
coach9_name = [coach9_name]
coach_names.append(coach9_name)
coach9 = []
team9_player1 = str(roster.readline())
team9_player2 = str(roster.readline())
team9_player3 = str(roster.readline())
team9_player4 = str(roster.readline())
team9_player5 = str(roster.readline())
team9_player6 = str(roster.readline())
team9_player7 = str(roster.readline())
team9_player8 = str(roster.readline())
team9_player9 = str(roster.readline())
coach9.append(team9_player1.strip())
coach9.append(team9_player2.strip())
coach9.append(team9_player3.strip())
coach9.append(team9_player4.strip())
coach9.append(team9_player5.strip())
coach9.append(team9_player6.strip())
coach9.append(team9_player7.strip())
coach9.append(team9_player8.strip())
coach9.append(team9_player9.strip())
final_coach9 = []

roster.readline()
coach10_name = str(roster.readline())
coach10_name = [coach10_name]
coach_names.append(coach10_name)
coach10 = []
team10_player1 = str(roster.readline())
team10_player2 = str(roster.readline())
team10_player3 = str(roster.readline())
team10_player4 = str(roster.readline())
team10_player5 = str(roster.readline())
team10_player6 = str(roster.readline())
team10_player7 = str(roster.readline())
team10_player8 = str(roster.readline())
team10_player9 = str(roster.readline())
coach10.append(team10_player1.strip())
coach10.append(team10_player2.strip())
coach10.append(team10_player3.strip())
coach10.append(team10_player4.strip())
coach10.append(team10_player5.strip())
coach10.append(team10_player6.strip())
coach10.append(team10_player7.strip())
coach10.append(team10_player8.strip())
coach10.append(team10_player9.strip())
final_coach10 = []

roster.readline()
coach11_name = str(roster.readline())
coach11_name = [coach11_name]
coach_names.append(coach11_name)
coach11 = []
team11_player1 = str(roster.readline())
team11_player2 = str(roster.readline())
team11_player3 = str(roster.readline())
team11_player4 = str(roster.readline())
team11_player5 = str(roster.readline())
team11_player6 = str(roster.readline())
team11_player7 = str(roster.readline())
team11_player8 = str(roster.readline())
team11_player9 = str(roster.readline())
coach11.append(team11_player1.strip())
coach11.append(team11_player2.strip())
coach11.append(team11_player3.strip())
coach11.append(team11_player4.strip())
coach11.append(team11_player5.strip())
coach11.append(team11_player6.strip())
coach11.append(team11_player7.strip())
coach11.append(team11_player8.strip())
coach11.append(team11_player9.strip())
final_coach11 = []

roster.readline()
coach12_name = str(roster.readline())
coach12_name = [coach12_name]
coach_names.append(coach12_name)
coach12 = []
team12_player1 = str(roster.readline())
team12_player2 = str(roster.readline())
team12_player3 = str(roster.readline())
team12_player4 = str(roster.readline())
team12_player5 = str(roster.readline())
team12_player6 = str(roster.readline())
team12_player7 = str(roster.readline())
team12_player8 = str(roster.readline())
team12_player9 = str(roster.readline())
coach12.append(team12_player1.strip())
coach12.append(team12_player2.strip())
coach12.append(team12_player3.strip())
coach12.append(team12_player4.strip())
coach12.append(team12_player5.strip())
coach12.append(team12_player6.strip())
coach12.append(team12_player7.strip())
coach12.append(team12_player8.strip())
coach12.append(team12_player9.strip())
final_coach12 = []

roster.close()

print "Retrieving Data..."
url = 'http://www.espn.com/mlb/teams'
mlb_teams = requests.get(url)
mlb_teams_text = BeautifulSoup(mlb_teams.text, 'html.parser')
team_names = mlb_teams_text.find_all('ul', class_='medium-logos')

teams = {}
team_lst = []
abb = {}
name = {}
for team_name in team_names:
    lis = team_name.find_all('li')
    for li in lis:
        info = li.h5.a
        team_url = info['href']
        teams.update({info.text : team_url})
        team_abb = team_url.split('/')[-2]
        abb.update({info.text : team_abb})
        team_name = team_url.split('/')[-1]
        name.update({info.text : team_name})

BASE_URL = 'http://www.espn.com/mlb/team/stats/batting/_/name/{0}/{1}'
category_header = ["MLB BATTING STATS"]
header = ["NAME", "H", "2B", "3B", "HR", "RBI", "TOTAL"]
    
league_points = []

for key in abb:
    mlb_team = requests.get(BASE_URL.format(abb[key], name[key]))
    team_page = BeautifulSoup(mlb_team.text, 'html.parser')
    tables = team_page.find_all('table')
    for table in tables:
        if table.text.startswith('Batting'):
            stats = []
            trs = table.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                data = []
                for td in tds:
                    data.append(td.text)
                stats.append(data)
            stats = stats[2:len(stats)-2]
    points = []
    for player in stats:
        points_row = []
        player[0] = player[0].encode('utf8', 'replace')
        suffix = '\xe2\x80\xa0'
        if player[0].endswith(suffix):
            player[0] = player[0][:len(player[0])-3]
        points_row.append(player[0])
        hits = int(player[4])
        doubles = int(player[5])
        triples = int(player[6])
        homeruns = int(player[7])
        RBIs = int(player[8])
        total = a*hits + b*doubles + c*triples + d*homeruns + e*RBIs
        points_row.append(hits)
        points_row.append(doubles)
        points_row.append(triples)
        points_row.append(homeruns)
        points_row.append(RBIs)
        points_row.append(total)
        points.append(points_row)
        league_points.append(points_row)
      
league_points.sort(key=lambda x: x[6], reverse=True)              

with open("All_Player_Stats.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(category_header)
    writer.writerow(header)
    for item in league_points:
        writer.writerow(item)

print "Calculating..."

with open("Standings.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)

for player in coach1:
    for item in league_points:
        if item[0] == player:
            final_coach1.append(item)       
for player in final_coach1:
    player[1:6] = []
final_coach1.sort(key=lambda x: x[1], reverse = True)
coach1_total = 0
for i in range(5):
    coach1_total+=final_coach1[i][1]
final_coach1.append(["Top 5 Total", coach1_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(coach_names[0])
    for item in final_coach1:
        writer.writerow(item)

for player in coach2:
    for item in league_points:
        if item[0] == player:
            final_coach2.append(item)         
for player in final_coach2:
    player[1:6] = []
final_coach2.sort(key=lambda x: x[1], reverse = True)
coach2_total = 0
for i in range(5):
    coach2_total += final_coach2[i][1]
final_coach2.append(["Top 5 Total", coach2_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[1])
    for item in final_coach2:
        writer.writerow(item)
        
for player in coach3:
    for item in league_points:
        if item[0] == player:
            final_coach3.append(item)         
for player in final_coach3:
    player[1:6] = []
final_coach3.sort(key=lambda x: x[1], reverse = True)
coach3_total = 0
for i in range(5):
    coach3_total += final_coach3[i][1]
final_coach3.append(["Top 5 Total", coach3_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[2])
    for item in final_coach3:
        writer.writerow(item)

for player in coach4:
    for item in league_points:
        if item[0] == player:
            final_coach4.append(item)         
for player in final_coach4:
    player[1:6] = []
final_coach4.sort(key=lambda x: x[1], reverse = True)
coach4_total = 0
for i in range(5):
    coach4_total += final_coach4[i][1]
final_coach4.append(["Top 5 Total", coach4_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[3])
    for item in final_coach4:
        writer.writerow(item)
        
for player in coach5:
    for item in league_points:
        if item[0] == player:
            final_coach5.append(item)         
for player in final_coach5:
    player[1:6] = []
final_coach5.sort(key=lambda x: x[1], reverse = True)
coach5_total = 0
for i in range(5):
    coach5_total += final_coach5[i][1]
final_coach5.append(["Top 5 Total", coach5_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[4])
    for item in final_coach5:
        writer.writerow(item)
       
for player in coach6:
    for item in league_points:
        if item[0] == player:
            final_coach6.append(item)         
for player in final_coach6:
    player[1:6] = []
final_coach6.sort(key=lambda x: x[1], reverse = True)
coach6_total = 0
for i in range(5):
    coach6_total += final_coach6[i][1]
final_coach6.append(["Top 5 Total", coach6_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[5])
    for item in final_coach6:
        writer.writerow(item)
 
for player in coach7:
    for item in league_points:
        if item[0] == player:
            final_coach7.append(item)         
for player in final_coach7:
    player[1:6] = []
final_coach7.sort(key=lambda x: x[1], reverse = True)
coach7_total = 0
for i in range(5):
    coach7_total += final_coach7[i][1]
final_coach7.append(["Top 5 Total", coach7_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[6])
    for item in final_coach7:
        writer.writerow(item)
        
for player in coach8:
    for item in league_points:
        if item[0] == player:
            final_coach8.append(item)         
for player in final_coach8:
    player[1:6] = []
final_coach8.sort(key=lambda x: x[1], reverse = True)
coach8_total = 0
for i in range(5):
    coach8_total += final_coach8[i][1]
final_coach8.append(["Top 5 Total", coach8_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[7])
    for item in final_coach8:
        writer.writerow(item)
        
for player in coach9:
    for item in league_points:
        if item[0] == player:
            final_coach9.append(item)         
for player in final_coach9:
    player[1:6] = []
final_coach9.sort(key=lambda x: x[1], reverse = True)
coach9_total = 0
for i in range(5):
    coach9_total += final_coach9[i][1]
final_coach9.append(["Top 5 Total", coach9_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[8])
    for item in final_coach9:
        writer.writerow(item)

for player in coach10:
    for item in league_points:
        if item[0] == player:
            final_coach10.append(item)         
for player in final_coach10:
    player[1:6] = []
final_coach10.sort(key=lambda x: x[1], reverse = True)
coach10_total = 0
for i in range(5):
    coach10_total += final_coach10[i][1]
final_coach10.append(["Top 5 Total", coach10_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[9])
    for item in final_coach10:
        writer.writerow(item)
        
for player in coach11:
    for item in league_points:
        if item[0] == player:
            final_coach11.append(item)         
for player in final_coach11:
    player[1:6] = []
final_coach11.sort(key=lambda x: x[1], reverse = True)
coach11_total = 0
for i in range(5):
    coach11_total += final_coach11[i][1]
final_coach11.append(["Top 5 Total", coach11_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[10])
    for item in final_coach11:
        writer.writerow(item)
        
for player in coach12:
    for item in league_points:
        if item[0] == player:
            final_coach12.append(item)         
for player in final_coach12:
    player[1:6] = []
final_coach12.sort(key=lambda x: x[1], reverse = True)
coach12_total = 0
for i in range(5):
    coach12_total += final_coach12[i][1]
final_coach12.append(["Top 5 Total", coach12_total])
with open("Standings.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow("")
    writer.writerow(coach_names[11])
    for item in final_coach12:
        writer.writerow(item)

print "Completed"      
 
os.system("open ~/Desktop/Random_Py/MLB/Fantasy_Calculator/Standings.csv")    
os.system("open ~/Desktop/Random_Py/MLB/Fantasy_Calculator/All_Player_Stats.csv")