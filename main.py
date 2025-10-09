from flask import Flask, render_template, request, jsonify, session
from flask_bootstrap import Bootstrap5
import requests
from requests.structures import CaseInsensitiveDict
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEOAPIFY_API_KEY")
GEOAPIFY_ENDPOINT = "https://api.geoapify.com/v2/places"

HEADERS = CaseInsensitiveDict()
HEADERS["Accept"] = "application/json"

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "my_super_secret_key_change_this"

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.get_json()
    session['lat'] = float(data.get('lat'))
    session['lon'] = float(data.get('lon'))
    return jsonify({"status": "success"})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    
    return render_template('search.html')

@app.route('/search-name', methods=['POST'])
def search_name():
    cafe_name = request.form.get('cafe-name', '')
    lat = session.get('lat')
    lon = session.get('lon')
    
    params = {
        "apiKey": API_KEY,
        "categories": "catering.cafe",
        "limit": 10,
        "name": cafe_name,
        "bias": f"proximity:{lon},{lat}",
    }

    resp = requests.get(GEOAPIFY_ENDPOINT, headers=HEADERS, params=params)

    cafes = resp.json().get('features', []) if resp.status_code == 200 else []

    return render_template('search-result.html', cafes=cafes)



@app.route('/search-nearest', methods=['POST'])
def search_nearest():
    
    lat = session.get('lat')
    lon = session.get('lon')

    params = {
        "apiKey": API_KEY,
        "categories": "catering.cafe",
        "limit": 10,
        "bias": f"proximity:{lon},{lat}"
    }

    resp = requests.get(GEOAPIFY_ENDPOINT, headers=HEADERS, params=params)
    cafes = resp.json().get('features', []) if resp.status_code == 200 else []

    return render_template('search-result.html', cafes=cafes)




if __name__ == '__main__':
    app.run(debug=True)