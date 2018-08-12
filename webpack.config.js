const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');


module.exports = {
    // mode: 'development',
    entry: path.join(__dirname, '/chronos_watch/client/scripts/main.ts'),
    output: {
        filename: 'main.js',
        path: path.join(__dirname, '/chronos_watch/client/assets')
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.tsx?$/,
                loader: 'ts-loader',
                exclude: /node_modules/,
                options: {
                    appendTsSuffixTo: [/\.vue$/]
                }
            },
            {
                test: /\.sass$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    {
                        loader: 'sass-loader',
                        options: {
                            indentedSyntax: false
                        }
                    }
                ]
            }
        ]
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js', '.vue'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};
