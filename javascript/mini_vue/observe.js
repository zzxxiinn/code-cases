function observe(obj) {
  if (!obj || typeof obj !== "object") {
    return;
  }

  for (const key in obj) {
    let intervalValue = obj[key];
    // const deps = new Set();
    const deps = [];
    Object.defineProperty(obj, key, {
      get() {
        // deps.add();
        if (window.__func && !deps.includes(window.__func)) {
          deps.push(window.__func);
        }
        return intervalValue;
      },
      set(newVal) {
        intervalValue = newVal;
        for (const dep of deps) {
          dep();
        }
      },
    });
  }
}

function autorun(func) {
  window.__func = func;
  func();
  window.__func = null;
}
