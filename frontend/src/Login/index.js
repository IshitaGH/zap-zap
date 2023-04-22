import './index.scss'
import React from 'react';
import { useNavigate } from "react-router-dom";



class Login extends React.Component {
    //login for users
    handleSignIn = () => {
        const navigate = useNavigate();
        navigate("/signin");
    }
    
    handleSignUp = () => {
        const navigate = useNavigate();
        navigate("/signup");
    }
    constructor(props) {
        super(props);
        this.state = {
            reveal: false
        }
        this.handleChange = this.handleChange.bind(this);
    }
    handleChange() {
        this.setState({
            reveal: true
        })
    }
    componentDidUpdate() {
        const element = document.getElementById('buttons-container');
        // window.scroll({
        //     top: document.body.offsetHeight,
        //     left: 0, 
        //     behavior: 'smooth',
        // });
        
        element.scrollIntoView({behavior: 'smooth'});
    }
    
    render() {
        let buttons_container;
        const reveal = this.state.reveal;
        if (reveal) {
            buttons_container = 
            <div id='buttons-container'>
                <button id='create-account-button' onClick={this.handleSignIn} type="button">Sign up!</button>
                <button id='login-button' onClick={this.handleClick} type="button">Sign in!</button>
            </div>;
        } 
        else {
            buttons_container = 
            <div id='get-started-button'><button id='get-started-button' onClick={this.handleChange}>  Get Started!</button></div>;
        }
        return (
            <div className='page-container'>
                <div className='content-container'>
                    <h1 id='welcome-header'>Zap-Zap!</h1>
                    {buttons_container}
                </div>
            </div>
        );
    }
}
export default Login;