const Image = require("@11ty/eleventy-img");
const path = require("path");
const htmlmin = require("html-minifier-terser");

module.exports = function(eleventyConfig) {

  // HTML minification transform
  eleventyConfig.addTransform("htmlmin", function(content, outputPath) {
    if (outputPath && outputPath.endsWith(".html")) {
      return htmlmin.minify(content, {
        collapseWhitespace: true,
        removeComments: true,
        minifyCSS: true,
        minifyJS: true
      });
    }
    return content;
  });

  // Image shortcode for responsive images with srcset
  eleventyConfig.addNunjucksAsyncShortcode("responsiveImage", async function(src, alt, sizes = "100vw", widths = [320, 640, 1280, 2560], className = "") {
    // Resolve the image path
    let inputPath = path.join(__dirname, "src", src);

    // Generate images in multiple formats and sizes
    let metadata = await Image(inputPath, {
      widths: widths,
      formats: ["avif", "webp", "jpeg"],
      outputDir: "./_site/media/optimized/",
      urlPath: "/media/optimized/",
      filenameFormat: function (id, src, width, format) {
        const extension = path.extname(src);
        const name = path.basename(src, extension);
        return `${name}-${width}w.${format}`;
      }
    });

    // Generate HTML with picture element
    let imageAttributes = {
      alt,
      sizes,
      loading: "lazy",
      decoding: "async",
      class: className
    };

    return Image.generateHTML(metadata, imageAttributes);
  });

  // Simple image shortcode for thumbnails (background-image style)
  eleventyConfig.addNunjucksAsyncShortcode("optimizedImage", async function(src, width = 1280) {
    let inputPath = path.join(__dirname, "src", src);

    let metadata = await Image(inputPath, {
      widths: [width],
      formats: ["webp", "jpeg"],
      outputDir: "./_site/media/optimized/",
      urlPath: "/media/optimized/"
    });

    // Return just the webp URL for background-image use
    return metadata.webp[0].url;
  });

  // Social preview image generator (1200x630)
  eleventyConfig.addNunjucksAsyncShortcode("socialImage", async function(src) {
    let inputPath = path.join(__dirname, "src", src);

    let metadata = await Image(inputPath, {
      widths: [1200],
      formats: ["jpeg"],
      outputDir: "./_site/media/social-previews/",
      urlPath: "/media/social-previews/",
      sharpJpegOptions: {
        quality: 85
      }
    });

    return metadata.jpeg[0].url;
  });

  // Copy media files as-is (previews, videos, social-previews)
  // Photography and thumbnail images will be processed by Image plugin
  eleventyConfig.addPassthroughCopy("src/media/previews");
  eleventyConfig.addPassthroughCopy("src/media/posters");
  eleventyConfig.addPassthroughCopy("src/media/social-previews");
  eleventyConfig.addPassthroughCopy("src/media/gallery");
  eleventyConfig.addPassthroughCopy("src/media/thumbnails");

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
