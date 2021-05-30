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
}
