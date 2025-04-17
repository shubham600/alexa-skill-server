from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Alexa Skill Server is running!"

@app.route("/", methods=["POST"])
def webhook():
    return jsonify({
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Hi! Your Alexa skill is now talking to you from Render."
            },
            "shouldEndSession": False
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
