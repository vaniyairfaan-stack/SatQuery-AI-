// SatQuery AI - Basic interactions

const analyzeButton = document.getElementById("analyzeBtn");
const queryInput = document.getElementById("queryInput");
const resultBox = document.getElementById("result");

analyzeButton.addEventListener("click", function () {

    const query = queryInput.value.trim();

    if (query === "") {
        resultBox.innerHTML = "⚠️ Please enter a question first.";
        return;
    }

    resultBox.innerHTML = `
        <strong>Analysis:</strong><br>
        Your query was received successfully.<br><br>
        <strong>Query:</strong> ${query}<br><br>
        🛰️ SatQuery AI is processing the remote-sensing data...
    `;
});

queryInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        analyzeButton.click();
    }
});
