from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_post_request():
    received_data = json.loads(request.data)
    text = received_data.get('text', '')
    
    response_message = text + " Hello"
    
    return response_message

if __name__ == '__main__':
    app.run(host='188.225.85.124', port=80) 
