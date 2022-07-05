from flask import *

def main():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify({"message": "Hello, World"})

    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()
