from src.data_layer import DataLayer
from src.business_layer import BusinessLayer
from src.presentation_layer import PresentationLayer
import pandas as pd

file_id = '1S5Nl793vcL5ZPTGjzKaIEbwbLaDplvIP'

# Camada de Dados
data_layer = DataLayer(file_id)
data_layer.extract_data()
data_layer.transform_data()
df_encoded, label_encoder_sex, label_encoder_cabin, label_encoder_title, label_encoder_embarked = data_layer.get_encoded_data()

# Camada de Negócios
business_layer = BusinessLayer(df_encoded)
business_layer.train_model()
prob, cla = business_layer.predict()

df_encoded['Probability'] = prob
df_encoded['Classification'] = cla

label_encoders = {
    'Sex': label_encoder_sex,
    'Cabin': label_encoder_cabin,
    'Title': label_encoder_title,
    'Embarked': label_encoder_embarked
}

# Camada de Apresentação
presentation_layer = PresentationLayer(business_layer, label_encoders, df_encoded)
app = presentation_layer.create_app()

if __name__ == "__main__":
    app.run(debug=True)
