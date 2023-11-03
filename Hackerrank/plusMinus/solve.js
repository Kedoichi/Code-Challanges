"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
  let positives = 0,
    negatives = 0,
    zeros = 0;
  arr.forEach((num) => {
    if (num > 0) positives++;
    else if (num == 0) zeros++;
    else negatives++;
  });
  // Get the total number in arr
  const total = arr.length;
  // Calculate and log the ratios
  console.log((positives / total).toFixed(6));
  console.log((negatives / total).toFixed(6));
  console.log((zeros / total).toFixed(6));
}

function main() {
  const n = parseInt(readLine().trim(), 10);

  const arr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  plusMinus(arr);
}
