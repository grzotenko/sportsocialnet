import axios from 'axios'

export default {
    getData() {
        return axios.get(`${process.env.REACT_APP_API_BASE_URL}/api/test/`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': "*"
            }
        })
    },
}