#!/usr/bin/node
const line = 'C is fun';
const x = parseInt(process.argv[2]);

for (let i = 0; i < x; i++) {
  console.log(line);
}
