from sklearn.preprocessing import LabelEncoder, StandardScaler

from .datacleaning import Cleaner

cleaner = Cleaner()
x,y = cleaner.clean()

class Transform:
    def __init__(self):
        pass

    def transformer(self):
        categorical = x.select_dtypes("object").columns.to_list()
        numeric = x.select_dtypes("number").columns.to_list()
        x['Item_Weight'] = x['Item_Weight'].fillna(x['Item_Weight'].mean())
        x['Outlet_Size'] = x['Outlet_Size'].fillna(x['Outlet_Size'].mode()[0])
        scaler = StandardScaler()
        scaler.fit(x[numeric])
        x[numeric] = scaler.transform(x[numeric])

        label_encoder = LabelEncoder()
        categorical = x.select_dtypes(include=['object']).columns.to_list()
        for col in categorical:
             x[col] = label_encoder.fit_transform(x[col])
        
        return x,y