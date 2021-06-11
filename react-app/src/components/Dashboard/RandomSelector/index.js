import React, { useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";


import { getEveryProblem } from "../../../store/problems";
import { addProblemToReview } from "../../../store/reviews";
import { allSolved } from "../../../store/solved";

const RandomProblem = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session?.user);
    const allProblems = useSelector(state => state.problems?.allProblems);
    const problemsSolvedList = useSelector(state => state.solvedLists?.allSolvedLists);

    let listOfSolved = []

    for (let i in problemsSolvedList) {
        let problem = problemsSolvedList[i];

        if (user?.id === problem?.users_id) {
            listOfSolved.push(problem.problems_id);
        }
    }
    // console.log('list of problems solved', listOfSolved);

    listOfSolved.sort();

    let unsolvedProblems = []

    for (let i in allProblems) {
        let problem = allProblems[i];
        unsolvedProblems.push(problem.id);
    }

    console.log('butthole', unsolvedProblems);

    let problemsToStudy = [];

    for (let i = 0; i < unsolvedProblems.length; i++) {
        let id = unsolvedProblems[i];
        let bool = listOfSolved.includes(id);
        if (!bool) {
            problemsToStudy.push(id);
        }
    }

    console.log('butt', problemsToStudy);

    useEffect(() => {
        dispatch(allSolved())
    }, [dispatch])

    useEffect(() => {
        dispatch(getEveryProblem())
    }, [dispatch])

    const onClick = () => {
        console.log('button works');
    }

    return (
        <div onClick={onClick}>Get Random Problem</div>
    )

}

export default RandomProblem;
