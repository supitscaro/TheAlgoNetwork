import React from 'react';
// import { useSelector, useDispatch } from 'react-redux';
import './topnav.css';

const TopNavBar = () => {

    return (
        <nav className="nav-top">
            <div className="logo-box"><i className="fas fa-code"></i></div>
            <div className="logo">
                The Algo Network.
            </div>
            <div className="creator">
                Made with 💜 by Caro
                <div className="links">
                    <a href="https://www.linkedin.com/in/caroline-mendez-41a181134/">
                        <i className="fab fa-linkedin-in"></i>
                    </a>
                    <a href="https://github.com/CaroMen">
                        <i className="fab fa-github-alt"></i>
                    </a>
                </div>
            </div>
        </nav>
    );
}

export default TopNavBar;
