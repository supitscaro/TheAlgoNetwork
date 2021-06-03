const GET_SOLVED_LIST = "solvedLists/GET_SOLVED_LIST";


// ACTIONS ----------------------------

const getSolvedList = (solved) => ({
    type: GET_SOLVED_LIST,
    solved
});


// THUNKS ------------------------------------------------------

export const getAllSolved = (userId) => async (dispatch) => {
    const res = await fetch(`/api/solved/${userId}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getSolvedList(data))
    }
}


// REDUCER ------------------------------------------------------

let initialState = {
    solvedList: {}
};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_SOLVED_LIST:
            return {
                ...state,
                solvedList: action.solved
            }
        default:
            return state;
    }
};
