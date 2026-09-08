import {useState} from "react"; import {useNavigate,Link} from "react-router-dom"; import api from "../api";
export default function Register(){
 const [form,setForm]=useState({name:"",email:"",password:""}),[error,setError]=useState(""); const nav=useNavigate();
 async function submit(e){e.preventDefault();try{const r=await api.post("/api/auth/register",form);localStorage.setItem("token",r.data.access_token);localStorage.setItem("name",r.data.name);nav("/game")}catch(e){setError(e.response?.data?.detail||"Registration failed")}}
 return <main className="min-h-[calc(100vh-73px)] flex items-center justify-center p-6"><form onSubmit={submit} className="w-full max-w-md bg-white/10 p-8 rounded-3xl border border-white/10">
 <h2 className="text-3xl font-black text-yellow-400 mb-6">Create Account</h2>{error&&<p className="text-red-400 mb-3">{error}</p>}
 {["name","email","password"].map(x=><input key={x} className="w-full mb-4 p-3 rounded-lg bg-black/30" placeholder={x==="name"?"Full name":x} type={x==="password"?"password":x==="email"?"email":"text"} required onChange={e=>setForm({...form,[x]:e.target.value})}/>)}
 <button className="w-full bg-yellow-400 text-black font-bold p-3 rounded-lg">Register</button>
 <p className="mt-4 text-white/60">Already registered? <Link className="text-yellow-400" to="/login">Login</Link></p></form></main>
}
