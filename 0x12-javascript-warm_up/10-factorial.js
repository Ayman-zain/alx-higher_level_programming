#!/usr/bin/node
const { argv } = require('node:process');
const n = argv[2];
if (!isNaN(n)) {
  const x = fact(Number(n));
  console.log(x);
} else {
  console.log(1);
}
function fact (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
