#!/usr/bin/node

const args = process.argv;

const parsed = Number.parseInt(args[2]);

if (Number.isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
