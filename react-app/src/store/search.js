const GET_SEARCH = "search/GET_SEARCH";

// ACTIONS ----------------------------

const getUserSearch = (search) => ({
    type: GET_SEARCH,
    search
});


// THUNKS ------------------------------------------------------

export const getSearch = () => async (dispatch) => {
    const res = await fetch(`/api/search}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getSolvedList(data))
    }
};


// REDUCER ------------------------------------------------------

let initialState = {
    userSearch: {}
};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_SEARCH:
            return {
                userSearch: action.search
            }
        default:
            return state;
    }
};
