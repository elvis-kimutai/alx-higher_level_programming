#!/usr/bin/node

const process = require('process');
const oneArg = process.argv[2];
const number = parseInt(oneArg);

if (!isNaN(number)) {
  console.log('My number:', number);
} else {
  console.log('Not a number');
}
