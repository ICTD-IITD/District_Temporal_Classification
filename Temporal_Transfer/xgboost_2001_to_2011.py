from xgboost import XGBClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

filepath  = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/2001_districts_quant.csv"
df_2001 = pd.read_csv (filepath)
df_2001["census_code"] = df_2001["0"]

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/District - Ground Truth - 2011&2001.csv"
y1 = pd.read_csv(path_groundtruth)

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/FEMP&LIT.csv"
y2 = pd.read_csv(path_groundtruth)

y3 = pd.merge(y1,y2,on ='census_code')
final_2001 = pd.merge(df_2001,y3, on='census_code')

filepath  = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Output_Features_and_Labels/2011_districts_quant.csv"
df_2011 = pd.read_csv (filepath)
df_2011["census_code"] = df_2011["censuscode"]

final_2011 = pd.merge(df_2011,y3, on='census_code')
cols = [str(i) for i in range(1,121)]

l = ['ASSET','BF','CHH','FC','MSL','MSW','LIT','FEMP']
for indicator in l :
    clf = XGBClassifier()
    clf.fit(final_2001[cols],final_2001[indicator+'_2001'])
    y_pred = clf.predict(final_2011[cols])
    print(indicator," => ",f1_score(final_2011[indicator+"_2011"],y_pred, average='weighted'))

