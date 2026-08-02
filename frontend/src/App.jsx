import { useEffect, useState } from "react";
import BarChart from "./BarChart";
import './App.css'

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/data")
            .then((res) => res.json())
            .then((json) => setData(json));
    }, []);

    return (
        <div>
            <h1>Employment Data</h1>

            {data.length > 0 ? (
                <BarChart data={data} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}


export default App
