# 📊 Journal Metrics Bubble Charts - Scientific Visualization

A comprehensive project for analyzing and visualizing journal metrics (Impact Factor, Citations, Article Count) using R and Python, designed for scientific publications.


## 🎯 Project Overview

This project provides a complete workflow for:

1. **Scientific Data Visualization**: Creating dual-configuration bubble charts comparing journal Impact Factors, citation counts, and article counts
2. **Publication-Ready Figure Preparation**: Professional image merging and labeling for scientific papers

## 🔧 Features

### R Script Features (`bubble_plot_merge.R`)
- **Dual Visualization**: Two complementary bubble chart configurations
- **Professional Styling**: Publication-ready formatting and color schemes
- **Custom Legends**: Carefully designed legend systems for clear interpretation
- **High-Resolution Output**: TIFF format with LZW compression for journals

### Python Script Features (`publication_figure_merge.py`)
- **Intelligent Merging**: Automatic size normalization and alignment
- **Professional Labeling**: Panel labels (A, B) with optimal sizing and contrast
- **Publication Quality**: High DPI (600) output with lossless compression
- **Cross-Platform Font Handling**: Multiple font fallback strategies

## 📊 Chart Configurations

### Plot A: "Bubble Size: Cites | Fill: Articles"
- **X-axis**: Impact Factor (2023)
- **Y-axis**: Journal names (sorted by Articles then Cites)
- **Bubble Size**: Total citations
- **Bubble Fill**: Number of articles (gradient: blue → yellow → red)

### Plot B: "Bubble Size: Articles | Fill: Cites"
- **X-axis**: Impact Factor (2023)
- **Y-axis**: (hidden for compactness)
- **Bubble Size**: Number of articles
- **Bubble Fill**: Total citations (gradient: blue → yellow → red)

## ⚙️ Requirements

### R Dependencies

library(readr)     # Data import
library(dplyr)     # Data manipulation
library(ggplot2)   # Visualization
library(RColorBrewer) # Color schemes
library(cowplot)   # Plot arrangement
```

### Python Dependencies

Pillow>=9.0.0


## 🚀 Installation & Setup

###Using Conda

# Create and activate environment
conda create -n journal-viz python=3.9 r-base=4.1 r-ggplot2 r-dplyr r-readr
conda activate journal-viz

# Install additional R packages
R -e "install.packages(c('RColorBrewer', 'cowplot'), repos='https://cloud.r-project.org')"

# Install Python dependencies
pip install Pillow


## 📈 Usage Instructions

### Step 1: Prepare Your Data
Ensure your `journal_metrics.csv` file has the following columns:
- `Journal` (character): Journal name
- `IF(2023)` (numeric): Impact Factor 2023
- `Cites` (numeric): Total citations
- `Articles` (numeric): Number of articles

### Step 2: Generate Bubble Charts

# Run the R script
Rscript journal_metrics_analysis.R


This will produce:
- Console output of sorted data
- `ISI_bubble_charts_final_v2.tiff` (combined figure)

### Step 3: Merge Separate Images (Optional)
If you have two separate images to merge:


# Method 1: Professional merging (auto-adjusts)
python image_merger.py

# Method 2: Simple merging with large labels
python -c "from image_merger import merge_images_simple_fixed; merge_images_simple_fixed('image1.tiff', 'image2.tiff', 'merged_figure.tiff')"


## 🎨 Customization Options

### R Script Customization

# Modify color scheme
scale_fill_gradientn(
  colours = colorRampPalette(c("#2c7bb6", "#ffffbf", "#d7191c"))(100),
  # Change colors as needed
)

# Adjust bubble sizes
scale_size_continuous(
  range = c(4, 22),  # Min and max bubble sizes
)

# Change figure dimensions
ggsave("output.tiff", width = 20, height = 10, dpi = 600)


### Python Script Customization

# Adjust spacing between panels
spacing = 80  # Pixels between images

# Change label size
font_size = 150  # Label font size

# Modify output DPI
merged.save(output_path, 'TIFF', dpi=(600, 600))


## 📝 Output Specifications

### Generated Figure
- **Format**: TIFF with LZW compression
- **Resolution**: 600 DPI
- **Dimensions**: ~20×10 inches (variable)
- **Color Space**: RGB
- **File Size**: ~2-10 MB (depending on content)

### Data Output
- Sorted journal list printed to console
- Visual comparison of three key metrics

## 🔍 Interpretation Guide

1. **Bubble Position**: Horizontal position = Impact Factor
2. **Bubble Size**: Represents either Citations or Articles (see plot title)
3. **Bubble Color**: Gradient indicates the third metric
4. **Journal Order**: Sorted by Articles (ascending), then by Citations

## 🐛 Troubleshooting

### Common Issues and Solutions

**Issue**: R packages fail to install

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))


**Issue**: Fonts not found in Python
```python
# Specify font path directly
font = ImageFont.truetype("/path/to/arialbd.ttf", font_size)
```

**Issue**: Image merging misalignment

# Adjust target height
target_height = 2000  # Fixed height for consistency


**Issue**: Low-resolution output

# Increase DPI
merged.save(output_path, 'TIFF', dpi=(1200, 1200))


## 📊 Sample Data Structure

Journal;IF(2023);Cites;Articles
"Nature";12.5;1500;45
"Science";11.8;1400;42
"Cell";9.7;1200;38
"Lancet";8.9;1100;35


## 📚 Citation & Attribution

If you use this code in your research, please consider:

1. Citing the R packages (ggplot2, dplyr, etc.)
2. Acknowledging the visualization methodology
3. Modifying the color scheme for colorblind accessibility if needed

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

This project is available for academic and research use. For commercial applications, please contact the author.

## 🆘 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the R/ggplot2 documentation
3. Open an issue in the GitHub repository

## 📈 Future Enhancements

Planned features:
- [ ] Interactive Shiny application
- [ ] Additional chart types (radar, bar plots)
- [ ] Automated journal categorization
- [ ] Web scraping for real-time data updates
- [ ] Export to multiple formats (PDF, SVG, PNG)

---

**Maintained by**: [Your Name/Institution]  
**Last Updated**: $(date +%Y-%m-%d)  
**Version**: 1.0.0  
**Compatibility**: R 4.1+, Python 3.8+

---

*For scientific visualization and data analysis*

