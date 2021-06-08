import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import NavBar from "../NavBar";

import './login.css';

import loginpic from '../../images/login.png';

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-form-body">
      <div>
        <NavBar />
      </div>
      <div className="login-component">
        <div className="login-form">
          <form onSubmit={onLogin}>
            <div className="inputs">
              <div>
                {errors.map((error) => (
                  <div>{error}</div>
                ))}
              </div>
              <div className="login-inputs">
                <div className="login-input">
                  <input
                    name="email"
                    type="text"
                    placeholder="Email"
                    value={email}
                    onChange={updateEmail}
                  />
                </div>
                <div className="login-input">
                  <input
                    name="password"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={updatePassword}
                  />
                  <button className="login-btn" type="submit">Login</button>
                </div>
              </div>
            </div>
          </form>
        </div>
        <div className="login-img">
          <img src={loginpic} />
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
