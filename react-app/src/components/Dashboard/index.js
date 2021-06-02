import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { BrowserRouter, Route, Link } from "react-router-dom";
import ArraysComponent from './Arrays';
import HashComponent from './Hash';
import StringsComponent from './Strings';

const Dashboard = () => {
    // const problems = useSelector(state => state.problems);

    // console.log(problems);

    return (
        <>
            <Link to={'/arrays'}>
                <h2>Arrays</h2>
                <ArraysComponent />
            </Link>
            <Link to={'/strings'}>
                <h2>Strings</h2>
                <StringsComponent />
            </Link>
            <Link to={'/hash'}>
                <h2>Hash</h2>
                <HashComponent />
            </Link>
        </>
    )
}

export default Dashboard;
