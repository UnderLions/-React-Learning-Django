
// webpack.config.js
const path = require('path');

module.exports = {
  mode: 'production',
  entry: './leadmanager/frontend/src/index.js',
  output: {
    path: path.resolve(__dirname, 'leadmanager/frontend/static/frontend'),
    filename: 'main.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Match JavaScript files
        exclude: /node_modules/, // Exclude node_modules directory
        use: {
          loader: 'babel-loader', // Use Babel for transpilation
        },
      },
    ],
  }
};
