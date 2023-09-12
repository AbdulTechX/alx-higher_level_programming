#!/usr/bin/node
const PrevSquare = require('./5-square');
module.exports = class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let mySqr = '';
      for (let j = 0; j < this.width; ++j) mySqr += myChar;
      console.log(mySqr);
    }
  }
};
