let fs = require('fs')
const { type } = require('os')

let filename = "day01_input.txt"
let content = fs.readFileSync(process.cwd() + "/" + filename).toString().split("\n")
var len = content.length

function arith_3(a, b, c, op) {
    return op === '+' 
                ? parseInt(a) + parseInt(b) + parseInt(c)
                : op === '-'
                ? parseInt(a) - parseInt(b) - parseInt(c)
                : op === '*'
                ? parseInt(a) * parseInt(b) * parseInt(c)
                : parseInt(a) / parseInt(b) / parseInt(c)
}

function arith_2(a, b, op) {
    return op === '+' 
                ? parseInt(a) + parseInt(b)
                : op === '-'
                ? parseInt(a) - parseInt(b)
                : op === '*'
                ? parseInt(a) * parseInt(b)
                : parseInt(a) / parseInt(b)
}


for (let i = 0; i < len; i = i + 1) {
    for (let j = i; j < len; j = j + 1) {
        if (arith_2(content[i], content[j], '+') === 2020) {
            console.log(arith_2(content[i], content[j], '*'))
        }
        else { }
    }
}

for (let i = 0; i < len; i = i + 1) {
    for (let j = i; j < len; j = j + 1) {
        for (let k = j; k < len; k = k + 1) {
            if (arith_3(content[i], content[j], content[k], '+') === 2020) {
                console.log(arith_3(content[i], content[j], content[k], '*'))
            }
            else { }
        } 
    }
}