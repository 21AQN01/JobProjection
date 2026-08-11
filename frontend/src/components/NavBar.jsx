import "./Navbar.css";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" className="nav-links">
        Home
      </Link>
      <Link to="/employment" className="nav-links">
        Explore Majors
      </Link>
      <Link to="/salary" className="nav-links">
        Explore Careers
      </Link>
      <Link to="/trend" className="nav-links">
        Industry Trends
      </Link>
      <Link to="/about" className="nav-links">
        About Us
      </Link>
    </nav>
  );
}

export default Navbar;
