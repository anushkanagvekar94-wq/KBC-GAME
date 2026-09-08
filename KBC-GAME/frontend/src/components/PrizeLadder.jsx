export default function PrizeLadder({ current }) {
  const prizes = [
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
    70000000,
  ];

  return (
    <div className="bg-black/30 p-4 rounded-2xl w-full max-w-xs">
      <h3 className="text-yellow-400 font-black text-center mb-3">
        PRIZE LADDER
      </h3>

      {prizes.map((p, i) => (
        <div
          key={p}
          className={`flex justify-between px-3 py-1 rounded ${
            i + 1 === current
              ? "bg-yellow-400 text-black font-black"
              : ""
          }`}
        >
          <span>{i + 1}</span>
          <span>₹{p.toLocaleString("en-IN")}</span>
        </div>
      ))}
    </div>
  );
}