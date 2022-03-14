let numbers = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  s2: "twenty",
  s3: "thirty",
  s4: "forty",
  s5: "fifty",
  s6: "sixty",
  s7: "seventy",
  s8: "eighty",
  s9: "ninety"
}

let sum = 0;

function fun(number) {
  switch (number.length) {
    case 1:
      let str = numbers[number];
      sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      break;

    case 2:
      if (number[0] == 1) {
        let str = numbers[number];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[0] != 1 && number[1] != 0) {
        let str = numbers["s" + number[0]] + "-" + numbers[number[1]];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[0] != 1 && number[1] == 0) {
        let str = numbers["s" + number[0]];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      break;

    case 3:
      if (number[1] == 0 && number[2] == 0) {
        let str = numbers[number[0]] + " hundred";
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[1] == 0 && number[2] != 0) {
        let str = numbers[number[0]] + " hundred and " + numbers[number[2]];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[1] == 1) {
        let str = numbers[number[0]] + " hundred and " + numbers[number.substr(1, 2)];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[1] != 1 && number[2] == 0) {
        let str = numbers[number[0]] + " hundred and " + numbers["s" + number[1]];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      else if (number[1] != 1 && number[2] != 0) {
        let str = numbers[number[0]] + " hundred and " + numbers["s" + number[1]] + "-" + numbers[number[2]];
        sum += str.replace(/ /gi, "").replace(/[^a-zA-Z ]/gi, "").length;
      }
      break;
  }
}

for (let i = 1; i < 1000; i++) {
  fun(String(i));
}
console.log(sum + 11);