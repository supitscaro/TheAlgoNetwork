import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";

import '../Arrays/problem.css'

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';
import NavBar from '../../NavBar';

const StringsProblems = () => {
    const { problemId } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problem);

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem("strings", problemId))
    }, [dispatch, "strings", problemId])

    return (
        <div className="problems-outer-div">
            <div>
                <NavBar />
            </div>
            {problems.map((problem) => (
                <div>
                    <div>{problem.title}</div>
                    <div>{problem.category}</div>
                    <div>{problem.description}</div>
                    <SyntaxHighlighter
                        language="python"
                        wrapLines={true}
                        style={duotoneLight}
                    >
                        {problem.examples}
                    </SyntaxHighlighter>
                    <SyntaxHighlighter
                        language="python"
                        lineProps={{ style: { wordBreak: 'break-all', whiteSpace: 'pre-wrap' } }}
                        style={materialOceanic}
                        showLineNumbers={true}
                        wrapLines={true}>
                        {problem.solution}
                    </SyntaxHighlighter>
                    <div>
                        <input type="checkbox" name="checked" value="Solved" />
                        <h3>Solved</h3>
                        <button>Save Changes</button>
                    </div>
                    <div>
                        <input type="checkbox" name="checked" value="Review" />
                        <h3>Review</h3>
                        <button>Save Changes</button>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default StringsProblems;
