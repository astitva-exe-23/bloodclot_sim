async function fetchRiskData() {
    try {
        const response = await fetch('http://127.0.0.1:5000/get-data'); // Adjust URL if needed
        const data = await response.json();

        if (data.error) {
            document.getElementById('status').textContent = `STATUS: ${data.error}`;
            return;
        }

        const riskLevel = data.clot_risk.toUpperCase(); // Get clot risk from API response

        // Reset indicators
        document.getElementById('low-indicator').classList.remove('low-risk');
        document.getElementById('moderate-indicator').classList.remove('moderate-risk');
        document.getElementById('high-indicator').classList.remove('high-risk');

        // Update indicators based on risk level
        if (riskLevel === 'LOW RISK') {
            document.getElementById('low-indicator').classList.add('low-risk');
            document.getElementById('status').textContent = 'STATUS: LOW RISK';
        } else if (riskLevel === 'MODERATE RISK') {
            document.getElementById('moderate-indicator').classList.add('moderate-risk');
            document.getElementById('status').textContent = 'STATUS: MODERATE RISK';
        } else if (riskLevel === 'HIGH RISK') {
            document.getElementById('high-indicator').classList.add('high-risk');
            document.getElementById('status').textContent = 'STATUS: CRITICAL';
        } else {
            document.getElementById('status').textContent = 'STATUS: UNKNOWN RISK';
        }
    } catch (error) {
        console.error('Error fetching risk data:', error);
        document.getElementById('status').textContent = 'STATUS: ERROR FETCHING DATA';
    }
}

// Fetch risk data on page load
window.onload = fetchRiskData;

// Optionally, refresh data every few seconds (e.g., every 10 seconds)
setInterval(fetchRiskData, 10000);
