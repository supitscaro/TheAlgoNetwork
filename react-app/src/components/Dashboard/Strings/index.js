import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";
import NavBar from '../../NavBar';

import './index.css';

const StringsComponent = () => {
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
        dispatch(getAllProblems("strings"))
    }, [dispatch])

    return (
        <div className="strings-outer-div">
            <NavBar />
            <div className="outer-div">
                <div>
                    <div className="category-title">Easy ✨</div>
                    {easyProblems.map((problem) => (
                        <div className="problem-div">
                            {easyColor}
                            <div>
                                <Link className="problem-title" to={`/${problem.category}/${problem.id}`}>
                                    <div>{problem.title}</div>
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
                <div>
                    <div className="category-title">Medium 🙏🏼</div>
                    {mediumProblems.map((problem) => (
                        <div className="problem-div">
                            {mediumColor}
                            <div>
                                <Link className="problem-title" to={`/${problem.category}/${problem.id}`}>
                                    <div>{problem.title}</div>
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
                <div>
                    <div className="category-title">Hard 🔥</div>
                    {hardProblems.map((problem) => (
                        <div className="problem-div">
                            {hardColor}
                            <div>
                                <Link className="problem-title" to={`/${problem.category}/${problem.id}`}>
                                    <div>{problem.title}</div>
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default StringsComponent;
