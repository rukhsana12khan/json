# import json 
# dict1 ='{"name":"Lisa","designation":"programmer","age":"34","salary":"54000"}'
# y=json.loads(dict1)
# print(y)
# print(type(y))

# import json
# dict1 ='{"name":"Lisa","designation":"programmer","age":"34","salary":"54000"}'
# y=open("myfilesave.json","")
# json.load(dict1)
# y.close()


a={2:3,5:6,4:2,1:5}
s={}
for i in a.items():
    if a[i]==1:
        s[i]=i
        print(s)