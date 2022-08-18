import React from 'react'
import axios from 'axios'
import './App.css';
import UserList from './components/UserList.js'
import ProjectList from './components/ProjectList.js'
import ToDoList from './components/ToDoList.js'
import MenuList from "./components/MenuList.js"
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
        }
    }



    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/todos'>Todos</Link></li>
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
                        <Route path="*" element={<NotFound />}/>
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;


