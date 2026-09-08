import {useEffect,useState} from "react"; import {useNavigate} from "react-router-dom"; import api from "../api"; import PrizeLadder from "../components/PrizeLadder"; import Lifelines from "../components/Lifelines";
export default function Game(){
 const nav=useNavigate(); const [qs,setQs]=useState([]),[game,setGame]=useState(null),[idx,setIdx]=useState(0),[selected,setSelected]=useState(null),[result,setResult]=useState(null),[time,setTime]=useState(30),[used,setUsed]=useState({}),[help,setHelp]=useState(null);
 useEffect(()=>{if(!localStorage.getItem("token"))return nav("/login");(async()=>{const q=await api.get("/api/questions");setQs(q.data);const g=await api.post("/api/game/start");setGame(g.data)})()},[]);
 useEffect(()=>{if(!game||result||selected)return; if(time<=0){submit("X");return} const t=setTimeout(()=>setTime(x=>x-1),1000);return()=>clearTimeout(t)},[time,game,result,selected]);
 if(!qs.length||!game)return <div className="p-10 text-center">Loading game...</div>;
 const q=qs[idx];
 async function submit(ans){setSelected(ans);try{const r=await api.post("/api/game/answer",{game_id:game.game_id,question_id:q.id,answer:ans});setResult(r.data);setTimeout(()=>{if(r.data.status==="playing"){setIdx(i=>i+1);setSelected(null);setResult(null);setTime(30);setHelp(null)}else nav("/result",{state:r.data})},1800)}catch(e){alert(e.response?.data?.detail||"Error")}}
 async function lifeline(type){if(used[type])return;setUsed({...used,[type]:true});const r=await api.post("/api/game/lifeline",{game_id:game.game_id,question_id:q.id,lifeline:type});setHelp(r.data)}
 async function quit(){const r=await api.post(`/api/game/quit?game_id=${game.game_id}`);nav("/result",{state:r.data})}
 const options={A:q.option_a,B:q.option_b,C:q.option_c,D:q.option_d};
 return <main className="p-6 bg-gradient-to-br from-[#11165c] to-[#070b2b] min-h-[calc(100vh-73px)]"><div className="max-w-7xl mx-auto grid lg:grid-cols-[1fr_280px] gap-8">
  <section><div className="flex justify-between items-center mb-5"><span className="text-yellow-400 font-bold">Question {idx+1} / 15</span><span className={`text-2xl font-black ${time<=10?"text-red-400":"text-yellow-400"}`}>{time}s</span></div>
   <div className="bg-black/40 border border-yellow-400/30 rounded-3xl p-8"><p className="text-2xl md:text-3xl font-bold text-center min-h-24 flex items-center justify-center">{q.question}</p>
   <div className="grid md:grid-cols-2 gap-4 mt-8">{Object.entries(options).map(([key,val])=><button key={key} disabled={selected||help?.remove?.includes(key)} onClick={()=>submit(key)} className={`text-left p-5 rounded-2xl border border-white/20 hover:border-yellow-400 hover:bg-yellow-400/10 ${result&&key===result.correct_answer?"border-green-400 bg-green-400/20":result&&selected===key?"border-red-400 bg-red-400/20":""}`}><b className="text-yellow-400 mr-3">{key}.</b>{val}</button>)}</div>
   <Lifelines used={used} onUse={lifeline}/>{help?.poll&&<div className="mt-4 text-center">Audience: {Object.entries(help.poll).map(([k,v])=><span className="mx-2">{k} {v}%</span>)}</div>}{help?.answer&&<div className="mt-4 text-center text-yellow-400">Expert suggests: {help.answer}</div>}
   <button onClick={quit} className="block mx-auto mt-5 text-white/50 hover:text-red-400">Quit Game</button></div></section>
  <PrizeLadder current={idx+1}/></div></main>
}
