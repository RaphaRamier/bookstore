// Defina os dados para janeiro a dezembro
var dados = [65, 59, 80, 81, 56, 55, 40, 60, 55, 30, 25, 40];

// Obtenha o elemento canvas e seu contexto
var ctx = document.getElementById('myBarChart').getContext('2d');

// Crie o gráfico de barras
var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        datasets: [{
            label: 'Vendas por Mês',
            data: dados,
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
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