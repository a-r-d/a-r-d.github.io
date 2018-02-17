import numpy as np

### <summary>
### Basic template algorithm simply initializes the date range and cash. This is a skeleton
### framework you can use for designing an algorithm.
### </summary>
class BasicTemplateAlgorithm(QCAlgorithm):
    '''Basic template algorithm simply initializes the date range and cash'''

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''
        self.SetStartDate(2015,1,1)  #Set Start Date
        self.SetEndDate(2017,2,1)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash
        self.SetWarmUp(100) #warm u for 100 days
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)
        #self.sizing = startCash * 0.02
        # Find more symbols here: http://quantconnect.com/data
        # self.SetBenchmark("NFLX")
        self.AddEquity("SPY", Resolution.Daily)
        self.Debug("numpy test >>> print numpy.pi: " + str(np.pi))
        self.longOnly = True

        '''
        Smooth and high sensitive moving Average. This moving average reduce lag of the informations but still being smooth to reduce noises.
        Is a weighted moving average, which weights have a Normal shape; the parameters Sigma and Offset affect the kurtosis and skewness of the weights respectively.
        Source: http://www.arnaudlegoux.com/index.html
        '''


        self.load_symbols()
        for symbol in self.symbols:
            symbol.weight = 0
            symbol.stopprice = None
            symbol.lastSignal = "NA"
            # https://github.com/Quantconnect/Lean/blob/master/Algorithm.Python/MACDTrendAlgorithm.py1
            # 72, 189, 9,  VS  10,100,5  vs 50, 150, 9 --- seems that best are short is 1/2 to 1/4 ratio of the long
            #symbol.slow = self.ALMA(symbol, 10, 6, 0.85, Resolution.Daily)
            #symbol.fast = self.ALMA(symbol, 30, 6, 0.85, Resolution.Daily)
            symbol.slow = self.KAMA(symbol, 50, Resolution.Daily)
            symbol.fast = self.KAMA(symbol, 150, Resolution.Daily)

        # trade every day 30 minutes after open
        self.Schedule.On(self.DateRules.EveryDay("SPY"), self.TimeRules.AfterMarketOpen("SPY", 30), Action(self.trade))

    def OnData(self, data):
        pass

    def trade(self):
        for symbol in self.symbols:
            self.Debug("In symbol block")
            if not symbol.slow.IsReady:
                continue

            self.Debug("indictors ready")
            holdings = self.Portfolio[symbol].Quantity
            numHoldings = len(self.symbols)
            tradeQty = 1.25 / numHoldings

            fast = symbol.fast.Current.Value
            slow = symbol.slow.Current.Value
            self.Debug("fast / slow value: " + str(fast) + " " + str(slow))

            if holdings <= 0 and  fast > slow:  # 0.01%
                symbol.lastSignal = 'LONG'
                #self.Debug("MACD signal long:" + str(symbol) + " signal:" + str(signal) + " slow:" + str(slow) + " fast:" + str(fast))
                self.SetHoldings(symbol, tradeQty)
            elif holdings >= 0 and slow > fast:
                symbol.lastSignal = 'SHORT'
                #self.Debug("MACD signal short: signal: " + str(signal))
                if not self.longOnly:
                    self.SetHoldings(symbol, -1 * tradeQty)
                else:
                    self.Liquidate(symbol)


    def load_symbols(self):
        syl_list = [
            #'SPY' #, 'USO', 'GLD', 'SLV', 'VNQ', 'HYG', 'EWJ'
            #'CAT', 'DE', 'CVX', 'LMT', 'HON', 'GM'
            #'IBB', 'SPY', 'IYR', 'IYF', 'IYH', 'IYM'
            'SPY'
        ]
        self.symbols = []
        for i in syl_list:
            self.symbols.append(self.AddEquity(i, Resolution.Daily, Market.USA, True, 1.5).Symbol)
