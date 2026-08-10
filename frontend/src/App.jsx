import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import BarChart from "./components/BarChart";
import Navbar from "./components/NavBar";
import About from "./pages/About";
import "./App.css";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/data")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <div>
              <h1>Job Projection For College Students</h1>
              <h3>By Anh Nguyen and Song Vu Nguyen</h3>

              {data.length > 0 ? <BarChart data={data} /> : <p>Loading...</p>}

              <p>
                Explore employment trends, salaries, occupations accross majors
              </p>
            </div>
          }
        />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;
