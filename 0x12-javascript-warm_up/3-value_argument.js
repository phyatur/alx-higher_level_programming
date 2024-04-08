#!/usr/bin/node
argc = process.argv;
if (argc[2] == null) {
  console.log("No argument");
} else {
  console.log(argc[2]);
}
