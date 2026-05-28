#!/bin/bash
# Script to convert Mermaid diagrams to PNG images
# Run from the repo root: bash docs/mermaid/convert.sh

MMDC="/home/runner/work/_temp/ghcca-node/node/bin/mmdc"
MERMAID_DIR="docs/mermaid"
IMAGES_DIR="docs/pan-paper-template/images"

mkdir -p "$IMAGES_DIR"

echo "Converting radar_architecture.mmd ..."
$MMDC -i "$MERMAID_DIR/radar_architecture.mmd" \
      -o "$IMAGES_DIR/radar_architecture.png" \
      -w 1400 -H 900 \
      --backgroundColor white \
      --puppeteerConfigFile "$MERMAID_DIR/puppeteer-config.json"

echo "Converting data_pipeline.mmd ..."
$MMDC -i "$MERMAID_DIR/data_pipeline.mmd" \
      -o "$IMAGES_DIR/data_pipeline.png" \
      -w 1600 -H 800 \
      --backgroundColor white \
      --puppeteerConfigFile "$MERMAID_DIR/puppeteer-config.json"

echo "Done. Images written to $IMAGES_DIR"
