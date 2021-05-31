import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";

const ArraysComponent = () => {
    const { arrays } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problems);

    console.log('teeeeeeeeeeeeeeeest', all_problems)

    let problems = []

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    console.log('probleeeeeeeeeeeems', problems)

    useEffect( () => {
        dispatch(getAllProblems(arrays))
    }, [dispatch])
    
    return (
        <div>
            {problems.map((problem) => (
                <Link to={`/${problem.category}/${problem.id}`}>
                    <div>{problem.title}</div>
                </Link>
            ))}
            Hi
        </div>
    )
}

export default ArraysComponent;
