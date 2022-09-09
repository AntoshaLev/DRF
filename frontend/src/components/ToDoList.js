const TodoItem = ({ToDo}) => {
    return (
        <tr>
        <td>
            {ToDo.todo_text}
        </td>
        <td>
            {ToDo.is_active}
        </td>
        <td>
            {ToDo.todo_project}
        </td>
        <td>
            {ToDo.users}
        </td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
        <th>
            TodoText
        </th>
        <th>
            IsActive
        </th>
        <th>
            TodoProject
        </th>
        <th>
            Users
        </th>
        {todos.map((ToDo) => <TodoItem todo={ToDo}/>)}
        </table>
    )
}

export default TodoList