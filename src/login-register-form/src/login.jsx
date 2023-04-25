import React, { useState } from "react";
import logo from "./pill_logo.svg";

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
      }

    return (
        <div className="auth-form-container">
            <img src={logo} className="Pill-logo" alt="logo" />
            <h2>Login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="Email" id="email" name="email"/>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="Password" id="password" name="password"/>
                <button type="submit">Log In</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here</button>
            <div className="social-buttons">
                <button className="google-btn">Log in with Google</button>
                <button className="apple-btn">Log in with Apple</button>
            </div>

        </div>
    )
}