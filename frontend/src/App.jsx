import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import BarChart from "./components/BarChart";
import BarChart2 from "./components/BarChart2";
import Navbar from "./components/NavBar";
import Employment from "./pages/Employment";
import Salary from "./pages/Salary";
import Trend from "./pages/Trend";
import About from "./pages/About";
import "./App.css";

function App() {
  const [data1, setData1] = useState([]);
  const [data2, setData2] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/employPerDeg")
      .then((res) => res.json())
      .then((json) => setData1(json));

    fetch("http://127.0.0.1:8000/majorEarnings")
      .then((res) => res.json())
      .then((json) => setData2(json));
  }, []);

  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <div>
              <h1>Job Data through the Looking Glass</h1>
              {/* place holder, create new visuals to fit needs */}
              <div id="barchart1">
                {data1.length > 0 ? (
                  <BarChart data={data1} />
                ) : (
                  <p>Loading...</p>
                )}
              </div>
              <div id="barchart2">
                {data2.length > 0 ? (
                  <BarChart2 data={data2.slice(0, 10)} />
                ) : (
                  <p>Loading...</p>
                )}
              </div>
            </div>
          }
        />
        <Route path="/employment" element={<Employment />} />
        <Route path="/salary" element={<Salary />} />
        <Route path="/trend" element={<Trend />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;
