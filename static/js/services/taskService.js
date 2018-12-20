import axios from 'axios';

const apiURL = "http://localhost:8000/api/tasks/";

export const getTasks = () => {
    return axios.get(apiURL)
        .then(res => {
            const tasks = res.data;
            return tasks;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const createTask = (task) => {
    return axios.post(apiURL + 'create/', task )
        .then(res => {
            console.log(res);
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const editTask = (task) => {
    return axios.put(apiURL + 'edit/' + task.id, task )
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const deleteTask = (id) => {
    return axios.delete(apiURL + 'delete/' + id)
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        })
}