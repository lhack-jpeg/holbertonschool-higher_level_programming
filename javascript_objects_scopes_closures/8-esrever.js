#!/usr/bin/node

exports.esrever = (list) => {
  const myArray = [];
  list.forEach((element) => {
    myArray.unshift(element);
  });
  return myArray;
};
