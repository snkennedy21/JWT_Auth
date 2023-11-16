import React, { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useCheckLoginStatusQuery } from "./store/mainApi";
import { authenticateUser } from "./store/userSlice";

import Login from "./Login";
import Page from "./Page";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Signup from "./Signup";
import UnprotectedEndpoint from "./UnprotectedEndpoint";
import PartiallyProtectedEndpoint from "./PartiallyProtectedEndpoint";
import ProtectedEndpoint from "./ProtectedEndpoint";

function App() {
  const dispatch = useDispatch();
  const {
    data: userLoggedIn,
    isLoading: userLoginStatusLoading,
    error: userLoggedInError,
    refetch: refetchUserLoginStatus,
  } = useCheckLoginStatusQuery();

  useEffect(() => {
    if (userLoggedIn) {
      dispatch(authenticateUser(userLoggedIn));
    }
    if (userLoggedInError?.data?.detail === "Expired Token") {
      refetchUserLoginStatus();
    }
  }, [userLoggedIn, dispatch, userLoggedInError]);

  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Page content={<HeroSection />} />} />
          <Route path="/login" element={<Page content={<Login />} />} />
          <Route path="/signup" element={<Page content={<Signup />} />} />
          <Route
            path="/unprotected"
            element={<Page content={<UnprotectedEndpoint />} />}
          />
          <Route
            path="/partially-protected"
            element={<Page content={<PartiallyProtectedEndpoint />} />}
          />
          <Route
            path="/protected"
            element={<Page content={<ProtectedEndpoint />} />}
          />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
