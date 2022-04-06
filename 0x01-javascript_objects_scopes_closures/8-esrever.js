#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  const limit = len / 2;
  for (let i = 0; i <= limit; i++) {
    const temp = list[i];
    list[i] = list[len - i];
    list[len - i] = temp;
  }
  return list;
};
