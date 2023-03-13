#!/usr/bin/node

let count = Number.parseInt(process.argv[2]);
const t = 'C is fun';

if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  while (count !== 0) {
    console.log(t);
    count--;
  }
}
