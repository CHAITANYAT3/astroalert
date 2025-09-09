module.exports = {
  plugins: [
    {
      plugin: require("craco-cesium")(),
    },
  ],
  webpack: {
    configure: (webpackConfig) => {
      // Ensure html-webpack-plugin is before html-webpack-tags-plugin
      const HtmlWebpackPlugin = webpackConfig.plugins.find(
        (plugin) => plugin.constructor.name === "HtmlWebpackPlugin"
      );
      if (HtmlWebpackPlugin) {
        webpackConfig.plugins = webpackConfig.plugins.filter(
          (plugin) => plugin.constructor.name !== "HtmlWebpackTagsPlugin"
        );
      }
      return webpackConfig;
    },
  },
};
