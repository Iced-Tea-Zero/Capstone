// 버튼 클릭 이벤트 함수
function showNewButton() {
  const newBtn = document.createElement("button");
  newBtn.textContent = "# 다이어그램";
  newBtn.classList.add("imsibutton1");

  const closeBtn = document.createElement("span");
  closeBtn.textContent = "×";
  closeBtn.classList.add("close");
  newBtn.appendChild(closeBtn);
  newBtn.addEventListener("click", function () {
    this.remove(); // 클릭된 버튼을 삭제
  });

  document.getElementById("pick").appendChild(newBtn);
}

document.getElementById("show-btn").addEventListener("click", showNewButton);

