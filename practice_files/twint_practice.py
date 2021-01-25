# twint documentation: https://github.com/twintproject/twint/wiki

import twint

#config
config = twint.Config()
config.Search = "U.S. Capitol"
config.Limit = 20
config.Store_csv = True
config.Output = "practice.csv"

twint.run.Search(config)
