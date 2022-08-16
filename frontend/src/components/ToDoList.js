const TodoItem = ({todo}) => {
    return (
        <tr>
        <td>
            {todo.todo_text}
        </td>
        <td>
            {todo.is_active}
        </td>
        <td>
            {todo.todo_project}
        </td>
        <td>
            {todo.users}
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
        {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}

export default TodoList