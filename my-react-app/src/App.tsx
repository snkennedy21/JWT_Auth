import Login from "./Login";
import React from "react";
import Page from "./Page";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Page content={<HeroSection />} />} />
          <Route path="/login" element={<Page content={<Login />} />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
