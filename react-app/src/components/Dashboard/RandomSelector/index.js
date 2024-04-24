import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";

import { getEveryProblem } from "../../../store/problems";
import { allSolved } from "../../../store/solved";

import "./random.css";

const RandomProblem = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const user = useSelector((state) => state.session?.user);
  const allProblems = useSelector((state) => state.problems?.allProblems);
  const problemsSolvedList = useSelector(
    (state) => state.solvedLists?.allSolvedLists
  );

  // create a list of the problem's id a user has solved
  let listOfSolved = [];

  for (let i in problemsSolvedList) {
    let problem = problemsSolvedList[i];

    if (user?.id === problem?.users_id) {
      listOfSolved.push(problem.problems_id);
    }
  }

  listOfSolved.sort();
  // create a list of every problem's id to then filter if the id is present in listOfSolved
  let unsolvedProblems = [];

  for (let i in allProblems) {
    let problem = allProblems[i];
    unsolvedProblems.push(problem.id);
  }

  // create a new list of all the id's not present in user's solved list
  let problemsToStudy = [];

  for (let i = 0; i < unsolvedProblems.length; i++) {
    let id = unsolvedProblems[i];
    let bool = listOfSolved.includes(id);
    if (!bool) {
      problemsToStudy.push(id);
    }
  }

  // randomly get an id of the problems the user has left to study
  let randomProblemId = Math.floor(Math.random() * problemsToStudy.length);

  // grab the category and id to redirect a user to that problem they haven't solved
  let category;
  let id;
  for (let i in allProblems) {
    let problem = allProblems[i];

    if (problem.id === problemsToStudy[randomProblemId]) {
      category = problem.category;
      id = problem.id;
    }
  }

  useEffect(() => {
    dispatch(allSolved());
  }, [dispatch]);

  useEffect(() => {
    dispatch(getEveryProblem());
  }, [dispatch]);

  const onClick = () => {
    history.push(`/${category}/${id}`);
  };

  return (
    <div className="rand-btn" onClick={onClick}>
      Generate a Random Problem
    </div>
  );
};

export default RandomProblem;
