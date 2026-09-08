import { useNavigate } from "react-router-dom";
export default function Home(){
 const nav=useNavigate();
 return <main className="min-h-[calc(100vh-73px)] flex items-center justify-center p-6 bg-gradient-to-br from-[#11165c] via-[#070b2b] to-[#02030e]">
  <div className="text-center max-w-3xl">
   <div className="mx-auto mb-8 w-32 h-32 rounded-full border-8 border-yellow-400 flex items-center justify-center text-5xl font-black shadow-[0_0_50px_rgba(250,204,21,.4)]">K</div>
   <h1 className="text-6xl font-black text-yellow-400">Kaun Banega Crorepati</h1>
   <p className="text-xl text-white/70 mt-4">The ultimate 15-question quiz challenge.</p>
   <button onClick={()=>localStorage.getItem("token")?nav("/game"):nav("/login")} className="mt-10 px-10 py-4 bg-yellow-400 text-black font-black text-xl rounded-full hover:scale-105 transition">START GAME</button>
  </div>
 </main>
}
