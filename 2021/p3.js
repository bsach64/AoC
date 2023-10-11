const fs = require('fs');

fs.readFile('in3.txt', (err, file_data) => {
    if (err) throw err;
    data = file_data.toString();
    data = data.split('\n');
    let gamma_rate = '';
    let epsilon_rate = '';
    let total_count = data.length;
    let one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    for (entry of data) {
        for (let i = 0; i < entry.length; i++) {
            if (entry[i] === '1') {
                one_count[i]++;
            }
        }
    }
    for (entry of one_count) {
        if (entry > (total_count - entry)) {
            gamma_rate += '1';
            epsilon_rate += '0';
        } else {
            gamma_rate += '0';
            epsilon_rate += '1';
        }
    }
    gamma_rate = parseInt(gamma_rate, 2);
    epsilon_rate = parseInt(epsilon_rate, 2);
    console.log(gamma_rate*epsilon_rate);    
})