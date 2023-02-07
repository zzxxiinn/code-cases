const equals = (a, b) => {
  if (a === b) {
    return true;
  }

  if (a instanceof Date && b instanceof Date) {
    return a.getTime() === b.getTime()
  }

  if (!a || !b || (typeof a !== 'object' && typeof b !== 'object')) {
    return a === b;
  }

  if (a.prototype !== b.prototype) return false

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every(k => equals(a[k], b[k]));
}

// STREAM
const isStream = (val) => {
  return val !== null && typeof val === 'object' && typeof val.pipe === 'function'
}

/**
 * @param val
 * @returns {boolean}
 *
 * - 检查是否为 null
 * - 使用 typeof 检查是不是 object 类型，并且存在 pipe 方法
 * - 使用 typeof 检查他的 _read 和 _write 方法，及 _readable 和 _writable 属性
 */
const isDuplexStream = (val) => {
  return val !== null &&
    typeof val === 'object' &&
    typeof val.pipe === 'function' &&
    typeof val._read === 'function' &&
    typeof val._readableState === 'object' &&
    typeof val._write === 'function' &&
    typeof val._writableState === 'object';
}

const isWritableStream = (val) => {
  return val !== null &&
    typeof val === 'object' &&
    typeof val.pipe === 'function' &&
    typeof val._write === 'function' &&
    typeof val._writableState === 'object';
}

const isReadableStream = (val) => {
  return val !== null &&
    typeof val === 'object' &&
    typeof val.pipe === 'function' &&
    typeof val._read === 'function' &&
    typeof val._readableState === 'object';
}


// FUNCTION
const isFunction = val => typeof val === 'function';

const isPromiseLike = (val) => {
  return val !== null &&
    ['object', 'function'].includes(typeof val) &&
    typeof val.then === 'function';
}

// [object AsyncFunction] -> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction
const isAsyncFunction = val => Object.prototype.toString.call(val) === '[object AsyncFunction]'

// [object GeneratorFunction] -> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction
const isGeneratorFunction = val => Object.prototype.toString.call(val) === '[object GeneratorFunction]';


// ARRAY & Object

/**
 * @param val
 * @returns {boolean}
 *
 * @example
 * isEmpty([]); // true
 * isEmpty({}); // true
 * isEmpty(''); // true
 * isEmpty([1, 2]); // false
 * isEmpty({ a: 1, b: 2 }); // false
 * isEmpty('text'); // false
 * isEmpty(123); // true - type is not considered a collection
 * isEmpty(true); // true - type is not considered a collection
 */
const isEmpty = val => val == null || !(Object.keys(val) || val).length;

// 是否可迭代
const isArrayLike = val => val != null && typeof val[Symbol.iterator] === 'function';

const isValidJSON = (val) => {
  try {
    JSON.parse(val)
    return true
  } catch (e) {
    return false
  }
}

const isObject = (val) => val === Object(val);

const isPlainObject = (val) => {
  return !!val &&
    typeof val === 'object' &&
    val.constructor === Object
}

const isObjectLike = (val) => val !== null && typeof val === 'object';

const isUndefined = (val) => val === undefined

const isNull = (val) => val === null

const isNil = (val) => isUndefined(val) || isNull(val)

const isSymbol = (val) => typeof val === 'symbol';

const isNumber = (val) => typeof val === 'number' && val === val;

const isBoolean = (val) => typeof val === 'boolean';

const isString = (val) => typeof val === 'string';
