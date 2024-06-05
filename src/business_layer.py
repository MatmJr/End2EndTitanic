from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

class BusinessLayer:
    def __init__(self, df_encoded):
        self.df_encoded = df_encoded
        self.model = None

    def train_model(self):
        x_train, x_test, y_train, y_test = train_test_split(self.df_encoded.drop(['Survived'], axis=1),
                                                            self.df_encoded['Survived'],
                                                            test_size=0.3,
                                                            random_state=1234)
        self.model = RandomForestClassifier(n_estimators=1000, criterion='gini', max_depth=5)
        self.model.fit(x_train, y_train)

    def predict(self):
        if self.model is None:
            return None, None

        prob = self.model.predict_proba(self.df_encoded.drop('Survived', axis=1))[:, 1]
        cla = self.model.predict(self.df_encoded.drop('Survived', axis=1))
        return prob, cla

    def prever_sobrevivencia(self, attributes, df_template):
        attributes['Cabin'] = 0
        attributes['Title'] = 0

        df = pd.DataFrame([attributes])
        columns_to_use = df_template.drop(['Survived', 'Probability', 'Classification', 'Name', 'Ticket'], axis=1, errors='ignore').columns
        df = df.reindex(columns=columns_to_use, fill_value=0)

        probabilidade = self.model.predict_proba(df)[:, 1][0]
        classificacao = self.model.predict(df)[0]

        return probabilidade, classificacao
