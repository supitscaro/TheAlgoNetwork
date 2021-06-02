import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { BrowserRouter, Route, Link } from "react-router-dom";
import { getAllReviews } from "../../store/reviews";


const Profile = () => {
    const { id } = useParams();
    const dispatch = useDispatch();
    const allProblemsToReview = useSelector(state => state.reviews.reviews);
    console.log('butthole', allProblemsToReview)
    let reviews = [];

    for (let key in allProblemsToReview) {
        let val = allProblemsToReview[key];
        reviews.push(val.title)
    }

    useEffect(() => {
        dispatch(getAllReviews(id))
    }, [dispatch])

    return (
        <>
            Problems To Review:
            {reviews.map((review) => (
                <div>{review}</div>
            ))}
        </>
    )
}

export default Profile;
