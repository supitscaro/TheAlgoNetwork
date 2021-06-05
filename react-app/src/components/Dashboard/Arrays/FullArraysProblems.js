import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, Link } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";
import { addProblemToSolved, allSolved } from "../../../store/solved";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';
import NavBar from '../../NavBar';
import './problem.css';

const ArrayProblems = () => {
    const { problemId } = useParams();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const all_problems = useSelector(state => state.problems.problem);
    const problemsSolvedList = useSelector(state => state.solvedLists.allSolvedLists);

    console.log('butthole2', problemsSolvedList);

    const [choice, setChoice] = useState(false);
    const [solved, setSolved] = useState(false);
    const [isSolved, setIsSolved] = useState(false);
    let userId = user?.id

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem("arrays", problemId, userId))
    }, [dispatch, "arrays", problemId, userId]);

    useEffect(() => {
        dispatch(allSolved())
    }, [dispatch]);

    const addReview = async (e) => {
        let choiceMade = choice;

        await dispatch(addProblemToReview(problemId, userId, choiceMade))
    };

    const addProblem = async (e) => {
        let problemSolved = solved;

        await dispatch(addProblemToSolved(problemId, userId, problemSolved))
    };

    for (let item in problemsSolvedList) {
        let problem = problemsSolvedList[item];

        if ((userId === problem.users_id) && (problemId === problem.problems_id)) {
            setIsSolved(true)
        }
    }

    return (
        <div className="problems-outer-div">
            <div>
                <NavBar />
            </div>
            <div className="problems-div">
                {problems.map((problem) => (
                    <div className="problem-div-container">
                        <div className="problem-container">
                            <div className="prob-title">Question: {problem.title}</div>
                            <div className="prob-cat">Category: {problem.category}</div>
                            <div className="prob-desc">{problem.description}</div>
                            <div className="code-blocks">
                                <div className="examples">
                                    Example:
                                <SyntaxHighlighter
                                        language="python"
                                        wrapLines={true}
                                        style={duotoneLight}
                                    >
                                        {problem.examples}
                                    </SyntaxHighlighter>
                                </div>
                            </div>
                            <div className="solved-mark">
                                <label className="pill-btn">
                                    <input className="radio-btn" type="radio" name="checked" onChange={() => [setSolved(true), setIsSolved(true)]} />
                                    <h3 className="label">Solved</h3>
                                </label>
                                <button disabled={!solved || isSolved} onClick={addProblem}>Solved</button>
                            </div>
                            <div className="review-mark">
                                <div className="pill-btn">
                                    <input className="radio-btn" type="radio" name="checked" onChange={() => setChoice(true)}>

                                    </input>
                                    <h3 className="label">Review</h3>
                                </div>
                                <button disabled={!choice} onClick={addReview}>Review</button>
                            </div>
                        </div>
                        <div className="code-block">
                            <SyntaxHighlighter
                                language="python"
                                lineProps={{ style: { wordBreak: 'break-all', whiteSpace: 'pre-wrap' } }}
                                style={materialOceanic}
                                showLineNumbers={true}
                                wrapLines={true}>
                                {problem.solution}
                            </SyntaxHighlighter>
                        </div>
                    </div>
                ))}
            </div>
        </div >
    )
}

export default ArrayProblems;
