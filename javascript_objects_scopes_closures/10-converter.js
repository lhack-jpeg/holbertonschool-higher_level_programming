#!/usr/bin/node

exports.converter = (base) => {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
