from flask import *

def main():
    app = Flask(__name__)

    message = "Hello, World"

    # messageを出力
    @app.route("/")
    def index():
        return jsonify({"message": message})

    # messageを入力
    @app.route("/message", methods=["POST"])
    def post_message():
        json_request = json.loads(request.data.decode("utf-8"))
        msg = str(json_request["message"])
        result = msg != ""
        if result:
            message = msg
        return jsonify({"result": result, "message": message})

    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()
