function showNewButton() {
    const buttonId = this.id;
    let buttonText = "";
    let hashtag = "";

    if (buttonId === "show-btn-1") {
      buttonText = "제작";
      hashtag = "제작";
    } else if (buttonId === "show-btn-2") {
      buttonText = "프로그램";
      hashtag = "프로그램";
    } else if (buttonId === "show-btn-3") {
      buttonText = "개발";
      hashtag = "개발";
    } else if (buttonId === "show-btn-4") {
      buttonText = "디자인";
      hashtag = "디자인";
    } else if (buttonId === "show-btn-5") {
      buttonText = "문서";
      hashtag = "문서";
    } else if (buttonId === "show-btn-6") {
      buttonText = "홈페이지";
      hashtag = "홈페이지";
    } else if (buttonId === "show-btn-7") {
      buttonText = "협업";
      hashtag = "협업";
    } else if (buttonId === "show-btn-8") {
      buttonText = "무료";
      hashtag = "무료";
    } else if (buttonId === "show-btn-9") {
      buttonText ="웹";
      hashtag = "웹";
    } else if (buttonId === "show-btn-10") {
      buttonText = "동영상";
      hashtag = "동영상";
    } else if (buttonId === "show-btn-11") {
      buttonText = "콘텐츠";
      hashtag = "콘텐츠";
    } else if (buttonId === "show-btn-12") {
      buttonText = "플랫폼";
      hashtag = "플랫폼";
    } else if (buttonId === "show-btn-13") {
      buttonText = "템플릿";
      hashtag = "템플릿";
    } else if (buttonId === "show-btn-14") {
      buttonText = "소프트웨어";
      hashtag = "소프트웨어";
    } else if (buttonId === "show-btn-15") {
      buttonText = "코드";
      hashtag = "코드";
    } else if (buttonId === "show-btn-16") {
      buttonText = "코딩";
      hashtag = "코딩";
    } else if (buttonId === "show-btn-17") {
        buttonText = "이미지";
        hashtag = "이미지";
      } else if (buttonId === "show-btn-18") {
        buttonText = "편집";
        hashtag = "편집";
      } else if (buttonId === "show-btn-19") {
        buttonText = "앱";
        hashtag = "앱";
      } else if (buttonId === "show-btn-20") {
        buttonText = "게임";
        hashtag = "게임";
      } else if (buttonId === "show-btn-21") {
        buttonText = "합성";
        hashtag = "합성";
      } else if (buttonId === "show-btn-22") {
        buttonText = "설치";
        hashtag = "설치";
      } else if (buttonId === "show-btn-23") {
        buttonText = "모델링";
        hashtag = "모델링";
      } else if (buttonId === "show-btn-24") {
        buttonText = "온라인";
        hashtag = "온라인";
      } else if (buttonId === "show-btn-25") {
        buttonText = "작성";
        hashtag = "작성";
      } else if (buttonId === "show-btn-26") {
        buttonText = "공유";
        hashtag = "공유";
      } else if (buttonId === "show-btn-27") {
        buttonText = "포토샵";
        hashtag = "포토샵";
      } else if (buttonId === "show-btn-28") {
        buttonText = "그래프";
        hashtag = "그래프";
      } else if (buttonId === "show-btn-29") {
        buttonText = "엑셀";
        hashtag = "엑셀";
      } else if (buttonId === "show-btn-30") {
        buttonText = "한글";
        hashtag = "한글";
      } else if (buttonId === "show-btn-31") {
        buttonText = "스케치";
        hashtag = "스케치";
      } else if (buttonId === "show-btn-32") {
        buttonText = "프로젝트";
        hashtag = "프로젝트";
      } else if (buttonId === "show-btn-33") {
        buttonText = "모자이크";
        hashtag = "모자이크";
      } else if (buttonId === "show-btn-34") {
        buttonText = "프로토타입";
        hashtag = "프로토타입";
      } else if (buttonId === "show-btn-35") {
        buttonText = "모바일";
        hashtag = "모바일";
      } else if (buttonId === "show-btn-36") {
        buttonText = "액터";
        hashtag = "액터";
      } else if (buttonId === "show-btn-37") {
        buttonText = "Google Cloud";
        hashtag = "Google Cloud";
      } else if (buttonId === "show-btn-38") {
        buttonText = "로드맵";
        hashtag = "로드맵";
      } else if (buttonId === "show-btn-39") {
        buttonText = "DB";
        hashtag = "DB";
      } else if (buttonId === "show-btn-40") {
        buttonText = "아이콘";
        hashtag = "아이콘";
      } else if (buttonId === "show-btn-41") {
        buttonText = "디자인 트렌드";
        hashtag = "디자인 트렌드";
      }

      const newBtn = document.createElement("button");
      newBtn.textContent = buttonText; // 생성한 버튼의 텍스트 설정
      newBtn.classList.add("button", "btnLightBlue", "btnFade");
    
      const closeBtn = document.createElement("span");
      closeBtn.textContent = "×";
      closeBtn.classList.add("close");
      newBtn.appendChild(closeBtn);
      newBtn.addEventListener("click", function () {
        this.remove();
        document.getElementById(buttonId).addEventListener("click", showNewButton);
      });
    
      document.querySelector(".pick").appendChild(newBtn);
      document.getElementById(buttonId).removeEventListener("click", showNewButton);
    
      localStorage.setItem("filter", hashtag);
  }
  
  
  document.getElementById("show-btn-1").addEventListener("click", showNewButton);
  document.getElementById("show-btn-2").addEventListener("click", showNewButton);
  document.getElementById("show-btn-3").addEventListener("click", showNewButton);
  document.getElementById("show-btn-4").addEventListener("click", showNewButton);
  document.getElementById("show-btn-5").addEventListener("click", showNewButton);
  document.getElementById("show-btn-6").addEventListener("click", showNewButton);
  document.getElementById("show-btn-7").addEventListener("click", showNewButton);
  document.getElementById("show-btn-8").addEventListener("click", showNewButton);
  document.getElementById("show-btn-9").addEventListener("click", showNewButton);
  document.getElementById("show-btn-10").addEventListener("click", showNewButton);
  document.getElementById("show-btn-11").addEventListener("click", showNewButton);
  document.getElementById("show-btn-12").addEventListener("click", showNewButton);
  document.getElementById("show-btn-13").addEventListener("click", showNewButton);
  document.getElementById("show-btn-14").addEventListener("click", showNewButton);
  document.getElementById("show-btn-15").addEventListener("click", showNewButton);
  document.getElementById("show-btn-16").addEventListener("click", showNewButton);
  document.getElementById("show-btn-17").addEventListener("click", showNewButton);
  document.getElementById("show-btn-18").addEventListener("click", showNewButton);
  document.getElementById("show-btn-19").addEventListener("click", showNewButton);
  document.getElementById("show-btn-20").addEventListener("click", showNewButton);
  document.getElementById("show-btn-21").addEventListener("click", showNewButton);
  document.getElementById("show-btn-22").addEventListener("click", showNewButton);
  document.getElementById("show-btn-23").addEventListener("click", showNewButton);
  document.getElementById("show-btn-24").addEventListener("click", showNewButton);
  document.getElementById("show-btn-25").addEventListener("click", showNewButton);
  document.getElementById("show-btn-26").addEventListener("click", showNewButton);
  document.getElementById("show-btn-27").addEventListener("click", showNewButton);
  document.getElementById("show-btn-28").addEventListener("click", showNewButton);
  document.getElementById("show-btn-29").addEventListener("click", showNewButton);
  document.getElementById("show-btn-30").addEventListener("click", showNewButton);
  document.getElementById("show-btn-31").addEventListener("click", showNewButton);
  document.getElementById("show-btn-32").addEventListener("click", showNewButton);
  document.getElementById("show-btn-33").addEventListener("click", showNewButton);
  document.getElementById("show-btn-34").addEventListener("click", showNewButton);
  document.getElementById("show-btn-35").addEventListener("click", showNewButton);
  document.getElementById("show-btn-36").addEventListener("click", showNewButton);
  document.getElementById("show-btn-37").addEventListener("click", showNewButton);
  document.getElementById("show-btn-38").addEventListener("click", showNewButton);
  document.getElementById("show-btn-39").addEventListener("click", showNewButton);
  document.getElementById("show-btn-40").addEventListener("click", showNewButton);
  document.getElementById("show-btn-41").addEventListener("click", showNewButton);
