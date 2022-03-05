dic={"shopping_list":{ 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } }
import json
s={}
for i in dic:
    s=dic[i]
    user=input("kon sa item chahiye")
    for j in s:
        if j==user:
            if user in s:
                iteam=int(input("kitne item chahiye"))
                total=(int(s[j])-iteam)
            break
    s[user]=str(total)
print(s)            
# y=open("myfile9.json","w")
# json.dump(s,y)
# y.close()


