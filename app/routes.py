from flask import Flask, render_template

app = Flask(__name__)

def configure_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
