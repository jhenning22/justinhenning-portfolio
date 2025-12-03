#!/bin/bash

SOURCE_DIR="$HOME/Documents/website-source-videos"
PREVIEW_DIR="$(dirname "$0")/media/previews"

cd "$SOURCE_DIR"

echo "Creating high-quality preview clips with auto-crop..."
echo ""

for video in *.{mp4,mov}; do
  if [ -f "$video" ]; then
    output_name="${video%.*}.mp4"
    echo "Processing: $video -> $output_name"

    # Step 1: Detect black bars (run for 5 seconds to get accurate detection)
    echo "  → Detecting black bars..."
    crop_params=$(/opt/homebrew/bin/ffmpeg -i "$video" -t 5 -vf cropdetect=24:16:0 -f null - 2>&1 | \
      grep -o 'crop=[0-9:]*' | tail -1)

    if [ -z "$crop_params" ]; then
      # No crop detected, use full frame
      crop_params="crop=iw:ih:0:0"
      echo "  → No black bars detected, using full frame"
    else
      echo "  → Black bars detected, applying: $crop_params"
    fi

    # Step 2: Create preview with crop and high quality settings
    echo "  → Encoding preview (1280px, CRF 23, slower preset)..."
    /opt/homebrew/bin/ffmpeg -i "$video" -t 5 \
      -vf "$crop_params,scale=1280:-2" \
      -c:v libx264 -preset slower -crf 23 \
      -an \
      "$PREVIEW_DIR/$output_name" -y 2>&1 | grep -E "(Duration|kb/s|time=)"

    # Show file size
    file_size=$(ls -lh "$PREVIEW_DIR/$output_name" | awk '{print $5}')
    echo "✓ Created preview for $video ($file_size)"
    echo ""
  fi
done

echo "All preview clips created!"
echo ""
echo "Preview folder contents:"
ls -lh "$PREVIEW_DIR"
echo ""
echo "Total preview folder size:"
du -sh "$PREVIEW_DIR"
