import "./Navbar.css";
import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <nav className="navbar">
      {/* <ul className="nav-links">
        <li>
          <a href="/">Home</a>
        </li>
        <li>
          <a href="/employment">Explore Majors</a>
        </li>
        <li>
          <a href="/salary">Explore Careers</a>
        </li>
        <li>
          <a href="/trend">Industry Trends</a>
        </li>
        <li>
          <a href="/about">About Us</a>
        </li>
      </ul> */}
      <Link to="/">Home</Link>
      <Link to="/employment">Explore Majors</Link>
      <Link to="/salary">Explore Careers</Link>
      <Link to="/trend">Industry Trends</Link>
      <Link to="/about">About Us</Link>
    </nav>
  );
}

export default Navbar;
