#!/usr/bin/node
const reader = require('fs');

reader.readFile(process.argv[2], 'utf8', function (err, content)
{
if (error)
{
console.error('Error reading file:', error);
}
else
{
process.stdout.write(content);
}
});
