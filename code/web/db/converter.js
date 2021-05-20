
/*
  somewhat sloppy modification of another script
  did the trick on OSX to convert videos captured on a RPI
  https://gist.github.com/manno-xx/58a122407aac4ef9f850deb0efc7e77d
*/
const fs = require('fs');
const execSync = require('child_process').execSync;

function ish264File(value) {
    return value.endsWith(".h264");
}

// var myArgs = process.argv.slice(2);
// var folder = myArgs[0];

function convertH264ToMp4(){
    const videoFolder = '/home/pi/Raspi_DashCam/code/videos/';
    const destFolder = '/home/pi/Raspi_DashCam/code/web/public/img/videos/';
    var files = fs.readdirSync(videoFolder);
    var h264Files = files.filter(ish264File).sort().reverse();
    var destFilename = 'img/videos/';
    
    if(h264Files.length > 1){
        var latestFile = h264Files[1]; 
        var baseName = latestFile.slice(0, -5);
        // var mp4Filename = destFolder + baseName + ".mp4";
        var mp4Filename = destFolder + "video.mp4";
	    var destFilename = destFilename + "video.mp4";
        var entryFilename = videoFolder + latestFile;

        
        var commandString = "ffmpeg -y -framerate 24 -i file:" + entryFilename + " -c copy " + mp4Filename;

        console.log(commandString);
        execSync(commandString);

        return  { fileName: baseName, filePath: destFilename};            
    }
    return  { fileName: '', filePath: destFilename};
}
//     console.log(h264Files.length);

//     h264Files.forEach(function(entry) {
//         var baseName = entry.slice(0, -5);
//         var mp4Filename = videoFolder + baseName + ".mp4";
//         var entryFilename = videoFolder + entry;

        
//         var commandString = "ffmpeg -framerate 24 -i file:" + entryFilename + " -c copy " + mp4Filename;

//         console.log(commandString);
//         execSync(commandString);


// });

module.exports = {
    convertH264ToMp4
}