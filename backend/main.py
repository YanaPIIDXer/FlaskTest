from flask import *
from flask_cors import CORS

def main():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    global message
    message = "Hello, World"

    # messageを出力
    @app.route("/")
    def index():
        return jsonify({"message": message})

    # messageを入力
    @app.route("/message", methods=["POST"])
    def post_message():
        msg = request.json["message"]
        result = msg != ""
        if result:
            global message
            message = msg
        return jsonify({"result": result, "message": message})

    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()
