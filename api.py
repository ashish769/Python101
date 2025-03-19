#api=Application programming interface --->it is used to communicate two or more program or software to in teract with each other
# DRF-django rest framework
# json-->javascript object notation-->java script ko ibject jasto dekhni vayerw javascript object notation rakheko ho
# it is help to understand the data in all programming languagetype--string formate
# json-->is used to store and transfer the data from web browser to server and vice versa
#json vitra ko data jaile pani""vitra hunx
a={
    "name":'sujan',
    'age':99
}
print(a)
print(type(a))

import json
b=json.dumps(a)#it is used to convert python  dictionary to json string
print(b)
print(type(b))

f=open('msg.json','r')
var=f.read()

print(var)
v=json.loads(var)#itis used to convert json to python dictionary
print(v)
print(type(v))

with open('msg.json','r') as f:
    v=json.load(f)#it load all the content line by line