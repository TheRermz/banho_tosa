import "./venda.css";
import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const Cliente = () => {
  const [venda, setVenda] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/venda");
    setVenda(response.data);
  };

  const formatDate = (dateInSeconds) => {
    const formattedDate = new Date(dateInSeconds);
    const day = (formattedDate.getDate() + 1).toString().padStart(2, "0");
    const month = (formattedDate.getMonth() + 1).toString().padStart(2, "0");
    const year = formattedDate.getFullYear().toString();

    return `${day}/${month}/${year}`;
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <div className="venda">
      <Link to="/venda/adicionar">Adicionar venda</Link>
      <h1>VENDA</h1>
      <table>
        <thead>
          <tr>
            <th>Tipo da venda</th>
            <th>Data da venda</th>
            <th>Nome do cliente</th>
            <th>Nome do pet</th>
          </tr>
        </thead>
        <tbody>
          {venda.map((venda) => (
            <tr key={venda.ID_VENDA}>
              <td>{venda.TIPO_VENDA}</td>
              <td>{formatDate(venda.DATA_VENDA)}</td>
              <td>{venda.NOME_CLIENTE}</td>
              <td>{venda.NOME_PET}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Cliente;
