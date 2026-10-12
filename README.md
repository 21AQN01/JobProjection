# Career Insights: A Data-Driven Analysis of Salaries, Employment, and Growth

## Overview

Career Insights is a data-driven project designed to help students make more informed decisions about their college majors and future careers. By analyzing relationships between college majors, occupations, salaries, and employment projections, this project aims to provide students with a better understanding of their potential career outcomes and opportunities in the labor market.

Many students enter college without knowing exactly which career they want to pursue. This uncertainty can lead to switching majors, spending additional time in college, and accumulating unnecessary educational expenses. Our goal is to bridge the gap between education and employment by transforming publicly available data into meaningful insights and interactive visualizations.

Through dashboards, charts, and an interactive major-to-career roadmap, students will be able to explore career options, compare salaries, and understand projected employment trends.

## Motivation

Choosing a college major is an important decision that can influence a student's future career opportunities, earning potential, and professional development. However, many students lack access to clear and accessible information about the occupations associated with their majors.

Our team recognized this challenge through our own experiences and wanted to develop a tool that helps students better understand their career prospects before making significant educational investments.

Career Insights aims to make labor-market information more accessible and help students make informed decisions about their education and future careers.

## Project Objectives

The primary objectives of this project are to:

- **Major-to-Occupation Mapping:** Identify common occupations associated with different college majors.
- **Salary Analysis:** Analyze and compare salary information across occupations and career paths.
- **Employment Analysis:** Examine employment outcomes and relationships between educational attainment and employment.
- **Job Growth Projections:** Investigate historical employment trends and projected occupational growth.
- **Interactive Data Visualization:** Present findings through interactive charts, dashboards, and visualizations.
- **Career Roadmap:** Develop an interactive interface that allows students to select potential majors and explore related occupations, salaries, and employment outlooks.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning, processing, and transformation |
| FastAPI | Backend API and data delivery |
| React | Frontend application and user interface |
| JavaScript / JSX | Frontend development |
| D3.js | Interactive data visualization |
| Uvicorn | Backend development server |
| Vite | Frontend development server |
| Git and GitHub | Version control and collaboration |
| InfinityFree | Planned web hosting |

## Data Sources

This project uses publicly available datasets from government agencies and occupational information providers to analyze relationships between education, employment, salaries, and projected job growth.

### Primary Data Sources

**U.S. Bureau of Labor Statistics (BLS)**

