#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

try {
  request.get(url, (e, response, body) => {
    if (e) {
      console.log(e);
    } else {
      fs.writeFileSync(process.argv[3], body);
    }
  });
} catch (e) {
  console.log(e);
}
