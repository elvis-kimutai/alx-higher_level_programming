#!/usr/bin/node
const process = require('process');
const argls = process.argv;

if (isNaN(argls[2]) || isNaN(argls[3])) {
  console.log('0');
} else {
  const array = argls.map(Number);
  array.slice(2, argls.length);
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
