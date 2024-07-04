document.addEventListener('DOMContentLoaded', function() {
    let chart;

    function fetchDataAndRenderChart(filter = 'All') {
        fetch('/API/cashflow/buyers/monthly-trend/')
            .then(response => response.json())
            .then(data => {
                const monthlyTrends = data.monthly_trends || [];

                if (!monthlyTrends.length) {
                    console.error('No data found.');
                    return;
                }

                const filteredTrends = filter === 'All' ? monthlyTrends : monthlyTrends.filter(entry => entry.buyer__name === filter);

                const months = [...new Set(filteredTrends.map(entry => entry.month.substring(0, 7)))];
                const buyers = [...new Set(filteredTrends.map(entry => entry.buyer__name))];

                const datasets = buyers.map(buyer => {
                    const buyerData = filteredTrends.filter(entry => entry.buyer__name === buyer);
                    return {
                        label: buyer,
                        data: months.map(month => {
                            const entry = buyerData.find(data => data.month.substring(0, 7) === month);
                            return entry ? entry.total_spending : 0;
                        }),
                        backgroundColor: getRandomColor(),
                        borderColor: getRandomColor(),
                        borderWidth: 1,
                        fill: false,
                    };
                });

                const chartData = {
                    labels: months,
                    datasets: datasets,
                };

                const ctx = document.getElementById('buyerChart');

                if (!ctx) {
                    console.error('Canvas element not found.');
                    return;
                }

                if (chart) {
                    chart.destroy();
                }

                chart = new Chart(ctx.getContext('2d'), {
                    type: 'bar',
                    data: chartData,
                    options: {
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'month',
                                    displayFormats: {
                                        month: 'MMM YYYY',
                                    },
                                },
                                title: {
                                    display: true,
                                    text: 'Month',
                                },
                            },
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'Total Spending',
                                },
                                ticks: {
                                    callback: function (value) {
                                        return '$' + value.toFixed(2);
                                    },
                                },
                            },
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14,
                                    },
                                },
                            },
                            tooltip: {
                                callbacks: {
                                    label: function (context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        if (context.parsed.y !== null) {
                                            label += '$' + context.parsed.y.toFixed(2);
                                        }
                                        return label;
                                    },
                                },
                            },
                        },
                    },
                });
            })
            .catch(error => {
                console.error('Error fetching buyer monthly trend:', error);
            });
    }

    // Initial render with default data
    fetchDataAndRenderChart();

    // Event listeners for the filter buttons
    document.querySelectorAll('.buyer-filter').forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            fetchDataAndRenderChart(filter);
        });
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color + '80'; // Adding 80 for 50% opacity
}
