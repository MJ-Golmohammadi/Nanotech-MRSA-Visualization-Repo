library(readr)
library(dplyr)
library(ggplot2)
library(RColorBrewer)
library(cowplot)

# --- Reading the file with semicolon delimiter
df <- read_delim("journal_metrics.csv", 
                 delim = ";",
                 locale = locale(decimal_mark = ".", grouping_mark = ""),
                 show_col_types = FALSE)

# --- Converting columns to numeric
df <- df %>%
  mutate(
    across(c(`IF(2023)`, Cites, Articles), as.character),
    `IF(2023)` = as.numeric(gsub(",", ".", `IF(2023)`)),
    Cites = as.numeric(gsub(",", ".", Cites)),
    Articles = as.numeric(gsub(",", ".", Articles))
  )

# --- Sorting: first by Articles (ascending), then by Cites (ascending) if ties
df <- df %>%
  arrange(Articles, Cites) %>%
  mutate(Journal = factor(Journal, levels = unique(Journal)))

# --- Displaying sorted data
print("Sorted data:")
print(df %>% select(Journal, Articles, Cites, `IF(2023)`))

# --- Plot A: Bubble Size = Cites, Fill = Articles
p1 <- ggplot(df, aes(x = `IF(2023)`, y = Journal)) +
  geom_vline(xintercept = seq(4, 14, by = 2), color = "gray90", linewidth = 0.3) +
  geom_point(aes(size = Cites, fill = Articles),
             shape = 21, color = "black", stroke = 0.5, alpha = 0.9) +
  scale_fill_gradientn(
    colours = colorRampPalette(c("#2c7bb6", "#ffffbf", "#d7191c"))(100),
    limits = c(min(df$Articles), max(df$Articles)),
    name = "Articles",
    guide = guide_colorbar(
      order = 2,  # lower position
      direction = "vertical",
      title.position = "top",
      barheight = unit(2.5, "cm")
    )
  ) +
  scale_radius(  # modification here
    range = c(2, 10),  # smaller values
    limits = c(min(df$Cites), max(df$Cites)),
    breaks = c(500, 1000, 1500, 2000),
    name = "Cites"
  ) +
  scale_size_continuous(
    range = c(4, 22),
    limits = c(min(df$Cites), max(df$Cites)),
    breaks = c(500, 1000, 1500, 2000),
    name = "Cites",
    guide = guide_legend(
      order = 1,  # upper position
      direction = "vertical",
      title.position = "top",
      override.aes = list(fill = "gray70")
    )
  ) +
  scale_x_continuous(
    limits = c(3, 14),
    breaks = seq(3, 14, by = 1),
    expand = c(0, 0)
  ) +
  theme_minimal(base_size = 14) +
  labs(
    title = "Bubble Size: Cites | Fill: Articles",
    x = "Impact Factor (2023)",
    y = NULL
  ) +
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
    axis.text.y = element_text(size = 14, color = "black"),
    axis.text.x = element_text(size = 14, color = "black"),
    axis.title.x = element_text(size = 16, face = "bold", margin = margin(t = 10)),
    panel.grid.major.x = element_line(color = "gray95", linewidth = 0.5),
    panel.grid.minor.x = element_blank(),
    panel.grid.major.y = element_line(color = "gray95", linewidth = 0.5),
    panel.grid.minor.y = element_blank(),
    panel.border = element_rect(fill = NA, color = "gray80", linewidth = 0.5),
    plot.margin = margin(20, 20, 20, 20),
    legend.position = "right",
    legend.box = "vertical",
    legend.spacing = unit(0.5, "cm")
  )

# --- Plot B: Bubble Size = Articles, Fill = Cites
p2 <- ggplot(df, aes(x = `IF(2023)`, y = Journal)) +
  geom_vline(xintercept = seq(4, 14, by = 2), color = "gray90", linewidth = 0.3) +
  geom_point(aes(size = Articles, fill = Cites),
             shape = 21, color = "black", stroke = 0.5, alpha = 0.9) +
  scale_fill_gradientn(
    colours = colorRampPalette(c("#2c7bb6", "#ffffbf", "#d7191c"))(100),
    limits = c(min(df$Cites), max(df$Cites)),
    name = "Cites",
    guide = guide_colorbar(
      order = 2,  # lower position
      direction = "vertical",
      title.position = "top",
      barheight = unit(2.5, "cm")
    )
  ) +
  scale_radius(  # modification here
    range = c(2, 10),
    limits = c(min(df$Articles), max(df$Articles)),
    breaks = seq(30, 60, by = 10),
    name = "Articles"
  ) +
  scale_size_continuous(
    range = c(4, 22),
    limits = c(min(df$Articles), max(df$Articles)),
    breaks = seq(30, 60, by = 10),
    name = "Articles",
    guide = guide_legend(
      order = 1,  # upper position
      direction = "vertical",
      title.position = "top",
      override.aes = list(fill = "gray70")
    )
  ) +
  scale_x_continuous(
    limits = c(3, 14),
    breaks = seq(3, 14, by = 1),
    expand = c(0, 0)
  ) +
  theme_minimal(base_size = 14) +
  labs(
    title = "Bubble Size: Articles | Fill: Cites",
    x = "Impact Factor (2023)",
    y = NULL
  ) +
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
    axis.text.y = element_blank(),  # remove y-axis labels in second plot
    axis.text.x = element_text(size = 14, color = "black"),
    axis.title.x = element_text(size = 16, face = "bold", margin = margin(t = 10)),
    panel.grid.major.x = element_line(color = "gray95", linewidth = 0.5),
    panel.grid.minor.x = element_blank(),
    panel.grid.major.y = element_line(color = "gray95", linewidth = 0.5),
    panel.grid.minor.y = element_blank(),
    panel.border = element_rect(fill = NA, color = "gray80", linewidth = 0.5),
    plot.margin = margin(20, 20, 20, 20),
    legend.position = "right",
    legend.box = "vertical",
    legend.spacing = unit(0.5, "cm")
  )

# --- Combining plots with spacing and large labels
final_plot <- plot_grid(p1, p2, 
                        labels = c("A", "B"),
                        label_size = 28,
                        label_fontface = "bold",
                        ncol = 2,
                        rel_widths = c(1.1, 0.65),  # spacing between plots
                        align = "h",
                        axis = "tb")

print(final_plot)

# --- Saving plot with high quality
ggsave("ISI_bubble_charts_final_v2.tiff",
       plot = final_plot,
       width = 20,
       height = 10,
       dpi = 600,
       device = "tiff",  # change device to tiff
       bg = "white",
       compression = "lzw")  # compression to reduce file size
