import React from 'react'
import axios from 'axios'
import './App.css';
import UserList from './components/UserList.js'
import MenuList from "./components/MenuList.js";
import Footer from "./components/footer.js";


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': []
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
    }

    render() {
    return (
      <div>
        <MenuList />

        <UserList users={this.state.users}/>

        <Footer />
     </div>
    );
  }
}

export default App;


