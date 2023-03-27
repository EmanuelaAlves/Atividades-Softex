// Função tradicional com a palavra reservada Function
function exibirMenu() {
    console.log("Selecione uma operação:");
    console.log("1. Soma");
    console.log("2. Subtração");
    console.log("3. Multiplicação");
    console.log("4. Divisão");
  }
  
  // Função tradicional com parâmetros e retorno
  function calcular(operacao, num1, num2) {
    let resultado;
  
    switch (operacao) {
      case 1:
        resultado = num1 + num2;
        break;
      case 2:
        resultado = num1 - num2;
        break;
      case 3:
        resultado = num1 * num2;
        break;
      case 4:
        resultado = num1 / num2;
        break;
      default:
        console.log("Operação inválida!");
        return;
    }
  
    console.log(`O resultado é: ${resultado}`);
    return resultado;
  }
  
  // Arrow function com parâmetros e retorno
  const calcularRaizQuadrada = (num) => Math.sqrt(num);
  
  exibirMenu();
  const operacao = parseInt(prompt("Digite o número da operação desejada:"));
  const num1 = parseFloat(prompt("Digite o primeiro número:"));
  const num2 = parseFloat(prompt("Digite o segundo número:"));
  
  calcular(operacao, num1, num2);
  
  if (operacao === 5) {
    console.log(`A raiz quadrada de ${num1} é: ${calcularRaizQuadrada(num1)}`);
  }