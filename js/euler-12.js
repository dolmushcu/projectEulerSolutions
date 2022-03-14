function divisorNum(e){
  let count = 2;
  let max = e;

  let i = 2;
  while (i < max) {
    if (e % i == 0) {
      count += 2;
      max = e / i;
    }
    i += 1;
  }

  return count;
}

let sum = 0;
for (let i = 0; i < 1000000; i++) {
  sum += i;
  if (divisorNum(sum) > 500) {
    console.log(sum);
    break;
  }
}