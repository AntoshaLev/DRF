import {Link} from "react-router-dom";

const ProjectItem = ({Project}) => {
    return(
        <tr>
            <td>
                <Link to={`/projects/${Project.id}`}>{Project.name}</Link>
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

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                Repo
            </th>
            <th>
                Users
            </th>
            {projects.map((Project) => <ProjectItem Project={Project} />)}
        </table>
    )
}

export default ProjectList;