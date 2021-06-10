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

    console.log('list of problems solved', listOfSolved);

    console.log('all problems', allProblems);

    let unsolvedProblems = []

    for (let i in allProblems) {
        let problem = allProblems[i];
        console.log('probleeeeeems', problem.id);

    }

    // let randomProblem = Math.floor(Math.random() * listOfSolved.length);

    // console.log('randomproblem', listOfSolved[randomProblem]);

    // let problems = listOfSolved[randomProblem]; // returns a number

    // for (let problem in problems) {
    //     console.log('problem id?', problem);
    //     let id;
    //     if (problem === 'problems_id') {
    //         id = problem;
    //     }

    //     console.log('is this the id????', problems.id);
    // }
    // // console.log('random problem id', randomProblem.id)

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
