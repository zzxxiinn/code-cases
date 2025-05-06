// toString  遇到 (+-*/==><)自动调用 toString
console.log(toString.call(() => {})); // [object Function]
console.log(toString.call({})); // [object Object]
console.log(toString.call([])); // [object Array]
console.log(toString.call("")); // [object String]
console.log(toString.call(22)); // [object Number]
console.log(toString.call(undefined)); // [object undefined]
console.log(toString.call(null)); // [object null]
console.log(toString.call(new Date())); // [object Date]
console.log(toString.call(Math)); // [object Math]
// toString.call(window); // [object Window]
console.log(toString.call(Symbol())); // [object Symbol]
console.log(toString.call(BigInt(123))); // [object BigInt]
console.log(toString.call(true)); // [object Boolean]
console.log(toString.call(false)); // [object Boolean]
console.log(toString.call(NaN)); // [object Number]
console.log(toString.call(Infinity)); // [object Number]

// valueOf 遇到 (+-*/==><)自动调用 valueOf
// 共同点： 在输出对象时，会自动调用。
// 不同点： 默认返回值不同，存在优先级关系
// 数值运算中，优先调用 valueOf，字符串运算中，优先调用 toString

class A {
  valueOf() {
    return 2;
  }
  toString() {
    return "hhh";
  }
}

const a = new A();
console.log(a + 1); // 3 => valueOf
console.log(String(a)); // hhh => toString
console.log(Number(a)); // 2 => valueOf
console.log(Boolean(a)); // true => valueOf

// ========================
// a === 1 && a === 2 && a === 3 为 true
let value = 1;
Object.defineProperty(globalThis, "v", {
  get() {
    return value++;
  },
});
console.log(v === 1 && v === 2 && v === 3); // true
