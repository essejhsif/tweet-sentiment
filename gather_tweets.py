 from pattern.web import Twitter, plaintext
  2 from pattern.db  import Datasheet
  3 from pattern.en import polarity
  4
  5 class GatherTweets:
  6
  7   file = open("companies.txt")
  8   csv= Datasheet()
  9
 10   for line in file:
 11     for tweet in Twitter().search(line.rstrip('\n').rstrip('0xD')):
 12       tweet_desc = plaintext(tweet.description)
 13       tweet_pol = polarity(tweet.description)
 14       csv.append([tweet.date, tweet_desc, tweet_pol])
 15
 16   csv.save('gathered_tweets.csv')
