#!/usr/bin/node

function findSecondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  }

  let biggest = Number.MIN_SAFE_INTEGER;
  let secondBiggest = Number.MIN_SAFE_INTEGER;

  for (const num of arr) {
    const num1 = parseInt(num);
    if (num1 > biggest) {
      secondBiggest = biggest;
      biggest = num1;
    } else if (num1 > secondBiggest && num1 < biggest) {
      secondBiggest = num1;
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
const result = findSecondBiggest(args);
console.log(result);
