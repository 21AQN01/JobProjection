function About() {
  return (
    <div className="about-page">
      <section className="about-hero">
        <h1>About Our Project</h1>
        <p>
          Exploring employment trends and career opportunities across
          college majors.
        </p>
      </section>

      <section className="about-content">
        <div className="about-card">
          <h2>What is this website?</h2>
          <p>
            This website helps students explore career and employment
            trends associated with different college majors.
          </p>
        </div>

        <div className="about-card">
          <h2>Our Purpose</h2>
          <p>
            Our goal is to make employment data easier to understand
            and help students make more informed decisions about their
            education and career paths.
          </p>
        </div>

        <div className="about-card">
          <h2>Our Data</h2>
          <p>
            We use employment and career data to visualize trends such
            as employment rates, salaries, industries, and job
            opportunities across different majors.
          </p>
        </div>
      </section>
    </div>
  )
}

export default About