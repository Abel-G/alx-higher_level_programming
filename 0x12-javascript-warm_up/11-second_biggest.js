#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length > 2) {
  const seconedBig = arr.sort(function (a, b) { return a - b; })[arr.length - 2];
  console.log(seconedBig);
} else {
  console.log(0);
}
