import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { BrowserRouter, Route, Link } from "react-router-dom";
import { getAllReviews, deleteProblemFromReview } from "../../store/reviews";
import NavBar from '../NavBar';

import './index.css';

const Profile = () => {
    const { id } = useParams();
    const dispatch = useDispatch();
    const allProblemsToReview = useSelector(state => state.reviews.reviews);

    console.log('butt', allProblemsToReview);

    let reviews = [];

    for (let key in allProblemsToReview) {
        let val = allProblemsToReview[key];
        reviews.push(val)
    }

    useEffect(() => {
        dispatch(getAllReviews(id))
    }, [dispatch]);


    let deleteProblem = async (id) => {
        dispatch(deleteProblemFromReview(id))
    }

    return (
        <div className="profile-outer-div">
            <NavBar />
            <div>
                Problems To Review:
                {reviews.map((review) => (
                <div>
                    <Link to={`/${review.category}/${review.id}`}>
                        <div>{review.title}</div>
                    </Link>
                    <button onClick={() => deleteProblem(review.id)}>Delete</button>
                </div>
            ))}
            </div>
            <div>
                Problems Solved
            </div>
        </div>
    )
}

export default Profile;
