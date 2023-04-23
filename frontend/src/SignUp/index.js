import { endpoint } from '../util';
import './index.scss'
import { useEffect, useState } from 'react';

import CSRFToken from '../csrftoken';

function SignUp() {
    //login for users


    return (
        <form method="POST" action={endpoint("add-user")}>
            <input name="username" />
            <input type="password" name="password" />
            <button type="submit">Sign Up</button>
            <CSRFToken />
        </form>
    );
}
export default SignUp;
