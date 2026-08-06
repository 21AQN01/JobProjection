import "./Navbar.css";

function Navbar() {
    return (
        <nav className="navbar">

            <ul className="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/employment">Explore Majors</a></li>
                <li><a href="/salary">Explore Careers</a></li>
                <li><a href="/trend">Industry Trends</a></li>
                <li><a href="/about">About Us</a></li>
            </ul>
        </nav>
    );
}

export default Navbar;