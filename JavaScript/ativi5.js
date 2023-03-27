function som(valor1, valor2) {
    return +valor1 + +valor2
}
function sub(valor1, valor2) {
    return +valor1 - +valor2
}
function mult(valor1, valor2) {
    return +valor1 * +valor2
}
function div(valor1, valor2) {
    return +valor1 / +valor2
}

function calcular(valor1, valor2, operation) {
    if (operation === "+") return som(valor1, valor2)
    if (operation === "-") return sub(valor1, valor2)
    if (operation === "*") return mult(valor1, valor2)
    if (operation === "/") return div(valor1, valor2)
    return "Informe uma operação válida."
}

const result = calcular(7,3,"+")
console.log(result)