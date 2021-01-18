import twint

#config
config = twint.Config()
config.Search = "U.S. Capitol"
config.Limit = 20
config.Store_csv = True
config.Output = "practice.csv"

twint.run.Search(config)

#having an error when running the code: https://github.com/twintproject/twint/issues/604
#error resolved by downloading from git
