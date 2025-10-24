// src/App.jsx
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import GuestsList from "./app/GuestsList";
import Layout from "./app/Layout";
import LandingPage from "./pages/LandingPage";

export default function App() {
  return (
    <Router>
      <Routes>
        {/* Página de inicio */}
        <Route path="/" element={<LandingPage />} />

        {/* Rutas del Dashboard */}
        <Route path="/app" element={<Layout />}>
          <Route index element={<GuestsList />} />
          {/* <Route path="guest/:id" element={<GuestDetail />} /> */}
        </Route>
      </Routes>
    </Router>
  );
}
