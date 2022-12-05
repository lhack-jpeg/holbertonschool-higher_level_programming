#!/usr/bin/node

const lines = {
  first: 'C is Fun',
  second: 'Python is cool',
  third: 'JavaScript is amazing'
};

for (const key in lines) {
  console.log(lines[key]);
}
