function sub(nota1, nota2){
    return  26 - +nota1 - +nota2
}
const resultado = sub(9,9)
console.log ("Sua terceira nota precisa ser no mínimo:", resultado)

function calculator(nota1, nota2, nota3){
    var nota1 = parseFloat(document.getElementById("nota1").value);
    var nota2 = parseFloat(document.getElementById("nota2").value);
    var nota3 = parseFloat(document.getElementById("nota3").value);
    var media = +nota1 + +nota2 + +nota3/ 3;
    var media = (media >= 7) ? "aprovado" : "reprovado";}

    





