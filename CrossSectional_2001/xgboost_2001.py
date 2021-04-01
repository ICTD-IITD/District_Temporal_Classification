from xgboost import XGBClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

filepath  = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/2001_districts_quant.csv"
df = pd.read_csv (filepath)
df["census_code"] = df["0"]

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/District - Ground Truth - 2011&2001.csv"
y1 = pd.read_csv(path_groundtruth)

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/FEMP&LIT.csv"
y2 = pd.read_csv(path_groundtruth)

y3 = pd.merge(y1,y2,on ='census_code')
final = pd.merge(df,y3, on='census_code')

X = final[[str(i) for i in range(1,121)]]

l = ['ASSET_2001','BF_2001','CHH_2001','FC_2001','MSL_2001','MSW_2001','LIT_2001','FEMP_2001']
for indicator in l :
    y = final[[indicator]]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=42)
    clf = XGBClassifier()
    clf.fit(X_train, y_train.values.ravel())
    y_pred = clf.predict(X_test)
    print(indicator," => ",accuracy_score(y_test.values.ravel(), y_pred))