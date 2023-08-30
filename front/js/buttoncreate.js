var buttonContainer = $("#button-container");
var numButtons = 53;
var buttonColors = ["btnLightBlue", "btn2Blue", "btn3Blue", "btn4Blue"];
var buttonLetters = [
  "제작",
  "프로그램",
  "개발",
  "디자인",
  "문서",
  "홈페이지",
  "협업",
  "무료",
  "웹",
  "동영상",
  "콘텐츠",
  "플랫폼",
  "템플릿",
  "소프트웨어",
  "코드",
  "코딩",
  "이미지",
  "편집",
  "앱",
  "게임",
  "합성",
  "설치",
  "모델링",
  "온라인",
  "작성",
  "공유",
  "포토샵",
  "그래프",
  "엑셀",
  "한글",
  "스케치",
  "프로젝트",
  "모자이크",
  "프로토타입",
  "모바일",
  "액터",
  "Google Cloud",
  "로드맵",
  "DB",
  "아이콘",
  "디자인 트렌드",
  "의상",
  "굿즈",
  "상품",
  "움짤",
  "자막",
  "AI",
  "다운로드",
  "인쇄물",
  "모자이크",
  "크로마키",
  "사진",
  "UI",
];

for (var i = 0; i < numButtons; i++) {
  var button = $("<a>", {
    class: "button btnFade " + "btnLightBlue",
    href: "#",
    text: buttonLetters[i],
    id: "show-btn-" + (i + 1),
  });
  buttonContainer.append(button);
  if ((i + 1) % 4 == 0) {
    buttonContainer.append("<br><br><br>");
  }
}
