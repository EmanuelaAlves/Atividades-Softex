const pessoa = {
    nome: "Bruno",
    idade: 30,
    cidade: "São Paulo"
  };
  
  const frutas = ["banana", "maçã", "laranja"];
  
  function listarPropriedades(objeto) {
    for (let propriedade in objeto) {
      console.log(propriedade);
    }
  }
  
  function listarElementos(array) {
    for (let i = 0; i < array.length; i++) {
      console.log(array[i]);
    }
  }
  
  listarPropriedades(pessoa);
  listarElementos(frutas);