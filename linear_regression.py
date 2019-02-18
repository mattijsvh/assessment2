import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

USAhousing = pd.read_csv("C:/Users/matti/Desktop/USA_Housing.csv")

USAhousing.head()

#sns.pairplot(USAhousing)

print(USAhousing.corr())

#Pak alleen features die numeric zijn
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]

#Pak voor y-as de prijs feature
y = USAhousing['Price']

#Maak train en test subsets aan
#Test is 40% van totale data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#Maak linear model
lm = LinearRegression()

#Fit het lineare model op de train data
lm.fit(X_train,y_train)

#Pas voorspelling toe op testdata
predictions = lm.predict(X_test)

#R^2: Hoeveelheid verklaarbare variatie in de voorspellingen
lm.score(X,y)

#Plot de test data
plt.scatter(y_test,predictions)



