const fs = require('fs');

function readLogs(callback) {
    fs.readFile('db/log.log', (err, data) => {
        callback(err, data);
    });
}
console.log('This is after the read call');

module.exports = { 
    readLogs
}