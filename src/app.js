import testVal from './testModule';

const d = 10;
console.log(testVal.a());

const a = new WeakMap();
const obj = {};
a.set(obj, 'objxxx');
console.log(a.get(obj));

const p = new Promise(function(ok) {
  ok('wow');
});

p.then(a => {
  console.log(a);
});
