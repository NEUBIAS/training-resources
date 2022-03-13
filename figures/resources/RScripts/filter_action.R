# Creates different images for showing how filter with different structuring elements act on an image

# ----
library(reshape2)
library(ggplot2)
library(plotly)
library(gganimate)
library(magick)
library(gifski)
# ----
## Change it
#setwd("/Users/apoliti/ownCloud/Teaching/Fundamentals_in_Imaging2/Slidematerial/")

# ----
# a moving 3x3 filter
dimM <- 9
idx <- 1
vecDatasetG <- list()
for (i in seq(1,dimM-3)) {
  
  for (j in seq(1,dimM-3)) {
    
    dataset <- matrix(0, nrow = dimM, ncol=dimM)
    dataset[i:(i+2),j:(j+2)] <- 1
    colnames(dataset) <- seq(1,dim(dataset)[1])
    rownames(dataset) <- seq(1,dim(dataset)[2])
    vecDataset <- melt(dataset)
    vecDataset$Var3 <- idx
    idx <- idx+1
    vecDatasetG <- rbind(vecDatasetG, vecDataset)
  }
}


p <- ggplot(vecDatasetG, aes(x = Var2, y = -Var1))
p <- p + geom_raster(aes(fill = value),  hjust = 0,
                     vjust = 0)
p <- p + transition_states(Var3, transition_length = 0, state_length = 1)
p <- p + geom_vline(xintercept = seq(1,dimM,1), color="black", size=1) 
p <- p + geom_hline(yintercept = -seq(1,dimM,1), color="black", size=1) 
p <- p + theme(axis.title = element_blank(), 
               axis.text = element_blank(),
               legend.position = "none",
               panel.border = element_rect(line = "solid", fill = NA, size = 2))
p <- p + scale_fill_gradient(low = "white", high = "green2", limits = c(0,1) )
#p <- p + coord_cartesian(xlim = c(0.3, dimM-1.25), ylim = c(-dimM+0.25, -1.25))
p <- p + coord_fixed(xlim = c(0.4, dimM-1.4), ylim = c(-dimM+0.4, -1.5))
animate(p, duration = 15, fps = 20, width = 300, height = 300)
animate(p, duration = 15, fps = 20, width = 300, height = 300, renderer = gifski_renderer(loop = FALSE))

anim_save("filter_move.gif")

    
# -----
# a moving convolved image
  dimM <- 9
  idx <- 1
  vecDatasetG <- list()
  dataset <- matrix(0, nrow = dimM, ncol=dimM)
  for (i in seq(1,dimM-3)) {
    for (j in seq(1,dimM-3)) {
      dataset[(i+1):(i+1),(j+1):(j+1)] <- 1
      colnames(dataset) <- seq(1,dim(dataset)[1])
      rownames(dataset) <- seq(1,dim(dataset)[2])
      vecDataset <- melt(dataset)
      vecDataset$Var3 <- idx
      idx <- idx+1
      vecDatasetG <- rbind(vecDatasetG, vecDataset)
    }
  }

p <- ggplot(vecDatasetG, aes(x = Var2, y = -Var1))
p <- p + geom_raster(aes(fill = value),  hjust = 0,
                     vjust = 0)
p <- p + transition_states(Var3, transition_length = 0, state_length = 1)
p <- p + geom_vline(xintercept = seq(1,dimM,1), color="black", size=1) 
p <- p + geom_hline(yintercept = -seq(1,dimM,1), color="black", size=1) 
p <- p + scale_fill_gradient(low = "white", high = "darkgreen", limits = c(0,1) )
p <- p + theme(axis.title = element_blank(), 
               axis.text = element_blank(),
               legend.position = "none",
               panel.border = element_rect(line = "solid", fill = NA, size = 2))
p <- p + coord_fixed(xlim = c(0.4, dimM-1.4), ylim = c(-dimM+0.4, -1.5))
animate(p, duration = 15, fps = 20, width = 300, height = 300)
animate(p, duration = 15, fps = 20, width = 300, height = 300, renderer = gifski_renderer(loop = FALSE))
anim_save("filtered_image.gif", loop = FALSE)    

# ----
# assembly of a synchronous animated gof
  a_gif <- image_read(path = "./filter_move.gif")
  b_gif <- image_read(path = "./filtered_image.gif")
  new_gif <- image_append(c(a_gif[1], b_gif[1]))
    
  for(i in 2:length(a_gif)){
    combined <- image_append(c(a_gif[i], b_gif[i]))
    new_gif <- c(new_gif, combined)
  }
  image_write(new_gif, path = "combined_filter.gif", format = "gif") 
  image_write(new_gif[1], path = "combined_filter01.png", format = "png") 
  image_write(new_gif[2], path = "combined_filter_last.png", format = "png") 
  
  
