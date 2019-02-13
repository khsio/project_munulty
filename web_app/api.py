import numpy as np
import pickle

pipeline = pickle.load(open('./model.pkl', 'rb'))

example = {
  'age': 63,  # int
  'sex': 1,    # M or F
  'resting_blood_pressure': 145,    # int
  'serum_cholesterol': 233,  # int
  'chest_pain_2.0': 0,  # int
  'chest_pain_3.0': 0,    # float
  'chest_pain_4.0': 0,
  'slope_2.0': 0,
  'slope_3.0': 1,
  'num_major_vessels_1.0': 0,
  'num_major_vessels_2.0': 0,
  'num_major_vessels_3.0': 0,
  'thal_6.0': 1,
  'thal_7.0': 0
}

def make_prediction(features):
    X = np.array([features['age'], int(features['sex'] == 'M'), features['resting_blood_pressure'],
                  features['serum_cholesterol'], int(features['chest_pain_2.0']=='AA'), int(features['chest_pain_3.0']=='NP'),
                 int(features['chest_pain_4.0']=='A'), int(features['slope_2.0']=='F'), int(features['slope_3.0']=='DS'),
                 int(features['num_major_vessels_1.0']=='O'), int(features['num_major_vessels_2.0']=='T'),
                 int(features['num_major_vessels_3.0']=='TH'),
                 int(features['thal_6.0']=='FD'), int(features['thal_7.0']=='RD')]).reshape(1,-1)
    prob_heart_diseased = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_heart_diseased > 0.5),
        'prob_heart_diseased': prob_heart_diseased
    }
    return result

# example = {
#   'Pclass': 3,  # int
#   'Sex': 'M',    # M or F
#   'Age': 22,    # int
#   'SibSp': 1,  # int
#   'Parch': 0,  # int
#   'Fare': 7.25    # float
# }
#
# def make_prediction(features):
#     X = np.array([features['Pclass'], int(features['Sex'] == 'M'), features['Age'],
#                   features['SibSp'], features['Parch'], features['Fare']]).reshape(1,-1)
#     prob_survived = pipeline.predict_proba(X)[0, 1]
#
#     result = {
#         'prediction': int(prob_survived > 0.5),
#         'prob_survived': prob_survived
#     }
#     return result

if __name__ == '__main__':
    print(make_prediction(example))
