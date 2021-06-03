import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";

const ArraysComponent = () => {
    const { arrays } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => Object.values(state.problems.problems));

    let easy_problems = [];

    let medium_problems = [];

    let hard_problems = [];

    for (let key in all_problems) {
        let val = all_problems[key];
        if (val.difficulty === 'Easy') {
            easy_problems.push(val);
        };
        if (val.difficulty === 'Medium') {
            medium_problems.push(val);
        };
        if (val.difficulty === 'Hard') {
            hard_problems.push(val);
        }
    }

    useEffect(() => {
        dispatch(getAllProblems("arrays"))
    }, [dispatch])

    return (
        <div>
            <div>
                Easy
                {easy_problems.map((problem) => (
                <div>
                    <div>
                        <Link to={`/${problem.category}/${problem.id}`}>
                            <div>{problem.title}</div>
                        </Link>
                    </div>
                </div>
            ))}
            </div>
            <div>
                Medium
                {medium_problems.map((problem) => (
                <div>
                    <Link to={`/${problem.category}/${problem.id}`}>
                        <div>{problem.title}</div>
                    </Link>
                </div>
            ))}
            </div>
            <div>
                Hard
                {hard_problems.map((problem) => (
                <div>
                    <Link to={`/${problem.category}/${problem.id}`}>
                        <div>{problem.title}</div>
                    </Link>
                </div>
            ))}
            </div>
        </div>
    )
}

export default ArraysComponent;
