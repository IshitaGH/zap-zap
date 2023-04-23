import './index.scss'
import { useState } from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

function SignIn() {
    //login for users
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);
    const navigate = useNavigate();
    async function validateUser(username, password) {
        const response = await fetch('http://localhost:8000/endpoints/user'); //insert http request
        if (response.status == 200) {
            for (const user in response.data) {
                if (user.username == username && user.password == password) {
                    window.sessionStorage.setItem("user-data", user);
                }
            }
            navigate(`/dashboard${window.sessionStorage.getItem("user-data").id}`);
        }
        else {
            setError(true);
        } 
    }
    function validateForm() {
        return username.length > 0 && password.length > 0;
    }
    
    function handleSubmit(event) {
        event.preventDefault();
        validateUser(username, password);
    }
    return (
        <div id='login-container'>
            <Form onSubmit={handleSubmit}>
                <Form.Group size="lg" controlId="username" id='form-label'>
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                        autoFocus
                        type="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}/>
                </Form.Group>
                <Form.Group size="lg" controlId="password" id='form-label'>
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </Form.Group>
            <Button block size="lg" type="submit" disabled={!validateForm()}>Login</Button>
            </Form>
            {error ? 
                <div>Invalid username or password.</div> :
                <div></div>
            }
        </div>
        
    );
}
export default SignIn;