import json
import time
import codecs

users = ["comscoreinc", "conchoresources", "csodcommunity", "WorkAtBRAVO", "iHeartMedia", "CTGinc", "GrouponJobs", "InsperityJobs", "tmobilecareers", "ReachLocal", "SymmetryMedical", "Zillow"]

time2011 = time.strptime("2011-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")
time2012_begin = time.strptime("2012-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")
time2012_end = time.strptime("2012-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
time2013 = time.strptime("2013-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")

text2011 = ""
text2013 = ''

with codecs.open("fb-2011.txt", "w", "utf-8") as outfile1, codecs.open("fb-2013.txt", "w", "utf-8") as outfile2:
    for user in users:
        with open("fb_data/"+user+"_timeline.json") as infile:
            timeline_arr = json.load(infile)
            for i in range(0, len(timeline_arr)):
                message_arr = timeline_arr[i]["data"]
                for j in range(0, len(message_arr)):
                    message_obj = message_arr[j]

                    if "message" in message_obj:
                        message = message_obj["message"]
                    if "story" in message_obj:
                        message = message_obj["story"]
                    message = message.replace("\n", " ").replace("\r\n", " ").replace("\r", " ")

                    # 2010-02-12T16:52:30+0000
                    time_str = message_obj["created_time"]
                    time_str = time_str.replace("T", " ").replace("+0000","")
                    t = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                    if t>=time2011 and t<=time2012_begin:
                        # print message, t
                        # print user, time.strftime("%Y\t%m\t%d", t), time.strftime("%Y-%m-%d %H:%M:%S", t), message
                        # outfile.write(user+"\t"+time.strftime("%Y\t%m\t%d", t)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", t)+"\t"+message+"\n")
                        text2011 += message+'\n'

                    if t>=time2012_end and t<=time2013:
                        # print message, t
                        # print user, time.strftime("%Y\t%m\t%d", t), time.strftime("%Y-%m-%d %H:%M:%S", t), message
                        # outfile.write(user+"\t"+time.strftime("%Y\t%m\t%d", t)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", t)+"\t"+message+"\n")
                        text2013 += message+'\n'
    outfile1.write(text2011)
    outfile2.write(text2013)


