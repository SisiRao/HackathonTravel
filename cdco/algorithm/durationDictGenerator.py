
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


# In[2]:


train_file = r"train.csv"
df_train = pd.read_csv(train_file)


# In[3]:


df_train = df_train.loc[df_train['store_and_fwd_flag'] == 'N']
df_train = df_train.loc[df_train['pickup_latitude'] != df_train['dropoff_latitude']]
df_train = df_train.loc[df_train['pickup_longitude'] != df_train['dropoff_longitude']]


# In[4]:


df_train['time'] = df_train['pickup_datetime'].apply(lambda x: int(datetime.strptime(x, '%Y/%m/%d %H:%M:%S').timestamp()))


# In[109]:


def ret_schedule(cur_lat, cur_lon, cur_time, candidates, error, hist_time_win):
    ret = {}
    print(cur_time)
    print(hist_time_win)
    df_candidates = df_train.loc[((cur_time - hist_time_win*60*60*24) <= df_train['time'])  & (df_train['time'] < cur_time)]
    for num, pair in zip(candidates.keys(), candidates.values()):
        lat = pair[0]
        lon = pair[1]
        start_cir = Circle((cur_lat, cur_lon), radius = error)
        end_cir = Circle((lat, lon), radius = error)
        df_start = np.array([start_cir.contains_point([j, i]) for i,j in zip(df_candidates['pickup_longitude'], df_candidates['pickup_latitude'])])
        df_end = np.array([end_cir.contains_point([j, i]) for i,j in zip(df_candidates['dropoff_longitude'], df_candidates['dropoff_latitude'])])
        #df_start_lat = (df_candidates['pickup_latitude'] <= cur_lat+error) & (df_candidates['pickup_latitude'] >= cur_lat-error)
        #df_start_lon = (df_candidates['pickup_longitude'] <= cur_lon+error) & (df_candidates['pickup_longitude'] >= cur_lon-error)
        #df_end_lat = (df_candidates['dropoff_latitude'] <= lat+error) & (df_candidates['dropoff_latitude'] >= lat-error)
        #df_end_lon = (df_candidates['dropoff_longitude'] <= lon+error) & (df_candidates['dropoff_longitude'] >= lon-error)
        #df_finals = df_candidates.loc[df_start_lat & df_start_lon & df_end_lat & df_end_lon]
        df_finals = df_candidates.loc[df_start & df_end]
        ret[num] = []
        for hour in range(0, 24):
            df_cur_hour = df_finals.loc[pd.to_datetime(df_finals['pickup_datetime']).dt.hour == hour]
            s = np.sum(df_cur_hour['trip_duration']) - np.max(df_cur_hour['trip_duration'])*0.5 - np.min(df_cur_hour['trip_duration'])*0.5
            ret[num].append(s/len(df_cur_hour))
        ret[num].append(np.mean(ret[num]))
    return ret


# In[131]:


test_lon = -73.9584503173828
test_lat = 40.7274284362792
candidates = {1:[40.689249, -74.0445], 2:[40.779437, -73.963244], 3:[40.759011, -73.9844722], 4:[40.7828647, -73.9653551], 5:[40.7484405, -73.9856643999999], 6:[36.1314583, -95.9664236999999]}
error = 0.05
hist_time_win = 7
cur_time = "2016/3/12  14:00:11"
cur_time = int(datetime.strptime(cur_time, '%Y/%m/%d %H:%M:%S').timestamp())
source_data = {1:{'time':"2016/3/12  14:00:11", 'loc':[40.7274284362792, -73.9584503173828]}, 2:{'time':"2016/1/7  9:29:54", 'loc':[40.7557296752929, -73.9903182983398]}}
ret_list = {}
for idx in source_data:
    time = source_data[idx]['time']
    loc = source_data[idx]['loc']
    test_lat = loc[0]
    test_lon = loc[1]
    cur_time = int(datetime.strptime(time, '%Y/%m/%d %H:%M:%S').timestamp())
    ret_list[idx] = ret_schedule(test_lat, test_lon, cur_time, candidates, error, hist_time_win)


# In[132]:


print(ret_list)

