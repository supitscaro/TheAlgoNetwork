import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import { authenticate } from "./store/session";
import Dashboard from "./components/Dashboard";
import ArraysComponent from "./components/Dashboard/Arrays";
import ArrayProblems from "./components/Dashboard/Arrays/FullArraysProblems";
import StringsComponent from "./components/Dashboard/Strings";
import HashComponent from "./components/Dashboard/Hash";
import StringsProblems from "./components/Dashboard/Strings/FullStringProblems";
import HashProblems from "./components/Dashboard/Hash/FullHashProblems";
import TreesComponent from "./components/Dashboard/Trees";
import TreesProblems from "./components/Dashboard/Trees";
import Profile from "./components/Profile";

function App() {
  const user = useSelector(state => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route exact path="/">
          <Dashboard />
        </Route>
        {/* <Route exact path="/:userId">
          <Profile />
        </Route> */}
        <Route exact path="/:arrays">
          <ArraysComponent />
        </Route>
        <Route exact path="/:arrays/:problemId">
          <ArrayProblems />
        </Route>
        <Route exact path="/:strings">
          <StringsComponent />
        </Route>
        <Route exact path="/:strings/:problemId">
          <StringsProblems />
        </Route>
        <Route exact path="/:hash">
          <HashComponent />
        </Route>
        <Route exact path="/:hash/:problemId">
          <HashProblems />
        </Route>
        <Route exact path="/:trees">
          <TreesComponent />
        </Route>
        <Route exact path="/:trees/:problemId">
          <TreesProblems />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
