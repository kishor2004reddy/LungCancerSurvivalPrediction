document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    // Convert numeric fields
    data.Episode_Length_minutes = parseFloat(data.Episode_Length_minutes);
    data.Host_Popularity_percentage = parseFloat(data.Host_Popularity_percentage);
    data.Guest_Popularity_percentage = parseFloat(data.Guest_Popularity_percentage);
    data.Number_of_Ads = parseInt(data.Number_of_Ads);

    const resultDiv = document.getElementById('result');
    resultDiv.textContent = "Predicting...";

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (response.ok) {
            resultDiv.textContent = `Predicted Listening Time: ${result.prediction.toFixed(2)} minutes`;
        } else {
            resultDiv.textContent = result.error || "Prediction failed.";
        }
    } catch (err) {
        resultDiv.textContent = "Error connecting to server.";
    }
});