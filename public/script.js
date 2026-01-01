const predictionForm = document.getElementById('predictionForm')
predictionForm.addEventListener('submit', async(e) => {
    e.preventDefault();
    const hoursStudied = document.getElementById('hoursStudied').value;
    const previousScores = document.getElementById('previousScores').value;
    const sleepHours = document.getElementById('sleepHours').value;
    const papersPracticed = document.getElementById('papersPracticed').value;
    if (hoursStudied < 0 || previousScores < 0 || sleepHours < 0 || papersPracticed < 0) {
        window.alert('Invalid input(s)!')
    } else {
        const formData = new FormData(predictionForm);
        const data = Object.fromEntries(formData)
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            const result = await response.json();
            if (result.success) {
                document.getElementById('result').innerHTML = `<h2>Result: ${result.prediction}</h2>`
            } else {
                document.getElementById('result').innerHTML = `<p>Error</p>`
            } 
        } catch (error) {
            document.getElementById('result').innerHTML = `<p>Error</p>`
        }
    }
})
