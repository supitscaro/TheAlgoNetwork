import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Link } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { logout } from "../../store/session";
import './navbar.css';

const NavBar = () => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogout = async (e) => {
    dispatch(logout());
  };

  let sessionNav;
  if (user) {
    sessionNav = (
      <div className="sidebar-nav-outer">
        <div className="upper-siderbar">
          <div className="link">
            <NavLink className="nav-link" to="/" exact={true} activeClassName="active">
              <i className="fas fa-home"></i>
            </NavLink>
                Dashboard
          </div>
          <div className="link">
            <NavLink className="nav-link" to={`/${user.id}`} exact={true} activeClassName="active">
              <i className="far fa-user"></i>
            </NavLink>
                Profile
          </div>
        </div>
        <div className="logout-btn">
          <div className="nav-link" onClick={onLogout}>
            <i class="fas fa-power-off"></i>
          </div>
          Logout
        </div>
      </div>
    );
  } else {
    sessionNav = (<div>
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
    </div>
    )
  }

  return (
    <nav className="nav-outer">
      <div className="nav-div">
        {sessionNav}
      </div>
    </nav>
  );
}

export default NavBar;
