import "./adicionarCliente.css";

export const AdicionarCliente = () => {
  return (
    <div className="addCliente">
      <h1>Adicionar Cliente</h1>
      <form action="" method="post" className="form">
        <label htmlFor="nome">Nome</label>
        <input type="text" name="nome" id="nome" required />
        <label htmlFor="telefone">Telefone</label>
        <input type="text" name="telefone" id="telefone" required />
        <label htmlFor="rua">Rua</label>
        <input type="text" name="rua" id="rua" required />
        <label htmlFor="bairro">Bairro</label>
        <input type="text" name="bairro" id="bairro" required />
        <label htmlFor="numero">Numero</label>
        <input type="text" name="numero" id="numero" required />
        <button className="btn-add" type="submit">
          Adicionar
        </button>
      </form>
    </div>
  );
};
