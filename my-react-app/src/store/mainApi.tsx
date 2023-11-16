import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const mainApi = createApi({
  reducerPath: "mainApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8000",
  }),

  tagTypes: ["User"],

  endpoints: (builder) => ({
    login: builder.mutation({
      query: (credentials) => ({
        url: "/login",
        method: "POST",
        credentials: "include",
        body: credentials,
      }),
      invalidatesTags: ["User"],
    }),

    logout: builder.mutation({
      query: () => ({
        url: "/logout",
        method: "DELETE",
        credentials: "include",
      }),
      invalidatesTags: ["User"],
    }),

    refresh: builder.mutation({
      query: () => ({
        url: "/refresh",
        method: "GET",
        credentials: "include",
      }),
    }),

    signup: builder.mutation({
      query: (credentials) => ({
        url: "/user",
        method: "POST",
        credentials: "include",
        body: credentials,
      }),
      invalidatesTags: ["User"],
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
      providesTags: ["User"],
    }),

    protectedEndpoint: builder.query({
      query: () => ({
        url: "/protected",
        method: "GET",
        credentials: "include",
      }),
      providesTags: ["User"],
    }),
  }),
});

export const {
  useLoginMutation,
  useLogoutMutation,
  useSignupMutation,
  useCheckLoginStatusQuery,
  useUnprotectedEndpointQuery,
  usePartiallyProtectedEndpointQuery,
  useProtectedEndpointQuery,
} = mainApi;
