import axios from "axios";
import "./adicionarVenda.css";
import { useState } from "react";

export const AdicionarVenda = () => {
  const [venda, setVenda] = useState({
    tipo_venda: "",
    nome_cliente: "",
    nome_pet: "",
  });

  const handleInput = (e) => {
    setVenda({ ...venda, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:8080/api/venda", venda).then((response) => {
      if (response.status === 200) {
        alert("Venda adicionada com sucesso");
        setVenda({
          tipo_venda: "",
          nome_cliente: "",
          nome_pet: "",
        });
      }
    });
  };

  return (
    <div className="addVenda">
      <h1>Adicionar Venda</h1>
      <form onSubmit={handleSubmit} className="form">
        <label htmlFor="tipo_venda">Tipo da venda</label>
        <input
          type="text"
          onChange={handleInput}
          name="tipo_venda"
          id="tipo_venda"
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
        <label htmlFor="nome_pet">Nome do pet</label>
        <input
          type="text"
          onChange={handleInput}
          name="nome_pet"
          id="nome_pet"
          required
        />
        <button className="btn-add" type="submit">
          Adicionar venda
        </button>
      </form>
    </div>
  );
};
