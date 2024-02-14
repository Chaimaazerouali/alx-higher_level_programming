#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sum = '';
      for (let j = 0; j < this.width; j++) {
        sum += c;
      }
      console.log(sum);
    }
  }
}

module.exports = Square;
