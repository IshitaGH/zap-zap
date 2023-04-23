import { endpoint } from '../util';
import './index.scss'
import { useEffect, useState } from 'react';

function SignUp() {
    //login for users
    

    return (
        <form method="POST" action={endpoint("add-user")}>
            <input name="username"></input>
            <input type="password" name="password"></input>
            <button type="submit">Sign Up</button>
        </form>
    );
}
export default SignUp;
