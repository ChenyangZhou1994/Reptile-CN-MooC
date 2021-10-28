import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import pandas as pd
import csv

###爬取课程页信息###
def GetDetail(url,result):
    
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    html=driver.page_source
    bsobject=BeautifulSoup(html, "lxml")

    #print(bsobject)
    course_name=bsobject.find(class_="course-title f-ib f-vam").get_text()
    result.append(course_name)
    subject=bsobject.find(class_="breadcrumb_item sub-category").get_text()
    result.append(subject)
    num_of_join=bsobject.find(class_="breadcrumb_item sub-category").get_text()
    result.append(num_of_join)
    num_of_mark=bsobject.find(id="review-tag-num").get_text()
    result.append(num_of_mark[1:-1])
    a = driver.find_element_by_id("review-tag-button") 
    a.click()
    time.sleep(2)
    html=driver.page_source
    bsobject=BeautifulSoup(html, "lxml")
    star=bsobject.find(class_="ux-mooc-comment-course-comment_head_rating-scores")
    #print(star)
    if star is not None:
        result.append(star.get_text())
        #print(star.get_text())
    else:
        result.append("")
    driver.close()
    #print(cont4)
#url="https://www.icourse163.org/course/WHU-1457456166"
#GetDetail(url)



###爬取单个页面###
def getHTMLText(url):
    try:
        time.sleep(3)
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


###爬取首页所有高校页面链接###
def getSchoolURLs():
    school_ls = []
    school_url_ls = []
    
    html = getHTMLText(base_url)
    soup = BeautifulSoup(html)
    for link in soup.body.findAll(class_='u-usity f-fl'):
        if 'href' in link.attrs:
            #print(link.attrs['href'])
            school_ls.append(link.attrs['href'])
    #print(school_ls)
    for item in school_ls:
        school_url_ls.append("https://www.icourse163.org"+item+"#/c")
    return school_url_ls
#print(school_url_ls)
#生成目标学校url



base_url="https://www.icourse163.org/university/view/all.htm#/" #首页url
SchoolURLs=getSchoolURLs() #得到存放了所有大学页面url的列表
print(SchoolURLs)  #成功

###打开csv文件，写入文件头
headers_of_csv = ["学校", "课程名称", "科目", "参加人数", "评价人数", "评分"]
csvFile = open("中国大学MOOC课程信息.csv", "w+", newline='', encoding='utf-8')
f_csv = csv.writer(csvFile)
f_csv.writerow(headers_of_csv)

results = []  #数组存放学校，课程名，科目，参与人数，评价人数，评分

for school in SchoolURLs: 
    print("在读取的学校是：{}".format(school))
    course_ls=[]
    course_url_ls=[]
    driver=webdriver.Chrome() #打开浏览器
    def OpenSchoolWeb(url):  
        driver.get(url)
        time.sleep(3)
        html=driver.page_source
        bsobject=BeautifulSoup(html,"lxml")
        cont=bsobject.findAll(class_="u-courseCardWithTime-container_a160") 
        for items in cont:
            if 'href' in items.attrs: 
                if items.attrs['href'] in course_ls:
                    return
                course_ls.append(items.attrs['href']) #找到课程链接 
        for items in course_ls:
            course_url_ls.append("https:"+items) #构造完整url
        try:
            a = driver.find_element_by_link_text("下一页")  #翻页
            a.click()
            time.sleep(3)
        except:
            return
        OpenSchoolWeb(url)

    OpenSchoolWeb(school)   #打开该学校页面并获取所有课程
    driver.close()   #关闭浏览器
    
    CourseURLs=set(course_url_ls) #去重
    print("找到{}门课程".format(len(CourseURLs)))
    
    for course in CourseURLs:
        print("在读取的课程是：{}".format(course))
        result=[]
        result.append(str(school)[38:-3])  #第一个元素是该课程开设的高校
        GetDetail(course,result) #爬取课程页面信息
        f_csv.writerow(result) #写入数据
        print(result) #成功
csvFile.close() #结束关闭csv文件

