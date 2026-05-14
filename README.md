### `bubble_plot_merge.R`

An R script that generates two publication‑ready bubble charts (A and B) from journal metrics.

**Input:** `journal_metrics.csv` (semicolon‑separated) with columns:
- `Journal` – journal name
- `IF(2023)` – Impact Factor
- `Cites` – total citations
- `Articles` – number of articles

**Output:** `ISI_bubble_charts_final_v2.tiff` (600 DPI, LZW compression)

**What it does:**
1. Reads and sorts data (by `Articles`, then `Cites`)
2. Creates two plots:
   - **Plot A:** Bubble size = Citations, fill color = Articles
   - **Plot B:** Bubble size = Articles, fill color = Citations
3. Combines them into a single TIFF figure with labels A/B


### `publication_figure_merge.py`

A Python script that merges two scientific images into a single publication‑ready figure with professional panel labels.

**Input:** two image files (e.g., TIFF, JPEG, PNG)

**Output:** merged TIFF file (600 DPI, LZW compression)

**What it does:**
1. Resizes both images to the same height (maintaining aspect ratio)
2. Places them side by side with adjustable spacing
3. Adds bold **A** and **B** labels with shadow/outline for clarity
4. Saves the result as a high‑resolution TIFF

**Two methods included:**
- `merge_images_professional()` – auto‑scales font and spacing
- `merge_images_simple_fixed()` – uses fixed height and very large labels
