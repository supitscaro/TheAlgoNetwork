import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';

const ArrayProblems = () => {
    const { problemId } = useParams();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    console.log('user?', user)

    const all_problems = useSelector(state => state.problems.problem);

    const [checked, setChecked] = useState(false);
    const [choice, setChoice] = useState(false);
    let userId = user?.id

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem("arrays", userId, problemId))
    }, [dispatch, "arrays", userId, problemId])

    const addProblem = async (e) => {
        let problem = problems.id;
        let choiceMade = checked;

        await dispatch(addProblemToReview(userId, problem, choiceMade))
    }

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
                        <button>Save Changes</button>
                    </div>
                    <div>
                        <h3>Review</h3>
                        <input type="radio" name="checked" checked={checked === true} onChange={() => setChoice(true)} />
                        <button disabled={!choice} onClick={addProblem}>Save Changes</button>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default ArrayProblems;
