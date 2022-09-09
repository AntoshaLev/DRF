import React from 'react'
import axios from 'axios'
import './App.css';
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import ToDoList from './components/ToDoList.js'
import LoginForm from "./components/LoginForm"
import UserProjectList from "./components/UserProjectList"
import ProjectForm from './components/ProjectForm.js';
import TODOForm from './components/TODOForm.js';
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
            'token': '',
            'redirect': false
        }
    }

 createTODO(project, text, user) {

            let headers = this.getHeaders()

            axios
                .post(`http://127.0.0.1:8000/api/projects/`, {'project': project, 'text': text, 'user': user} , {headers})
                .then(response => {
                    this.loadData();
                })
                .catch(error => {
                    console.log(error)
                })
        }

    deleteTODO(todoId) {

        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/todos/${todoId}/`, {headers})
            .then(response => {
                this.setState( {
                    'todos': this.state.todos.filter((todo) => todo.todoId != todoId)
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    createProject(name, users) {

            let headers = this.getHeaders()

            axios
                .post(`http://127.0.0.1:8000/api/projects/`, {'name': name, 'users': users} , {headers})
                .then(response => {
                    this.getData();
                })
                .catch(error => {
                    console.log(error)
                })
        }

    deleteProject(projectId) {

        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/projects/${projectId}/`, {headers})
            .then(response => {
                this.setState( {
                    'projects': this.state.projects.filter((project) => project.projectId != projectId)
                })
        })
        .catch(error => {
            console.log(error)
        })
    }

    getData() {
         this.setState({
            'redirect': false
        })

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
                    {this.state.redirect ? <Navigate to={this.state.redirect} /> : <div/>}
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/todos'>Todos</Link></li>
                        <li> <Link to='/create_project'>Create project</Link> </li>
                        <li> <Link to='/create_todo'>Create todo</Link> </li>
                        <li>
                        {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} users={this.state.users} deleteProject={(projectId) => this.deleteProject(projectId)} />} />
                        <Route exact path='/create_book' element={<ProjectForm users={this.state.users} createProject={(name, users) => this.createProject(name, users)} />} />
                        <Route exact path='/todos' element={<ToDoList todos={this.state.todos} user={this.state.user} deleteTODO={(todoId) => this.deleteTODO(todoId)} />} />
                        <Route exact path='/create_todo' element={<TODOForm user={this.state.user} createTODO={(project, text, user) => this.createTODO(project, text, user)} />} />
                        <Route exact path='/' element={<Navigate to={'/users'}/>}/>
                        <Route exact path='/users'>
                            <Route index element={<UserList users={this.state.users}/>}/>
                            <Route path=':userId' element={<UserProjectList projects={this.state.projects}/>}/>
                        </Route>
                        <Route exact path='/login' element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route path="*" element={<NotFound />}/>
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;


