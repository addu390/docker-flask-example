from flask import Flask, request

app = Flask(__name__)


@app.route("/find", methods=['POST'])
def hello():
    data = request.get_json()
    word = data.get("word")
    result = {"word": word}

    with open("database/dictionary.txt") as file:
        for line in file:
            word_list = line.split("=")
            if word == word_list[0].strip().lower():
                result["definition"] = word_list[1].strip().lower()
                return result, 200

    result["error"] = "Word not found in dictionary."
    return result, 400


if __name__ == "__main__":
    app.run(host='0.0.0.0')
