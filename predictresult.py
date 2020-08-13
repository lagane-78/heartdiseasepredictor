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


def prediction(inputfilename):

    # KNN model
    # loaded_model = pickle.load(open('knnpickle_file.sav', 'rb'))
    loaded_model = pickle.load(open('heart_disease_trained_model.sav', 'rb'))
    dataset = pd.read_csv(inputfilename)
    encoded = dataset
    # print(dataset)
    # encoded = pd.get_dummies(dataset, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],drop_first=True)
    # standardScaler = StandardScaler()
    # columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    # encoded[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])
   
    y_pred = loaded_model.predict(dataset)
    y_predval = ["has heart disease" if i==1 else "Does not have heart disease" for i in y_pred]
    dataset['heart_disease_predictor']=y_predval
    print(y_pred)

    return  dataset