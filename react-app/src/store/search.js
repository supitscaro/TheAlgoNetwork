const GET_SEARCH = "search/GET_SEARCH";

// ACTIONS ----------------------------

const getUserSearch = (search) => ({
    type: GET_SEARCH,
    search
});


// THUNKS ------------------------------------------------------

export const getAllSolved = (userId) => async (dispatch) => {
    const res = await fetch(`/api/solved/${userId}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getSolvedList(data))
    }
};


// REDUCER ------------------------------------------------------

let initialState = {};

export default function reducer(state = initialState, action) {
    let newState = {};
    switch (action.type) {

        default:
            return state;
    }
};
