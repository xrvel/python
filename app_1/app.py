from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import requests
from bs4 import BeautifulSoup
from pprint import pprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'http://localhost/my_git/python/app_1/test.html'  # Replace with the actual URL
    print("URL = {}". format(url))
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    
    # print(dir(r))
    # print(vars(r))
    pprint(vars(r))
    
    content_str = r._content.decode('utf-8')
    print(content_str)

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
