document.addEventListener('DOMContentLoaded', function() {
    let chart; // To store the Chart.js instance

    function fetchDataAndRenderChart() {
        fetch('/API/sales/monthly-trend/')
            .then(response => response.json())
            .then(data => {
                const monthlyTrends = data.monthly_trends;
                const months = monthlyTrends.map(entry => entry.month.substring(0, 7));
                const percentageDifference = monthlyTrends.map(entry => entry.percentage_difference);

                const reversedMonths = months.reverse();
                const reversedPercentageDifference = percentageDifference.reverse();

                const ctx = document.getElementById('lineChart').getContext('2d');

                const chartData = {
                    labels: reversedMonths,
                    datasets: [{
                        label: 'Percentage Difference',
                        backgroundColor: 'rgba(54, 200, 0, 0.5)',
                        borderColor: 'rgba(54, 200, 0, 1)',
                        borderWidth: 1,
                        data: reversedPercentageDifference
                    }]
                };

                if (chart) {
                    chart.destroy(); // Destroy the previous chart instance
                }

                chart = new Chart(ctx, {
                    type: 'line',
                    data: chartData,
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Error fetching monthly trend:', error);
            });
    }

    // Initial render with default data
    fetchDataAndRenderChart();

    // Optional: Add event listeners for dropdown buttons if needed
});
