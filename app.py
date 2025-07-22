import pandas as pd
from flask import Flask, render_template, request
import joblib
model = joblib.load('credit_model.joblib')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        age = request.form['age']
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        balance = request.form['balance']
        housing = request.form['housing']
        duration = request.form['duration']
        campaign = request.form['campaign']

        # Prepare input for model (order: age, job, marital, education, balance, housing, duration, campaign)
        input_data = pd.DataFrame([[age, job, marital, education, balance, housing, duration, campaign]],
                                 columns=['age', 'job', 'marital', 'education', 'balance', 'housing', 'duration', 'campaign'])
        prediction = model.predict(input_data)[0]
        result = 'Approved' if prediction == 'yes' else 'Not Approved'
        return render_template('check.html', result=result)
    return render_template('check.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)