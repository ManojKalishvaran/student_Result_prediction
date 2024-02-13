from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,f1_score
import pandas as pd

data={
    "Attendance" : ["good","bad","bad","good","bad","good","good","good","bad","good"],
    "Study" :[5,7,3,6,7,5,4.5,4,7,3],
    "result":["pass","pass","fail","pass","fail","pass","pass","pass","pass","fail"]
}
df=pd.DataFrame(data)

#mapping
df["Attendance"]=df["Attendance"].map({"good":1,"bad":0})
df["result"]=df["result"].map({"pass":1,"fail":0})
print(df["Attendance"],"\n",df["result"])

#feature selection 
X=df[["Attendance","Study"]]
Y=df["result"]

#train test split
x_train,x_test,y_train,y_test=train_test_split(X,Y, train_size=0.8,random_state=5)

#model building
dec=DecisionTreeClassifier(random_state=65)
dec.fit(x_train,y_train)

#y pred
y_pred= dec.predict(x_test)

#accuracy
accuracy=accuracy_score(y_test,y_pred)
accuracy_2=f1_score(y_test,y_pred)
print('accuracy',accuracy,"\n","accuracy2",accuracy_2)

#application
new=dec.predict([[0,10]])
new_="pass" if new[0]==1 else "fail"
print("new_pred :\n",new_)
