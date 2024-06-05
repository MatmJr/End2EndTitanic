import pandas as pd
import requests
from io import StringIO
import re
from sklearn.preprocessing import LabelEncoder

class DataLayer:
    def __init__(self, file_id):
        self.file_id = file_id
        self.data = None

    def extract_data(self):
        url = f"https://drive.google.com/uc?id={self.file_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            csv_raw = StringIO(response.text)
            self.data = pd.read_csv(csv_raw)
        except requests.RequestException as e:
            raise Exception(f"Erro ao acessar o arquivo: {e}")

    def transform_data(self):
        if self.data is None or self.data.empty:
            return

        self.data = self.data.set_index("PassengerId")

        def extract_title(name):
            title_search = re.search(' ([A-Za-z]+)\.', name)
            if title_search:
                return title_search.group(1)
            return ""

        self.data['Title'] = self.data['Name'].apply(extract_title)
        self.data['Age'] = self.data.groupby(['Sex', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.median()))
        self.data['Embarked'] = self.data['Embarked'].fillna('S')

        for num in [1, 2, 3]:
            if num == 1:
                self.data.loc[self.data['Pclass'] == 1, 'Cabin'] = self.data.loc[self.data['Pclass'] == 1, 'Cabin'].fillna('ABC')
            elif num == 2:
                self.data.loc[self.data['Pclass'] == 2, 'Cabin'] = self.data.loc[self.data['Pclass'] == 2, 'Cabin'].fillna('DE')
            elif num == 3:
                self.data.loc[self.data['Pclass'] == 3, 'Cabin'] = self.data.loc[self.data['Pclass'] == 3, 'Cabin'].fillna('FG')

    def get_encoded_data(self):
        if self.data is None or self.data.empty:
            return pd.DataFrame()

        label_encoder_sex = LabelEncoder().fit(self.data['Sex'])
        label_encoder_cabin = LabelEncoder().fit(self.data['Cabin'])
        label_encoder_title = LabelEncoder().fit(self.data['Title'])
        label_encoder_embarked = LabelEncoder().fit(self.data['Embarked'])

        df_encoded = self.data.copy()
        df_encoded['Sex'] = label_encoder_sex.transform(self.data['Sex'])
        df_encoded['Cabin'] = label_encoder_cabin.transform(self.data['Cabin'])
        df_encoded['Title'] = label_encoder_title.transform(self.data['Title'])
        df_encoded['Embarked'] = label_encoder_embarked.transform(self.data['Embarked'])

        df_encoded = df_encoded.drop(['Name', 'Ticket'], axis=1)
        return df_encoded, label_encoder_sex, label_encoder_cabin, label_encoder_title, label_encoder_embarked
