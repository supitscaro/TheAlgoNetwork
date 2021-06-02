import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';

const ArrayProblems = () => {
    const { arrays, problemId } = useParams();
    const dispatch = useDispatch();
    const all_problems = useSelector(state => state.problems.problem);

    const [checked, setChecked] = useState(false);
    const [choice, setChoice] = useState(false);

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem(arrays, problemId))
    }, [dispatch, arrays, problemId])

    const addProblemToReview = (e) => {
        let problem = problems.id;

        await dispatch(addProblemToReview(problem))
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
                        <input type="checkbox" name="checked" checked={checked === true} onClick={() => setChoice(true)} />
                        <h3>Review</h3>
                        <button disabled={!choice}>Save Changes</button>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default ArrayProblems;
