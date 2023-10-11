const fs = require('fs');

var horizontal = 0;
var vertical = 0;
var aim = 0;

function update_move(input) {
    input = input.split(' ');
    if (input[0] == 'forward') {
        horizontal += parseInt(input[1]);
        vertical += (parseInt(input[1]) * aim);
    } else if (input[0] == 'down') {
        aim += parseInt(input[1]);
    } else {
        aim -= parseInt(input[1]);
    }
}

fs.readFile('in2.txt', (err, file_data) => {
    if (err) throw err;
    data = file_data.toString();
    data = data.split('\n');
    for (entry of data) {
        update_move(entry);
    }
    console.log(horizontal, vertical, horizontal*vertical);
})
