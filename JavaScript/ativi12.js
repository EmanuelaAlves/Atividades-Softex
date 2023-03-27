const sql = require('mssql');

const config = {
  user: '<username>',
  password: '<password>',
  server: '<servername>',
  database: '<database>'
};

sql.connect(config, (err) => {
  if (err) {
    console.log('Erro ao conectar com o banco de dados: ', err);
  } else {
    console.log('Conexão com o banco de dados estabelecida com sucesso!');
    // Aqui você pode executar as operações desejadas no banco de dados
  }
});

sql.on('error', (err) => {
  console.log('Erro no driver do SQL Server: ', err);
});





