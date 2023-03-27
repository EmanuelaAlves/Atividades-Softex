const Banco = {
    conta: "000000-0",
    saldo: 0000,
    tipoConta: "Corrente",
    agencia: "0000-0",
  
    buscarSaldo: function() {
      return this.saldo;
    },
  
    deposito: function(valor) {
      this.saldo += valor;
    },
  
    saque: function(valor) {
      if (valor > this.saldo) {
        console.log("Saldo insuficiente.");
        return;
      }
      this.saldo -= valor;
    },
  
    numeroConta: function() {
      return this.conta;
    }
  };

  
 
  
