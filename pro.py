#Plotting the data on the graph
from turtle import color
from cv2 import COLOR_Luv2RGB
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt 
import logisticRegression as lp
df = pd.read_csv("115.csv")
score_list = df["Score"].tolist()
accepted_list =df["Accepted"].tolist()
X=np.reshape(score_list,(len(score_list),1))
Y=np.reshape(accepted_list,(len(accepted_list),1))
lr=lp()
lr.fit(X,Y)
plt.figure()
#scatter plot
plt.scatter(X.ravel(),Y,color="black",zorder=20)
def model(x): 
    return 1 / (1 + np.exp(-x)) 
    #Using the line formula 
    
X_test = np.linspace(0, 100, 200)
chances = model(X_test * lr.coef_ + lr.intercept_).ravel()
plt.plot(X_test, chances, color='red', linewidth=3) 
plt.axhline(y=0, color='k', linestyle='-') 
plt.axhline(y=1, color='k', linestyle='-') 
plt.axhline(y=0.5, color='b', linestyle='--') 
# do hit and trial by changing the value of X_test 
plt.axvline(x=X_test[165], color='b', linestyle='--') 
plt.ylabel('y') 
plt.xlabel('X') 
plt.xlim(75, 85) 
plt.show()