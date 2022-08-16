const UserItem = ({User}) => {
    return(
        <tr>
            <td>
                {User.user_name}
            </td>
            <td>
                {User.first_name}
            </td>
            <td>
                {User.last_name}
            </td>
            <td>
                {User.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                User name
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Email
            </th>
            {users.map((User) => <UserItem User={User} />)}
        </table>
    )
}

export default UserList;