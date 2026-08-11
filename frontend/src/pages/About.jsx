import "./About.css";
function About() {
  return (
    <div className="about-page">
      <section className="about-card">
        <h1>About Us</h1>
        <p>
          This project is made by us, two University of Missouri students, Anh
          Nguyen and Song Vu Nguyen
        </p>
      </section>

      <section className="about-content">
        <div className="about-card">
          <h2>The Problem</h2>
          <p>
            The problem that we are trying to solve is how students are often
            going into college not knowing what exactly they want to spend the
            rest of their lives doing and understanding their career outcomes.
            Thus, it is our goal to analyze relationships between majors,
            salaries, occupations, and the employment outlook to help students
            get a prospective on their future.
          </p>
        </div>

        <div className="about-card">
          <h2>Why are we doing this/why this matters</h2>
          <p>
            Many including ourselves didn’t really know what they wanted to do
            going into college. Many ended up wasting time and money trying to
            see if they liked their major and ended up switching. Therefore, we
            wanted students to understand their career prospects and what is
            available in the labor market.
          </p>
        </div>

        <div className="about-card">
          <h2>Objectives and goals</h2>
          <p>
            Use data to identify common occupations associated with majors and
            analyze each of the job’s salary trends. We will also examine,
            predict, and show projected job growth from the past to the future.
            All of these will be presented in such forms: dashboards,
            interactive UI (so students can input possible majors), interactive
            data viz.
          </p>
        </div>
      </section>
    </div>
  );
}

export default About;
