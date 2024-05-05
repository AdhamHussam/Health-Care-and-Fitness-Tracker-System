import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv(r'C:\Users\IShop\Documents\Fitness Tracker\Data.csv')

##################################################Heart rate level

X3= data.drop("heart_level", axis=1)
Y3= data["heart_level"]
X_train, X_test, y_train, y_test = train_test_split(X3, Y3, test_size=0.3, shuffle =True)
DT1 = DecisionTreeClassifier()
DT1.fit(X_train, y_train)
print("_"*50)
print(DT1.score(X_train, y_train))
print(DT1.score(X_test, y_test))
print("_"*50)
y_pred = DT1.predict(X_test)

##################################################Calories rate level
X3= data.drop("calories_classes", axis=1)
Y3= data["calories_classes"]

X_train, X_test, y_train, y_test = train_test_split(X3, Y3, test_size=0.3, shuffle =True)
DT2 = DecisionTreeClassifier()
DT2.fit(X_train, y_train)
print("_"*50)
print(DT2.score(X_train, y_train))
print(DT2.score(X_test, y_test))
print("_"*50)
y_pred = DT2.predict(X_test)
######################################################################
# Function to get row values excluding the last column
def get_row_values(input_id):
    try:
        row = data[data['id'] == input_id].iloc[0]  # Get the row based on ID
        row_values = row.iloc[:-1].values  # Exclude the last column
        return row_values
    except IndexError:
        return f"No row found with ID {input_id}"
################################################################################
joblib_file="Heart_file"
joblib.dump(DT1,joblib_file)
loaded_model1=joblib.load(open(joblib_file,'rb'))

joblib_file="Calories_file"
joblib.dump(DT2,joblib_file)
loaded_model2=joblib.load(open(joblib_file,'rb'))

