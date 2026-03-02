import api from "./api";

/**
 * Login API
 * No token required
 */
export const loginApi = (data) => {
  return api.post("/users/login", data);
};

/**
 * Register API
 * No token required
 */
export const registerApi = (data) => {
  return api.post("/users/register", data);
};