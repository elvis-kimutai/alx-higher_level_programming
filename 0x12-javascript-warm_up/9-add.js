#!/usr/bin/node

const A = parseInt(process.argv[2]);
const B = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(A, B));
