
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle 
from matplotlib import rcParams
from matplotlib.cm import rainbow
import warnings
warnings.filterwarnings('ignore')
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# dirname = os.path.dirname(__file__)
# model = load_model(os.path.join(dirname, 'name_of_file.h5'))

loaded_model = pickle.load(open('knnpickle_file.sav', 'rb'))
dataset = pd.read_csv('../static/data/user_data.csv')
encoded = pd.get_dummies(dataset, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],drop_first=True)
standardScaler = StandardScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
encoded[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])

y = encoded['target']
X = encoded.drop(['target'], axis = 1)
y_pred = loaded_model.predict(X)
print(y_pred)