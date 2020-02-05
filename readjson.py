import json


file = open('usertest.json')
data = json.load(file)
file.close()

a = 0
place = ['bangalore','chennai','mumbai','bangalore','hyderabad','chandigarh','delhi','kochin','calcutta']

for j in data:
    a += 1
    if j['location'] in place:
        area = 'Urban'

    else:
        area = 'Rural'
    print("user"+str(a),"\n \tUsername:",j['username'],"\n","\tPhone:",j['phone'],"\n","\tLocation:",j['location'],"\n","\tAREA:",area)
