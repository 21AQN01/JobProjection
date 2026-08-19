import { useState } from "react";

function Roadmap({ data }) {
  const [selectedMajor, setSelectedMajor] = useState("");

  const majors = [
    ...new Set(data.map((row) => row.CIP2020Title)),
  ].sort();

  const jobs = data.filter(
    (row) => row.CIP2020Title === selectedMajor
  );

  return (
    <div className="roadmap-container">
      <h2>Explore Your Career Path</h2>

      <p>
        Select a college major to explore potential jobs associated
        with that major
      </p>

      <div className="major-selector">
        <label htmlFor="major">Select a major:</label>

        <select
          id="major"
          value={selectedMajor}
          onChange={(e) => setSelectedMajor(e.target.value)}
        >
          <option value="">Choose a major</option>

          {majors.map((major) => (
            <option key={major} value={major}>
              {major}
            </option>
          ))}
        </select>
      </div>

      {selectedMajor && (
        <div className="career-results">
          <h2>{selectedMajor}</h2>

          <p className="career-description">
            Potential jobs associated with this major:
          </p>

          <div className="career-grid">
            {jobs.map((job, index) => (
              <div
                className="job-card"
                key={`${job.SOC2018Code}-${index}`}
              >
                <h3>{job.SOC2018Title}</h3>

                <p>
                  <strong>SOC:</strong> {job.SOC2018Code}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default Roadmap;