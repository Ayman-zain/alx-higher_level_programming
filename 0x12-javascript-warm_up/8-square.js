#!/usr/bin/node
const { argv } = require('node:process');

if (!isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    for (let j = 0; j < argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
