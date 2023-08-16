#!/usr/bin/node
const g = parseInt(process.argv[2]);
if (!(isNaN(g))) {
  for (let i = 0; i < g; i++) {
    let line = '';
    for (let j = 0; j < g; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Mising size');
}
