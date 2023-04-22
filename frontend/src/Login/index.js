import './index.scss'
import React from 'react';
import {Link} from "react-router-dom";



class Login extends React.Component {
    //login for users
    nextPath(path) {
        this.props.history.push(path);
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
                <Link id='create-account-button' to='/signup'>Sign up!</Link>
                <Link id='login-button' to='/signin'>Sign in!</Link>
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