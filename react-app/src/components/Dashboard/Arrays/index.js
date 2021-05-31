import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { getAllProblems } from "../../../store/problems";

const ArraysComponent = () => {
    const { arrays } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problems);

    console.log(all_problems);

    useEffect(async () => {
        await dispatch(getAllProblems(arrays))
    }, [dispatch])
    
    return (
        <h1>Arrays</h1>
    )
}

export default ArraysComponent;
