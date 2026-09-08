import { Routes, Route, Navigate, Link, useNavigate } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Game from "./pages/Game";
import Result from "./pages/Result";
import Admin from "./pages/Admin";

function Navbar(){
  const navigate=useNavigate();
  const logged=!!localStorage.getItem("token");
  function logout(){localStorage.clear();navigate("/login")}
  return <nav className="bg-black/40 border-b border-white/10 px-6 py-4 flex justify-between items-center text-white">
    <Link to="/" className="font-black text-2xl text-yellow-400">KBC</Link>
    <div className="flex gap-4 items-center">
      {logged ? <button onClick={logout} className="px-4 py-2 rounded-lg bg-red-600">Logout</button> :
      <><Link to="/login">Login</Link><Link to="/register" className="bg-yellow-400 text-black px-4 py-2 rounded-lg font-bold">Register</Link></>}
    </div>
  </nav>
}
export default function App(){
 return <div className="min-h-screen text-white"><Navbar/><Routes>
  <Route path="/" element={<Home/>}/><Route path="/login" element={<Login/>}/>
  <Route path="/register" element={<Register/>}/><Route path="/game" element={<Game/>}/>
  <Route path="/result" element={<Result/>}/><Route path="/admin" element={<Admin/>}/>
  <Route path="*" element={<Navigate to="/"/>}/>
 </Routes></div>
}
