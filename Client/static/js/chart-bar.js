document.addEventListener('DOMContentLoaded', function() {
    fetch('/API/sales/monthly-trend/')
        .then(response => response.json())
        .then(data => {
            const monthlyTrends = data.monthly_trends;
            const months = monthlyTrends.map(entry => entry.month.substring(0, 7));
            const totalQuantities = monthlyTrends.map(entry => entry.total_quantity);

            const reversedMonths = months.reverse();
            const reversedTotalQuantities = totalQuantities.reverse();

            const ctx = document.getElementById('EarningsChartBar').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: reversedMonths,
                    datasets: [{
                        label: 'Total Quantity',
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        data: reversedTotalQuantities
                    }]
                },
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
});
