import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";

const ArrayProblems = () => {
    const { id } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problems);

    console.log('probleeeeeeeems', Object.values(all_problems));

    useEffect( () => {
        dispatch(getAllProblems(arrays))
    }, [dispatch])
    
    return (
        <div>
            Array Problem
        </div>
    )
}

export default ArrayProblems;
