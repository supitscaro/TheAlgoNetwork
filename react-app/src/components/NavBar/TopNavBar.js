import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Link } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './topnav.css';

const TopNavBar = () => {
    const user = useSelector(state => state.session.user);

    return (
        <nav className="nav-top">
            <div className="logo">
                The Algo Network.
            </div>
        </nav>
    );
}

export default TopNavBar;
