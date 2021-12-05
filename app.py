import joblib
import pandas as pd
from flask import Flask, request, render_template

# Create flask app
flask_app = Flask(__name__)
model = joblib.load("./random_forest.joblib")

# List of features
list_of_features = ["elevation", "precip 01", "precip 02",
                    "precip 03", "precip 04", "precip 05",
                    "precip 06", "precip 07", "LC_Type1_mode"]


@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    form_input_values = [float(x) for x in request.form.values()]
    feature_value_dict = {}
    for i in range(0, len(form_input_values)):
        feature_value_dict[list_of_features[i]] = form_input_values[i]

    df = pd.DataFrame(feature_value_dict, index=[0])
    df['LC_Type1_mode'] = pd.Categorical(df['LC_Type1_mode'])

    prediction = model.predict(df.values)

    return render_template("index.html", prediction_text="{0:10.2f}".format(prediction[0]), code_text=feature_value_dict)


if __name__ == "__main__":
    flask_app.run(debug=True)
