normal_answers = ["你们懂吗","人生的意义是什么","你们的开发经验是什么","我要屎了","男人要的是到底什么样的女人","加我飞书","我不行了","我要建立资产", "龙腾世纪","内裤","我为什么总是有很多的想法","你们用扫地机器人吗","你们思考吗","你们学数学吗","五感","为别人着想"]
special_answers = {"lqt":"lqt的家像宫殿一样","美女":"哪里有有才的美女，在电脑上查找美女","你们有Google voice吗":"没有","养孩子":"自己的事情都没搞好 养什么孩子"}
import random
import re
def answer(question):
    if re.match(question,r"\s+"):
        return "我们教信息技术的老师很漂亮，我很想草她"
    if random.uniform(0,1) <= (random_rate := 0.114514):
        return "是的，你很懂{}".format(question)
    elif random.uniform(0,1) <= (random_rate := 0.233):
        return "什么是{}".format(question)
    elif question in special_answers.keys():
        return special_answers[question]
    return random.choice(normal_answers)
while True:
    user_input = input("<<< ")
    print(">>> {}".format(answer(user_input)))