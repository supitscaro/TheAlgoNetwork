const GET_ALL_PROBLEMS = "problems/GET_ALL_PROBLEMS";


// ACTIONS

const getProblems = (problems) => ({
    type: GET_ALL_PROBLEMS,
    problems
});


// THUNKS

export const getAllProblems = (category) => async (dispatch) => {
    const res = await fetch(`/api/problems/${category}`);

    if (res.ok) {
        let data = await res.json();
        dispatch(getProblems(Object.values(data)));
    }
};


// REDUCER

let initialState = {
    problems: {}
}

export default function reducer(state = initialState, action) {
    switch(action.type) {
        case GET_ALL_PROBLEMS:
            return {
                ...state,
                problems: action.problems
            }
        default:
            return state;
    }
}