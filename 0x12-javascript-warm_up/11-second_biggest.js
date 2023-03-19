#!/usr/bin/node

let args = process.argv.map(arg => Number.parseInt(arg));

args = args.filter(arg => Number.isInteger(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const l = args.reduce((a, val) => a > val ? a : val, 0);
  console.log(l);
}
