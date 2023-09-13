 #!/usr/bin/node

const dict = require('./101-data').dict;
const newd = {};

for (const key in dict) {
  if (newd[dict[key]] === undefined) {
    newd[dict[key]] = (key);
  } else {
    newd[dict[key]].push(key);
  }
}
console.log(newd);
