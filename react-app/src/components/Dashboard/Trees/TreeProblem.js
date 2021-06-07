import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, useHistory } from "react-router-dom";
import { getSpecificProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";
import { addProblemToSolved, allSolved } from "../../../store/solved";

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { duotoneLight, materialOceanic } from 'react-syntax-highlighter/dist/esm/styles/prism';
import NavBar from '../../NavBar';
import '../Arrays/problem.css'

const TreesProblems = () => {
    const { problemId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session.user);
    const all_problems = useSelector(state => state.problems.problem);
    const problemsSolvedList = useSelector(state => state.solvedLists?.allSolvedLists);

    const [choice, setChoice] = useState(false);
    const [solved, setSolved] = useState(false);
    const [isSolved, setIsSolved] = useState(false);
    let userId = user?.id;

    let problems = [];

    for (let key in all_problems) {
        problems.push(all_problems[key])
    }

    useEffect(() => {
        dispatch(getSpecificProblem("trees", problemId))
    }, [dispatch, "trees", problemId]);

    useEffect(() => {
        dispatch(allSolved())
    }, [dispatch]);

    const addReview = async (e) => {
        let choiceMade = choice;

        await dispatch(addProblemToReview(problemId, userId, choiceMade))
    }

    const addProblem = async (e) => {
        let problemSolved = solved;

        await dispatch(addProblemToSolved(problemId, userId, problemSolved))
    }

    const redirectAfterSolved = () => {
        addProblem();
        history.push("/");
    }

    let problemIsSolved = false;
    let problem;

    // grabs each individual problem from the list of solved problems
    for (let item in problemsSolvedList) {
        problem = problemsSolvedList[item];
        if ((parseInt(userId) === problem?.users_id) && (parseInt(problemId) === problem?.problems_id)) {
            problemIsSolved = true;
        }
    }

    let solvedComponent = () => {
        return (
            <div className="solved-mark">
                <label className="pill-btn">
                    <input className="radio-btn" type="radio" name="checked" onChange={() => [setSolved(true), setIsSolved(true)]} />
                    <h3 className="label">Solved</h3>
                </label>
                <button disabled={!solved} onClick={redirectAfterSolved}>Solved</button>
            </div>
        );
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
                        {problemIsSolved ? <div>You've marked this as solved!</div> : solvedComponent()}
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

export default TreesProblems;
