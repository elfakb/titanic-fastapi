import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib 



df = pd.read_csv('/Users/elifakbas/Desktop/AI Engineering/+AI ENGINEERING ROADMAP/Bölüm 1-Python & ML Temelleri/Proje 1/titanic_project/Titanic-Dataset.csv')

df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']] # df için değişkenleri aldık 
df['Sex'] = df['Sex'].map({'male':0 , 'female': 1}) # cinsiyet değişkenini sayısal hale getirdik
df['Age'] = df['Age'].fillna(df['Age'].median()) # eksik yaşları doldurduk ort deeğerle

X = df.drop('Survived' , axis = 1) # ne istediğimizi belirledik
y = df['Survived'] 

# model eğitimi
model = RandomForestClassifier(n_estimators=100, random_state=42) # model oluştu
model.fit(X,y)

# modeli kaydet
joblib.dump(model , "titanic_model.pkl")
print("Model 'titanic_model.pkl' olarak kaydedildi!")

