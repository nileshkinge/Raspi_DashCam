const fs = require('fs');

function readConfig(callback) {
    fs.readFile('/home/pi/Raspi_DashCam/code/config.json', (err, data) => {
        callback(err, data);
    });
}
console.log('This is after the read call');

module.exports = { 
    readConfig
}