- [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/oes/) — Occupational employment estimates and wage information.
- [Employment Projections](https://www.bls.gov/emp/) — Employment forecasts and labor-market outlook.
- [Employment Projections by Education and Training](https://www.bls.gov/emp/tables/education-summary.htm) — Employment projections organized by education and training requirements.
- [Educational Attainment](https://www.bls.gov/cps/demographics/educational-attainment.htm) — Employment and labor-force statistics by educational attainment.

**U.S. Census Bureau**

- [American Community Survey Data](https://www.census.gov/programs-surveys/acs/data.html) — Demographic, educational, and employment-related data.
- [Employment and College Majors Data](https://www.census.gov/data/tables/2019/demo/industry-occupation/college-jobs.html) — Data relating college majors to employment and occupations.

**U.S. Department of Education**

- [College Scorecard](https://collegescorecard.ed.gov/) — Information about colleges, educational programs, and student outcomes.
- [College Scorecard Data](https://collegescorecard.ed.gov/data/) — Downloadable datasets for educational and institutional analysis.

**O*NET Resource Center**

- [O*NET Database](https://www.onetcenter.org/database.html) — Occupational classifications and related career information.

**National Center for Education Statistics (NCES)**

- [Classification of Instructional Programs (CIP)](https://nces.ed.gov/pubs2002/cip2000/index.asp) — Classification resources for organizing and identifying college majors and educational programs.

### Data Integration

The project seeks to combine information from multiple datasets to establish relationships between college majors and occupations. Classification systems, including CIP codes and occupational identifiers, will be used where appropriate to connect relevant records.

Because datasets may differ in their reporting periods, definitions, and classification systems, data compatibility and limitations must be considered throughout the analysis.

## Data Collection and Processing

The initial phase of the project focused on organizing available datasets and determining which variables were relevant to our research objectives.

We developed a master data table to examine the structure of each dataset, identify useful fields, and understand how different tables could be connected. This process helped establish which data would contribute meaningfully to the project's analysis.

The data-processing workflow consists of the following stages:

1. **Data Collection:** Gather relevant datasets from government agencies and occupational information providers.
2. **Data Exploration:** Examine table structures, variables, classification codes, and reporting periods.
3. **Data Cleaning:** Prepare datasets for analysis and address inconsistencies where necessary.
4. **Data Integration:** Connect education, occupation, salary, and employment datasets using compatible identifiers.
5. **Variable Selection:** Retain fields that meaningfully support the project's objectives.
6. **Data Preparation:** Transform the resulting datasets into formats suitable for backend processing and frontend visualization.

Not every dataset or variable collected will necessarily be included in the final application. Selection will depend on data quality, relevance, and usefulness for answering the project's research questions.

## Project Roadmap

**Current Status: In Progress**

The primary feature under development is an interactive major-to-career roadmap that connects students' academic interests with potential employment opportunities.

### Planned Features

- [ ] Allow users to select or search for college majors.
- [ ] Identify occupations and career fields associated with selected majors.
- [ ] Display available salary statistics, including median wages.
- [ ] Show the percentage or distribution of workers associated with relevant majors and occupations when supported by the data.
- [ ] Present historical employment trends and projected job growth.
- [ ] Develop interactive charts for comparing occupational outcomes.
- [ ] Integrate occupation, wage, and major-to-occupation datasets using compatible classification codes.
- [ ] Improve dashboard usability and accessibility.

### Major-to-Career Roadmap

The roadmap will allow students to explore potential career paths based on their selected college majors.

The intended workflow is:

1. The user selects a potential college major.
2. The application identifies related occupations using available education-to-occupation mapping data.
3. Related occupations are displayed in individual cards or tabs.
4. Each occupation displays available salary statistics, employment information, and projected growth.
5. Users can compare career options through interactive visualizations.

The roadmap will integrate relevant information from occupation, wage, and major-to-occupation datasets. CIP codes and other compatible classification identifiers will be used where appropriate to establish relationships between academic programs and career outcomes.

Since a college major may lead to multiple occupations, and occupations may be associated with multiple majors, these relationships will be treated as mappings rather than definitive career pathways.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Prerequisites

Ensure that the following software is installed:

- [Python](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/)
- [Git](https://git-scm.com/downloads/)

### 1. Clone the Repository

Open a terminal and clone the repository:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Replace the placeholders with your repository URL and project directory name.

### 2. Install Frontend Dependencies

Navigate to the frontend directory:

```bash
cd frontend
npm install
```

Return to the project root:

```bash
cd ..
```

### 3. Install Root Dependencies

If the project contains a root-level `package.json`, install its dependencies:

```bash
npm install
```

### 4. Start the Backend

Open a terminal and navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

The backend API will be available at:

- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs

The documentation URL is available if the application uses FastAPI's default documentation configuration.

### 5. Start the Frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd frontend
npm run dev
```

The frontend development server will be available at:

http://localhost:5173

### 6. Access the Application

Once both servers are running, access the application through your browser.

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://127.0.0.1:8000 |
| API Documentation | http://127.0.0.1:8000/docs |

Keep both terminal sessions running while using the application.

**Note:** These instructions assume the frontend uses Vite and the backend uses FastAPI. The exact commands may vary depending on the project's configuration and available npm scripts.

## Key Project Files

The main files used for development and maintenance are listed below.

### Backend

| File | Description |
|---|---|
| `backend/app.py` | Defines the FastAPI application and API endpoints. |
| `backend/process.py` | Handles data processing and transformation logic. |

### Frontend

| File | Description |
|---|---|
| `frontend/src/App.jsx` | Main React application component. |
| `frontend/src/BarChart.jsx` | Bar chart visualization component. |
| `frontend/src/main.jsx` | Frontend entry point. |

The frontend paths assume that these files are located in `frontend/src/`. Adjust the paths if the repository uses a different structure.

## Expected Outcomes

Career Insights aims to make education and labor-market data more accessible to students exploring their future careers.

The expected outcomes include:

- Improved visibility into career opportunities associated with different college majors.
- Easier comparisons of salaries across occupations.
- A better understanding of employment trends and projected job growth.
- Interactive exploration of potential career paths.
- A data-driven resource to support educational and career planning.

The application is intended to support informed decision-making rather than guarantee specific employment outcomes or future earnings.

## Limitations

The accuracy and usefulness of the analysis depend on the quality, availability, and compatibility of the underlying datasets.

Users should consider the following limitations:

- Salary and employment statistics may represent different reporting periods.
- Major-to-occupation relationships may be incomplete or indirect.
- Employment projections are estimates and may differ from actual future outcomes.
- Individual salaries and employment opportunities vary based on location, experience, skills, and other factors.
- Historical trends do not guarantee future labor-market conditions.

## Contributing

Contributions, suggestions, and feedback are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your changes locally.
5. Submit a pull request describing your updates.

When adding datasets or modifying data-processing logic, document the relevant sources, transformations, and assumptions to support reproducibility.

## Acknowledgments

We would like to acknowledge the public institutions and organizations that provide the datasets used to support this project:

- U.S. Bureau of Labor Statistics
- U.S. Census Bureau
- U.S. Department of Education
- National Center for Education Statistics
- O*NET Resource Center

Their publicly available resources provide the foundation for analyzing relationships between college majors, occupations, salaries, and employment projections.

---

## Project Summary

Career Insights is a data-driven application that connects college majors to potential career paths through salary analysis, employment statistics, and projected job growth.

By combining Python-based data processing with a React frontend and interactive data visualizations, the project aims to help students better understand their career options and make more informed decisions about their educational futures.
