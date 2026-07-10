from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Trained model load cheddam
model = pickle.load(open('models/HDI.pkl', 'rb'))

@app.route('/')
def home():
    # Renders the initial landing page
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    # Form nunchi input values teesukovadam
    life_expectancy = float(request.form['life_expectancy'])
    expected_schooling = float(request.form['expected_schooling'])
    mean_schooling = float(request.form['mean_schooling'])
    gni = float(request.form['gni'])

    # Model ki input array ga pampali
    input_data = np.array([[life_expectancy, expected_schooling, mean_schooling, gni]])
    prediction = model.predict(input_data)[0]

    # HDI category decide cheddam
    if prediction >= 0.8:
        category = "Very High"
    elif prediction >= 0.7:
        category = "High"
    elif prediction >= 0.55:
        category = "Medium"
    else:
        category = "Low"

    return render_template('dashboard.html', prediction=round(prediction, 3), category=category)

if __name__ == '__main__':
    app.run(debug=True)