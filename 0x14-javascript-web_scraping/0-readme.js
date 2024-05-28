#!/usr/bin/node
const reader = require('fs');

reader.readFile(process.argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.error('Error reading file:', error);
  } else {
    process.stdout.write(content);
  }
});

