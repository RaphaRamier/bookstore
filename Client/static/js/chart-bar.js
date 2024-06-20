document.addEventListener('DOMContentLoaded', function() {
    let chart; // To store the Chart.js instance

    function fetchDataAndRenderChart(type) {
        fetch('/API/sales/monthly-trend/')
            .then(response => response.json())
            .then(data => {
                const monthlyTrends = data.monthly_trends;
                const months = monthlyTrends.map(entry => entry.month.substring(0, 7));
                const totalQuantities = monthlyTrends.map(entry => entry.total_quantity);
                const totalValues = monthlyTrends.map(entry => entry.total_value);

                const reversedMonths = months.reverse();
                const reversedTotalQuantities = totalQuantities.reverse();
                const reversedTotalValues = totalValues.reverse();

                const ctx = document.getElementById('EarningsChartBar').getContext('2d');

                const chartData = {
                    labels: reversedMonths,
                    datasets: [{
                        label: type === 'quantity' ? 'Total Quantity' : 'Total Value',
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        data: type === 'quantity' ? reversedTotalQuantities : reversedTotalValues
                    }]
                };

                if (chart) {
                    chart.destroy(); // Destroy the previous chart instance
                }

                chart = new Chart(ctx, {
                    type: 'bar',
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
    fetchDataAndRenderChart('quantity');

    // Add event listeners for dropdown buttons
    document.querySelectorAll('.dropdown-item').forEach(button => {
        button.addEventListener('click', function() {
            const filterType = this.getAttribute('data-filter');
            fetchDataAndRenderChart(filterType);
        });
    });
});
