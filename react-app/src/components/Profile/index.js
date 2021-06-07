import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { BrowserRouter, Route, Link } from "react-router-dom";
import { getAllReviews, deleteProblemFromReview } from "../../store/reviews";
import { getAllSolved, deleteProblemFromSolved } from "../../store/solved";
import NavBar from '../NavBar';

import './index.css';

const Profile = () => {
    const { id } = useParams();
    const dispatch = useDispatch();
    const allProblemsToReview = useSelector(state => state.reviews.reviews);
    const problemsSolvedList = useSelector(state => state.solvedLists.solvedList);

    let reviews = [];
    let probSolved = []

    for (let key in allProblemsToReview) {
        let val = allProblemsToReview[key];
        reviews.push(val)
    }

    for (let key in problemsSolvedList) {
        let val = problemsSolvedList[key]
        probSolved.push(val);
    }

    const difficultyRender = (difficulty) => {
        if (difficulty === 'Easy') {
            return <div className="easy-button"></div>
        } else if (difficulty === 'Medium') {
            return <div className="medium-button"></div>
        } else if (difficulty === 'Hard') {
            return <div className="hard-button"></div>
        }
    }

    useEffect(() => {
        dispatch(getAllReviews(id))
    }, [dispatch]);

    useEffect(() => {
        dispatch(getAllSolved(id))
    }, [dispatch])


    let deleteProblem = async (id) => {
        dispatch(deleteProblemFromReview(id))
    }

    let deleteSolved = async (id) => {
        dispatch(deleteProblemFromSolved(id))
    }

    return (
        <div className="profile-outer-div">
            <NavBar />
            <div className="problem-review">
                <h2 className="prob-review-title">Problems To Review:</h2>
                {reviews.map((review) => (
                    <div className="prob-review">
                        <div className="prob-title-diff">
                            {difficultyRender(review.difficulty)}
                            <Link className="review-prof-title" to={`/${review.category}/${review.id}`}>
                                <div>{review.title}</div>
                            </Link>
                        </div>
                        <div onClick={() => deleteProblem(review.id)}><i class="fas fa-times"></i></div>
                    </div>
                ))}
            </div>
            <div className="prob-solved-div">
                <h2 className="prob-solved-title">Problems Solved:</h2>
                {probSolved.map((problem) => (
                    <div className="prob-solved">
                        <div className="prob-title-diff">
                            {difficultyRender(problem.difficulty)}
                            <Link className="solved-prof-title" to={`/${problem.category}/${problem.id}`}>
                                <div>{problem.title}</div>
                            </Link>
                        </div>
                        <div onClick={() => deleteSolved(problem.id)}><i class="fas fa-times"></i></div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Profile;
