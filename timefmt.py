"""Shared time-range helpers (12h, true overall range for blocks split at midnight)."""
import datetime as dt
def _m(t): h,m=map(int,t.split(':')); return h*60+m
def _p(m): m%=1440; h=m//60; return f"{(h%12) or 12}:{m%60:02d}", 'AM' if h<12 else 'PM'
def rng(s,e):
    (a,pa),(b,pb)=_p(_m(s)),_p(_m(e))
    return f"{a}–{b} {pb}" if pa==pb and _m(s)<_m(e) else f"{a} {pa}–{b} {pb}"
def true_range(ev,events):
    s,e=ev['start'],ev['end']; d=dt.date.fromisoformat(ev['date'])
    if s=='00:00':
        p=(d-dt.timedelta(1)).isoformat()
        for x in events:
            if x['date']==p and x['type']==ev['type'] and x['end']=='24:00': s=x['start']
    if e=='24:00':
        n=(d+dt.timedelta(1)).isoformat()
        for x in events:
            if x['date']==n and x['type']==ev['type'] and x['start']=='00:00': e=x['end']
    return rng(s,e)
