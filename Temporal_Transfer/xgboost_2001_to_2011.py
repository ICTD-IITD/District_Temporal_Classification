from xgboost import XGBClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

filepath  = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/CrossSectional_2001/2001_Anuj_Method/Features_100m_quantile@10.csv"
df_2001 = pd.read_csv (filepath)

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/CrossSectional_2001/District - Ground Truth - 2011&2001.csv"
y_2001 = pd.read_csv(path_groundtruth)

y_2001= y_2001[['census_code','EMP_2001', 'MSW_2001','BF_2001', 'MSL_2001','FC_2001','CHH_2001','F_EMP_2001','ASSET_2001']]
final_2001 = pd.merge(df_2001,y_2001, on='census_code')


filepath  = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/CrossSectional_2011/2011_Anuj_Method/Features_100m_quantile@10.csv"
df_2011 = pd.read_csv (filepath)

path_groundtruth = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/CrossSectional_2011/District - Ground Truth - 2011.csv"
y_2011 = pd.read_csv(path_groundtruth)

y_2011 = y_2011[['census_code','EMP_2011', 'MSW_2011','BF_2011', 'MSL_2011','FC_2011','CHH_2011','ASSET_2011']]
final_2011 = pd.merge(df_2011,y_2011, on='census_code')


X_2001 = final_2001[['band_1_1', 'band_1_2', 'band_1_3', 'band_1_4', 'band_1_5', 'band_1_6', 'band_1_7', 'band_1_8', 'band_1_9', 'band_1_10', 'band_2_1', 'band_2_2', 'band_2_3', 'band_2_4', 'band_2_5', 'band_2_6', 'band_2_7', 'band_2_8', 'band_2_9', 'band_2_10', 'band_3_1', 'band_3_2', 'band_3_3', 'band_3_4', 'band_3_5', 'band_3_6', 'band_3_7', 'band_3_8', 'band_3_9', 'band_3_10', 'band_4_1', 'band_4_2', 'band_4_3', 'band_4_4', 'band_4_5', 'band_4_6', 'band_4_7', 'band_4_8', 'band_4_9', 'band_4_10', 'band_5_1', 'band_5_2', 'band_5_3', 'band_5_4', 'band_5_5', 'band_5_6', 'band_5_7', 'band_5_8', 'band_5_9', 'band_5_10', 'band_6_1', 'band_6_2', 'band_6_3', 'band_6_4', 'band_6_5', 'band_6_6', 'band_6_7', 'band_6_8', 'band_6_9', 'band_6_10', 'band_7_1', 'band_7_2', 'band_7_3', 'band_7_4', 'band_7_5', 'band_7_6', 'band_7_7', 'band_7_8', 'band_7_9', 'band_7_10', 'band_8_1', 'band_8_2', 'band_8_3', 'band_8_4', 'band_8_5', 'band_8_6', 'band_8_7', 'band_8_8', 'band_8_9', 'band_8_10', 'band_9_1', 'band_9_2', 'band_9_3', 'band_9_4', 'band_9_5', 'band_9_6', 'band_9_7', 'band_9_8', 'band_9_9', 'band_9_10', 'band_10_1', 'band_10_2', 'band_10_3', 'band_10_4', 'band_10_5', 'band_10_6', 'band_10_7', 'band_10_8', 'band_10_9', 'band_10_10', 'band_11_1', 'band_11_2', 'band_11_3', 'band_11_4', 'band_11_5', 'band_11_6', 'band_11_7', 'band_11_8', 'band_11_9', 'band_11_10', 'band_12_1', 'band_12_2', 'band_12_3', 'band_12_4', 'band_12_5', 'band_12_6', 'band_12_7', 'band_12_8', 'band_12_9', 'band_12_10']]
print(X_2001.shape)
X_2011 = final_2011[['band_1_1', 'band_1_2', 'band_1_3', 'band_1_4', 'band_1_5', 'band_1_6', 'band_1_7', 'band_1_8', 'band_1_9', 'band_1_10', 'band_2_1', 'band_2_2', 'band_2_3', 'band_2_4', 'band_2_5', 'band_2_6', 'band_2_7', 'band_2_8', 'band_2_9', 'band_2_10', 'band_3_1', 'band_3_2', 'band_3_3', 'band_3_4', 'band_3_5', 'band_3_6', 'band_3_7', 'band_3_8', 'band_3_9', 'band_3_10', 'band_4_1', 'band_4_2', 'band_4_3', 'band_4_4', 'band_4_5', 'band_4_6', 'band_4_7', 'band_4_8', 'band_4_9', 'band_4_10', 'band_5_1', 'band_5_2', 'band_5_3', 'band_5_4', 'band_5_5', 'band_5_6', 'band_5_7', 'band_5_8', 'band_5_9', 'band_5_10', 'band_6_1', 'band_6_2', 'band_6_3', 'band_6_4', 'band_6_5', 'band_6_6', 'band_6_7', 'band_6_8', 'band_6_9', 'band_6_10', 'band_7_1', 'band_7_2', 'band_7_3', 'band_7_4', 'band_7_5', 'band_7_6', 'band_7_7', 'band_7_8', 'band_7_9', 'band_7_10', 'band_8_1', 'band_8_2', 'band_8_3', 'band_8_4', 'band_8_5', 'band_8_6', 'band_8_7', 'band_8_8', 'band_8_9', 'band_8_10', 'band_9_1', 'band_9_2', 'band_9_3', 'band_9_4', 'band_9_5', 'band_9_6', 'band_9_7', 'band_9_8', 'band_9_9', 'band_9_10', 'band_10_1', 'band_10_2', 'band_10_3', 'band_10_4', 'band_10_5', 'band_10_6', 'band_10_7', 'band_10_8', 'band_10_9', 'band_10_10', 'band_11_1', 'band_11_2', 'band_11_3', 'band_11_4', 'band_11_5', 'band_11_6', 'band_11_7', 'band_11_8', 'band_11_9', 'band_11_10', 'band_12_1', 'band_12_2', 'band_12_3', 'band_12_4', 'band_12_5', 'band_12_6', 'band_12_7', 'band_12_8', 'band_12_9', 'band_12_10']]
print(X_2011.shape)

l = ['ASSET','BF','CHH','FC','MSL','MSW']
for indicator in l :
    y = final_2001[[indicator+"_2001"]]
    clf = XGBClassifier()
    clf.fit(X_2001, y.values.ravel())
    y_pred = clf.predict(X_2011)
    print(y_2011[indicator+"_2011"].shape,y_pred.shape)
    print(indicator," => ",f1_score(final_2011[indicator+"_2011"].values.ravel(),y_pred, average='weighted'))
    ##print(indicator," => ",accuracy_score(y_2011[indicator+"_2011"].values.ravel(), y_pred))

