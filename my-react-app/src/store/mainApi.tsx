import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const mainApi = createApi({
  reducerPath: "mainApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8000",
  }),

  endpoints: (builder) => ({
    login: builder.mutation({
      query: (credentials) => ({
        url: "/login",
        method: "POST",
        credentials: "include",
        body: credentials,
      }),
    }),

    signup: builder.mutation({
      query: (credentials) => ({
        url: "/user",
        method: "POST",
        credentials: "include",
        body: credentials,
      }),
    }),

    checkLoginStatus: builder.query({
      query: () => ({
        url: "/check",
        method: "GET",
        credentials: "include",
      }),
    }),
  }),
});

export const { useLoginMutation, useSignupMutation, useCheckLoginStatusQuery } =
  mainApi;
