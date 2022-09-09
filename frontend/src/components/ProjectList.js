import {Link} from "react-router-dom";

const ProjectItem = ({project, users, deleteProject}) => {
    return(
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.repo}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                <button onClick={() => deleteProject(project.id) }>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users, deleteProject}) => {
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
            {projects.map((project) => <ProjectItem project={project} deleteProject={'deleteProject'} />)}
        </table>
    )
}

export default ProjectList;