#!/usr/bin/node
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (!(isNaN(a)) && !(isNaN(b))) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}

const num1 = process.argv[2];
const num2 = process.argv[3];
add(num1, num2);
