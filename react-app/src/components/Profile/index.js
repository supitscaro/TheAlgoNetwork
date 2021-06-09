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
    const user = useSelector(state => state.session.user);
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
            <div className="profile-body">
                <div className="user-intro">
                    <h3 className="user-name">Hi, {user.fname} {user.lname} 👋🏼</h3>
                </div>
                <div className="user-stats">
                    <div className="reviews-component">
                        <h2 className="prob-review-title">The problems you want to review:</h2>
                        <div className="problem-review">
                            {reviews.map((review, i) => (
                                <div className="prob-review" key={i}>
                                    <div className="prob-title-diff">
                                        {difficultyRender(review.difficulty)}
                                        <Link className="review-prof-title" to={`/${review.category}/${review.id}`}>
                                            <div>{review.title}</div>
                                        </Link>
                                    </div>
                                    <div onClick={() => deleteProblem(review.id)}><i className="fas fa-times"></i></div>
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className="solved-component">
                        <div className="prob-solved-div">
                            <h2 className="prob-solved-title">The problems you've solved:</h2>
                            {probSolved.map((problem, i) => (
                                <div className="prob-solved" key={i}>
                                    <div className="prob-title-diff">
                                        {difficultyRender(problem.difficulty)}
                                        <Link className="solved-prof-title" to={`/${problem.category}/${problem.id}`}>
                                            <div>{problem.title}</div>
                                        </Link>
                                    </div>
                                    <div onClick={() => deleteSolved(problem.id)}><i className="fas fa-times"></i></div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Profile;
