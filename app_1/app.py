from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'http://localhost/my_git/python/app_1/test.html'  # Replace with the actual URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        items = []

        # Find all <a> tags with the class "something"
        for a_tag in soup.find_all('a', class_='something'):
            items.append(a_tag.text)  # Get the text between <a>...</a>

        return jsonify({'items': items})
    else:
        return jsonify({'error': 'Failed to retrieve data', 'status_code': r.status_code})

if __name__ == '__main__':
    app.run(port=5000)
