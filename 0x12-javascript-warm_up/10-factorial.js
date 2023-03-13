#!/usr/bin/node

const a = Number.parseInt(process.argv[2]);

function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  }

  if (a < 0) {
    return NaN;
  }

  return a * factorial(a - 1);
}

if (Number.isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
