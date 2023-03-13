#!/usr/bin/node

let count = Number.parseInt(process.argv[2]);
let t = 'X';

if (Number.isNaN(count)) {
  console.log('Missing size');
} else {
  t = t.repeat(count);

  while (count !== 0) {
    console.log(t);
    count--;
  }
}
