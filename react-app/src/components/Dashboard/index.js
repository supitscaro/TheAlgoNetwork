import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from "react-router-dom";
import { getEveryProblem } from "../../store/problems";
import { allSolved } from "../../store/solved";


import NavBar from '../NavBar';
import './dash.css';

import { VictoryPie, VictoryBar, VictoryChart } from "victory";


const Dashboard = () => {
    const dispatch = useDispatch();
    const allProblems = useSelector(state => state.problems.allProblems);
    const problemsSolvedList = useSelector(state => state.solvedLists.allSolvedLists);
    const user = useSelector(state => state.session.user);

    let allSolvedProblems = Object.values(problemsSolvedList).length;
    let listOfProblems = Object.values(allProblems).length;

    // console.log('problems solved', Object.values(problemsSolvedList));

    let problemsArr = Object.values(allProblems);

    let problems;
    let problemsSolvedId = []

    for (let item in problemsSolvedList) {
        let problem = problemsSolvedList[item];
        problemsSolvedId.push(problem.problems_id)
    }

    let setOfProblems = new Set(problemsSolvedId)

    let filterById = problemsArr.filter((item) => setOfProblems.has(item.id))

    let stringsProblems = filterById.filter((item) => item.category === 'Strings');
    let arraysProblems = filterById.filter((item) => item.category === 'Arrays');
    let treesProblems = filterById.filter((item) => item.category === 'Trees');
    let hashProblems = filterById.filter((item) => item.category === 'Hash');

    console.log('strings filter?', stringsProblems);

    useEffect(() => {
        dispatch(getEveryProblem())
    }, [dispatch])

    useEffect(() => {
        dispatch(allSolved())
    }, [dispatch])

    let pieChart;
    let barChart;
    if (user) {
        pieChart = (
            <div className="pie">
                <VictoryPie
                    colorScale={["#8A2BE2", "#CFD8DC"]}
                    data={[
                        { x: 1, y: allSolvedProblems, label: "solved" },
                        { x: 2, y: listOfProblems, label: "all problems" },
                    ]}
                    innerRadius={100}
                />
            </div>
        );
        barChart = (
            <div className="bar">
                <VictoryChart
                    domainPadding={20}
                >
                    <VictoryBar
                        style={{ data: { fill: "#c43a31" } }}
                        data={[
                            { x: 'arrays', y: arraysProblems.length },
                            { x: 'trees', y: treesProblems.length },
                            { x: 'hash', y: hashProblems.length },
                            { x: 'strings', y: stringsProblems.length },
                        ]}
                    />
                </VictoryChart>
            </div>
        )
    }

    // 8A2BE2

    return (
        <div className="dashboard-body">
            <NavBar />
            <div className="dashboard-content">
                <div className="category-divs">
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
                <div className="graphs">
                    {pieChart}
                </div>
                <div className="graphs">
                    {barChart}
                </div>
            </div>
        </div>
    )
}

export default Dashboard;
