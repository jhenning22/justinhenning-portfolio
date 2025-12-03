module.exports = function(eleventyConfig) {
  // Copy media files as-is (previews, thumbnails, photography images)
  eleventyConfig.addPassthroughCopy("src/media");

  // Copy stylesheets
  eleventyConfig.addPassthroughCopy("src/style.css");
  eleventyConfig.addPassthroughCopy("src/photography-style.css");

  // Copy JavaScript
  eleventyConfig.addPassthroughCopy("src/script.js");
  eleventyConfig.addPassthroughCopy("src/work-script.js");

  // Copy fonts
  eleventyConfig.addPassthroughCopy("src/fonts");

  // Copy other assets
  eleventyConfig.addPassthroughCopy("src/create_previews.sh");

  // Configure 11ty
  return {
    dir: {
      input: "src",           // Source files
      output: "_site",        // Built files
      includes: "_includes",  // Templates and components
      data: "_data"          // JSON data files
    },
    templateFormats: ["njk", "html", "md"],
    htmlTemplateEngine: "njk",  // Use Nunjucks for HTML processing
    markdownTemplateEngine: "njk"
  };
};
