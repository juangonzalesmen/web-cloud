import React, { Component } from 'react';  // nuevo
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';


// nuevo
class App extends Component {
  // new
  constructor() {
    super();
    // nuevo
    this.state = {
      users: []
    };
  };
  // new
  componentDidMount() {
    this.getUsers();
  };
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)  // nuevo
    .then((res) => { this.setState({ users: res.data.data.users }); })
    .catch((err) => { console.log(err); });
  };
  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-half">  {/* new */}
              <br/>
              <h1 className="title is-1">All Users</h1>
              <hr/><br/>
              <AddUser/>  {/* nuevo */}
              <br/><br/>  {/* nuevo */}
              <UsersList users={this.state.users}/>
            </div>
          </div>
        </div>
      </section>
    )
  }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);




// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//  <React.StrictMode>
//    <App />
//  </React.StrictMode>,
//  document.getElementById('root')
//);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
