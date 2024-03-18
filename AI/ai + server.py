from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    prompt = {
        "modelUri": "gpt://ВВЕСТИ СВОЙ/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": data["question"]
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key ВВЕСТИ СВОЙ"
    }

    response = requests.post(url, headers=headers, json=prompt)
    data = json.loads(response.text)
    answer = data["result"]["alternatives"][0]["message"]["text"]

    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(debug=True)
