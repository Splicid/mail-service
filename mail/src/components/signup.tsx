import React from "react"
import "../styling/signup.css"

const Signup: React.FC = () => {

    return (
        <div className="signup-container">
            <div className="signup-box">
                <h2>Sign Up</h2>
                <form className="signup-form">
                    <input type="text" placeholder="Username" className="input-field" required />
                    <input type="email" placeholder="Email" className="input-field" required />
                    <input type="password" placeholder="Password" className="input-field" required />
                    <input type="password" placeholder="Confirm Password" className="input-field" required />
                    <button type="submit" className="custom-button signup-button">Sign Up!</button>
                </form>
            </div>
      </div>
    );
}

export default Signup;