import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df=pd.read_csv('data.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['maths score'],show_hist=False)
fig.show()
population_mean=statistics.mean(data)
print('population mean is : ',population_mean)
std_deviation=statistics.stdev(data)
print('stdev of population is : ',std_deviation)

def random_set_of_mean(counter):
  dataset=[]
  for i in range(0,counter):
    random_index=random.randint(0,len(data)-1)
    value=data[random_index]
    dataset.append(value)
  mean=statistics.mean(dataset)
  return(mean)

mean_list=[]
for i in range(0,1000):
  set_of_means=random_set_of_mean(100)
  mean_list.append(set_of_means)
std_deviation=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print('mean of sampling distribution is:',mean)
print('stdev of sampling distribution is : ',std_deviation)

fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name='Mean'))
fig.show()

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-2*std_deviation,mean+2*std_deviation
third_std_deviation_start,third_std_deviation_end=mean-3*std_deviation,mean+3*std_deviation
print('std1',first_std_deviation_start,first_std_deviation_end)
print('std2',second_std_deviation_start,second_std_deviation_end)
print('std3',third_std_deviation_start,third_std_deviation_end)

fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3'))
fig.show()

df=pd.read_csv('impact1.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([mean_list],['maths score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
impact1_mean=statistics.mean(data)
print('impact1 mean is : ',impact1_mean)
fig.add_trace(go.Scatter(x=[impact1_mean,impact1_mean],y=[0,0.17],mode='lines',name='Mean of sample 1'))
std_deviation1=statistics.stdev(data)
print('stdev of impact1 is : ',std_deviation1)
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='fist std dev 1 end'))
fig.show()

df=pd.read_csv('impact2.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([mean_list],['maths score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
impact2_mean=statistics.mean(data)
print('impact2 mean is : ',impact2_mean)
fig.add_trace(go.Scatter(x=[impact2_mean,impact2_mean],y=[0,0.17],mode='lines',name='Mean of sample 2'))
std_deviation1=statistics.stdev(data)
print('stdev of impact2 is : ',std_deviation1)
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='fist std dev end'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='second std dev end'))
fig.show()

df=pd.read_csv('impact3.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([mean_list],['maths score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
impact3_mean=statistics.mean(data)
print('impact3 mean is : ',impact3_mean)
fig.add_trace(go.Scatter(x=[impact3_mean,impact3_mean],y=[0,0.17],mode='lines',name='Mean of sample 3'))
std_deviation1=statistics.stdev(data)
print('stdev of impact3 is : ',std_deviation1)
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='fist std dev end'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='second std dev end'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='third std dev end'))
fig.show()