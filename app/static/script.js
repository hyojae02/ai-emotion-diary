function analyzeEmotion() {
  const text = document.getElementById("userInput").value;
  if (!text.trim()) {
    alert("텍스트를 입력해주세요.");
    return;
  }

  axios.post("/analyze", { text })
    .then(response => {
      const data = response.data;
      document.getElementById("inputText").innerText = data.input;
      document.getElementById("translated").innerText = data.translation;
      document.getElementById("emotions").innerText = data.emotions.join(", ");
      document.getElementById("resultBox").style.display = "block";
    })
    .catch(error => {
      console.error(error);
      alert("감정 분석 중 오류가 발생했습니다.");
    });
}
