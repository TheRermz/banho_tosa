import { useState } from "react";
import "./adicionarPet.css";
import axios from "axios";

export const AdicionarPet = () => {
  const [pet, setPet] = useState({
    nome_pet: "",
    raca: "",
    nome_cliente: "",
  });
  const handleInput = (e) => {
    setPet({ ...pet, [e.target.name]: e.target.value });
  };
  const handleSubit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:8080/api/pet", pet).then((response) => {
      if (response.status === 200) {
        alert("Pet adicionado com sucesso");
        setPet({
          nome_pet: "",
          raca: "",
          nome_cliente: "",
        });
      }
    });
  };
  return (
    <div className="addPet">
      <h1>Adicionar Pet</h1>
      <form onSubmit={handleSubit} className="form">
        <label htmlFor="nome_pet">Nome do pet</label>
        <input
          type="text"
          onChange={handleInput}
          name="nome_pet"
          id="nome_pet"
          required
        />
        <label htmlFor="raca">Raça do pet</label>
        <input
          type="text"
          onChange={handleInput}
          name="raca"
          id="raca"
          required
        />
        <label htmlFor="nome_cliente">Nome do cliente</label>
        <input
          type="text"
          onChange={handleInput}
          name="nome_cliente"
          id="nome_cliente"
          required
        />
        <button className="btn-add" type="submit">
          Adicionar pet
        </button>
      </form>
    </div>
  );
};
