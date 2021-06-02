import React from 'react';
import { BrowserRouter, Route, Link } from "react-router-dom";


const Dashboard = () => {

    return (
        <>
            <Link to={'/arrays'}>
                <h2>Arrays</h2>
            </Link>
            <Link to={'/strings'}>
                <h2>Strings</h2>
            </Link>
            <Link to={'/hash'}>
                <h2>Hash</h2>
            </Link>
            <Link to={'/trees'}>
                <h2>Trees</h2>
            </Link>
        </>
    )
}

export default Dashboard;
