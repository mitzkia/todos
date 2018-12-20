import axios from 'axios';

const apiURL = "http://localhost:8000/api/categories/";

export const getCategories = () => {
    return axios.get(apiURL)
        .then(res => {
            const categories = res.data;
            return categories;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const createCategory = (category) => {
    return axios.post(apiURL + 'create/', category )
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const editCategory = (category) => {
    return axios.put(apiUrl + 'edit/' + category.id,  category )
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}

export const deleteCategory = (id) => {
    return axios.delete(apiURL + 'delete/' + id)
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        })
}

export const getCategorysTasks = (id) => {
    return axios.get('http://localhost:8000/api/category_tasks/' + id)
        .then(res => {
            return res.data;
        })
        .catch(error => {
            return JSON.parse(error);
        });
}
