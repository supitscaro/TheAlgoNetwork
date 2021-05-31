import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";

const ArrayProblems = () => {
    const { arrays, problemId } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problem);

    console.log('diiiiiiiiiiiiiiiiiick', all_problems);

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect( () => {
        dispatch(getSpecificProblem(arrays, problemId))
    }, [dispatch, arrays, problemId])
    
    return (
        <div>
            {problems.map((problem) => (
                <div>
                    <div>{problem.title}</div>
                    <div>{problem.category}</div>
                    <div>{problem.description}</div>
                </div>
            ))}
        </div>
    )
}

export default ArrayProblems;
