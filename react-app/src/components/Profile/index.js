import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { BrowserRouter, Route, Link } from "react-router-dom";
import { getAllReviews } from "../../store/reviews";
import NavBar from '../NavBar';

import './index.css';

const Profile = () => {
    const { id } = useParams();
    const dispatch = useDispatch();
    const allProblemsToReview = useSelector(state => state.reviews.reviews);
    console.log('butthole', allProblemsToReview)
    let reviews = [];

    for (let key in allProblemsToReview) {
        let val = allProblemsToReview[key];
        reviews.push(val)
    }

    useEffect(() => {
        dispatch(getAllReviews(id))
    }, [dispatch])

    return (
        <div className="profile-outer-div">
            <NavBar />
            <div>
                Problems To Review:
                {reviews.map((review) => (
                <Link to={`/${review.category}/${review.id}`}>
                    <div>{review.title}</div>
                </Link>
            ))}
            </div>
        </div>
    )
}

export default Profile;
