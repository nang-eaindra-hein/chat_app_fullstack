
//signup
export type SignupPayload = {
  username: string;
  email: string;
  password: string;
  number:string
};

export type SignupResponse = {
  id: number;
  username: string;
  email: string;
  number:string
};
//profile
export type GetUserPayload = {
  id:number;
  username:string;
  email:string;
  number:string
 
}
//update
export type updateResponse = {
  email:string;
  username:string;
  number:string;
}

//login
export type LoginPayload = {
  login: string;
  password: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
};
