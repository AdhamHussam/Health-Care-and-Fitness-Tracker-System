import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv(r'Mental_Data.csv')

##################################################Sleep Disorder

X3= data.drop("Sleep Disorder", axis=1)
Y3= data["Sleep Disorder"]
X_train, X_test, y_train, y_test = train_test_split(X3, Y3, test_size=0.2, shuffle =True)
rf1=RandomForestClassifier()
rf1.fit(X_train, y_train)
print("_"*50)
print(rf1.score(X_train, y_train))
print(rf1.score(X_test, y_test))
print("_"*50)
y_pred = rf1.predict(X_test)

##################################################Stress Level
X3= data.drop("Stress Level", axis=1)
Y3= data["Stress Level"]
X_train, X_test, y_train, y_test = train_test_split(X3, Y3, test_size=0.2, shuffle =True)


rf2=RandomForestClassifier()
rf2.fit(X_train, y_train)
print("_"*50)
print(rf2.score(X_train, y_train))
print(rf2.score(X_test, y_test))
print("_"*50)
y_pred = rf2.predict(X_test)
######################################################################
# Function to get row values excluding the last column
'''
Person ID,Gender,Age,Occupation,Sleep Duration,Quality of Sleep,Physical Activity Level,
Stress Level,BMI Category,Blood Pressure,Heart Rate,Daily Steps,Sleep Disorder
'''
def get_row_values(input_id):
    try:
        row = data[data['Person ID'] == input_id].iloc[0]  # Get the row based on ID
        row_values = row.iloc[1:].values  # Exclude the last column
        return row_values
    except IndexError:
        return f"No row found with ID {input_id}"
################################################################################
joblib_file="Sleep Model"
joblib.dump(rf1,joblib_file)
loaded_model1=joblib.load(open(joblib_file,'rb'))

joblib_file="Stress Model"
joblib.dump(rf2,joblib_file)
loaded_model2=joblib.load(open(joblib_file,'rb'))

