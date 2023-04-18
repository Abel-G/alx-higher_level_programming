#!/usr/bin/node
class Square extends Rectangle('./5-square.js') {
  charPrint(c = 'X') {
    let row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
