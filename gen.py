#!/usr/bin/env python3
"""Generate data/schedule.json. Edit EVENTS (or regenerate from schedule.md) then run update.sh."""
import json,datetime
E=[]
def ev(d,s,e,t,l,n="",split=None):
    if t in("commute","meal"): return
    if t=="meal":
        if l.startswith(("Drive","Home")): t="commute"; l=l.split(" +")[0]; n=""
        else: return
    x={"date":(f"2026-10-{d:02d}" if isinstance(d,int) else d),"start":s,"end":e,"type":t,"label":l,"notes":n}
    if split:x["split"]=split
    E.append(x)
# Sat 17
ev(17,"00:00","04:00","sleep","Sleep")
ev(17,"04:00","04:20","meal","Breakfast")
ev(17,"04:20","05:00","commute","Prep + commute")
ev(17,"05:00","15:30","chartright","Chartright shift")
ev(17,"10:30","11:00","meal","Lunch at work")
ev(17,"15:30","16:00","meal","Drive to gym + packed dinner","30-min drive; eat packed dinner on the way")
ev(17,"16:00","18:00","workout","Chest & Shoulders","2h, straight from work","Chest & Shoulders")
ev(17,"18:00","19:00","commute","Drive home")
ev(17,"19:00","24:00","sleep","Sleep","Only 6.75h (19:00-01:45) - nap after Sun EA shift")
# Sun 18
ev(18,"00:00","01:45","sleep","Sleep")
ev(18,"01:45","02:45","commute","Prep + commute")
ev(18,"02:45","06:30","ea","EA – YKF GH Lead")
ev(18,"06:30","07:30","meal","Home + breakfast")
ev(18,"07:30","10:30","sleep","Nap")
ev(18,"11:00","11:30","meal","Lunch")
ev(18,"11:30","12:00","commute","Drive to gym")
ev(18,"12:00","14:00","workout","Back & Hamstrings","","Back & Hamstrings")
ev(18,"14:00","14:30","commute","Drive home")
ev(18,"14:30","21:00","guelph","Open for Guelph")
ev(18,"18:30","19:00","meal","Dinner")
ev(18,"22:30","24:00","sleep","Sleep")
# Mon 19
ev(19,"00:00","07:00","sleep","Sleep")
ev(19,"07:30","08:00","meal","Breakfast")
ev(19,"08:00","08:30","commute","Drive to gym")
ev(19,"08:30","10:30","workout","Quads & Calves","","Quads & Calves")
ev(19,"10:30","11:00","commute","Drive home")
ev(19,"13:30","16:00","guelph","Optional: Guelph visit (potential)","Tentative; leave by 17:00 for 18:00 EA shift")
ev(19,"12:30","13:00","meal","Lunch")
ev(19,"16:15","16:45","meal","Early dinner")
ev(19,"17:00","18:00","commute","Commute")
ev(19,"18:00","21:00","ea","EA – YKF GH Lead")
ev(19,"21:00","22:00","commute","Commute home + snack")
# Tue 20
ev(20,"01:00","09:00","sleep","Sleep","Later bedtime for late shift")
ev(20,"09:15","09:45","meal","Breakfast")
ev(20,"10:00","13:15","guelph","Optional: Guelph visit (potential)","Tentative; Chartright at 15:00")
ev(20,"13:00","13:30","meal","Lunch")
ev(20,"14:00","15:00","commute","Commute")
ev(20,"15:00","24:00","chartright","Chartright shift","Rest day; ends 01:30 Wed")
ev(20,"19:30","20:00","meal","Dinner at work")
# Wed 21
ev(21,"00:00","01:30","chartright","Chartright shift (cont.)")
ev(21,"01:30","02:30","commute","Commute home")
ev(21,"02:30","07:00","sleep","Sleep","Only 4.5h")
ev(21,"07:00","07:20","meal","Breakfast")
ev(21,"07:20","08:00","commute","Commute")
ev(21,"08:00","18:30","chartright","Chartright shift","Rest day")
ev(21,"12:30","13:00","meal","Lunch at work")
ev(21,"18:30","19:30","commute","Commute home")
ev(21,"19:30","20:00","meal","Quick dinner")
ev(21,"20:00","24:00","sleep","Sleep","6.5h – nap if you can")
# Thu 22
ev(22,"00:00","02:30","sleep","Sleep")
ev(22,"02:30","02:50","meal","Breakfast")
ev(22,"02:50","03:30","commute","Prep + commute")
ev(22,"03:30","14:00","chartright","Chartright shift")
ev(22,"09:30","10:00","meal","Lunch at work")
ev(22,"14:00","14:30","commute","Drive to gym")
ev(22,"14:30","16:30","workout","Shoulders & Triceps","","Shoulders & Triceps")
ev(22,"16:30","17:30","commute","Drive home")
ev(22,"18:00","18:30","meal","Dinner")
ev(22,"21:30","24:00","sleep","Sleep")
# Fri 23
ev(23,"00:00","07:30","sleep","Sleep")
ev(23,"15:30","17:30","workout","Back & Biceps","After the ceremony; skip if grad runs late","Back & Biceps")
ev(23,"08:30","09:30","event","🎓 Gown pickup","Must be done the morning of")
ev(23,"10:00","13:00","event","🎓 Graduation – UWaterloo","Ends around 13:00 at the latest")
ev(23,"18:00","19:30","meal","Celebration dinner")
ev(23,"19:30","21:00","guelph","Open for Guelph (if free)")
ev(23,"21:00","24:00","sleep","Sleep","Only 7h (wake 04:00 for Sat 05:00 shift) - bed 20:00 for 8h")
# ---- Week 2 (Payworks: no EA shifts Oct 20-Nov 1) ----
def gym(d,ds,gs,ge,de,dh,name):
    ev(d,ds,gs,"commute","Drive to gym"); ev(d,gs,ge,"workout",name,"2h",name); ev(d,ge,de if dh else de,"commute","Drive home")
