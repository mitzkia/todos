var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    mode: 'development',
    context: __dirname,
    entry: ['babel-polyfill', './static/js/index.js'], // entry point of our app
    output: {
        path: path.resolve('./static/bundles/'),
        filename: "bundle.js"
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015', 'stage-2']
                },
            },  // to transform JSX into JS
            {
                test:/\.css$/,
                use:['style-loader','css-loader'],
            },
            {
                test: /\.(png|svg|gif|jpg|jpeg)$/,
                loaders: [ 'url-loader' ]
            },
            {
                test: /\.scss$/,
                use: ['raw-loader', 'sass-loader']
            },
            {
                test: /\.less$/,
                use: ["style-loader", "css-loader", "less-loader"]
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    }
}
