const path = require('path');
const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  webpack: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
    plugins: {
      add: [
        new CopyWebpackPlugin({
          patterns: [
            {
              from: 'node_modules/cesium/Build/Cesium',
              to: 'cesium'
            }
          ]
        }),
        new webpack.DefinePlugin({
          CESIUM_BASE_URL: JSON.stringify('/cesium')
        })
      ]
    },
    configure: (webpackConfig) => {
      webpackConfig.module.rules.push({
        test: /\.js$/,
        enforce: 'pre',
        include: path.resolve(__dirname, 'node_modules/cesium'),
        use: [{
          loader: 'strip-pragma-loader',
          options: {
            pragmas: {
              debug: false
            }
          }
        }]
      });
      webpackConfig.resolve.fallback = {
        ...webpackConfig.resolve.fallback,
        https: require.resolve('https-browserify'),
        http: require.resolve('stream-http'),
        url: require.resolve('url/'),
        zlib: require.resolve('browserify-zlib'),
        stream: require.resolve('stream-browserify'),
      };
      return webpackConfig;
    }
  }
};
