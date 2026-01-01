document.getElementById('predictionForm').addEventListener('submit', async(e) => {
    e.preventDefault();
    const hoursStudied = parseFloat(document.getElementById('hoursStudied').value);
    const previousScores = parseFloat(document.getElementById('previousScores').value);
    const sleepHours = parseFloat(document.getElementById('sleepHours').value);
    const papersPracticed = parseFloat(document.getElementById('papersPracticed').value);
    if ((isNaN(hoursStudied) || hoursStudied < 0) || (isNaN(previousScores) || previousScores < 0) || (isNaN(sleepHours) || sleepHours < 0) || (isNaN(papersPracticed) || papersPracticed < 0)) {
        window.alert('Invalid input(s)!')
    } else {
        
    }
})