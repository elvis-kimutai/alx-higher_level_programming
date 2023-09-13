#!/usr/bin/node

const fs = require('fs');
const dis1 = fs.readFileSync(process.argv[2], 'utf8');
const dis2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], dis1 + dis2);
