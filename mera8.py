import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]  
e=[a,b,c,d]          
list=["name","designation","age","salary"]
f=["emp1","emp2","emp3","emp4"]
g={}
i=0
while i<len(e):
    h={}
    j=0
    while j<len(e[i]):
        if j==0:
            h[list[j]]=e[i][j]
            # print(h)
        if j==1:
            h[list[j]]=e[i][j]
            # print(h)
        if j==2:
            h[list[j]]=e[i][j]
            # print(h)
        if j==3:
            h[list[j]]=e[i][j]  
            # print(h)         
        j+=1
        g[f[i]]=h 
    i+=1    
# print(g)
with open ("myfile8.json","w") as f:
    json.dump(g,f,indent=4)