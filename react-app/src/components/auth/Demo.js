import React from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { login } from '../../store/session';

import './demo.css';

let DemoButton = () => {
    const history = useHistory();
    const dispatch = useDispatch();

    const handleClick = async (e) => {
        e.preventDefault();

        await dispatch(login('caro@bu.io', 'password'));
        history.push('/');
    }

    return (
        <div className="demo-btn" onClick={handleClick} type='submit'>Demo User</div>
    )
}

export default DemoButton;
