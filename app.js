
const TYPES=["chartright","ea","sleep","workout","guelph","event"],NAMES={chartright:"Chartright",ea:"EA",sleep:"Sleep",workout:"Workout",meal:"Meal",commute:"Commute",guelph:"Guelph",event:"Event"};
const K="schedule.overrides.v1",PX=40;let base=null,ov=JSON.parse(localStorage.getItem(K)||'{"edits":{},"deleted":[],"added":[]}'),view=innerWidth<700?"day":"week",cur=new Date(),editing=null;
const pad=n=>String(n).padStart(2,"0"),iso=d=>d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate()),mins=t=>{const[h,m]=t.split(":").map(Number);return h*60+m};
const parse=s=>{const[y,m,d]=s.split("-").map(Number);return new Date(y,m-1,d)};
function events(){const del=new Set(ov.deleted);return base.events.filter(e=>!del.has(e.id)).map(e=>ov.edits[e.id]?{...e,...ov.edits[e.id],_o:1}:e).concat(ov.added.map(e=>({...e,_o:1})))}
function save(){localStorage.setItem(K,JSON.stringify(ov));render()}
function nOv(){return Object.keys(ov.edits).length+ov.deleted.length+ov.added.length}
function weekStart(d){const x=new Date(d);x.setDate(x.getDate()-x.getDay());x.setHours(0,0,0,0);return x} // Sunday-start... use Sat:
function wStart(d){const x=new Date(d);x.setHours(0,0,0,0);x.setDate(x.getDate()-((x.getDay()+1)%7));return x}
function setView(v){view=v;render()}function nav(k){cur.setDate(cur.getDate()+(view=="week"?7:1)*k);render()}function goToday(){cur=new Date();render()}
function fmt(t){const m=mins(t)%1440;return pad(Math.floor(m/60))+":"+pad(m%60)}
function m12(m){m%=1440;return[pad(Math.floor(m/60))+":"+pad(m%60),""]}
function rng(s,e){return fmt(s)+"–"+fmt(e)}
function trueRng(ev,E){let s=ev.start,e=ev.end;const d=parse(ev.date);if(s=="00:00"){const p=new Date(d);p.setDate(p.getDate()-1);const x=E.find(x=>x.date==iso(p)&&x.type==ev.type&&x.end=="24:00");if(x)s=x.start}
if(e=="24:00"){const n=new Date(d);n.setDate(n.getDate()+1);const x=E.find(x=>x.date==iso(n)&&x.type==ev.type&&x.start=="00:00");if(x)e=x.end}return rng(s,e)}
function render(){vw.className=view=="week"?"on":"";vd.className=view=="day"?"on":"";const n=nOv();banner.style.display=n?"flex":"none";bantxt.textContent=`✎ ${n} local change${n>1?"s":""} (saved on this device only)`;
const E=events(),today=iso(new Date());main.innerHTML="";
if(view=="week"){const s=wStart(cur),days=[...Array(7)].map((_,i)=>{const d=new Date(s);d.setDate(d.getDate()+i);return d});
title.textContent=days[0].toLocaleDateString(undefined,{month:"short",day:"numeric"})+" – "+days[6].toLocaleDateString(undefined,{month:"short",day:"numeric"});
let h='<div class="week"><div></div>'+days.map(d=>`<div class="dh ${iso(d)==today?"today":""}" onclick="cur=parse('${iso(d)}');setView('day')">${d.toLocaleDateString(undefined,{weekday:"short"})}<b>${d.getDate()}</b></div>`).join("");
h+='<div class="hrs">'+[...Array(24)].map((_,i)=>i?`<div style="top:${i*PX}px">${pad(i)}</div>`:"").join("")+'</div>';
for(const d of days){const ds=iso(d),L=E.filter(e=>e.date==ds).sort((a,b)=>mins(a.start)-mins(b.start));
h+='<div class="col">'+[...Array(24)].map((_,i)=>`<div class="hl" style="top:${i*PX}px"></div>`).join("");
const bg=L.filter(e=>["sleep","guelph","chartright","ea","event"].includes(e.type)),fg=L.filter(e=>!bg.includes(e));
for(const e of bg.concat(fg)){const t=mins(e.start)*PX/60,ht=Math.max((mins(e.end)-mins(e.start))*PX/60,12),small=fg.includes(e)&&["meal","commute"].includes(e.type);
h+=`<div class="ev ${e._o?"over":""}" onclick="openEd('${e.id}')" style="top:${t}px;height:${ht}px;background:var(--${e.type});${small?"left:40%;right:2px;":"left:2px;right:2px;"}${e.type=="guelph"?"opacity:.55;":""}" title="${e.label} · ${trueRng(e,E)}">${ht<30?`<span style="font-size:.85em">${e.split||e.label} · ${trueRng(e,E)}</span>`:`${e.split||e.label}<br><span style="font-size:.85em;opacity:.9">${trueRng(e,E)}</span>`}</div>`}
if(ds==today){const nw=new Date();h+=`<div class="now" style="top:${(nw.getHours()*60+nw.getMinutes())*PX/60}px"></div>`}h+='</div>'}
main.innerHTML=h+'</div>'}
else{const ds=iso(cur);title.textContent=cur.toLocaleDateString(undefined,{weekday:"long",month:"short",day:"numeric"});
const L=E.filter(e=>e.date==ds).sort((a,b)=>mins(a.start)-mins(b.start)),nm=new Date().getHours()*60+new Date().getMinutes();
main.innerHTML='<div class="agenda">'+(L.length?L.map(e=>`<div class="it" onclick="openEd('${e.id}')" style="${ds==today&&mins(e.end)<nm?"opacity:.45":""}"><div class="dot" style="background:var(--${e.type})"></div><div class="t">${trueRng(e,E).replace("–","–<br>")}</div><div><div class="l">${e.label}${e._o?' <small style="color:var(--gold)">✎ edited</small>':""}</div><div class="n">${NAMES[e.type]}${e.split&&e.split!=e.label?" · "+e.split:""}${e.notes?" · "+e.notes:""}</div></div></div>`).join(""):'<p style="color:var(--muted);text-align:center;margin-top:40px">Nothing scheduled.</p>')+'</div>'}}
const f=document.getElementById("f");f.type.innerHTML=TYPES.map(t=>`<option value="${t}">${NAMES[t]}</option>`).join("");
function openEd(id){editing=id||null;const e=id?events().find(x=>x.id==id):{label:"",type:"event",date:iso(cur),start:"09:00",end:"10:00",notes:"",split:""};
for(const k of["label","type","date","start","end","notes","split"])f[k].value=k=="end"&&e.end=="24:00"?"23:59":(e[k]||"");dt.textContent=id?"Edit event":"New event";delb.style.display=id?"":"none";dlg.showModal()}
f.onsubmit=()=>{const v={};for(const k of["label","type","date","start","end","notes","split"])v[k]=f[k].value;if(v.end=="23:59")v.end="24:00";if(!v.split)delete v.split;
if(!editing)ov.added.push({id:"u"+Date.now(),...v});else{const a=ov.added.find(x=>x.id==editing);a?Object.assign(a,v):ov.edits[editing]=v}save()};
function delEv(){const a=ov.added.findIndex(x=>x.id==editing);if(a>=0)ov.added.splice(a,1);else{ov.deleted.push(editing);delete ov.edits[editing]}dlg.close();save()}
function resetAll(){if(confirm("Discard all local changes and reload from the published schedule?")){ov={edits:{},deleted:[],added:[]};save()}}
function exportJSON(){const out={...base,updated:new Date().toISOString(),events:events().map(({_o,...e})=>e)};const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([JSON.stringify(out,null,1)],{type:"application/json"}));a.download="schedule.json";a.click()}
legend.innerHTML=TYPES.map(t=>`<span style="--c:var(--${t})">${NAMES[t]}</span>`).join("");
fetch("data/schedule.json?"+Date.now()).then(r=>r.json()).then(d=>{base=d;upd.textContent="Updated "+new Date(d.updated).toLocaleString(undefined,{weekday:"short",month:"short",day:"numeric",hour:"2-digit",minute:"2-digit",hourCycle:"h23"});
const t=iso(new Date());if(d.events.length&&!d.events.some(e=>e.date==t)){const f=d.events.map(e=>e.date).filter(x=>x>t).sort()[0]||d.events[0].date;cur=parse(f)}render();setInterval(render,60000)}).catch(e=>upd.textContent="Couldn't load schedule");
