var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

chess = [1, 1, 2, 2, 2, 8]

for(i=0; i<6; i++){
    console.log(chess[i] - input[i])
}
