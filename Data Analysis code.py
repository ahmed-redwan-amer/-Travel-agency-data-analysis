import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv(r"C:\Users\Ahmed\Desktop\money fellows\sampled.csv")
data.head(5)

df=data
type(data)
df=df.drop("request_id",axis=1)
df=df.drop("client_id",axis=1)

s=df.source_id.value_counts().gt(8)
df.loc[df.source_id.isin(s[s].index)]
data = data[~data['source_id'].isin(['73.0','5.0','4.0','56.0','94.0','23.0','57.0','133.0','12.0','9.0','97.0','102.0','145.0','91.0','106.0','0.0','59.0','75.0','103.0','82.0','47.0','79.0','95.0','155.0','217.0','213.0','225.0','215.0','209.0','88.0','127.0','80.0','37.0','153.0','69.0','63.0','185.0'])]

s=df.sub_id.value_counts().gt(8)
df.loc[df.sub_id.isin(s[s].index)]
data = data[~data['sub_id'].isin(['30','167','40'])]


s=df.nation.value_counts().gt(8)
df.loc[df.nation.isin(s[s].index)]
df = df[~df['nation'].isin(["Peru","Philippines","Saudi Arabia","Switzerland","Belgium","Ireland","Malaysia","Ecuador","Japan","Russia","New Zealand","China","Pakistan","Singapore","Swaziland","Bangladesh","Bolivia","Uganda","Uruguay",
"Kenya","Portugal","Austria","Denmark","American Samoa","Jordan","Algeria","Syria","Costa Rica","Trinidad and Tobago","United Arab Emirates","Afghanistan","Wallis and Futuna","Albania","Nicaragua","Andorra",
"Sudan","United States Virgin Islands","Lebanon","Dominica","Yemen","Lesotho","Netherlands","Armenia","Morocco","Greece","South Korea","Thailand","Cyprus","Ukraine"
,"Bahamas","Romania","Bahrain","Brunei","Mauritius","Central African Republic","Salvadora","Venezuela","Anguilla","Oman","Czech Republic","Turkey","Cuba","Sweden","Kuwait"])]




df = df.drop(0 ,axis=0)
df = df.drop(999 ,axis=0)
df = df.drop(887 ,axis=0)
df = df.drop(762 ,axis=0)
df = df.drop(254 ,axis=0)
df=df.dropna(axis=0, subset=["arrival_date","departure_date"])

df.fillna(0,inplace=True)

df["num_of_adults"].fillna(method="ffill",inplace=True)


from collections import Counter
count_nation = Counter(list(zip(df.nation)))
count_nation = [list(i) for i in count_nation.items()]
count_nation = pd.DataFrame(count_nation)


count_currency = Counter(list(zip(df.currency_id)))
count_currency = [list(i) for i in count_currency.items()]
count_currency = pd.DataFrame(count_currency)

count_source_id = Counter(list(zip(df.source_id)))
count_source_id = [list(i) for i in count_currency.items()]
count_source_id = pd.DataFrame(count_source_id)


count_sub_id = Counter(list(zip(df.sub_id)))
count_sub_id = [list(i) for i in count_currency.items()]
count_sub_id = pd.DataFrame(count_sub_id)


count_adwords = Counter(list(zip(df.adwords)))
count_adwords = [list(i) for i in count_adwords.items()]
count_adwords = pd.DataFrame(count_adwords)


df.describe().transpose()

df.info()

f, ax = plt.subplots(figsize=(10, 10))
sns.countplot(y="source_id", data=data, color="c");
        
           
sns.catplot(y="adwords", hue="confemed", kind="count",
            palette="pastel", edgecolor=".6",
            data=df);
            
sns.catplot(y="sub_id", hue="sub_id", kind="count",
            palette="pastel", edgecolor=".6",
            data=data);
            
            
sns.catplot(y="nation", hue="adwords", kind="count",
            palette="pastel", edgecolor=".6",
            data=df);            
            

sns.catplot(y="num_of_children", hue="confemed", kind="count",
            palette="pastel", edgecolor=".6",
            data=df);


sns.catplot(x="currency_id", kind="count", palette="ch:.25", data=df);

sns.lmplot(x="time_of_vacation", y="num_of_adults", data= df,
           lowess=True);






































