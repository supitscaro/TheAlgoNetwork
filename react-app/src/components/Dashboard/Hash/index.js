import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";
import NavBar from '../../NavBar';

import './index.css';

const HashComponent = () => {
    // const { "" } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problems);

    let easyProblems = [];

    let mediumProblems = [];

    let hardProblems = [];

    let easyColor;
    let mediumColor;
    let hardColor;

    for (let key in all_problems) {
        let val = all_problems[key];
        if (val.difficulty === 'Easy') {
            easyProblems.push(val);
            easyColor = (
                <div className="easy-button"></div>
            )
        };
        if (val.difficulty === 'Medium') {
            mediumProblems.push(val);
            mediumColor = (
                <div className="medium-button"></div>
            )
        };
        if (val.difficulty === 'Hard') {
            hardProblems.push(val);
            hardColor = (
                <div className="hard-button"></div>
            )
        }
    }

    useEffect(() => {
        dispatch(getAllProblems("hash"))
    }, [dispatch])

    return (
        <div className="hash-outer-div">
            <NavBar />
            <div className="outer-div">
                <div className="easy-component">
                    <div className="category-title">Easy ✨</div>
                    <div className="easy-div">
                        {easyProblems.map((problem, i) => (
                            <Link className="problem-div" key={i} to={`/${problem.category}/${problem.id}`}>
                                {easyColor}
                                <div key={i}>
                                    <div key={i} className="problem-title">
                                        <div key={i}>{problem.title}</div>
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                </div>
                <div className="medium-component">
                    <div className="category-title">Medium 🙏🏼</div>
                    <div className="medium-div">
                        {mediumProblems.map((problem, i) => (
                            <Link className="problem-div" key={i} to={`/${problem.category}/${problem.id}`}>
                                {mediumColor}
                                <div key={i}>
                                    <div key={i} className="problem-title">
                                        <div key={i}>{problem.title}</div>
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                </div>
                <div className="hard-component">
                    <div className="category-title">Hard 🔥</div>
                    <div className="hard-div">
                        {hardProblems.map((problem, i) => (
                            <Link className="problem-div" key={i} to={`/${problem.category}/${problem.id}`}>
                                {hardColor}
                                <div key={i}>
                                    <div key={i} className="problem-title">
                                        <div key={i}>{problem.title}</div>
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HashComponent;
