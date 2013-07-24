 from pattern.web import Twitter, plaintext
  2 from pattern.db  import Datasheet
  3 from pattern.en import polarity
  4
  5 class GatherTweets:
  6
      # a file called companies.txt contains a list of companies to search Twitter for
  7   file = open("companies.txt")
  8   csv = Datasheet()
  9
      # traverse companies.txt and retrieve tweets and assign polarity to them 
 10   for line in file:
 11     for tweet in Twitter().search(line.rstrip('\n').rstrip('0xD')):
 12       tweet_desc = plaintext(tweet.description)
 13       tweet_pol = polarity(tweet.description)
 14       csv.append([tweet.date, tweet_desc, tweet_pol])
 15
      # save the tweet date, tweet, and the polairty of the tweet in gathered_tweets.csv
 16   csv.save('gathered_tweets.csv')
