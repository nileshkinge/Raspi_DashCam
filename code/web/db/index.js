var posts = require('./posts')
var authors = require('./authors')
var configService = require('./configService')
var logService = require('./logService')
var converter = require('./converter')

var db = {};

// console.log(posts);
// console.log(authors);

db.getPosts = function () {
    return posts;
};

db.getPost = function (id) {
    return posts.filter(p => p.id === id);
};

db.getAuthors = function(){
    return authors;
};

db.getConfig = function(callback){
    return configService.readConfig(callback);
};

db.getLog = function(callback){
    return logService.readLogs(callback);
};
db.convert = function(callback){
    return converter.convertH264ToMp4();
};

module.exports = db;