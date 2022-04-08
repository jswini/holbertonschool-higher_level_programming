#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
// let listUWC = [];
request(path, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasksFinished = {}
    const allUsers = JSON.parse(body);
    for (let i = 0; i < allUsers.length; i++) {
      const userIdent = allUsers[i].userId;
      const complete = allUsers[i].completed;
      if (complete) {
        if (!tasksFinished[userIdent]) {
          tasksFinished[allUsers[i].userId] = 1;
        } else {
          tasksFinished[allUsers[i].userId] += 1;
        }
      }
    }
    console.log (tasksFinished);
  }
});
