export default function Lifelines({used,onUse}){
 return <div className="flex gap-3 flex-wrap justify-center mt-6">
  {[["5050","50:50"],["audience","Audience Poll"],["expert","Ask Expert"]].map(([id,label])=>
   <button disabled={used[id]} onClick={()=>onUse(id)} className="px-4 py-2 rounded-full border border-yellow-400 text-yellow-400 disabled:opacity-30">{label}</button>)}
 </div>
}
