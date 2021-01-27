import twint

c = twint.Config()
c.Username = "narendramodi"
c.Format = "ID {id} | Username {username}"
c.Limit = 20
c.Store_csv = True
c.Output = "practice.csv"

twint.run.Following(c)

#getting error: CRITICAL:root:twint.feed:Follow:IndexError
