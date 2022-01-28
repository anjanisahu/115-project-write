#Plotting the data on the graph
import pandas as pd
import plotly.express as px
df = pd.read_csv("115.csv")
score_list = df["Score"].tolist()
accepted_list =df["Accepted"].tolist()


import numpy as np
score_array = np.array(score_list)
accepted_array =np.array(accepted_list)
m, c = np.polyfit(score_array,
accepted_array, 1)
y = []
for x in score_array:
  y_value = m*x + c
  y.append(y_value)
#plotting the graph
fig = px.scatter(x=score_array,
y=accepted_array)
fig.update_layout(shapes=[
dict(
type= 'line',
y0= min(y), y1= max(y),
x0= min(score_array), x1=
max(score_array)
)
])
fig.show()