#!/usr/bin/node

exports.esrever = function (list) {
  const tmp = [];

  list.forEach(el => {
    tmp.unshift(el);
  });

  return tmp;
};
