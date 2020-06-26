import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv(r'C:\Users\Pankaj\Downloads\new\image\hello11.csv')

from sklearn.model_selection import train_test_split


X = df.drop('Label',axis=1)
y = df['Label']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

dtree.fit(X_train,y_train)

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print("By Decision tree Classifie")
print(classification_report(y_test,predictions))

#--------------------------------------------------------------
print("By Random forest Classifie")
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

rfc_pred = rfc.predict(X_test)
print(confusion_matrix(y_test,rfc_pred))

print(classification_report(y_test,rfc_pred))
