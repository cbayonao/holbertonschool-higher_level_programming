#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completed = {};

request.get(url, (e, response, body) => {
  if (e) {
    console.log(e);
  }
  const json = JSON.parse(body);

  for (const task of json) {
    if (task.completed === true) {
      if (!(task.userId in completed)) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
