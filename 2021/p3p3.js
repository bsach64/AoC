const fs = require('fs');

function bit_criteria(data, index, oxygen=true) {
    ones = []
    zeros = []
    for (entry of data) {
        if (entry[index] === '1') {
            ones.push(entry);
        } else {
            zeros.push(entry);
        }
    }
    if (oxygen) {
        if (ones.length >= zeros.length) {
            return ones;
        } else {
            return zeros;
        }
    } else {
        if (zeros.length <= ones.length) {
            return zeros;
        } else {
            return ones;
        }
    }
}

fs.readFile('in3.txt', (err, file_data) => {
    if (err) throw err;
    data = file_data.toString();
    data = data.split('\n');
    let oxygen_generator = data;
    let CO2_scrubber = data;
    let index = 0;
    while(oxygen_generator.length > 1) {
        oxygen_generator = bit_criteria(oxygen_generator, index);
        index++;
    }
    index = 0;
    while(CO2_scrubber.length > 1) {
        CO2_scrubber = bit_criteria(CO2_scrubber, index, oxygen=false);
        index++;
    }
    console.log(parseInt(oxygen_generator[0], 2)*parseInt(CO2_scrubber[0], 2));
})