import "./cliente.css";
import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const Cliente = () => {
  const [clientes, setClientes] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/cliente");
    setClientes(response.data);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  const formatTelefone = (telefone) => {
    const cleaned = ("" + telefone).replace(/\D/g, "");
    const match = cleaned.match(/^(\d{2})(\d{5})(\d{4})$/);
    if (match) {
      return "(" + match[1] + ")" + match[2] + "-" + match[3];
    }
    return telefone;
  };

  return (
    <div className="cliente">
      <Link to="/cliente/adicionar">Adicionar cliente</Link>
      <h1>Lista de Clientes</h1>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Telefone</th>
            <th>Rua</th>
            <th>Bairro</th>
            <th>Numero</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map((cliente) => (
            <tr key={cliente.ID_CLIENTE}>
              <td>{cliente.NOME_CLIENTE}</td>
              <td>{formatTelefone(cliente.TELEFONE_CLIENTE)}</td>
              <td>{cliente.RUA}</td>
              <td>{cliente.BAIRRO}</td>
              <td>{cliente.NUMERO}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Cliente;
