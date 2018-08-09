const path = require('path');

module.exports = {
    entry: path.join(__dirname, '/chronos_watch/client/typescript/main.ts'),
    output: {
        filename: 'main.js',
        path: path.join(__dirname, '/chronos_watch/client/assets')
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                loader: 'ts-loader',
                exclude: /node_modules/,
            },
        ]
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    }
};