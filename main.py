from flask import Flask, render_template, request, jsonify
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search-result', methods=['POST'])
def search_result():
    lat = request.form.get('lat', type=float)
    lon = request.form.get('lon', type=float)

    params = {
        "apiKey": API_KEY,
        "categories": "catering.cafe",
        "limit": 10,
        "bias": f"proximity:{lon},{lat}"
    }

    resp = requests.get(GEOAPIFY_ENDPOINT, headers=HEADERS, params=params)
    cafes = resp.json().get('features', []) if resp.status_code == 200 else []

    return render_template('search-result.html', cafes=cafes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)