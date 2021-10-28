# -- coding: utf-8 --
import requests
import time
from bs4 import BeautifulSoup
import re
import csv
import json

if __name__ == '__main__':
    headers = {
        "cookie": '''EDUWEBDEVICE=58601d04d3d148deb10940ec74c9ed6b; __yadk_uid=4nDvWI0AKZhe8DaRyt8xNstriRiiyR1y; hasVolume=true; videoVolume=0.8; WM_TID=Frh2m8mE+wJAEQAAAEN60N+MoUceJ/Xs; MOOC_PRIVACY_INFO_APPROVED=true; bpmns=1; CLIENT_IP=211.101.60.67; NTESSTUDYSI=8b6b16d164d248a7b4048f61ea0d8828; NTES_YD_SESS=.Z.cf1waz3NBuN_BkctGuV8R5NLuIQzb.wjXNLtk3afgO1zGOBYERDRyBROzI5gELgKrnDOIaJG.Q4NIS8_mF1.2EJyS3T6u_CAf7pmNk1ZBeYXLtz6QUH2jTpgWEzhgZ0YGhNX.aRhIt3tUglE2nWOLz5dKQWftCPTzB.xEQ24TSQtrpku5m0UBvlP6275EZpYJ053X.bJwUGGVmsFVFJCWhDhYeaS7u; NTES_YD_PASSPORT=eIDWsczW0R4tQbGdM2xiisvVAffC9ROPzQSX8yqSO04mAZ_WA7Kw6g6j76A_a2Jw.JtiCgAaBNWRuc08ByoMHxEtk1mRiQc.5uAjHL4JK78mZNATJjw6EVHUjg4wsUFDx1BeQDieUIiyRSQB8B7y0mBgI8DGT22ESllef.kY3JzyUvHr.bLzdLa0F7U6uMCL4H.LlA_kHmHrpWkdIK71CVnG4; S_INFO=1634021290|0|0&60##|15754713985; P_INFO=15754713985|1634021290|1|imooc|00&99|null&null&null#bej&null#10#0|&0|null|15754713985; STUDY_INFO="yd.fc035288ce9c430eb@163.com|8|1383708100|1634021290616"; STUDY_SESS="cQ2popAg/46bXJnsXWt47zpy8n3jcHdD8phZNdHmrLooG/fHYJD4LRLRkhb5x4c+qVxgiNitD3z0yfGhpVqzVGIkcoeyElcEg3OYeQ7LNFwt4aEA75oGJQCmi0elvLyJB5mpHs1i7/046+DIAcY5M6cn8y0JIyN8oo587kkjfvoLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="NQgtN7iAjebGD9z9yJDHgjI2uPcHnb2J/UuKYOS6ERmO/9Cndqz2+Btaq2o4UZXw1xQfesBhf5wf0LsqclexKSowafLyjGsUO2imBpG7BHyYAisO32ZpwWQ106VedEq9uTk1Gsi+chMnZG+YOyp0ne9b2bEDiCDC9D9ylnZKM5S6yFl7Evbwa2zwPoNCixTW78kjiOpd7BWz/hY3Uh7DsYvCnTTnZHl8Ix8slBRLh9PZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1383708100#|#1546791321036; WM_NI=Q2ROkje5DQaEiP2TrCb6/fyA+fTA2sGTsRSF/EHEcxDVFPid/OqsIONXp4MvSg4t1xuCogm26AjnGBTNZHf5uoWf3/GQYQOvsP7wfDc2WIeSnO8XlLyZcHStsHH0HlL7b3o=; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9b7478aed9ba2f267a18a8ea3d55a869b9a84b57991ace587e439a68b8fa4fb2af0fea7c3b92a93ee9eb0ea62a7eb8cb2e44fab90feb5f149a2eae187fc4be9ba9ca2b179858cbdb3d24eed9b88a6e274888a8ab1ec70ed91bf94cc458e88c0d5d07e91b9fc95b474b79da188f03af69fa68fc64a989296a9e53fb7b19987b225858f97b2ce7eb190f998e550a1ee99aae859ae91f8b9ef48bb86ada9d280b19888d1cb6890e9aed4ee37e2a3; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9weXRob24xMjMuaW8v"; hb_MA-A976-948FFA05E931_source=python123.io; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1632725379,1632730645,1633941622,1634117204; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1634117714''',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    # csv
    headers_of_csv = ["schoolSN", "courseName", "courseId", "userId", "userName", "comments", "mark", "agreeCount"]
    csvFile = open("data.csv", "w+", newline='', encoding='utf-8')
    f_csv = csv.writer(csvFile)
    f_csv.writerow(headers_of_csv)
    #
    params = {'csrfKey': '8b6b16d164d248a7b4048f61ea0d8828'}
    school_Url = 'https://www.icourse163.org/university/view/all.htm#/'
    page_text = requests.get(url=school_Url, headers=headers1).text
    soup = BeautifulSoup(page_text, 'lxml')
    # 1.获取所有学校的网址
    school_List = []
    school_Url_List = []
    for link in soup.findAll(class_='u-usity f-fl'):
        if 'href' in link.attrs:
            school_List.append(link.attrs['href'])
    for item in school_List:
        school_Url_List.append("https://www.icourse163.org" + item + "#/c")
    print("获取所有学校网址 - 成功!")
    time.sleep(5)
    # 2.获取schoolId
    schoolId_List = []
    for url in school_Url_List:
        school_page_text = requests.get(url=url, headers=headers1).text
        school_soup = BeautifulSoup(school_page_text, 'lxml')
        text = school_soup.select('script')
        t = re.findall(r"window.schoolId = \"(.*?)\";", str(text))
        schoolId_List.append(t[0])
    print("获取schoolId - 成功!")
    time.sleep(10)
    # 3.获取某校的所有课程Id
    for schoolId in schoolId_List:
        data = {
            'schoolId': schoolId,
            'p': '1',
            'psize': '20',
            'type': '1',
            'courseStatus': '30'
        }
        courses_Url = "https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?"
        courses_res = requests.post(url=courses_Url, data=data, params=params, headers=headers).json()
        # 4. 获取具体课程的评论
        time.sleep(5)
        for course in courses_res['result']['list']:
            course_Id = course['id']
            school_shortName = course['schoolSN']
            course_Name = course['name']
            course_Url = 'https://www.icourse163.org/course/{}-{}'.format(school_shortName, course_Id)
            course_res = requests.get(url=course_Url, headers=headers1).text
            data1 = {
                'courseId': course_Id,
                'pageIndex': '1',
                'pageSize': '20',
                'orderBy': '3'
            }
            baseUrl = "https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?"
            comments_res = requests.post(url=baseUrl, data=data1, params=params, headers=headers).json()
            # 获取所有评论 - 进行分页处理
            pageSize = comments_res['result']['query']['pageSize']
            # for page in range(1, pageSize + 1):
            j = 0
            for item in comments_res['result']['list']:
                user_Id = item['id']
                user_Name = item['userNickName']
                content = item['content']
                mark = item['mark']
                agreeCount = item['agreeCount']
                result = []
                headers_of_csv = ["schoolSN", "courseName", "courseId", "userId", "userName", "comments", "mark", "agreeCount"]
                result.append(school_shortName)
                result.append(course_Name)
                result.append(course_Id)
                result.append(user_Id)
                result.append(user_Name)
                result.append(content)
                result.append(mark)
                result.append(agreeCount)
                f_csv.writerow(result)
                j += 1
                print(str(j) + "写入!")
                time.sleep(3)
    csvFile.close()