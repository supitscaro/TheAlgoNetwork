const GET_ALL_PROBLEMS = "problems/GET_ALL_PROBLEMS";
const GET_SPECIFIC_PROBLEM = "problems/GET_SPECIFIC_PROBLEM";
const GET_PROBLEMS = "problems/GET_PROBLEMS";

// ACTIONS ----------------------------

const getProblems = (problems) => ({
    type: GET_ALL_PROBLEMS,
    problems
});

const getProblem = (problem) => ({
    type: GET_SPECIFIC_PROBLEM,
    problem
});

const getProblemsList = (problemsList) => ({
    type: GET_PROBLEMS,
    problemsList
});


// THUNKS ------------------------------------------------------

// gets all problems based on category
export const getAllProblems = (category) => async (dispatch) => {
    const res = await fetch(`/api/problems/${category}`);

    if (res.ok) {
        let data = await res.json();
        dispatch(getProblems(Object.values(data)));
    }
};


// gets problem based on category and id
export const getSpecificProblem = (category, id) => async (dispatch) => {
    console.log('category', category);
    console.log('id', id);

    const res = await fetch(`/api/problems/${category}/${id}`);

    if (res.ok) {
        let data = await res.json();
        dispatch(getProblem(data));
    }
};

// get all problems regardless of category
export const getEveryProblem = () => async (dispatch) => {
    const res = await fetch(`/api/problems/`);

    if (res.ok) {
        let data = await res.json();
        dispatch(getProblemsList(data))
    }
};


// REDUCER ------------------------------------------------------

let initialState = {
    problems: {},
    problem: {},
    allProblems: {}
}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_PROBLEMS:
            return {
                ...state,
                problems: action.problems
            }
        case GET_SPECIFIC_PROBLEM:
            return {
                ...state,
                problem: action.problem
            }
        case GET_PROBLEMS:
            return {
                ...state,
                allProblems: action.problemsList
            }
        default:
            return state;
    }
}
