from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html")  # Načte šablonu z `templates/index.html`

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default port for local dev
    application.run(host="0.0.0.0", port=port)

