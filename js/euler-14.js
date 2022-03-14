function check(element) {
  let e = element;
  let sayac = 1;

  while (e > 1) {
    if (e % 2 === 0) {
      e = e / 2;
      sayac++;
    }
    else {
      e = (3 * e) + 1;
      sayac++;
    }
  }
  return sayac;
}

let foo = 100;
let sayi = 0;

for (let i = 3; i < 1000000; i++) {
  let element = check(i);
  if (element > foo) {
    foo = element;
    sayi = i;
  }
}

console.log(foo);
console.log(sayi);