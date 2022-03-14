function isPrime(n) {
  for (let i = 3; i <= Math.ceil(Math.sqrt(n)); i += 2) {
    if (n % i === 0) return false;
  }
  return true;
};



let arr = [2];

for (let i = 3; i < 600851; i += 2) {
  if (isPrime(i)) {
    arr.push(i);
  }
}

var carp = [];
var sayi = 600851475143;


arr.forEach(function fun(e) {
  if (sayi % e === 0) {
    carp.push(e);
    sayi = sayi / e;
    if (sayi < 10) {
      console.log("en buyuk: " + String(Math.max(...carp)));
    }
  }
});