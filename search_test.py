from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json
import os
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


with open('voting.json') as f:
    voting_data = json.load(f)



@app.route('/')
def index():
    return render_template("list.html")


@app.route('/data/search')
def search():
    query = request.args.get('q','').lower()
    print(f"Search query: {query}") #debug log
    if not query:
        return jsonify([])
    
    results = [item for item in voting_data if query in item['address_full'].lower()]
    return jsonify(results[:100]) #limit results for performanc




@app.route('/data/voting')
def get_voting_data():
    return jsonify(voting_data)


if __name__ == '__main__':
    app.run(debug=True)