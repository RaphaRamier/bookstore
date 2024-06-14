document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/sales/monthly-trend/')  // Endpoint da sua API
        .then(response => response.json())
        .then(data => {
            const monthlyData = data.monthly_data;
            const months = monthlyData.map(entry => entry.month);
            const totalQuantities = monthlyData.map(entry => entry.total_quantity);
            const totalValues = monthlyData.map(entry => entry.total_value);

            // Configurações do gráfico
            const ctx = document.getElementById('myBarChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: months,
                    datasets: [{
                        label: 'Total Quantity',
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        data: totalQuantities
                    }, {
                        label: 'Total Value',
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1,
                        data: totalValues
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
        });
});