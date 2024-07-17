import { useState } from "react";
import "./adicionarCliente.css";
import axios from "axios";

export const AdicionarCliente = () => {
  const [cliente, setCliente] = useState({
    nome: "",
    telefone: "",
    rua: "",
    bairro: "",
    numero: "",
  });
  const handleInput = (e) => {
    setCliente({ ...cliente, [e.target.name]: e.target.value });
  };
  const handleSubit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:8080/api/cliente", cliente)
      .then((response) => {
        if (response.status === 200) {
          alert("Cliente adicionado com sucesso");
          setCliente({
            nome: "",
            telefone: "",
            rua: "",
            bairro: "",
            numero: "",
          });
        }
      });
  };
  return (
    <div className="addCliente">
      <h1>Adicionar Cliente</h1>
      <form onSubmit={handleSubit} className="form">
        <label htmlFor="nome">Nome</label>
        <input
          type="text"
          onChange={handleInput}
          name="nome"
          id="nome"
          required
        />
        <label htmlFor="telefone">Telefone</label>
        <input
          type="text"
          onChange={handleInput}
          name="telefone"
          id="telefone"
          required
        />
        <label htmlFor="rua">Rua</label>
        <input
          type="text"
          onChange={handleInput}
          name="rua"
          id="rua"
          required
        />
        <label htmlFor="bairro">Bairro</label>
        <input
          type="text"
          onChange={handleInput}
          name="bairro"
          id="bairro"
          required
        />
        <label htmlFor="numero">Numero</label>
        <input
          type="text"
          onChange={handleInput}
          name="numero"
          id="numero"
          required
        />
        <button className="btn-add" type="submit">
          Adicionar
        </button>
      </form>
    </div>
  );
};
