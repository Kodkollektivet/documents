import requests as rq
import csv

name = "http://api.kolada.se/v2/municipality/"

api_result = "http://api.kolada.se/v2/data/kpi/N03014/year/"
api_pop = "http://api.kolada.se/v2/data/kpi/N01951/year/"

result_res = rq.get(api_result+str(1998))

result_vals = []
for itm in result_res.json()["values"]: 
    if not "G" in itm["municipality"]: 
        result_vals.append((itm["municipality"],itm["period"],float(itm["values"][0]["value"]) )) 

popul_res = rq.get(api_pop+str(1998))
popul_vals = [] 
for itm in popul_res.json()["values"]: 
    if not "G" in itm["municipality"]: 
        try:
            popul_vals.append((itm["municipality"],itm["period"],float(itm["values"][2]["value"]) )) 
        except:
             popul_vals.append((itm["municipality"],itm["period"],None))

names_ko =  ",".join(  [val[0] for val in popul_vals] )
names_res = rq.get("http://api.kolada.se/v2/municipality/"+names_ko)

id_names = {row["id"]:row["title"] for row in names_res.json()["values"]}

with open("Pop.cvs","w") as pop:
    write_pop = csv.writer(pop)
    for row in popul_vals:
        write_pop.writerow(row)

with open("Res.cvs","w") as res:
    write_res = csv.writer(res)
    for row in result_vals:
        write_res.writerow(row)

with open("Names.cvs","w") as names:
    write_names = csv.writer(names)
    for key in id_names.keys():
        write_names.writerow( (key,id_names[key]) )
