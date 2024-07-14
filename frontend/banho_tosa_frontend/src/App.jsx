import "./App.css";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Cliente from "./components/cliente/cliente";
import Pet from "./components/pet/pet";
import Venda from "./components/venda/venda";

function App() {
  return (
    <Router>
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/cliente">Clientes</Link>
        <Link to="/pet">Pets</Link>
        <Link to="/venda">Vendas</Link>
      </div>
      <Routes>
        <Route path="/" element={<h1>Home</h1>} />
        <Route path="/cliente" element={<Cliente />} />
        <Route path="/pet" element={<Pet />} />
        <Route path="/venda" element={<Venda />} />
      </Routes>
    </Router>
  );
}

export default App;
