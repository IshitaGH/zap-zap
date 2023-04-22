import './index.scss'
import logo from '../assets/logo.png'

function Dashboard() {
    //dsahboard for users
    return (
        <div className='page-container'>
            <div className='content-container'>
                <div id='dashboard-header'>
                <img src={logo} alt="logo"/>
                    <div id='user-box'>
                        <img src="https://preview.redd.it/oy43s2y9xym81.jpg?auto=webp&s=6ba16c42e3ce1e6328668f21ea48477fc6aa16ca" alt="profile-pic" id='profile-pic'/>
                        <p>Serena</p>
                        <button>Account Settings</button>
                        <button>Login</button>
                    </div>
                </div>
                <div id='settings-grid-container'>
                    <div id='summary-grid'>Summary
                        <button id='contact-button'>Call Emergency Contacts.</button>
                        <button id='contact-button'>Call 911</button>
                    </div>
                    <div id='security-settings-grid'>Security Settings
                        <button id='activate-button'>Activate Laser</button>
                        <button id='activate-button'>Activate Alarm</button>
                        <button id='activate-button'>Activate Auto Dial Emergency Contacts</button>
                    </div>
                    <div id='trusted-people-grid'>Trusted Profiles
                        <button id='trusted-button'>Add to Trusted People</button>
                        <button id='trusted-button'>Update Trusted Profiles</button>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default Dashboard;