# -----
# Show effect of filter on an image and their pixel values. 

library("rstudioapi") 
library(reshape2)
library(ggplot2) 
# -----
# Change it

setwd(dirname(getSourceEditorContext()$path))
dir.create('tmp')
figdir <- file.path(getwd(), 'tmp')

dataset <- read.csv('morpho_filter_blob.txt', sep = '\t', header = F)
dataset_dilate <- read.csv('morpho_filter_blob_dilate.txt', sep = '\t', header = F)
dataset_erode <- read.csv('morpho_filter_blob_erode.txt', sep = '\t', header = F)
dataset.width = 9
dataset.idx_start = 2
dataset.idx_end = min(dataset.width + (dataset.idx_start -1), dim(dataset)[1])
dataset.width = dataset.idx_end - dataset.idx_start + 1

wrap_dataset <- function (datain, width, idxs ) {
  datain <- as.matrix(datain)
  datain <- datain[idxs[1]:idxs[2],
                   idxs[1]:idxs[2]] 
  colnames(datain) <- seq(1,dim(datain)[1])-0.5
  rownames(datain) <- seq(1,dim(datain)[2])+0.5
  dataout <- melt(datain)
  colnames(dataout) <- c("x", "y", "value") 
  dataout$value[dataout$value < 255] <- 0
  dataout$value[dataout$value >= 255] <- 1
  return(dataout)
} 

vecDataset <- wrap_dataset(datain = dataset, width = dataset.width, idxs = c(dataset.idx_start, dataset.idx_end))
vecDataset_dilate <- wrap_dataset(datain = dataset_dilate, width = dataset.width, idxs = c(dataset.idx_start, dataset.idx_end))
vecDataset_erode <- wrap_dataset(datain = dataset_erode, width = dataset.width, idxs = c(dataset.idx_start, dataset.idx_end))

# Make binary 
# ---- Do some reformatting on the dataset -----



# ----
#' img_filter
#' Show a matrix with numbers and position of filter (3x3)
#' 
#' @param vector vectorized matrix wher 
#' @param width_matrix width of pixel matrix
#' @param pos_filter position of filter base 0, c(xpos, ypos)
#'
#' @return graph object
#' @export
#'
#' @examples
img_filter <- function(vector, vector2, width_matrix, pos_filter, color) {
  p <- ggplot(data =(vector), aes(x = y, y = -x))
  p <- p + geom_raster(aes(fill = factor(vector2$value)))
  p <- p + theme_void() + theme(legend.position = "none")

  p <- p + geom_text(aes(label = value), colour = "black")
  p <- p + geom_vline(xintercept = seq(1, width_matrix, 1), color="black", size=1) 
  p <- p + geom_hline(yintercept = -seq(1, width_matrix, 1), color="black", size=1) 
  p <- p + coord_fixed(xlim = c(0.4, width_matrix - 0.4), 
                       ylim = c(- width_matrix - 0.5, -1.4))
  p <- p + theme(axis.title = element_blank(), 
                 axis.text = element_blank(),
                 legend.position = "none",
                 panel.border = element_rect(line = "solid", fill = NA, size = 2))
  p <- p + annotate("rect", xmin = -1 + pos_filter[1], xmax= 2 + pos_filter[1], 
                    ymin = 0 - pos_filter[2], ymax = -3 - pos_filter[2],   fill = color, alpha = 0.3)
  p <- p + scale_fill_manual(values = c("0" = "white", "1" = color, "2" = "gray"))
  
  return(p) 
}


# ----- erosion example ----

p <- img_filter(vector = vecDataset, vector2 = vecDataset + vecDataset,  
                width_matrix = dataset.width, pos_filter =  c(2,3), color = "red")

p1 <- p

p <- img_filter(vector = vecDataset_erode, vector2 = vecDataset_erode + vecDataset,  
                width_matrix = dataset.width, pos_filter =  c(-2,-2), color = "red")

p2 <- p


p_erode <- cowplot::plot_grid(p1, NULL, p2, ncol = 3, rel_widths = c(1, 0.2, 1))



# ----- dilation example ----
p <- img_filter(vector = vecDataset, vector2 = vecDataset + vecDataset,  
                width_matrix = dataset.width, pos_filter =  c(1,2), color = "green2")

p1 <- p

p <- img_filter(vector = vecDataset_dilate, vector2 = vecDataset_dilate + vecDataset,  
                width_matrix = dataset.width, pos_filter =  c(-2,-2), color = "green2")

p2 <- p

p_dilate <- cowplot::plot_grid(p1, NULL, p2, ncol = 3, rel_widths = c(1, 0.2, 1))


ggsave(plot = p_erode, file = "./tmp/morphological_erode.png", width = 12, height = 12, device = "png", unit = "cm")
ggsave(plot = p_dilate, file = "./tmp/morphological_dilate.png", width = 12, height = 12, device = "png", unit = "cm")