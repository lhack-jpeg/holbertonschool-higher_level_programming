#!/usr/bin/node

exports.nbOccurences = (list, item) => {
  let count = 0;
  list.forEach((element) => {
    if (element === item) {
      count++;
    }
  });
  return count;
};
