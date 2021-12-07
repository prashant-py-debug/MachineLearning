library(shiny)

shinyServer(function( input , output){
  
  population <- rnorm(1000, mean = 25 , 5)
  
  output$plot1 <- renderPlot({
    set.seed(2-2-2021)
    n <- input$slider1
    b <- input$slider2
    resamples <- matrix(sample(population, n*b , replace= TRUE),b , n)
    means <- apply(resamples,1,mean)
    BS_mean <- mean(means)
    BS_quantile <- quantile(means , c(0.25,0.975))
    output$mean <- renderText({BS_mean})
    output$CI <- renderText({BS_quantile})
    output$Rmean <- renderText({25})
    
    hist(means, col = "lightblue")
    if(input$mean){
      abline(v = BS_mean, col = "red", lw = 3)}
    if(input$CI){
      abline(v = BS_quantile, col = "blue",lw = 2)}
    
    
  })
  
  
  
})