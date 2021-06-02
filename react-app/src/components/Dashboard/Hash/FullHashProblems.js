import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';

const HashProblems = () => {
    const { hash, problemId } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problem);

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    console.log('butthole', problems);

    useEffect(() => {
        dispatch(getSpecificProblem(hash, problemId))
    }, [dispatch, hash, problemId])

    return (
        <div>
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
                    </div>
                    <div>
                        <input type="checkbox" name="checked" value="Review" />
                        <h3>Review</h3>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default HashProblems;
