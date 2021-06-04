const GET_SOLVED_LIST = "solvedLists/GET_SOLVED_LIST";
const ADD_TO_SOLVED = "solvedLists/ADD_TO_SOLVED";
const REMOVE_SOLVED = "solvedLists/REMOVE_SOLVED";

// ACTIONS ----------------------------

const getSolvedList = (solved) => ({
    type: GET_SOLVED_LIST,
    solved
});

const addSolved = (problem, user, checked) => ({
    type: ADD_TO_SOLVED,
    payload: {
        problem,
        user,
        checked
    }
});

const deleteSolved = (problem) => ({
    type: REMOVE_SOLVED,
    problem
});


// THUNKS ------------------------------------------------------

export const getAllSolved = (userId) => async (dispatch) => {
    const res = await fetch(`/api/solved/${userId}`);

    if (res.ok) {
        let data = await res.json()
        dispatch(getSolvedList(data))
    }
};

export const addProblemToSolved = (problemId, userId, checked) => async (dispatch) => {
    const res = await fetch(`/api/solved/${problemId}/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ checked, userId, problemId })
    });

    if (res.ok) {
        dispatch(addSolved(problemId, userId, checked))
    }
};


export const deleteProblemFromSolved = (problemId) => async (dispatch) => {
    console.log('problem id in thunk', problemId);
    const res = await fetch(`/api/solved/${problemId}`, {
        method: 'DELETE'
    });

    if (res.ok) {
        let data = await res.json();

        dispatch(deleteSolved(data));
    }
};


// REDUCER ------------------------------------------------------

let initialState = {
    solvedList: {}
};

export default function reducer(state = initialState, action) {
    let newState = {};
    switch (action.type) {
        case GET_SOLVED_LIST:
            return {
                ...state,
                solvedList: action.solved
            }
        case ADD_TO_SOLVED:
            return {
                ...state,
                ...state.solvedList,
                solvedList: { ...state.solvedList, [action.payload.user]: action.payload }
            }
        case REMOVE_SOLVED:
            newState = { ...state, solvedList: { ...state.solvedList } };
            delete newState['solvedList'][action.problem.problems_id]
            return newState;
        default:
            return state;
    }
};
