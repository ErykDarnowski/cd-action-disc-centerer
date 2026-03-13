# Quick Start Guide

Get your CD-Action Disc Centerer up and running with these simple steps.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

### 1. Open Terminal in Project Directory

```bash
cd /path/to/cd-action-disc-centerer
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages: `opencv-python`, `numpy`, `scipy`, `matplotlib`

## Required Files

Ensure the following files exist before running:

- ✅ `input.jpg` or `input_OG.jpg` - Your CD scan image
- ✅ `template.png` - Template feature to detect on the disc
- ✅ `mask/mask.jpg` - Circular mask for extracting the disc area

## Usage

### Step 1: Crop and Cut Out the Disc

```bash
python 1-crop_n_cut_out.py
```

This creates `circle.png` with the isolated circular disc.

### Step 2: Center and Straighten the Disc

```bash
python 2-center.py --show
```

**Command-line options:**
- `--template <file>` - Specify template image (default: `template.png`)
- `--map <file>` - Specify input image to process (default: `circle.png`)
- `--show` - Display the result in a window
- `--save-dir <path>` - Save output to specified directory

## Output Files

After running Step 2, you'll get:
- `debug.jpg` - Visual debug showing matched features and detected regions
- `output.png` - The rotation-corrected (centered) disc image

## Quick Demo Command

For a quick showcase:

```bash
source venv/bin/activate && python 1-crop_n_cut_out.py && python 2-center.py --show
```

## Troubleshooting

### "No module named cv2"
Ensure you've activated your virtual environment and installed dependencies.

### "File not found" errors
Verify all required files (`input.jpg`, `template.png`, `mask/mask.jpg`) exist in the correct locations.

### No matches detected
- Check that your template image is clear and unrotated
- Try adjusting scan quality of input image
- Verify the disc contains the feature present in your template

## Tips for Showcase

1. Prepare multiple misaligned CD scan examples beforehand
2. Use `--show` flag to demonstrate real-time match detection
3. Show before/after comparison by displaying original vs output.png
