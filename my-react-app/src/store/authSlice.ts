import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  userAuthenticated: false,
};

export const authSlice = createSlice({
  name: "auth",
  initialState: initialState,
  reducers: {
    authenticateUser: (state) => {
      state.userAuthenticated = true;
    },
    unauthenticateUser: (state) => {
      state.userAuthenticated = false;
    },
  },
});

export const { authenticateUser, unauthenticateUser } = authSlice.actions;
