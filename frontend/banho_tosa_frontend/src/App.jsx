import "./App.css";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Cliente from "./components/cliente/cliente";
import Pet from "./components/pet/pet";
import Venda from "./components/venda/venda";
import { AdicionarCliente } from "./components/cliente/adicionarCliente";
import { AdicionarPet } from "./components/pet/adicionarPet";
import { AdicionarVenda } from "./components/venda/adicionarVenda";

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
        <Route path="/cliente/adicionar" element={<AdicionarCliente />} />
        <Route path="/pet/adicionar" element={<AdicionarPet />} />
        <Route path="/venda/adicionar" element={<AdicionarVenda />} />
      </Routes>
    </Router>
  );
}

export default App;
