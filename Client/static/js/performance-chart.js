document.addEventListener('DOMContentLoaded', function () {
    let chart; // Para armazenar a instância do Chart.js

    function fetchDataAndRenderChart() {
        fetch('/API/cashflow/performance-data/')  // Endpoint da sua view Django
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Verificar a resposta da API

                const chartData = {
                    labels: data.dates,
                    datasets: [
                        {
                            label: 'Revenue',
                            data: data.revenues,
                            borderColor: '#8957ff',
                            backgroundColor: 'rgba(137, 87, 255, 0.1)',
                            borderWidth: 1,
                            fill: true,
                            tension: 0.4,
                            pointBackgroundColor: '#8957ff',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: '#8957ff'
                        },
                        {
                            label: 'Expenses',
                            data: data.expenses,
                            borderColor: '#00cc88',
                            backgroundColor: 'rgba(0, 204, 136, 0.1)',
                            borderWidth: 1,
                            fill: true,
                            tension: 0.4,
                            pointBackgroundColor: '#00cc88',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: '#00cc88'
                        }
                    ]
                };

                const ctx = document.getElementById('performanceChart').getContext('2d');

                if (chart) {
                    chart.destroy(); // Destruir a instância anterior do gráfico, se existir
                }

                chart = new Chart(ctx, {
                    type: 'line',
                    data: chartData,
                    options: {
                        responsive: true,
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'month'
                                },
                                title: {
                                    display: true,
                                    text: 'Month'
                                }
                            },
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'Amount'
                                },
                                ticks: {
                                    callback: function (value) {
                                        return '$' + value.toFixed(2);
                                    }
                                }
                            }
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14
                                    }
                                }
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
                                    }
                                }
                            }
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Erro ao buscar os dados:', error);
            });
    }

    // Renderização inicial do gráfico
    fetchDataAndRenderChart();
});
