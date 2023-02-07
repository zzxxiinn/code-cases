/**
 * 转换一个异步函数以返回一个 Promise
 * @param func
 * @returns {function(...[*]): Promise<unknown>}
 *
 * @example
 * const delay = promisify((d, cb) => setTimeout(cb, d));
 * delay(2000).then(() => console.log('Hi!')); // Promise resolves after 2s
 */

const promisify = func => {
  return (...args) => {
    return new Promise((resolve, reject) => {
      return func(...args, (err, result) => err ? reject(err) : resolve(result))
    })
  }
}
