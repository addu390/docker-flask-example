from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/definition", methods=['POST'])
def definition():
    data = request.get_json(force=True)
    word = data.get("word")
    if word is None:
        error = {"word": None, "error": "Invalid JSON input."}
        return error, 400

    word = data.get("word").strip().lower()

    result = {"word": word}
    response = requests.post('http://flask-processor:5050/find', json=result)
    print('response from server:', response.text)
    if response.ok:
        return response.json(), 200
    else:
        return response.json(), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0')
