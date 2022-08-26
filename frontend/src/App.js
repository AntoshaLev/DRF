import React from 'react'
import axios from 'axios'
import './App.css';
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import ToDoList from './components/ToDoList.js'
import MenuList from "./components/MenuList.js"
import LoginForm from "./components/LoginForm"
import UserProjectList from "./components/UserProjectList"
import Footer from "./components/footer.js"
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useParams, useLocation} from 'react-router-dom'

const NotFound = () => {
    var {pathname} = useLocation()
    return (
        <div>
            Page {pathname} not found
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }



    getData() {
        let headers = this.getHeader()
        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'users': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'projects': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/todos/', {headers})
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'todos': []
                })
            })
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeader() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getToken(login, password) {
    // console.log(login, password)
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
            .then(response => {
                const token = response.data.token
                // console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
        .catch(error => console.log(error))
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/todos'>Todos</Link></li>
                        <hr/>
                        <li>
                        {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/' element={<Navigate to={'/users'}/>}/>
                        <Route exact path='/users'>
                            <Route index element={<UserList users={this.state.users}/>}/>
                            <Route path=':userId' element={<UserProjectList projects={this.state.projects}/>}/>
                        </Route>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todos' element={<ToDoList todos={this.state.todos}/>}/>
                        <Route exact path='/login' element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route path="*" element={<NotFound />}/>
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;


