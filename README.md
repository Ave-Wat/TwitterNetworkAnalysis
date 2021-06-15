# TwitterNetworkAnalysis

![alt text](https://github.com/johnsont4/TwitterNetworkAnalysis/blob/main/visualization.png?raw=true)

This project examines how populists target their constituencies on social media. Social media is an especially important medium for populists to reach their audiences because of their rejection of traditional media. However, the horizontal nature of social media makes it difficult to partition one's message to appeal to different audiences. This research seeks to determine how populists are coping with this difficulty. Do they primarily target online constituencies by constructing one community through vague messaging or do they appeal to the specific, individualized grievances of multiple insulated communities? We used Indian Prime Minister Narendra Modi as a case study, studying the structure and composition of his constituencies through a social network analysis of his Twitter network. 

To complete this task, we built a Twitter scraping tool using selenium and beautifulsoup. This tool was able to avoid the rate limits of Tweepy and has the capability to scrape Twitter friends, unlike popular tools currently in use, such as Twint. Using our tool, we found the first two degrees of P.M. Modi's Twitter network. We then calculated the top 1000 users by in-degree centrality, and created a graph of these users in the graph visualization software Gephi.
