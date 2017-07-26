#############################################################
###  _____           _  ___  _ _   
### |___ /_  ___ __ / |/ _ \(_) |_ 
###   |_ \ \/ / '_ \| | | | | | __|
###  ___) >  <| |_) | | |_| | | |_ 
### |____/_/\_\ .__/|_|\___/|_|\__|
###           |_|                  
###                                                          
### name: efficient.py
### function: efficient study
### date: 2017-07-19
### author: quanyechavshuo
### blog: http://3xp10it.cc
#############################################################
import time
import os
import random
import re
from exp10it import CLIOutput
from exp10it import update_config_file_key_value
from exp10it import get_key_value_from_config_file
from exp10it import config_file_has_key_value
from exp10it import MyThread


def voiceTips(outputObj):
    import time
    import re
    import sys
    saidNowStartList = []
    saidNowEndList = []
    output=outputObj
    while 1:
        time.sleep(1)
        nowYear = time.strftime("%y")
        nowMonth = time.strftime("%m")
        nowDate = time.strftime("%d")
        todayDate = nowYear + nowMonth + nowDate
        if os.path.exists("plan.ini"):
            with open("plan.ini", "r+") as f:
                fileContent = f.read()
            matchToday = re.search(r"\[%s\]\n+([\s\S]+)(\[.+\])?" % todayDate, fileContent, re.I)
            if matchToday:
                tmpContent = matchToday.group(1)
                matchTime = re.findall(r"(\d{1,2}'\d{1,2})\-(\d{1,2}'\d{1,2})\s*=\s*(.*)", tmpContent, re.I)
                if matchTime:
                    #print(matchTime)
                    import datetime
                    # pdb.set_trace()

                    now = datetime.datetime.now()
                    now = now.strftime('%H:%M').replace(":", "'")
                    for each in matchTime:
                        startTime = each[0]
                        endTime = each[1]
                        if len(each[0].split("'")[0]) == 1:
                            startTime = '0' + each[0]
                        if len(each[1].split("'")[0]) == 1:
                            endTime = '0' + each[1]
                        if startTime == now:
                            if now not in saidNowStartList:
                                time.sleep(3)
                                output.stop_order=0
                                os.system("say 注意,现在开始进行%s" % each[2])
                                printString="[正在进行:"+each[2]+"]"
                                t=MyThread(output.continue_bottom_print,(printString,))
                                t.start()
                                saidNowStartList.append(now)

                            # time.sleep(60)
                        if endTime == now:
                            if now not in saidNowEndList:
                                os.system("say 注意,现在结束%s" % each[2])
                                #output.bottom_print("\r"+" "*len(printString))
                                output.bottom_print("[完成'%s']" % each[2])
                                #sys.stdout.flush()
                                output.stop_order=1
                                saidNowEndList.append(now)


output = CLIOutput()
jiangli = ["今日dj", "本周2次dj", "可以买一个礼物给家人", "可以买一本好书给自己", "可以获得一次抵消惩罚的机会",
           "明天完成main后可以自由娱乐或其他安排", "周末可以自由安排", "增加可购买想要的东西的基金200元[到2000元可购买机械键盘]"]
chengfa = ["周末Ndj", "周末全部时间用来学习,禁止娱乐", "周末全部时间用来练习五笔", "周末全部时间用来背单词", "周末背2000个单词后才可以休息, 否则不能进行任意娱乐", "减少基金200元"]
jiangliIndex = random.randint(0, len(jiangli) - 1)
chengfaIndex = random.randint(0, len(chengfa) - 1)

