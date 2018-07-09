
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import os
os.getcwd()


# In[33]:


# read sights.csv
sights = pd.read_csv(r"sights.csv") 


# In[34]:


# hardcode
my_loc = [-73.9584503173828,40.7274284362792]


# In[35]:


duration_dict = {1: [739.639344262295, 714.2045454545455, 732.5714285714286, 604.3666666666667, 407.3333333333333, 570.3214285714286, 629.6351351351351, 855.1084337349398, 994.2027027027027, 1061.157894736842, 1010.2760416666666, 1004.8693181818181, 1020.7105263157895, 1567.8658536585365, 982.1125, 1132.2083333333333, 1001.1083333333333, 988.72, 1003.1699029126214, 920.0442477876106, 839.5783132530121, 883.1173913043478, 830.2452830188679, 825.3510638297872, 888.2465842402102], 2: [806.1134930643127, 700.6946983546618, 716.8645598194131, 588.6822580645161, 728.6111111111111, 386.88528138528136, 422.5528771384137, 563.0468904244817, 707.277878513146, 808.7552724077328, 696.4080779944289, 733.4929343308396, 757.1273092369478, 877.666017147311, 764.4735023041475, 906.7677685950413, 832.0190771960959, 883.2945508100147, 714.6460459183673, 766.4466501240695, 668.0939306358382, 799.8499298737728, 757.1101503759398, 635.1818600368324, 717.5859218692798],4: [818.7688311688312, 703.0549242424242, 725.9858823529412, 591.4322033898305, 524.7525, 390.43973214285717, 422.17167721518985, 565.0567839195979, 712.1380111524163, 814.8339301700985, 697.5461828463714, 737.7950043066322, 757.3867610324729, 880.7878909382518, 768.7476303317535, 914.6128486897718, 836.942481884058, 890.9165402124431, 718.4715608465608, 772.125, 668.1973194341027, 804.5985454545455, 698.5564142194745, 635.6102099236641, 710.4553694114287]}


# In[36]:


sights


# In[37]:


# 计算两地的实际走路需要的距离
from math import cos, asin, sqrt
def distance(lat, lon, lat_, lon_):
    p = 0.017453292519943295     #Pi/180
    ret  = []
    for lat1, lon1, lat2, lon2 in zip(lat, lon, lat_, lon_):
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        ret.append(12742 * asin(sqrt(a)))
    return ret


# In[38]:


sights


# In[39]:


# input:
# * duration_dict(prefer_sight)
# * sights detail
# * begin_time and end_time
import sys
duration_df = pd.DataFrame.from_dict(duration_dict,orient='index')
duration_df = duration_df/60

place_list = duration_df.index.tolist()
print(place_list)


# In[40]:


data = duration_df

y_start = sights.loc[place_list, 'latitude']
x_start = sights.loc[place_list, 'longitude']
y_end = [(my_loc[1])]*len(place_list)
x_end = [(my_loc[0])]*len(place_list)


# In[41]:


def hour2min(hour_list, a):
    hour_list[a] = hour_list[a].apply(lambda x: int(x.split(':')[0])*60+int(x.split(':')[1]))
    return hour_list

data['distance'] = distance(y_start, x_start, y_end, x_end)
data['open_time_start'] = sights.loc[place_list, 'open_time_start']
data['open_time_end'] = sights.loc[place_list, 'open_time_end']
data['spend_time'] = sights.loc[place_list, 'spend_time']*60
data['visit_begin'] = "10:00"
data['visit_end'] = "18:00"

data = hour2min(data,"open_time_start")
data = hour2min(data,"open_time_end")
data = hour2min(data,"visit_begin")
data = hour2min(data,"visit_end")

data['visit_range'] = data["visit_end"] - data["visit_begin"]
data


# In[42]:


import math


# In[43]:


def time_format(now_time):
    hour = int(now_time/60)
    minute = now_time - int(now_time/60)*60
    if not (minute//10):
        return "%d:0%d"%(hour, minute)
    return "%d:%d"%(hour, minute)

def one_visit(now_time, df, sights, now_location, schedule, existed_order):
    while(now_time < visit_end and (not df.empty)):
        #pick the next place
        flag = False
        #print(existed_order)
        df_cur = []
        for idx in df.index[::-1]:
            #print(idx, len(place_order))
            if idx in existed_order[len(place_order)]:
                #print(idx, len(place_order))
                df_cur = df.drop(idx, axis = 0)
                flag = True
        if flag:
            t = (df_cur[math.ceil(now_time//60)]-df_cur[24]).idxmin()
            #print(df_cur)
        else:
            #print("df")
            t = (df[math.ceil(now_time//60)]-df[24]).idxmin()
        
        #check whether the finishing time is bigger than the visit ending time
        estimate_time = now_time + int(df.loc[t,int(now_time/60)]) + df.loc[t,"spend_time"]
        if estimate_time > visit_end:
            break
            
        #add the number of the palce to the schedule
        place_order.append(t)       

        timeline = {
            "time_start": time_format(now_time),
            "start_lat": now_location[0],
            "start_lon": now_location[1],
            "spend_time": int(df.loc[t,int(now_time/60)])
        }
        
        #add the traffic time and change to the new location
        now_time += int(df.loc[t,int(now_time/60)])
        now_location = [sights.loc[t, "longitude"],sights.loc[t, "latitude"]]
        timeline["time_end"] = time_format(now_time)
        timeline["end_lat"] = now_location[0]
        timeline["end_lon"] = now_location[1]
        timeline["end_sights"] = t
        schedule.append(timeline)

        #add the visit time
        now_time += df.loc[t,"spend_time"]
        timeline = {
            "time_start": time_format(now_time - df.loc[t,"spend_time"]),
            "start_lat": now_location[0],
            "start_lon": now_location[1],
            "spend_time": int(df.loc[t,"spend_time"]),
            "time_end": time_format(now_time),
            "end_lat": now_location[0],
            "end_lon": now_location[1],
            "end_sights": t
        }
        schedule.append(timeline)
        #begin the next generation
        m = t
        #print(m)
        #delete the visited place
        df = df.drop(t,axis=0)
    return now_time, df, sights, now_location, schedule, place_order


# In[44]:


existed_order = {idx:[] for idx in range(len(data))}
schedule_plan = []

for times in range(3):
    #initial condition
    place_order = []
    schedule = []
    visit_end = 1080
    visit_begin = 600
    now_time = visit_begin
    now_location = my_loc
    m = 0 # initial location
    
    now_time, df, sights, now_location, schedule, place_order = one_visit(now_time, data, sights, now_location, schedule, existed_order)
    for idx, item in enumerate(place_order):
        existed_order[idx].append(item)
    schedule_plan.append(schedule)
    print(schedule)