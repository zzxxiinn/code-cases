// 柯里化（Currying）是把接受多个参数的函数转变为接受一个单一参数的函数
// 并且返回接受余下的参数且返回结果的新函数。

const add = (a, b, c) => a + b + c;
console.log(add(1, 2, 3)); // 6

const curry = (fn, ...args) => {
  return args.length >= fn.length
    ? fn(...args)
    : (...args2) => curry(fn, ...args, ...args2);
};

const addCurry = curry(add);

console.log(addCurry(1)(2)(3)); // 6
console.log(addCurry(1)(2, 3)); // 6

// =============

function curryAdd(x) {
  const fn = (y) => curryAdd(x + y);
  fn.toString = () => x;
  return fn;
}

console.log(+curryAdd(1)(2)); // 3
console.log(+curryAdd(1)(2)(3)); // 6
console.log(+curryAdd(1)(2)(3)(4)); // 10

// ============= advance useage
function log(date, importance, message) {
  console.log(
    `[${date.getHours()}:${date.getMinutes()}] [${importance}] ${message}`
  );
}

log = curry(log);

log(new Date(), "DEBUG", "some debug"); // [12:30] [DEBUG] some debug
log(new Date())("DEBUG")("some debug"); // [12:30] [DEBUG] some debug
log(new Date(), "DEBUG")("some debug"); // [12:30] [DEBUG] some debug

const logNow = log(new Date());
logNow("INFO", "message"); // [12:30] [INFO] message

const debugNow = logNow("DEBUG");
debugNow("message"); // [12:30] [DEBUG] message
