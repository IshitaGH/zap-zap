import './index.scss'
import { useEffect, useState } from 'react';

function Login() {
    //login for users
    
    const [reveal, setReveal] = useState(false);
    useEffect(() => {
        console.log("hoe")
        window.scroll({
            top: document.body.offsetHeight,
            left: 0, 
            behavior: 'smooth',
        });
    }, [reveal]); //doesn't work :( someone fix bc i dont want to thanks one love
    function revealSection() {
        setReveal(!reveal);
    }

    function scoll() {
        
    }

    return (
        <div className='page-container'>
            <div className='content-container'>
                <h1 id='welcome-header'>Zap-Zap!</h1>
                {!reveal ? <div id='get-started-button'><button id='get-started-button' onClick={revealSection}>  Get Started!</button></div> :
                <div id='buttons-container'>
                    <button id='login-button'> Sign in!</button>
                    <button id='create-account-button'>Sign up!</button>
                </div>
                }
            </div>
        </div>
    );
}
export default Login;