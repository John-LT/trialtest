import json


file = open('usertest.json')
data = json.load(file)
file.close()

a = 0
for j in data:
    a += 1
    print("user"+str(a),'\n \tUsername:',j['username'],'\n','\tPhone:',j['phone'],'\n','\tLocation:',j['location'])
    
