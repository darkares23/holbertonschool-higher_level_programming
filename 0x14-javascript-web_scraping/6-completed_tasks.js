#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function countTodos (taskList) {
  const retObj = {};
  for (let i = 0; i < taskList.length; i++) {
    const userId = taskList[i].userId;
    const completed = taskList[i].completed;
    if (Object.prototype.hasOwnProperty.call(retObj, userId) && completed) {
      retObj[userId] += 1;
    } else if (completed) {
      retObj[userId] = 1;
    }
  }
  console.log(retObj);
}

request
  .get(url, (err, res, body) => {
    if (err) { console.log(err); }
    countTodos(JSON.parse(body));
  });
