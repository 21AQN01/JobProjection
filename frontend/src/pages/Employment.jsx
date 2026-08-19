import "./Employment.css";
import Roadmap from "../components/Roadmap";
import { useEffect, useState } from "react";

function Employment() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/roadmap")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  return (
    <div className="employment-page">
      {data.length > 0 ? <Roadmap data={data} /> : <p>Loading...</p>}
    </div>
  );
}

export default Employment;
