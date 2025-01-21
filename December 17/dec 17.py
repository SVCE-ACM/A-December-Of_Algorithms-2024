l=[]
choice=1
n=0
while choice!=0:
    d = {}
    d["id"]=str(input("Enter id:"))
    d["timestamp"]=str(input("Enter timestamp:"))
    d["threat-level"]=int(input("Enter threat level:"))
    l.append(d)
    n+=1
    choice=int(input("Do you want to enter more values?(0/1)"))
l1=[]
for j in l:
    alert_id = j["id"]
    alert_timestamp = j["timestamp"]

    if alert_id not in [item["id"] for item in l1]:
        l1.append(j)
    else:
        for c in l1:
            if c["id"] == alert_id and c["timestamp"] < alert_timestamp:
                l1.remove(c)
                l1.append(j)
l2=[]
for d in l:
    for x in l1:
        if d["timestamp"]==x["timestamp"]:
            l2.append(d)
for k in l2:
    print(k)
    
                
        
    
