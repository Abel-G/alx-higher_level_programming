#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destFilePath = process.argv[4];

const fileContents1 = fs.readFileSync(fileA, 'utf8');
const fileContents2 = fs.readFileSync(fileB, 'utf8');
const fileC = fileContents1 + fileContents2;
fs.writeFileSync(destFilePath, fileC);
