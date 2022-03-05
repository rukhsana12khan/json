import json

d={"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male",
 "Age":29}
y=open("merafile43.json","w") 
json.dump(d,y,indent=4)
y.close()








