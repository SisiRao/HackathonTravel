
# coding: utf-8

# In[3]:


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from math import cos, asin, sqrt


# In[5]:


train_file = r"train.csv"
df_train = pd.read_csv(train_file)


# In[6]:


is_connected = df_train['store_and_fwd_flag'] == 'N'
is_good = (df_train['pickup_latitude'] != df_train['dropoff_latitude']) & (df_train['pickup_longitude'] != df_train['dropoff_longitude'])
df_train = df_train.loc[is_connected & is_good]


# In[7]:


y_start = df_train['pickup_latitude']
x_start = df_train['pickup_longitude']
y_end = df_train['dropoff_latitude']
x_end = df_train['dropoff_longitude']


# In[5]:


#distribution of pickup points
plt.scatter(x_start, y_start, color = "red", label = "pickup")


# In[6]:


#ditribution of dropoff points
plt.scatter(x_end, y_end, color = "blue", label = "dropoff")


# In[7]:


#combination plot
plt.scatter(x_start, y_start, color = "red", label = "pickup")
plt.scatter(x_end, y_end, color = "blue", label = "dropoff")


# In[8]:


#num of data for the two company repectively
company1 = df_train.loc[df_train['vendor_id'] == 1]
company2 = df_train.loc[df_train['vendor_id'] == 2]
print("total number of data: %d"%(len(x_start)))
print("num of data: company1:%d, company2:%d"%(len(company1), len(company2)))


# In[10]:


#distence calculation
def distance(lat, lon, lat_, lon_):
    p = 0.017453292519943295     #Pi/180
    ret  = []
    for lat1, lon1, lat2, lon2 in zip(lat, lon, lat_, lon_):
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        ret.append(12742 * asin(sqrt(a))*1000)
    return ret


# In[11]:


df_train['distance'] = distance(y_start, x_start, y_end, x_end)


# In[18]:


plt.xlabel('Trip Duration in Log')
plt.hist(np.log(df_train['distance']), bins = 50)


# In[19]:


plt.xlabel('Trip Duration in Log')
plt.hist(np.log(df_train['trip_duration']), bins = 50)


# In[11]:


step = 5000
dic = {}
for dist in range(int(min(df_train['distance'])), int(max(df_train['distance']+step)), step):
    num = len(df_train.loc[(float(dist-step)< df_train['distance']) & (df_train['distance']<=float(dist))])
    if num: dic[dist] = num
print("max of distance:%d"%max(df_train['distance']))
#print(dic)


# In[12]:


#hist between count and day
df_train['day'] = pd.to_datetime(df_train['pickup_datetime']).dt.day
df_day_count = df_train.groupby(['day'])['day'].agg(['count'])
plt.hist2d(dic.keys(), dic.values())


# In[18]:


#bar between count and hour
def draw_bars(key):
    if key == 'day':
        df_train[key] = pd.to_datetime(df_train['pickup_datetime']).dt.day
    elif key == 'hour':
        df_train[key] = pd.to_datetime(df_train['pickup_datetime']).dt.hour
    elif key == 'month':
        df_train[key] = pd.to_datetime(df_train['pickup_datetime']).dt.month
    df_count = df_train.groupby([key])[key].agg(['count'])
    df_count.plot.bar()


# In[19]:


draw_bars('hour')


# In[20]:


draw_bars('day')


# In[21]:


draw_bars('month')

