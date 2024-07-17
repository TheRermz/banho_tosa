import "./pet.css";
import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const Cliente = () => {
  const [pet, setPet] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/pet");
    setPet(response.data);
  };

  const formatTelefone = (telefone) => {
    const cleaned = ("" + telefone).replace(/\D/g, "");
    const match = cleaned.match(/^(\d{2})(\d{5})(\d{4})$/);
    if (match) {
      return "(" + match[1] + ")" + match[2] + "-" + match[3];
    }
    return telefone;
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <div className="pet">
      <Link to="/pet/adicionar">Adicionar Pet</Link>
      <h1>PET</h1>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Telefone</th>
            <th>Nome do Pet</th>
            <th>Raça do Pet</th>
          </tr>
        </thead>
        <tbody>
          {pet.map((pet) => (
            <tr key={pet.ID_PET}>
              <td>{pet.NOME_CLIENTE}</td>
              <td>{formatTelefone(pet.TELEFONE_CLIENTE)}</td>
              <td>{pet.NOME_PET}</td>
              <td>{pet.RACA_PET}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Cliente;
