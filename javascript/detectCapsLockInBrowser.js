const inputEl = document.getElementById("target-input");

// 使用 KeyboardEvent.getModifierState() -> https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState
inputEl.addEventListener("keyup", (e) => {
  if (e.getModifierState("CapsLock")) {
    // 当前 CapsLock 启用
  } else {
    // 当前 CapsLock 未启用
  }
});
