import Login from "./Login";
import Page from "./Page";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Signup from "./Signup";
import UnprotectedEndpoint from "./UnprotectedEndpoint";
import PartiallyProtectedEndpoint from "./PartiallyProtectedEndpoint";
import ProtectedEndpoint from "./ProtectedEndpoint";
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
