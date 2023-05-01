import datetime
from flask import (
    Flask,
    render_template
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Site")


if __name__ == "__main__":
    app.run(host="localhost")
