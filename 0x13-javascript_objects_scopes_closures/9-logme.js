#!/usr/bin/node

let index = 0;

exports.logMe = function count (item) {
  console.log(`${index}: ${item}`);
  index += 1;
};
