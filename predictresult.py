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
    # dataset = pd.read_csv(inputfilename)
    # encoded = dataset
    # print(dataset)
    # encoded = pd.get_dummies(dataset, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],drop_first=True)
    # standardScaler = StandardScaler()
    # columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    # encoded[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])
    # print('age and sex inside the method')
    # print(inputfilename['age'],flush=True)
    # print(inputfilename['sex'].split(":")[0],flush=True)

    # dataset = pd.DataFrame(columns=['age','sex', 'cp', 'trestbp','chol','fbs', 'restecg','thalach', 'exang','oldpeak', 'slope', 'ca', 'thal'])
    data = {'age':[inputfilename['age']],
    'sex':[inputfilename['sex'].split(":")[0]],
    'cp':[inputfilename['cp'].split(":")[0]],
     'trestbp':[inputfilename['trestbp']],
     'chol':[inputfilename['chol']],
     'fbs':[inputfilename['fbs'].split(":")[0]],
      'restecg':[inputfilename['restecg'].split(":")[0]],
      'thalach':[inputfilename['thalach'].split(":")[0]], 
      'exang':[inputfilename['exang'].split(":")[0]],
      'oldpeak':[inputfilename['oldpeak']],
       'slope':[inputfilename['slope'].split(":")[0]], 
       'ca':[inputfilename['ca']],
        'thal':[inputfilename['thal'].split(":")[0]]}
    dataset = pd.DataFrame(data)
   

    print(dataset.head(), flush=True)
    y_pred = loaded_model.predict(dataset)
    y_predval = ["Has a likelihood of heart disease" if i==1 else "Does not have heart disease" for i in y_pred]
    dataset['heart_disease_predictor']=y_predval
    print(y_pred)

    return  dataset