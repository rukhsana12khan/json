import json
# a={'4': 5,'6': 7,'1': 3,'2': 4}
# k=list(a)
# # print(k)
# k.sort()
# #print(k)
# s={}
# for i in k:
#     for j in a:
#         if i==j:
#             s[j]=j
#             d=json.dumps(s)
# print(d)    

x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
y=json.dumps(x,indent=4,sort_keys=True)
print(y)    