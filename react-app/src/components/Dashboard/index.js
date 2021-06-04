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

    let problemsArr = Object.values(allProblems);

    // grab total of problems for each category
    let arraysTotal = problemsArr.filter((item) => item.category === 'Arrays');
    let stringsTotal = problemsArr.filter((item) => item.category === 'Strings');
    let hashTotal = problemsArr.filter((item) => item.category === 'Hash');
    let treesTotal = problemsArr.filter((item) => item.category === 'Trees');

    // grab total of problems for each difficulty
    let easyTotal = problemsArr.filter((item) => item.difficulty === 'Easy');
    let mediumTotal = problemsArr.filter((item) => item.difficulty === 'Medium');
    let hardTotal = problemsArr.filter((item) => item.difficulty === 'Hard');


    // creating an array of the solved problems' id
    let problemsSolvedId = []
    for (let item in problemsSolvedList) {
        let problem = problemsSolvedList[item];
        problemsSolvedId.push(problem.problems_id)
    }

    // Filtering the list of problems based on which have been solved
    let setOfProblems = new Set(problemsSolvedId)
    let filterById = problemsArr.filter((item) => setOfProblems.has(item.id))

    // Filtering solved problems by category
    let stringsProblems = filterById.filter((item) => item.category === 'Strings');
    let arraysProblems = filterById.filter((item) => item.category === 'Arrays');
    let treesProblems = filterById.filter((item) => item.category === 'Trees');
    let hashProblems = filterById.filter((item) => item.category === 'Hash');

    // Filtering solved problems by difficulty
    let easyProblems = filterById.filter((item) => item.difficulty === 'Easy');
    let mediumProblems = filterById.filter((item) => item.difficulty === 'Medium');
    let hardProblems = filterById.filter((item) => item.difficulty === 'Hard');

    console.log('strings filter?', stringsProblems);

    useEffect(() => {
        dispatch(getEveryProblem())
    }, [dispatch])

    useEffect(() => {
        dispatch(allSolved())
    }, [dispatch])

    let pieChart;
    let barChart;
    let horizontalGraph;
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
                        style={{ data: { fill: "#7442C8" } }}
                        barWidth={() => 18}
                        cornerRadius={{ topLeft: () => 10, topRight: () => 10, bottomRight: () => 10, bottomLeft: () => 10 }}
                        data={[
                            { x: 'arrays', y: arraysProblems.length / arraysTotal.length * 100 },
                            { x: 'trees', y: treesProblems.length / treesTotal.length * 100 },
                            { x: 'hash', y: hashProblems.length / hashTotal.length * 100 },
                            { x: 'strings', y: stringsProblems.length / stringsTotal.length * 100 },
                        ]}
                    />
                </VictoryChart>
            </div>
        );
        horizontalGraph = (
            <div className="horizontal">
                <VictoryChart
                    domainPadding={30}
                >
                    <VictoryBar horizontal
                        style={{ data: { fill: "#7442C8" } }}
                        barWidth={() => 18}
                        cornerRadius={{ topLeft: () => 10, topRight: () => 10, bottomRight: () => 10, bottomLeft: () => 10 }}
                        data={[
                            { x: 'easy', y: easyProblems.length / easyTotal.length * 100 },
                            { x: 'medium', y: mediumProblems.length / mediumTotal.length * 100 },
                            { x: 'hard', y: hardProblems.length / hardTotal.length * 100 },
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
                    <div>
                        {horizontalGraph}
                    </div>
                    <div>
                        {barChart}
                    </div>
                    <div>
                        {pieChart}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Dashboard;
