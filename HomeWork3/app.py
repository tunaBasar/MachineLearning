from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

expected_columns = pickle.load(open('features.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:

            length = float(request.form['length'])
            fin_height = float(request.form['fin_height'])
            age = float(request.form['age'])
            gender = int(request.form['gender'])
            species = request.form['species']

            input_data = pd.DataFrame(0, index=[0], columns=expected_columns)

            input_data['Length_cm'] = length
            input_data['Fin_Height_cm'] = fin_height
            input_data['Age'] = age

            if 'Gender' in input_data.columns:
                input_data['Gender'] = gender

            if species == 'Hammerhead':
                if 'Species_Hammerhead' in input_data.columns:
                    input_data['Species_Hammerhead'] = 1
            elif species == 'Tiger':
                if 'Species_Tiger' in input_data.columns:
                    input_data['Species_Tiger'] = 1
            prediction = model.predict(input_data)
            output = round(prediction[0], 2)

            return render_template('index.html', prediction_text=f'Tahmini Köpekbalığı Ağırlığı: {output} kg')

        except Exception as e:
            return render_template('index.html', prediction_text=f'Hata oluştu: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)