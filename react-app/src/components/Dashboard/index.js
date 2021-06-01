import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { BrowserRouter, Route, Link } from "react-router-dom";
import ArraysComponent from './Arrays';

const Dashboard = () => {
    // const problems = useSelector(state => state.problems);

    // console.log(problems);

    return (
        <>
            <Link to={'/arrays'}>
                <h2>Arrays</h2>
                <ArraysComponent />
            </Link>
        </>
    )
}

export default Dashboard;
