import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux'
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";
import { problems } from '../../store/problems';
import ArraysComponent from './Arrays/index';

const Dashboard = () => {
    // const problems = useSelector(state => state.problems);

    return (
        <>
            <h1>Hello</h1>
            <Link to="/arrays">
                <ArraysComponent />

            </Link>
        </>
    );
};

export default Dashboard;
