from flask import Flask, render_template

# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    return render_template("index.html", prediction_text="{0:10.2f}".format(20.5), code_text="feature_value_dict")


if __name__ == "__main__":
    flask_app.run(debug=True)
