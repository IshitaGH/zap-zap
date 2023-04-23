import './index.scss'
import { useState } from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

function SignIn() {
    //login for users
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);
    const navigate = useNavigate();
    async function validateUser(email, password) {
        const response = await fetch('https://pokeapi.co/api/v2/pokemon/dog'); //insert http request
        if (response.status == 200) {
            navigate(`/dashboard${response.id}`);
        }
        else {
            setError(true);
        } 
    }
    function validateForm() {
        return email.length > 0 && password.length > 0;
    }
    
    function handleSubmit(event) {
        event.preventDefault();
        validateUser(email, password);
    }
    return (
        <div id='login-container'>
            <Form onSubmit={handleSubmit}>
                <Form.Group size="lg" controlId="email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        autoFocus
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}/>
                </Form.Group>
                <Form.Group size="lg" controlId="password">
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