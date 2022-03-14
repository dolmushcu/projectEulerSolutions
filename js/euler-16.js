var sayi = 2 ** 1000;
var sum = 0;

var arr = String(BigInt(sayi)).split("");
arr.forEach(function fun(e) {
  sum += parseInt(e);
})
console.log(sum);