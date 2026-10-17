#!/usr/bin/env python3
"""Generate data/schedule.json. Edit EVENTS (or regenerate from schedule.md) then run update.sh."""
import json,datetime
E=[]
def ev(d,s,e,t,l,n="",split=None):
    x={"date":f"2026-10-{d:02d}","start":s,"end":e,"type":t,"label":l,"notes":n}
    if split:x["split"]=split
    E.append(x)
# Sat 17
ev(17,"00:00","04:00","sleep","Sleep")
ev(17,"04:00","04:30","meal","Breakfast")
ev(17,"04:00","05:00","commute","Prep + commute")
ev(17,"05:00","15:30","chartright","Chartright shift")
ev(17,"10:30","11:00","meal","Lunch at work")
ev(17,"15:30","16:30","commute","Commute home")
ev(17,"16:30","17:15","workout","Chest & Shoulders","Shortened to 45 min","Chest & Shoulders")
ev(17,"17:15","17:45","meal","Early dinner")
ev(17,"18:00","24:00","sleep","Sleep","Up at 01:45 for EA")
# Sun 18
ev(18,"00:00","01:45","sleep","Sleep")
ev(18,"01:45","02:45","commute","Prep + commute")
ev(18,"02:45","06:30","ea","EA – YKF GH Lead")
ev(18,"06:30","07:30","meal","Home + breakfast")
ev(18,"07:30","10:30","sleep","Nap")
ev(18,"11:00","11:30","meal","Lunch")
ev(18,"12:00","13:15","workout","Back & Hamstrings","","Back & Hamstrings")
ev(18,"13:45","21:00","guelph","Open for Guelph")
ev(18,"18:30","19:00","meal","Dinner")
ev(18,"22:30","24:00","sleep","Sleep")
# Mon 19
ev(19,"00:00","07:00","sleep","Sleep")
ev(19,"07:30","08:00","meal","Breakfast")
ev(19,"08:45","10:00","workout","Quads & Calves","","Quads & Calves")
ev(19,"10:45","16:15","guelph","Open for Guelph","Back before 17:00 departure")
ev(19,"12:30","13:00","meal","Lunch")
ev(19,"16:15","16:45","meal","Early dinner")
ev(19,"17:00","18:00","commute","Commute")
ev(19,"18:00","21:00","ea","EA – YKF GH Lead")
ev(19,"21:00","22:00","commute","Commute home + snack")
# Tue 20
ev(20,"01:00","09:00","sleep","Sleep","Later bedtime for late shift")
ev(20,"09:15","09:45","meal","Breakfast")
ev(20,"13:00","13:30","meal","Lunch")
ev(20,"14:00","15:00","commute","Commute")
ev(20,"15:00","24:00","chartright","Chartright shift","Rest day; ends 01:30 Wed")
ev(20,"19:30","20:00","meal","Dinner at work")
# Wed 21
ev(21,"00:00","01:30","chartright","Chartright shift (cont.)")
ev(21,"01:30","02:30","commute","Commute home")
ev(21,"02:30","07:00","sleep","Sleep","Only 4.5h")
ev(21,"07:00","08:00","commute","Commute")
ev(21,"07:15","07:45","meal","Breakfast")
ev(21,"08:00","18:30","chartright","Chartright shift","Rest day")
ev(21,"12:30","13:00","meal","Lunch at work")
ev(21,"18:30","19:30","commute","Commute home")
ev(21,"19:30","20:00","meal","Quick dinner")
ev(21,"20:00","24:00","sleep","Sleep","6.5h – nap if you can")
# Thu 22
ev(22,"00:00","02:30","sleep","Sleep")
ev(22,"02:45","03:15","meal","Breakfast")
ev(22,"02:30","03:30","commute","Prep + commute")
ev(22,"03:30","14:00","chartright","Chartright shift")
ev(22,"09:30","10:00","meal","Lunch at work")
ev(22,"14:00","15:00","commute","Commute home")
ev(22,"15:00","16:15","workout","Shoulders & Triceps","","Shoulders & Triceps")
ev(22,"18:00","18:30","meal","Dinner")
ev(22,"21:30","24:00","sleep","Sleep")
# Fri 23
ev(23,"00:00","05:30","sleep","Sleep")
ev(23,"06:00","06:30","meal","Breakfast")
ev(23,"06:45","08:00","workout","Back & Biceps","Move to evening if ceremony is in the morning","Back & Biceps")
ev(23,"10:00","15:00","event","🎓 Graduation – UWaterloo","Placeholder time – confirm ceremony time")
ev(23,"18:00","19:30","meal","Celebration dinner")
ev(23,"19:30","21:00","guelph","Open for Guelph (if free)")
ev(23,"21:00","24:00","sleep","Sleep","Sat shift 05:00, wake 04:00")
for d,s,e in [(24,"05:00","15:30"),(28,"05:00","15:30"),(29,"03:30","14:00"),(30,"03:30","14:00")]:
    ev(d,s,e,"chartright","Chartright shift")
for i,x in enumerate(E):x["id"]=f"e{i+1}"
json.dump({"timezone":"America/Toronto","updated":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),"events":E},open("data/schedule.json","w"),indent=1,ensure_ascii=False)
print(len(E),"events")
