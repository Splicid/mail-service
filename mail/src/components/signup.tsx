import React from "react"
import { useState } from 'react';
import axios from "axios";
import "../styling/signup.css"


interface userInfo {
    username: string,
    password: string,
}


const Signup: React.FC = () => {

    const [email, setEmail] = useState<string>("")
    const [username, setUsername] = useState<string>("")
    const [password, setPassword] = useState<string>("")

    const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            const response = await axios.post('http://localhost:5000/', {
                userEmail: email,
                user: username,
                userPassword: password
            });
            console.log(response)
        } catch (error) {
            console.log(error)
        }

    }

    return (
        <div className="signup-container">
            <div className="signup-box">
                <h2>Sign Up</h2>
                <form onSubmit={submit} className="signup-form">
                    <input type="text" placeholder="Username" className="input-field" 
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required />
                    <input type="email" placeholder="Email" className="input-field"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required />
                    <input type="password" placeholder="Password" className="input-field" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required />
                    <input type="password" placeholder="Confirm Password" className="input-field" required />
                    <button type="submit" className="custom-button signup-button">Sign Up!</button>
                </form>
            </div>
      </div>
    );
}

export default Signup;