# Sat 24
ev(24,"00:00","04:00","sleep","Sleep")
ev(24,"04:00","05:00","commute","Prep + commute")
ev(24,"05:00","15:30","chartright","Chartright shift")
gym(24,"15:30","16:00","18:00","19:00",1,"Hamstrings & Quads")
ev(24,"22:00","24:00","sleep","Sleep")
# Sun 25
ev(25,"00:00","06:00","sleep","Sleep")
gym(25,"09:30","10:00","12:00","12:30",1,"Arms & Calves")
ev(25,"13:30","20:30","guelph","Optional: Guelph visit (potential)","Tentative; watch for open EA coverage shift (03:00–06:30)")
ev(25,"22:30","24:00","sleep","Sleep")
# Mon 26
ev(26,"00:00","06:30","sleep","Sleep")
gym(26,"09:30","10:00","12:00","12:30",1,"Chest & Shoulders")
ev(26,"13:00","21:00","guelph","Open for Guelph")
ev(26,"22:30","24:00","sleep","Sleep")
# Tue 27
ev(27,"00:00","06:30","sleep","Sleep")
gym(27,"09:00","09:30","11:30","12:00",1,"Back & Hamstrings")
ev(27,"12:30","19:00","guelph","Open for Guelph","Back by 19:00 - early bed for Wed 05:00 shift")
ev(27,"20:00","24:00","sleep","Sleep","Wake 04:00")
# Wed 28 (rest)
ev(28,"00:00","04:00","sleep","Sleep")
ev(28,"04:00","05:00","commute","Prep + commute")
ev(28,"05:00","15:30","chartright","Chartright shift","Rest day")
ev(28,"15:30","16:30","commute","Commute home")
ev(28,"18:30","24:00","sleep","Sleep","Thu shift 03:30, wake 02:30")
# Thu 29
ev(29,"00:00","02:30","sleep","Sleep")
ev(29,"02:30","03:30","commute","Prep + commute")
ev(29,"03:30","14:00","chartright","Chartright shift")
gym(29,"14:00","14:30","16:30","17:30",1,"Quads & Calves")
ev(29,"18:30","24:00","sleep","Sleep","Fri shift 03:30, wake 02:30")
# Fri 30 (rest)
ev(30,"00:00","02:30","sleep","Sleep")
ev(30,"02:30","03:30","commute","Prep + commute")
ev(30,"03:30","14:00","chartright","Chartright shift","Rest day")
ev(30,"14:00","15:00","commute","Commute home")
ev(30,"15:30","19:00","guelph","Open for Guelph","Back by 19:00 - early bed for Sat 05:00 shift")
ev(30,"20:00","24:00","sleep","Sleep","Wake 04:00")
# ---- Week 3: Sat Oct 31 - Fri Nov 6 (Payworks: no EA shifts Oct 24-31; Nov not readable yet) ----
N=lambda d:f"2026-11-{d:02d}"
# Sat 31
ev(31,"00:00","04:00","sleep","Sleep")
ev(31,"05:00","15:30","chartright","Chartright shift")
gym(31,"15:30","16:00","18:00","18:30",1,"Shoulders & Triceps")
ev(31,"22:00","24:00","sleep","Sleep","Clocks fall back at 02:00 tonight (extra hour)")
# Sun Nov 1
ev(N(1),"00:00","06:00","sleep","Sleep")
gym(N(1),"09:30","10:00","12:00","12:30",1,"Back & Biceps")
ev(N(1),"13:00","17:30","guelph","Open for Guelph","Back before the 18:00 board meeting")
ev(N(1),"22:30","24:00","sleep","Sleep")
# Mon Nov 2
ev(N(2),"00:00","06:30","sleep","Sleep")
gym(N(2),"09:30","10:00","12:00","12:30",1,"Hamstrings & Quads")
ev(N(2),"13:00","21:00","guelph","Open for Guelph")
ev(N(2),"22:30","24:00","sleep","Sleep")
# Tue Nov 3
ev(N(3),"00:00","06:30","sleep","Sleep")
gym(N(3),"09:00","09:30","11:30","12:00",1,"Arms & Calves")
ev(N(3),"12:30","19:00","guelph","Open for Guelph","Back by 19:00 - early bed for Wed 05:00 shift")
ev(N(3),"20:00","24:00","sleep","Sleep","Wake 04:00")
# Wed Nov 4 (rest)
ev(N(4),"00:00","04:00","sleep","Sleep")
ev(N(4),"05:00","15:30","chartright","Chartright shift","Rest day")
ev(N(4),"22:00","24:00","sleep","Sleep")
# Thu Nov 5
ev(N(5),"00:00","06:00","sleep","Sleep")
gym(N(5),"09:00","09:30","11:30","12:00",1,"Chest & Shoulders")
ev(N(5),"12:30","17:00","guelph","Open for Guelph","Back by 17:00 - bed 18:30 for Fri 03:30 shift")
ev(N(5),"18:30","24:00","sleep","Sleep","Fri shift 03:30, wake 02:30")
# Fri Nov 6 (rest)
ev(N(6),"00:00","02:30","sleep","Sleep")
ev(N(6),"03:30","14:00","chartright","Chartright shift","Rest day")
ev(N(6),"15:30","19:00","guelph","Open for Guelph","Back by 19:00 - early bed for Sat 05:00 shift")
ev(N(6),"20:00","24:00","sleep","Sleep","Wake 04:00")
# ---- Week 4: Sat Nov 7 - Fri Nov 13 (released Oct 23) ----
# Sat Nov 7
ev(N(7),"00:00","04:00","sleep","Sleep")
ev(N(7),"05:00","15:30","chartright","Chartright shift")
gym(N(7),"15:30","16:00","18:00","18:30",1,"Back & Hamstrings")
ev(N(7),"22:00","24:00","sleep","Sleep")
# Sun Nov 8
ev(N(8),"00:00","06:00","sleep","Sleep")
gym(N(8),"08:30","09:00","11:00","11:30",1,"Quads & Calves")
ev(N(8),"15:00","24:00","chartright","Chartright shift","Ends 01:30 Mon; overlaps the 18:00 board meeting")
# Mon Nov 9 (rest)
ev(N(9),"00:00","01:30","chartright","Chartright shift (cont.)")
ev(N(9),"02:30","10:30","sleep","Sleep","After late shift")
ev(N(9),"15:00","24:00","chartright","Chartright shift","Rest day; ends 01:30 Tue")
# Tue Nov 10
ev(N(10),"00:00","01:30","chartright","Chartright shift (cont.)")
ev(N(10),"02:30","10:30","sleep","Sleep","After late shift")
gym(N(10),"11:30","12:00","14:00","14:30",1,"Shoulders & Triceps")
ev(N(10),"15:00","19:00","guelph","Open for Guelph","Back by 19:00 - early bed for Wed 05:00 shift")
ev(N(10),"20:00","24:00","sleep","Sleep","Wake 04:00; hard flip after two late shifts")
# Wed Nov 11 (rest)
ev(N(11),"00:00","04:00","sleep","Sleep")
ev(N(11),"05:00","15:30","chartright","Chartright shift","Rest day")
ev(N(11),"18:30","24:00","sleep","Sleep","Thu shift 03:30, wake 02:30")
# Thu Nov 12
ev(N(12),"00:00","02:30","sleep","Sleep")
ev(N(12),"03:30","14:00","chartright","Chartright shift")
gym(N(12),"14:00","14:30","16:30","17:00",1,"Back & Biceps")
ev(N(12),"22:00","24:00","sleep","Sleep")
# Fri Nov 13
ev(N(13),"00:00","06:00","sleep","Sleep")
gym(N(13),"09:00","09:30","11:30","12:00",1,"Hamstrings & Quads")
ev(N(13),"12:30","21:00","guelph","Open for Guelph")
ev(N(13),"22:30","24:00","sleep","Sleep")
# ---- Recurring: Weekly board meeting, every Sunday 18:00-18:30 from 2026-10-18, through the planned range ----
_ds=sorted({x["date"] for x in E}); _d=max(datetime.date(2026,10,18),datetime.date.fromisoformat(_ds[0])); _end=datetime.date.fromisoformat(_ds[-1])
_d+=datetime.timedelta((6-_d.weekday())%7)
while _d<=_end:
    _iso=_d.isoformat(); _g=any(x["date"]==_iso and x["type"]=="guelph" and x["start"]<"18:30" and x["end"]>"18:00" for x in E)
    E.append({"date":_iso,"start":"18:00","end":"18:30","type":"event","label":"Weekly board meeting with the crew","notes":"Recurring weekly (Sun)"+(" - overlaps Guelph open slot" if _g else ""),"recurrence":"FREQ=WEEKLY;BYDAY=SU"})
    _d+=datetime.timedelta(7)
for i,x in enumerate(E):x["id"]=f"e{i+1}"
json.dump({"timezone":"America/Toronto","updated":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),"events":E},open("data/schedule.json","w"),indent=1,ensure_ascii=False)
print(len(E),"events")
