import React from 'react';
import { BrowserRouter, Route, Link } from "react-router-dom";
import NavBar from '../NavBar';
import './dash.css';


const Dashboard = () => {

    return (
        <div className="dashboard-body">
            <NavBar />
            <Link className="cat-div" to={'/arrays'}>
                <h2 className="cat-title">Arrays</h2>
            </Link>
            <Link className="cat-div" to={'/strings'}>
                <h2 className="cat-title">Strings</h2>
            </Link>
            <Link className="cat-div" to={'/hash'}>
                <h2 className="cat-title">Hash</h2>
            </Link>
            <Link className="cat-div" to={'/trees'}>
                <h2 className="cat-title">Trees</h2>
            </Link>
        </div>
    )
}

export default Dashboard;
