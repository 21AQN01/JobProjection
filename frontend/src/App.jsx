import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import BarChart from "./components/BarChart";
import Navbar from "./components/NavBar";
import Employment from "./pages/Employment";
import Salary from "./pages/Salary";
import Trend from "./pages/Trend";
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
              <p>
                Explore employment trends, salaries, occupations accross majors
              </p>
              {/* place holder, create new visuals to fit needs */}
              {data.length > 0 ? <BarChart data={data} /> : <p>Loading...</p>}
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
