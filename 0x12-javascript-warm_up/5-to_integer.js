#!/usr/bin/node
if (typeof parseInt(process.argv[2]) === 'number' && !isNaN(process.argv[2])) {
  console.log(process.argv[2]);
} else {
  console.log('Not a number');
}
