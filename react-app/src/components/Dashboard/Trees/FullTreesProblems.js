import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { shadesOfPurple, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';

const TreesProblems = () => {
    const { trees, problemId } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problem);

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    console.log('butthole', problems);

    useEffect(() => {
        dispatch(getSpecificProblem(trees, problemId))
    }, [dispatch, trees, problemId])

    return (
        <div>
            {problems.map((problem) => (
                <div>
                    <div>{problem.title}</div>
                    <div>{problem.category}</div>
                    <div>{problem.description}</div>
                    <SyntaxHighlighter
                        language="python"
                        lineProps={{ style: { wordBreak: 'break-all', whiteSpace: 'pre-wrap' } }}
                        style={materialOceanic}
                        showLineNumbers={true}
                        wrapLines={true}>
                        {problem.solution}
                    </SyntaxHighlighter>
                    {/* <CodeBlock text={problem.solution} language={problem.language} theme={dracula} wraplines/> */}
                </div>
            ))}
        </div>
    )
}

export default TreesProblems;
