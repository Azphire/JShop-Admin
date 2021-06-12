import axios from "axios";

let base = "";

let baseURL = "http://127.0.0.1:5000";

export const requestLogin = (params) => {
  return axios
    .get(`${baseURL}/login`, { params: params })
    .then((res) => res.data);
};

export const getUserList = (params) => {
  return axios.get(`${baseURL}/user/list`, { params: params });
};

export const getUserFilter = (params) => {
  return axios.get(`${baseURL}/user/filter`, { params: params });
};

export const getUserListPage = (params) => {
  return axios.get(`${base}/user/listpage`, { params: params });
};

export const removeUser = (params) => {
  return axios.get(`${baseURL}/user/remove`, { params: params });
};

export const batchRemoveUser = (params) => {
  return axios.get(`${base}/user/batchremove`, { params: params });
};

export const editUser = (params) => {
  return axios.get(`${baseURL}/user/edit`, { params: params });
};

export const addUser = (params) => {
  return axios.get(`${base}/user/add`, { params: params });
};

export const getGoodList = (params) => {
  return axios.get(`${baseURL}/goods/list`, { params: params });
};

export const getGoodFilter = (params) => {
  return axios.get(`${baseURL}/goods/filter`, { params: params });
};

export const getQiugouList = (params) => {
  return axios.get(`${baseURL}/qiugou/list`, { params: params });
};

export const getQiugouFilter = (params) => {
  return axios.get(`${baseURL}/qiugou/filter`, { params: params });
};

export const getAskList = (params) => {
  return axios.get(`${baseURL}/question/list`, { params: params });
};

export const getAskFilter = (params) => {
  return axios.get(`${baseURL}/question/filter`, { params: params });
};

export const getRecommendList = (params) => {
  return axios.get(`${baseURL}/recommend/list`, { params: params });
};

export const getRecommendFilter = (params) => {
  return axios.get(`${baseURL}/recommend/filter`, { params: params });
};

export const removeGood = (params) => {
  return axios.get(`${baseURL}/good/remove`, { params: params });
};

export const removeQiugou = (params) => {
  return axios.get(`${baseURL}/qiugou/remove`, { params: params });
};

export const removeQuestion = (params) => {
  return axios.get(`${baseURL}/question/remove`, { params: params });
};

export const removeRecommend = (params) => {
  return axios.get(`${baseURL}/recommend/remove`, { params: params });
};
