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
          {/* <div className=""> */}
          {/* </div> */}
          <NavLink className="nav-link" to="/" exact={true} activeClassName="active">
            <i class="fas fa-home"></i>
          </NavLink>
            Dashboard
        </div>
        <div className="link">
          <NavLink className="nav-link" to="/login" exact={true} activeClassName="active">
          </NavLink>
            Login
        </div>
        <div className="link">
          <NavLink className="nav-link" to="/sign-up" exact={true} activeClassName="active">
          </NavLink>
            Sign Up
        </div>
        <div className="link">
          <NavLink className="nav-link" to={`/${user.id}`} exact={true} activeClassName="active">
            <i class="far fa-user"></i>
          </NavLink>
            Profile
        </div>
        <div>
          <LogoutButton />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
