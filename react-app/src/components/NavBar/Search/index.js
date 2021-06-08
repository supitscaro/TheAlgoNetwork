import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux"
import { Redirect, Link } from 'react-router-dom';
import { getSearch } from '../../store/search';

const SearchBar = () => {
    const dispatch = useDispatch();
    const search = useSelector(state => state.search.userSearch);


};

export default SearchBar;
