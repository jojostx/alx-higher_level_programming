#!/usr/bin/node

exports.esrever = function (list) {
	let tmp = [];

	list.forEach(el => {
		tmp.unshift(el);
	});

	return tmp;
}
