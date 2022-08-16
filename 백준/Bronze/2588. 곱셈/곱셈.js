var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = parseInt(input[0])
const B = input[1]

for(i=0; i<3; i++){
    console.log(A * parseInt(B[2-i]))
}
console.log(A * parseInt(B))
