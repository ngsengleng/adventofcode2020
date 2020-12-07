var fs = require('fs')
const { listenerCount } = require('process')
let dataset = fs.readFileSync('day03_input.txt').toString().split("\n")
let width = dataset[0].length
let height = dataset.length

function count(a) {
    dx = a[0]
    dy = a[1]
    total = 0
    x = 0
    y = 0
    while (y < height) {
        if (dataset[y][x] == '#') {
            total = total + 1
        }
        else { }
        x = (x + dx) % width
        y = y + dy
    }
    return total
}

let numberlist = [[1,1], [3,1], [5,1], [7,1], [1,2]]
console.log(count([3,1]))
console.log(numberlist.map(x => count(x)).reduce((a,b) => a * b))
