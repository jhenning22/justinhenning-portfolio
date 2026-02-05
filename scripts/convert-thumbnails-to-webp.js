#!/usr/bin/env node

/**
 * Convert all JPG thumbnails to WebP format
 * Maintains original quality while achieving 30-50% file size reduction
 */

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const THUMBNAILS_DIR = path.join(__dirname, '../src/media/thumbnails');

async function convertToWebP(inputPath, outputPath) {
  try {
    const stats = fs.statSync(inputPath);
    const originalSize = stats.size;

    await sharp(inputPath)
      .webp({ quality: 85 }) // High quality WebP
      .toFile(outputPath);

    const newStats = fs.statSync(outputPath);
    const newSize = newStats.size;
    const savings = ((originalSize - newSize) / originalSize * 100).toFixed(1);

    console.log(`✓ ${path.basename(inputPath)} → ${path.basename(outputPath)}`);
    console.log(`  ${(originalSize / 1024).toFixed(0)}KB → ${(newSize / 1024).toFixed(0)}KB (${savings}% smaller)`);

    return { originalSize, newSize };
  } catch (error) {
    console.error(`✗ Error converting ${inputPath}:`, error.message);
    return null;
  }
}

async function main() {
  console.log('Converting thumbnails to WebP format...\n');

  // Get all JPG files in thumbnails directory
  const files = fs.readdirSync(THUMBNAILS_DIR)
    .filter(file => file.match(/\.(jpg|jpeg)$/i))
    .sort();

  if (files.length === 0) {
    console.log('No JPG files found in', THUMBNAILS_DIR);
    return;
  }

  console.log(`Found ${files.length} JPG files to convert\n`);

  let totalOriginal = 0;
  let totalNew = 0;
  let successCount = 0;

  // Convert each file
  for (const file of files) {
    const inputPath = path.join(THUMBNAILS_DIR, file);
    const outputPath = path.join(THUMBNAILS_DIR, file.replace(/\.(jpg|jpeg)$/i, '.webp'));

    const result = await convertToWebP(inputPath, outputPath);

    if (result) {
      totalOriginal += result.originalSize;
      totalNew += result.newSize;
      successCount++;
    }

    console.log(''); // Empty line between files
  }

  // Summary
  console.log('='.repeat(50));
  console.log('CONVERSION COMPLETE');
  console.log('='.repeat(50));
  console.log(`Files converted: ${successCount}/${files.length}`);
  console.log(`Total size: ${(totalOriginal / 1024 / 1024).toFixed(1)}MB → ${(totalNew / 1024 / 1024).toFixed(1)}MB`);
  console.log(`Total savings: ${((totalOriginal - totalNew) / totalOriginal * 100).toFixed(1)}% (${((totalOriginal - totalNew) / 1024 / 1024).toFixed(1)}MB)`);
  console.log('='.repeat(50));
}

main().catch(console.error);
