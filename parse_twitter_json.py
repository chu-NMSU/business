import json
import time
import codecs

users = [ 'CNOCareers', 'PerficientLife', 'bwwcareers', 'echostarcareers', 'iheartmedia', 'nytimesrecruit', 'CTGjobs', 'TitanAg', 'carmartcareers', 'grouponjobs', 'insperityjobs', 'pandoracareers']

time2011 = time.strptime("2011-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")
time2012_begin = time.strptime("2012-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")
time2012_end = time.strptime("2012-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
time2013 = time.strptime("2013-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")

text2011 = ""
text2013 = ''

with codecs.open("twitter-2011.txt", "w", "utf-8") as outfile1, codecs.open("twitter-2013.txt", "w", "utf-8") as outfile2:
    for user in users:
        with open("twitter_data/"+user+".json") as infile:
            timeline_arr = json.load(infile)['user_timeline']
            for i in range(0, len(timeline_arr)):
                tweet_obj = timeline_arr[i]

                tweet = tweet_obj["tweet"]
                tweet = tweet.replace("\n", " ").replace("\r\n", " ").replace("\r", " ")

                # Fri Mar 29 13:15:10 MDT 2013
                time_str = tweet_obj["date"]
                t = time.strptime(time_str, "%a %b %d %H:%M:%S %Z %Y")

                if t>=time2011 and t<=time2012_begin:
                    # print tweet, t
                    # print user, time.strftime("%Y\t%m\t%d", t), time.strftime("%Y-%m-%d %H:%M:%S", t), tweet
                    # outfile.write(user+"\t"+time.strftime("%Y\t%m\t%d", t)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", t)+"\t"+tweet+"\n")
                    text2011 += tweet+'\n'

                if t>=time2012_end and t<=time2013:
                    # print tweet, t
                    # print user, time.strftime("%Y\t%m\t%d", t), time.strftime("%Y-%m-%d %H:%M:%S", t), tweet
                    # outfile.write(user+"\t"+time.strftime("%Y\t%m\t%d", t)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", t)+"\t"+tweet+"\n")
                    text2013 += tweet+'\n'
    outfile1.write(text2011)
    outfile2.write(text2013)


