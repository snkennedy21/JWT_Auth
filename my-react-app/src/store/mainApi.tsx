import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const mainApi = createApi({
  reducerPath: "mainApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://react-fastapi-website.com",
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

    unprotectedEndpoint: builder.query({
      query: () => ({
        url: "/unprotected",
        method: "GET",
        credentials: "include",
      }),
    }),

    partiallyProtectedEndpoint: builder.query({
      query: () => ({
        url: "/partially-protected",
        method: "GET",
        credentials: "include",
      }),
    }),

    protectedEndpoint: builder.query({
      query: () => ({
        url: "/protected",
        method: "GET",
        credentials: "include",
      }),
    }),
  }),
});

export const {
  useLoginMutation,
  useSignupMutation,
  useCheckLoginStatusQuery,
  useUnprotectedEndpointQuery,
  usePartiallyProtectedEndpointQuery,
  useProtectedEndpointQuery,
} = mainApi;
