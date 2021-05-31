import React, { useState } from "react";
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from "react-router-dom";
import { problems } from '../../../store/problems';

const ArraysComponent = () => {
    const { category } = useParams();
    console.log(category)
    // const problems = useSelector(state => state.problems);

    return (
        <h1>Arrays</h1>
    );
};

export default ArraysComponent;
