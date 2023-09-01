from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url_standing = "https://rugby-live-data.p.rapidapi.com/standings/1272/2024"
    url_fixture = "https://rugby-live-data.p.rapidapi.com/fixtures/1272/2024"

    headers = {
	    "X-RapidAPI-Key": "41ad73a184msh813945241c52d19p17560ejsnf7916cd400ea",
	    "X-RapidAPI-Host": "rugby-live-data.p.rapidapi.com"
    }

    response_standing = requests.get(url_standing, headers=headers)
    response_fixture = requests.get(url_fixture, headers=headers)

    data_standing = response_standing.json()
    standings = data_standing['results']['standings']

    data_fixture = response_fixture.json()
    fixtures = data_fixture['results']
    
    for result in fixtures:
        date_str = result['date']
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        formatted_date = date.strftime("%d de %B de %Y, %H:%M %Z")
        result['date'] = formatted_date

    groups_mapping = {
        "Pool A": "Grupo A",
        "Pool B": "Grupo B",
        "Pool C": "Grupo C",
        "Pool D": "Grupo D"
    }

    for table in standings:
        table["table_name"] = groups_mapping.get(table["table_name"], table["table_name"])

    return render_template('index.html', standings=standings, fixtures=fixtures)

def pageNoFound(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pageNoFound)
    app.run(debug=True, port=4000)