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
    console.log('butthole2', userId);
    const res = await fetch(`/api/reviews/${userId}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getReviewList(data))
    }
};


export const addProblemToReview = (problemId, userId, checked) => async (dispatch) => {
    console.log('butthole1', problemId);
    console.log('butthole2', userId);
    console.log('butthole3', checked);

    const res = await fetch(`/api/reviews/${problemId}/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ checked, userId, problemId })
    });

    if (res.ok) {
        // let data = await res.json()
        dispatch(addProblem(problemId, userId, checked))
    }
}


// REDUCER ------------------------------------------------------

let initialState = {
    reviews: {},
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_REVIEW_LIST:
            return {
                ...state,
                reviews: action.reviews
            }
        default:
            return state;
    }
}
