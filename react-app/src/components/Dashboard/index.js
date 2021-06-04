import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from "react-router-dom";
import { getEveryProblem } from "../../store/problems";

import NavBar from '../NavBar';
import './dash.css';

import { VictoryPie } from "victory";


const Dashboard = () => {
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.allProblems);
    const user = useSelector(state => state.session.user);

    console.log('all probleeeeeeems', all_problems);

    useEffect(() => {
        dispatch(getEveryProblem())
    }, [dispatch])

    let pieChart;
    if (user) {
        pieChart = (
            <div className="pie">
                <VictoryPie />
            </div>
        )
    }


    return (
        <div className="dashboard-body">
            <NavBar />
            <Link className="cat-div" to={'/arrays'}>
                <h2 className="cat-title">Arrays</h2>
            </Link>
            <Link className="cat-div" to={'/trees'}>
                <h2 className="cat-title">Trees</h2>
            </Link>
            <Link className="cat-div" to={'/strings'}>
                <h2 className="cat-title">Strings</h2>
            </Link>
            <Link className="cat-div" to={'/hash'}>
                <h2 className="cat-title">Hash</h2>
            </Link>
        </div>
    )
}

export default Dashboard;