while 1:
    import time
    nowYear = time.strftime("%y")
    nowMonth = time.strftime("%m")
    nowDate = time.strftime("%d")
    todayDate = nowYear + nowMonth + nowDate

    choose = input('''请输入你遇到的问题:
    1.效率不高
    2.原来计划二八法则的学习方式下学习,但是现在因为一些原因需要打破这个约定,想把时间花在学习其他的知识
    3.分心导致学习效率不高
    4.想做一些折腾的事又担心这样要花太多时间,又怕不折腾代表自己处理问题能力不强
    5.要履行的二八法则
    6.制订学习计划
    7.奖惩方法
    >>>''')
    if choose == '1':
        output.good_print('''
        https://www.zhihu.com/question/20280586/answer/14598214
        华罗庚先生曾经说,所有有伟大成就的人无一不是利用时间的能手.在时间有限而课业负担重、任务多的情况下,利
        用时间的能力也就显得十分重要了.要高效地利用时间,一个必不可少的步骤就是安排计划.每个人都需要准备一个专门的
        计划本,把安排计划的事情持之以恒地做下去并最终养成一种习惯.安排计划最好是分成两层:以天为单位和以周为单位.
        首先要做的事情是确定任务,也就是我必须做什么.确定任务不能等到每天自习的时候再来想,而必须是每节课或每个阶段
        的课程结束之后在产生了新的任务的同时就把它记录下来.例如,上完一节历史课之后,立刻就记下做本课练习题和复习本
        课内容的任务.确定了任务之后,在执行之前应排定优先序,也就是确定哪些应该先做,哪些在时间紧张的情况下可以延后1
        ～2天再做.安排计划还应有足够的勇气和智慧做好取舍和分散的工作.如果任务很多,时间有限,哪怕你觉得每一件事情都
        应该去做,也必须要取舍,把最次优先的事情取消或者延后,同时要对同一科的任务进行分散,绝对不能一个晚自习只做一
        两科的事情.
        ''')
    if choose == '2':
        output.good_print('''1.打破规则是因为这个实在具备价值(价值在7分以上),如果是这样你就打破吧
2.打破是因为这个近期没有完成,想尽快完成,如果不在近期完成,以后会花2倍以上的时间才能完成,如果是这样你就打破吧
3.打破是因为近期完成这个比较有效率,感觉有兴致,但是这个在不打破二八法则下也可完成,只是效率可能会下降,如果是这样,你还是别想着打破了,二八法则是长远的高效,比你这点效率重要多了
        ''')
    if choose == '3':
        output.good_print('''请关闭手机,不和别人说话,放弃导致分心的杂念,全心学习到计划完成的时间''')
    if choose == '4':
        output.good_print('''在你完成伟大的事业前是要牺牲很多的,
如果你觉得你已经完成了人生的最终目的,
你就去浪费时间折腾吧,
放下是一种智慧,二八法则是一种高智慧''')
    if choose == '5':
        output.good_print('''1.上班时间学习web,下班时间学习二进制
2.20%时间用于自己折腾,80%时间用于学习别人的成果
3.20%时间用于制定自己的计划,80%的时间用于完成计划''')
    if choose == '6':
        output.good_print('''
订目标和计划的领悟:

没有写下目标有或者写下的目标不明确有如下伤害:
1.没有动力
2.浪费精力，乱花精力
3.一事无成
有了目标也要有详细的计划，计划越详细，效率越高。目标和计划结合:

1)写出目标(当天,当周,当月,当年)
2)写出详细计划(当天,当周,当月,当年)
3)写出奖惩办法,实施奖惩行动
4)写出小结以优良循环改善效率(当天,当周,当月,当年)
                ''')

        choose = input('''1.制订年度计划
2.制订月度计划
3.制订本周计划
4.制订今日计划
>>>''')
        if not os.path.exists("plan.ini"):
            os.system("touch plan.ini")
        if choose == '1':
            pass
        if choose == '2':
            pass
        if choose == '3':
            pass
        if choose == '4':
            import os
            with open("plan.ini", "r+") as f:
                fileContent = f.read()
            if not config_file_has_key_value("plan.ini", todayDate, "plan"):
                # 没有plan的值
                plan = input("请输入今天的目标\n>>>")
                update_config_file_key_value("plan.ini", todayDate, "plan", plan)
            if not config_file_has_key_value("plan.ini", todayDate, "main"):
                main = input("请输入今天的主要目标\n>>>")
                update_config_file_key_value("plan.ini", todayDate, "main", main)
            if not config_file_has_key_value("plan.ini", todayDate, "未完成惩罚") and not config_file_has_key_value("plan.ini", todayDate, "完成奖励"):
                if int(nowDate) % 2 == 0:
                    choose = input("今日为惩罚日,你想自己选择惩罚方式还是由我随机帮你选一个? y|Y for your choose,n|N for random,default [n]\n>>>")
                    if choose in ['y', 'Y']:
                        while 1:
                            choose = input('''
    惩罚方法:
        1.周末Ndj
        2.周末全部时间用来学习,禁止娱乐
        3.周末全部时间用来练习五笔
        4.周末全部时间用来背单词
        5.周末背2000个单词后才可以休息,否则不能进行任意娱乐
        6.减少基金200元
        >>>''')
                            if choose not in ["1", "2", "3", "4", "5", "6"]:
                                continue
                            else:
                                output.good_print("你选择了:%s" % chengfa[int(choose)-1])
                                update_config_file_key_value("plan.ini", todayDate, "未完成惩罚",
                                        chengfa[int(choose)-1])
                                break
                    else:
                        output.good_print("随机选取为:%s" % chengfa[chengfaIndex])
                        update_config_file_key_value("plan.ini", todayDate, "未完成惩罚", chengfa[chengfaIndex])
                else:
                    choose = input("今日为奖励日,你想自己选择奖励方式还是由我随机帮你选一个? y|Y for your choose,n|N for random,default [n]\n>>>")
                    if choose in ['y', 'Y']:
                        while 1:
                            choose = input('''
        奖励方法:
        1.今日dj
        2.本周2次dj
        3.可以买一个礼物给家人
        4.可以买一本好书给自己
        5.可以获得一次抵消惩罚的机会
        6.明天完成main后可以自由娱乐或其他安排
        7.周末可以自由安排
        8.增加可购买想要的东西的基金200元[到2000元可购买机械键盘]
        (默认不奖励不惩罚状态应该是副业状态,工资太少,要赚钱,要保持hungery to gain money,knowledge,but not movie anymore,that's boring and meaningless)
        >>>''')
                            if choose not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                                continue
                            else:
                                output.good_print("你选择了:%s" % jiangli[int(choose)-1])
                                update_config_file_key_value("plan.ini", todayDate, "完成奖励",
                                        jiangli[int(choose)-1])
                                break
                    else:
                        output.good_print("随机选取为:%s" % jiangli[jiangliIndex])
                        update_config_file_key_value("plan.ini", todayDate, "完成奖励", jiangli[jiangliIndex])

            with open("plan.ini", "r+") as f:
                fileContent = f.read()
            tmpContent = re.search(r"\[%s\]\n+([\s\S]+)(\[.+\])?" % todayDate, fileContent, re.I).group(1)
            #if not re.search(r"\d{1,2}'\d{1,2}\-\d{1,2}'\d{1,2}\s*=", tmpContent, re.I):
            if 1:
                output.good_print("请输入详细时间计划")
                while 1:
                    timeSection = input("时间段[eg.6:00-7:05],q退出详细时间安排输入\n>>>")
                    timeSection = timeSection.replace(":", "'")
                    if timeSection in ['q', 'Q']:
                        break
                    else:
                        timeSectionPlan = input("请输入%s要完成的任务\n>>>" % timeSection)
                        update_config_file_key_value("plan.ini", todayDate, timeSection, timeSectionPlan)

            #from multiprocessing import Process
            #p = Process(target=voiceTips, args=())
            #p.start()
            t=MyThread(voiceTips,(output,))
            t.start()


            if not config_file_has_key_value("plan.ini", todayDate, "小结-缺点"):
                quedian = input("请输入今天小结的缺点,q退出\n>>>")
                if quedian not in ['q', 'Q']:
                    update_config_file_key_value("plan.ini", todayDate, "小结-缺点", quedian)
                else:
                    continue

            if not config_file_has_key_value("plan.ini", todayDate, "小结-改进"):
                quedian = input("请输入今天小结的改进\n>>>")
                update_config_file_key_value("plan.ini", todayDate, "小结-改进", quedian)
            if not config_file_has_key_value("plan.ini", todayDate, "小结-优点"):
                quedian = input("请输入今天小结的优点\n>>>")
                update_config_file_key_value("plan.ini", todayDate, "小结-优点", quedian)
    if choose == '7':
        output.good_print('''可以每天单独实施奖励或惩罚
    每周安排:
    3天为奖励项
    3天为惩罚项
    周五为奖励惩罚并存天

    奖励方法:
    1.今日dj
    2.本周2次dj
    3.可以买一个礼物给家人
    4.可以买一本好书给自己
    5.可以获得一次抵消惩罚的机会
    6.明天完成main后可以自由娱乐或其他安排
    7.周末可以自由安排
    8.增加可购买想要的东西的基金200元[到2000元可购买机械键盘]
    (默认不奖励不惩罚状态应该是副业状态,工资太少,要赚钱,要保持hungery to gain money,knowledge,but not movie anymore,that's boring and meaningless)

    惩罚方法:
    1.周末Ndj
    2.周末全部时间用来学习,禁止娱乐
    3.周末全部时间用来练习五笔
    4.周末全部时间用来背单词
    5.周末背2000个单词后才可以休息,否则不能进行任意娱乐
    6.减少基金200元''')
        while 1:
            choose = input("\n输入j随机奖励,输入c随机惩罚,输入b返回到上一层[default b]\n>>>")
            if choose in ['j', 'J']:
                output.good_print(jiangli[jiangliIndex])
            elif choose in ['c', 'C']:
                output.good_print(chengfa[chengfaIndex])
            else:
                break
