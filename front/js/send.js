const data = "data";

const aTag = document.querySelector("a");
aTag.addEventListener("click", () => {
  location.href = `receive.html?${data}`;
});
