import Login from "./Login";
import Page from "./Page";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Signup from "./Signup";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useCheckLoginStatusQuery } from "./store/mainAPI";
import { authenticateUser } from "./store/userSlice";
import { useDispatch } from "react-redux";
import { useEffect } from "react";

function App() {
  const dispatch = useDispatch();
  const { data: user } = useCheckLoginStatusQuery();

  useEffect(() => {
    if (user) {
      dispatch(authenticateUser(user));
    }
  }, [user, dispatch]);

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