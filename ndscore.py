import pandas as pd
import statistics 
import plotly.figure_factory as ff

df = pd.read_csv("score.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([df["Math_score"].tolist()], ["Height"], show_hist=False)
fig.show()

mean = statistics.mean(data)
sd = statistics.stdev(data)

range1_start, range1_end = mean - sd, mean + sd
range2_start, range2_end = mean - 2*sd, mean + 2*sd
range3_start, range3_end = mean - 3*sd, mean+ 3*sd

range1_array = [i for i in data if i > range1_start and i < range1_end]  
range2_array = [i for i in data if i > range2_start and i < range2_end]  
range3_array = [i for i in data if i > range3_start and i < range3_end]  

print(len(range1_array)*100/len(data))
print(len(range2_array)*100/len(data))
print(len(range3_array)*100/len(data))