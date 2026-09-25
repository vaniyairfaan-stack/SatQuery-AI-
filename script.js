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
        <strong>Analysis:</strong><br><br>
        Your query was received successfully!<br><br>
        <strong>Your Query:</strong> ${query}<br><br>
        🛰️ SatQuery AI is processing the remote-sensing data...
    `;
});
