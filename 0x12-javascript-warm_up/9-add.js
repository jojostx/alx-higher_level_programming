#!/usr/bin/node

const a = Number.parseInt(process.argv[2]);
const b = Number.parseInt(process.argv[3]);

function add (a, b) {
  console.log(a * b);
}

add(a, b);
