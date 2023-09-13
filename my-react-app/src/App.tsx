import Login from "./Login";
import React from "react";
import Page from "./Page";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Signup from "./Signup";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useCheckLoginStatusQuery } from "./store/mainAPI";

function App() {
  const { data: user, isLoading } = useCheckLoginStatusQuery();

  // if (isLoading) {
  //   console.log("isLoading");
  // }

  // if (user) {
  //   console.log("user", user);
  // }

  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Page content={<HeroSection />} />} />
          <Route path="/login" element={<Page content={<Login />} />} />
          <Route path="/signup" element={<Page content={<Signup />} />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
