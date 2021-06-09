import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux"
import { Redirect, Link } from 'react-router-dom';
import { signUp } from '../../store/session';
import NavBar from "../NavBar";

import './signup.css';

import signup from '../../images/signup.png';
import DemoButton from "./Demo";

const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [firstname, setFname] = useState("");
  const [lastname, setLname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      await dispatch(signUp(firstname, lastname, username, email, password));
    }
    const data = await dispatch(signUp(firstname, lastname, username, email, password))
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateFname = (e) => {
    setFname(e.target.value);
  };

  const updateLname = (e) => {
    setLname(e.target.value);
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="signup-form-body">
      <div>
        <NavBar />
      </div>
      <div className="signup-component">
        <div className="signup-form">
          <h2 className="signup-title">Create An Account:</h2>
          <form onSubmit={onSignUp}>
            <div className="errors">
              {errors.map((error, i) => (
                <div key={i}>{error}</div>
              ))}
            </div>
            <div className="inputs">
              <div className="input-div">
                <input
                  type="text"
                  name="first name"
                  onChange={updateFname}
                  value={firstname}
                  placeholder="First name"
                ></input>
              </div>
              <div className="input-div">
                <input
                  type="text"
                  name="last name"
                  onChange={updateLname}
                  value={lastname}
                  placeholder="Last name"
                ></input>
              </div>
              <div className="input-div">
                <input
                  type="text"
                  name="username"
                  onChange={updateUsername}
                  value={username}
                  placeholder="Username"
                ></input>
              </div>
              <div className="input-div">
                <input
                  type="text"
                  name="email"
                  onChange={updateEmail}
                  value={email}
                  placeholder="Email"
                ></input>
              </div>
              <div className="input-div">
                <input
                  type="password"
                  name="password"
                  onChange={updatePassword}
                  value={password}
                  placeholder="Password"
                ></input>
              </div>
              <div className="input-div">
                <input
                  type="password"
                  name="repeat_password"
                  onChange={updateRepeatPassword}
                  value={repeatPassword}
                  required={true}
                  placeholder="Confirm password"
                ></input>
                <button className="submit-btn" type="submit">Sign Up</button>
                <DemoButton />
              </div>
            </div>
          </form>
        </div>
        <div className="signup-img">
          <img src={signup} />
          <h3 className="slogan">Keep track of how you're doing on Leetcode</h3>
          <h3 className="has-account">
            Already have an account?
            <Link className="link-login" to="/login">Log In!</Link>
          </h3>
        </div>
      </div>
    </div>
  );
};

export default SignUpForm;
