import {useState} from "react"; import {useNavigate,Link} from "react-router-dom"; import api from "../api";
export default function Login(){
 const [form,setForm]=useState({email:"",password:""}),[error,setError]=useState(""); const nav=useNavigate();
 async function submit(e){e.preventDefault();try{const r=await api.post("/api/auth/login",form);localStorage.setItem("token",r.data.access_token);localStorage.setItem("name",r.data.name);nav("/game")}catch(e){setError(e.response?.data?.detail||"Login failed")}}
 return <main className="min-h-[calc(100vh-73px)] flex items-center justify-center p-6"><form onSubmit={submit} className="w-full max-w-md bg-white/10 p-8 rounded-3xl border border-white/10">
 <h2 className="text-3xl font-black text-yellow-400 mb-6">Login</h2>{error&&<p className="text-red-400 mb-3">{error}</p>}
 <input className="w-full mb-4 p-3 rounded-lg bg-black/30" placeholder="Email" type="email" required onChange={e=>setForm({...form,email:e.target.value})}/>
 <input className="w-full mb-6 p-3 rounded-lg bg-black/30" placeholder="Password" type="password" required onChange={e=>setForm({...form,password:e.target.value})}/>
 <button className="w-full bg-yellow-400 text-black font-bold p-3 rounded-lg">Login</button>
 <p className="mt-4 text-white/60">No account? <Link className="text-yellow-400" to="/register">Register</Link></p></form></main>
}
