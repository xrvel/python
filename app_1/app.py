from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url_to_scrape', 'http://localhost/my_git/python/app_1/test.html')  # Use POST field if available
    else:
        url = 'http://localhost/my_git/python/app_1/test.html'  # Default URL to scrape

    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        items = []

        for a_tag in soup.find_all('a', class_='something'):
            items.append(a_tag.text)

        return jsonify({'items': items})
    else:
        return jsonify({'error': 'Failed to retrieve data', 'status_code': r.status_code})

@app.route('/another', methods=['GET'])
def another_route():
    page = request.args.get('page', 0, type=int)
    name = request.args.get('name', "", type=str)
    print(f"Page variable is: {page}")
    return jsonify({"message": "Hello from another route!", "page" : page, "name" : name})

@app.route('/test', methods=['POST'])
def test_route():
    name = request.form.get('name', 'Anonymous')  # Default to "Anonymous" if "name" is not provided
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(port=5000)
