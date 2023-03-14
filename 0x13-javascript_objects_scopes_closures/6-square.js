#!/usr/bin/node

const _Square = require('./5-square');

class Square extends _Square {
	charPrint(c) {
		this.print(c);
	}
}

module.exports = Square;
