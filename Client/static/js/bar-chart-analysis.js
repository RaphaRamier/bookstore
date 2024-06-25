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

                // Agrupar os dados por dia e gênero
                const groupedData = {};
                filteredData.forEach(entry => {
                    const month = entry.month;
                    const genre = entry.genre;

                    if (!groupedData[genre]) {
                        groupedData[genre] = {};
                    }
                    if (!groupedData[genre][month]) {
                        groupedData[genre][month] = 0;
                    }
                    groupedData[genre][month] += entry.total_quantity;
                });

                // Ordenar os dias para garantir a ordenação correta no gráfico
                const months = Array.from(new Set(filteredData.map(entry => entry.month))).sort();

                const datasets = Object.keys(groupedData).map(genre => {
                    return {
                        label: genre,
                        backgroundColor: getRandomColor(), // Cor aleatória para o conjunto de dados
                        borderColor: getRandomColor(),
                        borderWidth: 1,
                        data: months.map(month => groupedData[genre][month] || 0),
                        fill: false // Para evitar preenchimento abaixo da linha
                    };
                });

                const chartData = {
                    labels: months,
                    datasets: datasets
                };

                const ctx = document.getElementById('barChart').getContext('2d');

                if (chart) {
                    chart.destroy(); // Destruir a instância anterior do gráfico, se existir
                }

                chart = new Chart(ctx, {
                    type: 'line',
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
