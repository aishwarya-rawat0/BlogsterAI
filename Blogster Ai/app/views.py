from flask import request, jsonify
from app import app
from .scraper import scrape_and_store

@app.route('/scrape', methods=['POST'])
def scrape():
    #get userid form the request parameters
    user_id = request.args.get('user_id')
    
    data = request.get_json()
   
    url = data.get('url')
    if user_id and url:
        scrape_and_store(user_id, url)
        return jsonify({"message": "Completed"}), 200
    else:
        return jsonify({'error': 'Invalid parameters.'}), 400
