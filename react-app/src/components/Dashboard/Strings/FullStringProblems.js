import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";
import { addProblemToSolved } from "../../../store/solved";

import '../Arrays/problem.css'

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';
import NavBar from '../../NavBar';
import '../Arrays/problem.css'

const StringsProblems = () => {
    const { problemId } = useParams();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const all_problems = useSelector(state => state.problems.problem);

    const [choice, setChoice] = useState(false);
    const [solved, setSolved] = useState(false);
    let userId = user?.id;

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem("strings", problemId))
    }, [dispatch, "strings", problemId, userId]);

    const addReview = async (e) => {
        let choiceMade = choice;

        await dispatch(addProblemToReview(problemId, userId, choiceMade))
    }

    const addProblem = async (e) => {
        let problemSolved = solved;

        await dispatch(addProblemToSolved(problemId, userId, problemSolved))
    }

    return (
        <div className="problems-outer-div">
            <div>
                <NavBar />
            </div>
            <div className="problems-div">
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
                            <h3>Solved</h3>
                            <input type="radio" name="checked" onChange={() => setSolved(true)} />
                            <button disabled={!solved} onClick={addProblem}>Save Changes</button>
                        </div>
                        <div>
                            <h3>Review</h3>
                            <input type="radio" name="checked" onChange={() => setChoice(true)} />
                            <button disabled={!choice} onClick={addReview}>Save Changes</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default StringsProblems;