# ----- 
# different form of filters
  plotgrid <- function (dataset, dimM){
    p <- ggplot(vecDataset, aes(x = Var2, y = -Var1))
    p <- p + geom_raster(aes(fill = value),  hjust = 0,
                         vjust = 0)
    p <- p + geom_vline(xintercept = seq(1,dimM,1), color="black", size=1) 
    p <- p + geom_hline(yintercept = -seq(1,dimM,1), color="black", size=1) 
    p <- p + theme(axis.title = element_blank(), 
                   axis.text = element_blank(),
                   legend.position = "none",
                   panel.border = element_rect(line = "solid", fill = NA, size = 2))
    p <- p + scale_fill_gradient(low = "white", high = "green2", limits = c(0,1) )
    #p <- p + coord_cartesian(xlim = c(0.3, dimM-1.25), ylim = c(-dimM+0.25, -1.25))
    p <- p + coord_fixed(xlim = c(0.4, dimM-1.4), ylim = c(-dimM+0.4, -1.5))
    return(p)
  }  
# ----
  
# squared 3x3
dimM <- 11
idx <- 1
vecDatasetG <- list()
dataset <- matrix(0, nrow = dimM, ncol=dimM)
dataset[1:3,1:3] <- 1
colnames(dataset) <- seq(1,dim(dataset)[1])
rownames(dataset) <- seq(1,dim(dataset)[2])
vecDataset <- melt(dataset)


p <- plotgrid(vecDataset, dimM)
p
ggsave(plot = p, file = "filter_square_3x3.png", width = 3, height = 3, device = "png")
# ---- 
# squared 5x5
dimM <- 11
idx <- 1
vecDatasetG <- list()
dataset <- matrix(0, nrow = dimM, ncol=dimM)
dataset[1:5,1:5] <- 1
colnames(dataset) <- seq(1,dim(dataset)[1])
rownames(dataset) <- seq(1,dim(dataset)[2])
vecDataset <- melt(dataset)


p <- plotgrid(vecDataset, dimM)
p
ggsave(plot = p, file = "filter_square_5x5.png", width = 3, height = 3, device = "png")

# -----
# circle
dataset <- matrix(0, nrow = dimM, ncol=dimM)
dataset[1:7,1:7] <- 1
dataset[1,1:2] <- 0
dataset[1,6:7] <- 0
dataset[2,1] <-0
dataset[2,7] <-0
dataset[6,1] <- 0
dataset[6,7] <- 0
dataset[7,6:7] <- 0

dataset[7,1:2] <- 0

colnames(dataset) <- seq(1,dim(dataset)[1])
rownames(dataset) <- seq(1,dim(dataset)[2])
vecDataset <- melt(dataset)


p <- plotgrid(vecDataset, dimM)
p 
ggsave(plot = p, file = "filter_disk_7x7.png", width = 3, height = 3, device = "png")

# -----
# diamond
dataset <- matrix(0, nrow = dimM, ncol=dimM)
dataset[1:7,1:7] <- 1
dataset[1,1:3] <- 0
dataset[1,5:7] <- 0
dataset[2,1:2] <-0
dataset[2,6:7] <-0
dataset[3,1] <-0
dataset[3,7] <-0
dataset[5,1] <-0
dataset[5,7] <-0
dataset[6,1:2] <-0
dataset[6,6:7] <-0
dataset[7,1:3] <- 0
dataset[7,5:7] <- 0
colnames(dataset) <- seq(1,dim(dataset)[1])
rownames(dataset) <- seq(1,dim(dataset)[2])
vecDataset <- melt(dataset)


p <- plotgrid(vecDataset, dimM)
p 
ggsave(plot = p, file = "filter_diamond_7x7.png", width = 3, height = 3, device = "png")

# -----
# line
dataset <- matrix(0, nrow = dimM, ncol=dimM)
dataset[2,1:7] <- 1

colnames(dataset) <- seq(1,dim(dataset)[1])
rownames(dataset) <- seq(1,dim(dataset)[2])
vecDataset <- melt(dataset)


p <- plotgrid(vecDataset, dimM)
p 
ggsave(plot = p, file = "filter_line_1x7.png", width = 3, height = 3, device = "png")
