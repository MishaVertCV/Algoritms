import pandas as pd
df = pd.read_csv('suck.csv')
my_df = pd.DataFrame({'id': [1, 2, 3],
'name': ['Bob', 'Alice', 'Scott'],
'age': [21, 15, 30]})
df.rename(columns = {'Overall rank':'Место в рейтинге', 
'Country or region':'Страна или регион', 
'Score':'Баллы', 'GDP per capita':'ВВП на душу населения', 
'Social support':'Социальная поддержка', 
'Healthy life expectancy':'Ожидаемая продолжительность здоровой жизни', 
'Freedom to make life choices':'Свобода жизненных выборов', 
'Generosity':'Щедрость', 'Perceptions of corruption':'Восприятие коррупции'}, 
inplace = True)
df.head()
print(df.head())
print(df.describe())
print(df.plot.scatter(x = 'Место в рейтинге', y = 'ВВП на душу населения'))
