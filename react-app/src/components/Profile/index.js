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
    let reviews = [];

    let reviewId;
    console.log('review', reviewId)

    for (let key in allProblemsToReview) {
        let val = allProblemsToReview[key];
        reviews.push(val)
        console.log('ok', val)
        // reviewId = val.id
    }

    useEffect(() => {
        dispatch(getAllReviews(id))
    }, [dispatch]);


    let deleteProblem = async (e) => {
        console.log('test', e)
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
                    <button onClick={(e) => deleteProblem(e.target.value)}>Delete</button>
                </div>
            ))}
            </div>
        </div>
    )
}

export default Profile;
