/**
 * make class singleton
 * @param className
 * @returns {object|null}
 *
 * @example
 * class MyClass {
 *   constructor(msg) {
 *     this.msg = msg;
 *   }
 *
 *   printMsg() {
 *     console.log(this.msg);
 *   }
 * }
 *
 * MySingletonClass = singleton(MyClass);
 * const myObj = new MySingletonClass('first');
 * myObj.printMsg();            // 'first'
 *
 * const myObj2 = new MySingletonClass('second');
 * myObj2.printMsg();           // 'first'
 */

const singleton = (className) => {
  return new Proxy(className.prototype.constructor, {
    instance: null,
    construct(target, argArray) {
      if (!this.instance) {
        this.instance = new target(...argArray)
      }
      return this.instance
    }
  })
}
