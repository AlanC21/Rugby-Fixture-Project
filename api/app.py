from flask import Flask, render_template
import pytz 
import requests
from dateutil import parser

app = Flask(__name__)

@app.route('/')
def index():
    url_standing = "https://rugby-live-data.p.rapidapi.com/standings/1272/2024"
    url_fixture = "https://rugby-live-data.p.rapidapi.com/fixtures/1272/2024"

    headers = {
	    "X-RapidAPI-Key": "21871335d0msh0bbae22097fd4b2p1ab400jsnb439334dca5a",
	    "X-RapidAPI-Host": "rugby-live-data.p.rapidapi.com"
    }

    response_standing = requests.get(url_standing, headers=headers)
    response_fixture = requests.get(url_fixture, headers=headers)

    data_standing = response_standing.json()
    standings = data_standing['results']['standings']

    data_fixture = response_fixture.json()
    fixtures = data_fixture['results']
    
    status_mapping = {
        "Not Started": "No iniciado",
        "First Half": "Primer tiempo",
        "HalfTime": "Medio tiempo",
        "Second Half": "Segundo tiempo",
        "Full Time": "Finalizado",
        "Postponed": "Pospuesto",
        "Cancelled": "Cancelado",
        "Result": "Resultado",
    }
    
    for result in fixtures:
            parsed_time = parser.parse(result["date"])
            est_time = parsed_time.astimezone(pytz.timezone('America/Argentina/Buenos_Aires'))
            result["date"] = est_time.strftime('%d de %B de %Y %H:%Mhrs')
            result["status"] = status_mapping.get(result["status"], result["status"])
        


    groups_mapping = {
        "Pool A": "Grupo A",
        "Pool B": "Grupo B",
        "Pool C": "Grupo C",
        "Pool D": "Grupo D"
    }

    team_logos = {
        "New Zealand": "new_zealand.png",
        "France": "france.png",
        "Italy": "italy.png",
        "Uruguay": "uruguay.png",
        "Namibia": "namibia.png",
        "South Africa": "south_africa.svg",
        "Ireland": "Ireland.png",
        "Scotland": "scotland.png",
        "Tonga": "tonga.png",
        "Romania": "romania.png",
        "Wales": "Wales.png",
        "Australia": "Australia.png",
        "Fiji": "Fiji.png",
        "Georgia": "Georgia.png",
        "Portugal": "Portugal.png",
        "England": "England.png",
        "Japan": "Japan.png",
        "Argentina": "Argentina.png",
        "Samoa": "Samoa.png",
        "Chile": "Chile.png",
    }


    for table in standings:
        table["table_name"] = groups_mapping.get(table["table_name"], table["table_name"])

    return render_template('index.html', standings=standings, fixtures=fixtures, team_logos=team_logos)

def pageNoFound(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pageNoFound)
    app.run(debug=True)
