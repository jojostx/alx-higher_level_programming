#!/usr/bin/node

const process = require('process');

const args = process.argv;

let first = args[2];

if (first === undefined) {
  first = 'No argument';
}

console.log(first);
