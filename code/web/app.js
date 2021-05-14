var express = require('express');
var app = express();

app.set('view engine', 'pug');
app.set('views', '/home/pi/Raspi_DashCam/code/web/views');

app.use(express.static('/home/pi/Raspi_DashCam/code/web/public'));
app.use(express.static('/home/pi/Raspi_DashCam/code/web/node_modules/bootstrap/dist'));
app.use(express.static('/home/pi/Raspi_DashCam/code/web/node_modules/popper.js/dist'));
app.use(express.static('/home/pi/Raspi_DashCam/code/web/node_modules/jquery/dist'));

var db = require('/home/pi/Raspi_DashCam/code/web/db');

app.get('/', (req, res) => {
    const posts = db.getPosts();
    db.getConfig(function (err, content) {
        if(err) throw err;
        let config = JSON.parse(content);
        console.log(config);
        
        res.render('index', {
            posts: posts,
            config: config
        });
    });
});

app.get('/settings', (req, res) => {
    db.getConfig(function (err, content) {
        if(err) throw err;
        let config = JSON.parse(content);
        console.log(config);
        
        res.render('settings', {
            config: config
        });
    });
});

app.post('/settings/update', (req, res, next) => {
    console.log(req.body.deleteFiles)
    console.log(req.body.framerate)
    
});

app.get('/logs', (req, res) => {
    db.getLog(function (err, content) {
        if(err) throw err;    
        console.log(content);
        
        res.render('logs', {
            title: 'Dashcam Logs',
            logs: content
        });
    });
});

// app.get('/authors/:author_id', (req, res) => {
//     const author_id = req.params.author_id;
//     console.log(`pulling profile page for - `, req.params);
//     const author = db.getAuthors().find(a => a.id === author_id);
//     res.render('profile', {
//         author,
//         bodyClass: 'profile-page',
//     });
// });

app.listen(3000, () => {
    console.log('Chat App running on port 3000');
});