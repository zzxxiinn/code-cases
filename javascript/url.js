/**
 * 将字符串转换为URL友好的段
 * @param {string} str
 * @returns {string}
 *
 * @example
 * slugify('Hello World!');
 * // returns 'hello-world'
 */
const slugify = str =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');


/**
 * 将所有给定的URL段连接在一起，然后规范化结果URL
 * @param args
 * @returns {string}
 * @constructor
 *
 * @example
 * // returns 'http://www.google.com/a/b/cd?foo=123&bar=foo'
 * URLJoin('http://www.google.com', 'a', '/b/cd', '?foo=123', '?bar=foo');
 */
const URLJoin = (...args) =>
  args.join('/')
    .replace(/[\/]+/g, '/')
    .replace(/^(.+):\//, '$1://')
    .replace(/^file:/, 'file:/')
    .replace(/\/(\?|&|#[^!])/g, '$1')
    .replace(/\?/g, '&')
    .replace('&', '?');


/**
 * 从给定的查询字符串或URL生成对象）
 * @param {string} url
 * @returns {*}
 *
 * @example
 * queryStringToObject("https://google.com?page=1&count=10")
 * // returns {page: '1', count: '10'}
 */
const queryStringToObject = url =>
  [...new URLSearchParams(url.split('?')[1])].reduce(
    (prev, [k, v]) => ((prev[k] = v), prev), {}
  );

module.exports = {
  slugify,
  URLJoin,
  queryStringToObject
}
