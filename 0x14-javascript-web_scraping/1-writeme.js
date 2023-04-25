#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
const path = process.argv[2];

fs.writeFileSync(path, data);
