const fs = require('fs')

fs.readFile('in1.txt', (err, file_data) => {
    if (err) throw err;
    data = file_data.toString();
    data = data.split('\n');
    var increase_count = 0;
    for (i in data) {
        data[i] = parseInt(data[i]);
    }
    for (let i = 2; i < data.length - 1; i++) {
        first_window = data[i - 2] + data[i - 1] + data[i];
        second_window = data[i - 1] + data[i] + data[i + 1];
        console.log(first_window, second_window);
        if (first_window < second_window) {
            increase_count++;
        }
    }
    console.log(increase_count);
})

