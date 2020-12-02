var fs = require('fs');
const { listenerCount } = require('process');
let dataset = fs.readFileSync('day02_input.txt').toString().split("\n");

function range(s) {
    return s.split("-").map(x => parseInt(x))
}

dataset = dataset.map(x => x.split(' '))
dataset = dataset.map(x => [range(x[0]), x[1][0], x[2]])

// first item is number range
// second item is letter
// third item is password

// qn 1
function one(arr) {
    function char_count(s, char) {
        let count = 0
        for (let i = 0; i < s.length; i = i + 1) {
            if (char === s[i]) {
                count = count + 1
            }
            else { }
        }
        return count
    }

    let count = 0
    for (let i = 0; i < arr.length; i = i + 1) {
        let elem = arr[i]
        var left = elem[0][0]
        var right = elem[0][1]
        var letter = elem[1]
        var pwd = elem[2]
        var num = char_count(pwd, letter)

        if (num < left || num > right) { }
        else {
            count = count + 1
        }
    }
    return count
}

// qn 2
function two(arr) {
    let count = 0
    for (let i = 0; i < arr.length; i = i + 1) {
        let elem = arr[i]
        var left = elem[0][0] - 1
        var right = elem[0][1] - 1
        var letter = elem[1]
        var pwd = elem[2]
        
        if (pwd[left] === letter && pwd[right] === letter) {

        }
        else if (pwd[left] !== letter && pwd[right] !== letter) {

        }
        else {
            count = count + 1
        }
    }
    return count
}

console.log(one(dataset))
console.log(two(dataset))