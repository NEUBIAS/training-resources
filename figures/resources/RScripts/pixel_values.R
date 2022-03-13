# Show effect of filter on an image and their pixel values. 



library(reshape2)
library(ggplot2)

# Change it
# setwd('/Users/apoliti/ownCloud/Teaching/Fundamentals_in_Imaging2/Slidematerial/')
dataset <- read.csv('pixel_values_associatedtoRfile.txt', sep = '\t', header = F)

dataset <- as.matrix(dataset)
dataset <- dataset[1:9,1:9]
# ----
colnames(dataset) <- seq(1,dim(dataset)[1])-0.5
rownames(dataset) <- seq(1,dim(dataset)[2])+0.5

# ----
vecDataset <- melt(dataset)

dimM <- 9
idx <- 1
pos <- 1
p <- ggplot(data = vecDataset, aes(x = Var2, y = -Var1))
#p <- p + geom_raster(aes())
p <- p + theme_void() + theme(legend.position = "none")
#p <- p + scale_fill_gradient(low = "black", high = "white", limits = c(0,110) )
p <- p + geom_text(aes(label = value), colour = "black")
p <- p + geom_vline(xintercept = seq(1,dimM,1), color="black", size=1) 
p <- p + geom_hline(yintercept = -seq(1,dimM,1), color="black", size=1) 
p <- p + coord_fixed(xlim = c(0.4, dimM-1.4), ylim = c(-dimM+0.4, -1.4))
p <- p + theme(axis.title = element_blank(), 
               axis.text = element_blank(),
               legend.position = "none",
               panel.border = element_rect(line = "solid", fill = NA, size = 2))
p <- p + annotate("rect", xmin=0+pos, xmax=3+pos, ymin=-1, ymax=-4,   fill = "green2", alpha = 0.3)

p

ggsave(plot = p, file = paste0("pixel_values_filter_", pos, ".png"), width = 3, height = 3, device = "png")


# ----
dimM <- 9
idx <- 1
pos <- 1
vecDataset <- melt(dataset)
vecDataset$value <- NA
vecDataset$value[11] <- round(mean(dataset[1:3, 1:3]))
if (pos == 1) vecDataset$value[20] <- round(mean(dataset[1:3, 2:4]))
p <- ggplot(data = vecDataset, aes(x = Var2, y = -Var1))
#p <- p + geom_raster(aes())
p <- p + theme_void() + theme(legend.position = "none")
#p <- p + scale_fill_gradient(low = "black", high = "white", limits = c(0,110) )
p <- p + geom_text(aes(label = value), colour = "black")
p <- p + geom_vline(xintercept = seq(1,dimM,1), color="black", size=1) 
p <- p + geom_hline(yintercept = -seq(1,dimM,1), color="black", size=1) 
p <- p + coord_fixed(xlim = c(0.4, dimM-1.4), ylim = c(-dimM+0.4, -1.4))
p <- p + theme(axis.title = element_blank(), 
               axis.text = element_blank(),
               legend.position = "none",
               panel.border = element_rect(line = "solid", fill = NA, size = 2))
p <- p + annotate("rect", xmin=1+pos, xmax=2+pos, ymin=-2, ymax=-3,   fill = "darkgreen", alpha = 0.5)
p
ggsave(plot = p, file = paste0("pixel_values_mean_", pos, ".png"), width = 3, height = 3, device = "png")
