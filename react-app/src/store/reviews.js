const GET_REVIEW_LIST = "reviews/GET_REVIEW_LIST";
const ADD_TO_REVIEW = "reviews/ADD_TO_REVIEW";

// ACTIONS ----------------------------


const getReviewList = (reviews) => ({
    type: GET_REVIEW_LIST,
    reviews
});

const addProblem = (review) => ({
    type: ADD_TO_REVIEW,
    review
})


// THUNKS ------------------------------------------------------

export const getAllReviews = (userId) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${userId}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getReviewList(data))
    }
};


export const addProblemToReview = (problemId, userId, checked) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${problemId}/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ checked, userId, problemId })
    });

    if (res.ok) {
        dispatch(addProblem(problemId, userId, checked))
    }
}


// REDUCER ------------------------------------------------------

let initialState = {
    reviews: {},
}

export default function reducer(state = initialState, action) {
    let newState = {};
    switch (action.type) {
        case GET_REVIEW_LIST:
            return {
                ...state,
                reviews: action.reviews
            }
        case ADD_TO_REVIEW:
            newState = { ...state };
            console.log('action.reviews', action.review);
            return {
                ...state,
                reviews: { ...state.reviews, [action.review.id]: action.review }
            }
        default:
            return state;
    }
}
