#!/usr/bin/node

exports.converter = function (base) {
  return function (no) {
    return no.toString(base);
  };
};
