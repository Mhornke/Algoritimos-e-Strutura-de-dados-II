let array =[]
let sizeArray = array.length
let soma = 0

for (let i=0; array.length < 5; i++){

fillingArray = (Math.floor(Math.random() * 10) + 1)
let valor =  array.includes(fillingArray)

if(valor == false || array.length <= 1){
array.push(fillingArray)
soma = soma + fillingArray
}

}
console.log(array[0])
console.log(array[4])
console.log(soma)

