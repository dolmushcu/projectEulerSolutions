var eb = 100;

for (let i = 100; i < 1000; i++) {
  let sum = 1;
  for (let a = 100; a < 1000; a++) {
    let sayi = String(i * a);
    if (sayi.length % 2 == 0) {
      let yari = sayi.length / 2;
      if (sayi.substr(0, yari) == sayi.substr(yari).split("").reverse().join("") && sayi > eb) {
        eb = sayi;
      }
    }
  }
}

console.log(eb);