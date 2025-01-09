from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

Rf = RandomForestClassifier()

class Model:
    def __init__(self):
        pass
    def model(self):
        params = {
            'n_estimators': [50, 100],
            'criterion': ['gini', 'entropy','log_loss'],
            'max_depth': [50],
            'min_samples_split' : [2],
            'min_samples_leaf': [1],
            'max_features': ['sqrt','sqrt']
        }

        grid =  GridSearchCV(estimator=Rf, cv=5, scoring='accuracy', param_grid=params)

        return grid










