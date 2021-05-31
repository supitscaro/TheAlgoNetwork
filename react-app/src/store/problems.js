const GET_ALL_PROBLEMS = "problems/GET_ALL_PROBLEMS";


// Actions

const getProblems = (problems) => ({
    type: GET_ALL_PROBLEMS,
    problems
})


// Thunks

export const problems = (category) => async (dispatch) => {
    const res = await fetch(`/api/problems/${category}`);

    console.log(res);

    if (res.ok) {
        let data = res.json();
        await dispatch(getProblems(data));
    }
}


// Reducer

let initialState = {
    problems: {}
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_PROBLEMS:
            return {
                ...state,
                problems: { ...action.problems }
            }
        default:
            return state
    }
}
