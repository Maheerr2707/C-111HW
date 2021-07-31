from typing import Counter
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["mathscore"].tolist()
fig = ff.create_distplot([data],["Math Scores"],show_hist=False)
#fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print(mean)
print(std_dev)

def randomsetofmean():
    dataset = []
    for i in range(0,30):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanList = []

def randomsetofmean(counter):
    dataset = []
    for i in range (0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    for i in range(0,100):
    setofmeans = randomsetofmean(30)
    meanList.append(setofmeans)
    show_fig(meanList)

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()    

sd_sapmle = statistics.stdev(meanList)
#sd is standard deviation

mean_sample = statistics.mean(meanList)

print(sd_sapmle)
print(mean_sample)

fig = ff.create_distplot([meanList],["Math Scores"],show_hist=False)
 
firstStandardDeviationStart,firstStandardDeviationEnd = mean-std_dev,mean+std_dev
secondStandardDeviationStart,secondStandardDeviationEnd = mean-(2*std_dev),mean+(2*std_dev)
thirdStandardDeviationStart,thirdStandardDeviationEnd = mean-(3*std_dev),mean+(3*std_dev)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[firstStandardDeviationStart,firstStandardDeviationStart],y=[0,0.17],mode="lines",name="FirstStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[firstStandardDeviationEnd,firstStandardDeviationEnd],y=[0,0.17],mode="lines",name="FirstStandardDeviationEnd"))

fig.add_trace(go.Scatter(x=[secondStandardDeviationStart,secondStandardDeviationStart],y=[0,0.17],mode="lines",name="SecondStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[secondStandardDeviationEnd,secondStandardDeviationEnd],y=[0,0.17],mode="lines",name="secondStandardDeviationEnd"))

fig.add_trace(go.Scatter(x=[thirdStandardDeviationStart,thirdStandardDeviationStart],y=[0,0.17],mode="lines",name="thirdStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[thirdStandardDeviationEnd,thirdStandardDeviationEnd],y=[0,0.17],mode="lines",name="ThirdStandardDeviationEnd"))


df3 = pd.read_csv("StudentsPerfomance.csv")
data3 = df3["mathscore"].tolist()
mean_sample3 = statistics.mean(data3)
print("mean of sample 1=",mean_sample3)


fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.17],mode = "lines", name = "mathScore"))
fig.show()

z_score3= (mean_sample - mean_sample3)/sd_sapmle
print("The z score3 is = ",z_score3)