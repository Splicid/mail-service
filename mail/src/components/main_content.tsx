import React from "react"
import '../styling/main-content.css'
import {
    BrowserRouter as Router,
    Route,
    Link
  } from "react-router-dom";


const Main_Content: React.FC = () => {

    return (
          <div className="main-content">
            <div className="left-content">
                <h3> Want to annoy people? Use this service!</h3>
                <div className="button-container">
                    <Link to="/signup">
                        <button className="custom-button signup-button">Sign Up!</button>
                    </Link>
                    <Link to="/">
                        <button className="custom-button compare-button">Compare Plans</button>
                    </Link>
                </div>
            </div>
          </div>
      );
}


export default Main_Content