import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  currentUser: false,
};

export const userSlice = createSlice({
  name: "user",
  initialState: initialState,
  reducers: {
    authenticateUser: (state, action) => {
      const currentUser = action.payload;
      state.currentUser = currentUser;
    },
    unauthenticateUser: (state) => {
      state.currentUser = false;
    },
  },
});

export const { authenticateUser, unauthenticateUser } = userSlice.actions;
