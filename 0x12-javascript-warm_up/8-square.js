#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < number) {
    let square = '';
    for (let j = 0; j < number; j++) {
      square += 'x';
    }
    console.log(square);
    i++;
  }
}
