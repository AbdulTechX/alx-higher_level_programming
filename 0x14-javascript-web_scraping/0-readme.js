#!/usr/bin/node
const fs = require('fs');

// Read the file using the provided file path argument
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
