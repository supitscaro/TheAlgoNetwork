const GET_REVIEW_LIST = "reviews/GET_REVIEW_LIST";

// ACTIONS ----------------------------

const getReviewList = (reviews) => ({
    type: GET_REVIEW_LIST,
    reviews
});
