import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from "react-router-dom";
import { getEveryProblem } from "../../store/problems";
import { allSolved } from "../../store/solved";


import NavBar from '../NavBar';
import './dash.css';

import { VictoryPie } from "victory";


const Dashboard = () => {
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.allProblems);
    const problemsSolvedList = useSelector(state => state.solvedLists.allSolvedLists);
    const user = useSelector(state => state.session.user);

    console.log('all solved probleeeeeeems', problemsSolvedList);

    // let problemsId;
    for (let item in all_problems) {
        let problem = all_problems[item];
        // problemsId = problem.id
        console.log('butthole', problem);
    }

    useEffect(() => {
        dispatch(getEveryProblem())
    }, [dispatch])

    useEffect(() => {
        dispatch(allSolved())
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
