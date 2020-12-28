import pandas
from googlesearch import search 

df = pandas.read_csv('test1.csv')

result = []
for i in range(len(df['keys'])):
    for j in search(df['keys'][i], tld="com", num=3, stop=1, pause=2): 
        result.append(j)

dict1 = {'keys': df['keys'], 'url': result}  
df = pandas.DataFrame(dict1) 
df.to_csv('answer.csv')   