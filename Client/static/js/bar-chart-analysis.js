document.addEventListener('DOMContentLoaded', function() {
    let chart; // Para armazenar a instância do Chart.js

    function fetchDataAndRenderChart(genreFilter = 'All') {
        fetch('/API/sales/monthly-trend/')  // Endpoint da sua view Django
            .then(response => response.json())
            .then(data => {
                let filteredData = data.genres_trend;

                // Filtrar os dados se um gênero específico for selecionado
                if (genreFilter !== 'All') {
                    filteredData = data.genres_trend.filter(entry => entry.genre === genreFilter);
                }

                // Agrupar os dados por mês para o gráfico de barras
                const groupedData = {};
                filteredData.forEach(entry => {
                    if (!groupedData[entry.month]) {
                        groupedData[entry.month] = 0;
                    }
                    groupedData[entry.month] += entry.total_value;
                });

                // Ordenar as chaves de mês para garantir a ordenação correta no gráfico
                const months = Object.keys(groupedData).sort();

                const chartData = {
                    labels: months,
                    datasets: [{
                        label: genreFilter === 'All' ? 'Total Value by Genre' : `Total Value for ${genreFilter}`,
                        backgroundColor: getRandomColor(), // Cor aleatória para o conjunto de dados
                        borderColor: '#333',
                        borderWidth: 1,
                        data: months.map(month => groupedData[month])
                    }]
                };

                const ctx = document.getElementById('barChart').getContext('2d');

                if (chart) {
                    chart.destroy(); // Destruir a instância anterior do gráfico, se existir
                }

                chart = new Chart(ctx, {
                    type: 'bar',
                    data: chartData,
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'Total Value'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Month'
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
                            }
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Erro ao buscar os dados:', error);
            });
    }

    // Função para obter cores aleatórias
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color + '80'; // Opacidade 50% (80 em hexa)
    }

    // Renderização inicial do gráfico com todos os gêneros
    fetchDataAndRenderChart();

    // Adicionar listeners de eventos para os botões de filtro de gênero
    document.querySelectorAll('.genre-filter').forEach(button => {
        button.addEventListener('click', function() {
            const genreFilter = this.getAttribute('data-filter');
            fetchDataAndRenderChart(genreFilter);
        });
    });
});
