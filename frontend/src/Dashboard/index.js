import './index.scss';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import React from 'react';
import logo from '../assets/logo.png';
import { Link } from "react-router-dom";
import { endpoint } from "../util";
import CSRFToken from "../csrftoken";

class Dashboard extends React.Component {
    //dsahboard for users
    constructor(props) {
        super(props);
        this.state = {
            add_targets: false,
            update_targets: false,
            new_target_name: "",
            new_target_pic: "",
            files: null
        }
        this.handleChange = this.handleChange.bind(this);
    }
    handleChange(evt) {
        if (evt.target.name == "logout") {
            sessionStorage.clear();
        } else if (evt.target.name == "add_targets") {
            this.setState({
                add_targets: !this.state.add_targets,
            })
        } else if (evt.target.name == "update_targets") {
            this.setState({
                update_targets: !this.state.update_targets,
            })
        }
    }

    handleSubmit(action) {
        return (event) => {
            event.preventDefault();
            if (action === "add") {
                fetch(endpoint("add-target"))
            } else {

            }
        }
    }

    render() {
        let trusted_add_form;
        let trusted_update_form;
        const add_targets = this.state.add_targets;
        const update_targets = this.state.update_targets;
        if (add_targets) {
            trusted_add_form =
                <form method="POST" action={endpoint("add-target")}>
                    <input name="target_name" placeholder="Target name" />
                    <input name="author" value="3" className="hidden" />
                    <button type="submit">Add Target</button>
                    <CSRFToken />
                </form>;
        }
        else {
            trusted_add_form = <div></div>
        }
        if (update_targets) {
            trusted_update_form =
                <form method="POST" action={endpoint("change-target-photo/2")} encType="multipart/form-data">
                    <input type="file" name="image" />
                    <button type="submit">Update Target Photo</button>
                    <CSRFToken />
                </form>;
        }
        else {
            trusted_update_form = <div></div>
        }
        return (
            <div className='page-container'>
                <div className='content-container'>
                    <div id='dashboard-header'>
                        <img src={logo} alt="logo" id="logo" />
                        <img src="https://preview.redd.it/oy43s2y9xym81.jpg?auto=webp&s=6ba16c42e3ce1e6328668f21ea48477fc6aa16ca" alt="profile-pic" id='profile-pic' />
                        <p>Serena</p>
                        <button className='main-button'>Account Settings</button>
                        <Link name="logout" className='main-button' to='/' onClick={this.handleChange}>Logout</Link>
                    </div>

                    <div id='settings-grid-container'>
                        <div id='summary-and-actions'>
                            <div id='summary-grid'>
                                <h3 id='summary-header'>Summary</h3>
                                <p className='status-message'>Mom entered your house at 10am on 4/10/23.</p>
                                <p className='status-message'>Ishita entered your house at 2am on 4/20/23.</p>
                                <p className='status-message'>JSON entered your house at 2am on 4/20/23.</p>
                                <p className='status-message'>Catherine entered your house at 11am on 4/21/23.</p>
                            </div>
                            <div className="button" id="contact-button">
                                <div id="spin"></div>
                                <a>Call Emergency Contacts.</a>
                            </div>
                            <div className="button" id="contact-button">
                                <div id="spin"></div>
                                <a>Call 911.</a>
                            </div>
                        </div>
                        <div id='security-settings-grid'>Security Settings
                            <div className="button" id="contact-button">
                                <div id="spin"></div>
                                <a>Activate Laser.</a>
                            </div>
                            <div className="button" id="contact-button">
                                <div id="spin"></div>
                                <a>Activate Alarm.</a>
                            </div>
                            <div className="button" id="contact-button">
                                <div id="spin"></div>
                                <a>Activate Auto Dial Emergency Contacts.</a>
                            </div>
                        </div>
                    </div>

                    <h2 id="trusted-title">Trusted Profiles</h2>
                    <div id='trusted-people-grid'>
                        <button className='main-button' name="add_targets" value={!this.state.add_targets} onClick={this.handleChange}>Create New Trusted Profile</button>
                        {trusted_add_form}
                        <button className='main-button' name="update_targets" value={!this.state.update_targets} onClick={this.handleChange}>Update Trusted Profiles</button>
                        {trusted_update_form}
                    </div>
                </div>
            </div>
        );
    }
}
export default Dashboard;
