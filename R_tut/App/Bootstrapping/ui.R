library(shiny)

shinyUI(fluidPage(
  titlePanel("BootStrapping"),
  sidebarLayout(
    sidebarPanel(
      h3("Instructions:"),
      HTML("1. This app uses bootstrapping to infer mean and CI for the population.<br>
         2. You can choose sample sizes and number of simulations from the sliders below.<br>
         3. App is interactive so you will see the effect of various selections made by you.<br>
         4.We are sampling from a random normal distribution with mean 25 , sd 5.<br>
         5.You can toggle mean and CI by clicking on the checkboxes provided below."),
      h3("Select the number of samples for Boot Strapping"),
      sliderInput("slider1","sample size" , 100,1000,value = 500,step = 100),
      h3("select number of simulations:"),
      sliderInput("slider2","Simulations",100,1000,step = 100,value = 700),
      h3("Toggle mean"),
      checkboxInput("mean","toggle mean",value = TRUE),
      h3("Toggle Confidence Interval"),
      checkboxInput("CI","toggle CI", value = FALSE )
    ),
    mainPanel(
      plotOutput("plot1"),
      h3("Mean after boot strapping"),
      textOutput("mean"),
      h3("Actual Mean of the concerned population:"),
      textOutput("Rmean"),
      h3("95% Confidence interval"),
      textOutput("CI")
      
    )
  )
  
  
))