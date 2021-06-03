import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Link } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './navbar.css';

const NavBar = () => {
  const user = useSelector(state => state.session.user);

  return (
    <nav className="nav-outer">
      <div className="nav-div">
        <div className="link">
          <NavLink className="nav-link" to="/" exact={true} activeClassName="active">
            Dashboard
          </NavLink>
        </div>
        <div className="link">
          <NavLink className="nav-link" to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
        </div>
        <div className="link">
          <NavLink className="nav-link" to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
        </div>
        <div className="link">
          <NavLink className="nav-link" to={`/${user.id}`} exact={true} activeClassName="active">
            Profile
          </NavLink>
        </div>
        <div>
          <LogoutButton />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
