import axios from "axios";
import type { SignupPayload,SignupResponse,LoginPayload,LoginResponse,GetUserPayload,updateResponse } from "./type";


export const api = axios.create({
  baseURL: "http://127.0.0.1:5001",
  headers: {
    "Content-Type": "application/json",
  },
});

//profile

export async function getUser(): Promise<GetUserPayload> {
  const token = localStorage.getItem("token");

  const res = await api.get("/profile", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.data;
}
//get users
export async function getUsers():Promise<GetUserPayload>{
  
  const res = await api.get('/getUsers')
  return res.data
}

//post sign up
export async function signupUser(data: SignupPayload): Promise<SignupResponse> {
  const res = await api.post("/signup", data);
  return res.data;
}

//login
export async function loginUser(data: LoginPayload): Promise<LoginResponse> {
  const res = await api.post("/login", data);
  return res.data;
}
//update 
export const updateChangesPatch = async (data: Partial<updateResponse> ) => {
  const response = await api.patch(`/update/${data.username}`,data);
  return response.data;
};
