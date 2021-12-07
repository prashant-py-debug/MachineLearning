library(plotly)
#line plot
data("airmiles")
plot_ly(x = time(airmiles) , y = airmiles , mode = "lines")
#muliple line plot
library(tidyr)
library(dplyr)

data("EuStockMarkets")
stocks <- as.data.frame(EuStockMarkets) %>% 
  gather(index,price) %>% mutate(time = rep(time(EuStockMarkets),4))

plot_ly(stocks , x = stocks$time , y = stocks$price , color = stocks$index , mode =  "lines")

#heatmap
terrain <- matrix(rnorm(100*100),100,100)
plot_ly(z = terrain , type = "heatmap")

#3d heatmap

terrain2 <-matrix(sort(rnorm(100*100)),100,100)
plot_ly(z = terrain2,type = "surface")

#choropleth map

state_pop <- data.frame(State = state.abb ,Pop = as.vector(state.x77[,1]))

state_pop$hover <- with(state_pop, paste(State, "<br>", "population:", Pop))

borders <- list(color = toRGB("red"))

map_options <- list(
  scope = "usa",
  projection = list(type= "albers usa"),
  showlakes = TRUE,
  lakecolor = toRGB("white")
)
plot_ly(state_pop , z = state_pop$Pop , text = state_pop$hover ,locations = state_pop$State,
        type = "choropleth" ,locationmode = "USA-states",
        color = state_pop$Pop,colors = "Blues" , marker = list(line = borders)) %>%
  layout(title = "US population in 1975" , geo = map_options)

#ggploty

set.seed(100)

d <- diamonds[sample(nrow(diamonds), 1000) ,]
p <- ggplot(data = d , aes(x = carat , y = price)) +
  geom_point(aes(text = paste("clarity:",clarity)) , size = 4)+
  geom_smooth(aes(colour = cut , fill = cut,)) + facet_wrap(~cut)
p

gg <- ggplotly(p)
gg



