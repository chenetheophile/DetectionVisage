const express = require('express');
const app = express();
const path = require("path");
const bodyParser = require('body-parser');
const { exec } = require('child_process')

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, '/dist/projet-esme')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, "/dist/projet-esme/index.html"));
  console.log('test')
});
app.get('/SeConnecter', function (req, res) {
  exec('python ./authentification.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
  res.sendFile(path.join(__dirname, "/dist/projet-esme/index.html"));
});

app.get('/Notreprojet', function (req, res) {
  res.sendFile(path.join(__dirname, "/dist/projet-esme/index.html"));
});
app.listen(4200)