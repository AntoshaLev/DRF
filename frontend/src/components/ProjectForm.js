import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '',
            'users': [],
            'todos': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            return;
        }

        let users = []
        for(let i = 0; i < event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            ['users']: users
        })
    }


    handleSubmit(event) {
        console.log(this.state.name, this.state.users)
        this.props.createProject(this.state.name, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="name" placeholder="name" value={this.state.name} onChange = {(event) => this.handleChange(event)} />
                <select multiple name="users" onChange = {(event) => this.handleAuthorsChange(event)}>
                    {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name} </option>)}
                </select>
                <input type="submit" value="Create" />
            </form>
        )
    }
}

export default ProjectForm