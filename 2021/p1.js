const fs = require('fs')

fs.readFile('s1.txt', (err, file_data) => {
    if (err) throw err;
    data = file_data.toString();
    data = data.split('\n');
    var increase_count = 0;
    for (let i = 1; i < data.length; i++) {
        if (data[i] > data[i - 1]) {
            increase_count++;
        }
    }
    console.log(increase_count);
})

