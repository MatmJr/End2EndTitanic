from flask import Flask, request, render_template
import pandas as pd

class PresentationLayer:
    def __init__(self, business_layer, label_encoders, df_encoded):
        self.business_layer = business_layer
        self.label_encoders = label_encoders
        self.df_encoded = df_encoded

    def create_app(self):
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/predict', methods=['POST'])
        def predict():
            pclass = int(request.form['Pclass'])
            sex = request.form['Sex']
            age = int(request.form['Age'])
            sibsp = int(request.form['SibSp'])
            parch = int(request.form['Parch'])
            fare = float(request.form['Fare'])
            embarked = request.form['Embarked']

            attributes = {
                'Pclass': pclass,
                'Sex': self.label_encoders['Sex'].transform([sex])[0],
                'Age': age,
                'SibSp': sibsp,
                'Parch': parch,
                'Fare': fare,
                'Embarked': self.label_encoders['Embarked'].transform([embarked])[0]
            }

            probabilidade, classificacao = self.business_layer.prever_sobrevivencia(attributes, self.df_encoded)
            result = {
                'probabilidade': f"{probabilidade:.2f}",
                'classificacao': 'Sobreviveu' if classificacao == 1 else 'Não Sobreviveu'
            }
            return render_template('result.html', result=result)

        return app
