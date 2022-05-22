import React from 'react'

const UsersItem = ({users}) => {
    return (
        <tr>
            <td>
                {users.username}
            </td>
            <td>
                {users.first_name}
            </td>
            <td>
                {users.last_name}
            </td>
            <td>
                {users.email}
            </td>
        </tr>
    )
}


const UsersList = ({users}) => {
    return (
        <table>
            <th>
                User Name
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                EMAIL
            </th>
            {users.map((users) => <UsersItem users={users} />)}
        </table>
    )
}

export default UsersList
