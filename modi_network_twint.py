import twint

c = twint.Config()
c.Username = "narendramodi"
c.Limit = 20
c.Store_csv = True
c.Output = "practice.csv"

twint.run.Followers(c)

#getting error: CRITICAL:root:twint.feed:Follow:IndexError
