import pandas as pd
import datetime as dt

dict={ "Date":dt.datetime(2011,1,1),
       "product":"Mi",
       "Type":"mobile",
       "cost":12000
        }

data=pd.read_csv("/home/vic/Downloads/MOCK_DATA.csv")
#df=pd.DataFrame(data)
data["date"]=pd.to_datetime(data.date)
#data.set_index('date',inplace=True)
#print(data.head())
#print(data[data.type=='tablet'].head())
print(data['product'][data.type=='tablet'])
print(data['type'][data.date=='2020-05-24'].describe())
#print(data.describe())


