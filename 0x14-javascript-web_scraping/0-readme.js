#!/usr/bin/node

// imports the module
const fs = require('fs');
const file = process.argv[2];

// read the files
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});
