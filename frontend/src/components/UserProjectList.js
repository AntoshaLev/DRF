import {Link, useParams} from "react-router-dom"

const UserProjectItem = ({Project}) => {
    return (
        <tr>
            <td>
                {Project.name}
            </td>
            <td>
                {Project.repo}
            </td>
            <td>
                {Project.users}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {
    var {id} = useParams()
    var filteredProjects = projects.filter((projects) => projects.users.includes(parseInt(id)))

    return (
        <table>
        <th>
            Title
        </th>
        <th>
            Link to repo
        </th>
        <th>
            Users
        </th>
        {filteredProjects.map((project) => <UserProjectItem project={project}/>)}
        </table>
    )
}

export default UserProjectList