const path = require('path');

module.exports = {
    entry: {
        main: './Client/static/js/main.js',       // Caminho para o seu arquivo main.js
        switcher: './Client/static/js/switcher.js' // Caminho para o seu arquivo switcher.js
    },
    output: {
        path: path.resolve(__dirname, './Client/static/js/'),  // Diretório de saída para os arquivos compilados
        filename: '[name].bundle.js',       // Nome dos arquivos de saída, [name] será substituído por 'main' ou 'switcher'
        sourceMapFilename: '[file].map'    // Nome dos arquivos de mapeamento
    },
    devtool: 'source-map'  // Configuração para gerar source maps
};
