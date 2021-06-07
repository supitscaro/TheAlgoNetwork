import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
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
