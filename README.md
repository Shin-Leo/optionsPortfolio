# Options Portfolio #
- - - -
This Django project is for simulating a portfolio of options strategies (butterfly, condor, straddle, ...) using the [yfinance](https://github.com/ranaroussi/yfinance) api.

## Try it Here! ##
https://options-portfolio.herokuapp.com/

## How It Works ##

* ### Call/Put Tables ###
    * Options chains were given as data frames from [yfinance](https://github.com/ranaroussi/yfinance) and were rendered dynamically using django template tags
      [](https://github.com/Shin-Leo/optionsPortfolio/blob/master/tables.png?raw=true)

* ### Graphing ###
    * Pay-off diagrams were made with [Chart.js](https://github.com/chartjs/Chart.js)
    [](https://github.com/Shin-Leo/optionsPortfolio/blob/master/graphs.png?raw=true)

* ### Database ###
    * Uses postgreSQL and django models to store portfolio data

## Current Progress ##
- [ ] Configure database with Heroku
- [ ] Upgrade data source
- [ ] Finish implementing all strategies
- [ ] Portfolio performance time-series graph
- [x] Add pay-off diagrams using [Chart.js](https://github.com/chartjs/Chart.js)
- [x] Create Django models for data 
- [x] Render options chains in scrollable tables 
