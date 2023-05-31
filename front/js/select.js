{
  fruits.map((fruit, index) => {
    return (
      //style 속성은 보이는 가독성을 높이기 위해서 설정한것
      <div
        style={{
          margin: "auto",
          marginTop: "50px",
          backgroundColor: "pink",
          fontSize: "20px",
          width: "100px",
        }}
        key={index}
      >
        {fruit.name}
      </div>
    );
  });
}
