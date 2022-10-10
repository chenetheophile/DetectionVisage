const express = require('express');
const app = express();
const path = require("path");
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, '/dist/projet-esme')));

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, "/dist/projet-esme/index.html"));
    console.log('test')
});

app.listen(4200)