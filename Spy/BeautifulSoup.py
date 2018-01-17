# coding=utf-8
from bs4 import BeautifulSoup
import re

# Only read. about del, modify, add please search other pages.

html = """
<html>
    <title name='projectName'>
        <h1>蛋卷问卷调查系统</h1>
        <h2><!--This is annotation--></h2>
        <h3><!--This is annotation-->Do not welcome you</h2>
    </title>
    <body id='formBody'>
        下面是一张表
        <form>
            <input type='radio'>男</input>
            <input class='2radius' type='radio'>女</input>
            <input class='2radius' id='name' type='text'>请输入姓名</input>
            <input id='hobby' type='text'>请输入兴趣</input>
            <a class="link" href="http://www.baidu.com" id="link1">百度一下，你就知道</a>  
        </form>
    </body>
</html>
"""

# html = re.sub(r'[\t\n\r\f\v]|([ ]{2,})|(<!---->)', '', html)
# print html
soup = BeautifulSoup(re.sub(r'[\t\n\r\f\v]|([ ]{2,})', '', html))
# print soup.prettify()

# print soup.title    # <title><h1>蛋卷问卷调查系统</h1><h2>不欢迎你</h2></title>
# print soup.input    # <input type="radio">男</input>
# print soup.html
# print type(soup.input)  # <class 'bs4.element.Tag'>

# print soup.name     # [document], soup is a Tag too
# print soup.title.name   # title
# print type(soup.title.name)     # <type 'unicode'>

# print soup.title.attrs      # {u'name': u'projectName'}
# print soup.input.attrs       # {u'type': u'radio'}
# print soup.title.attrs['name']   # projectName
#
# print soup.body.string      # None, oh how to get '下面是一张表'?
# print soup.input.string     # 男, Only match the first input
# print type(soup.input.string)   # <class 'bs4.element.NavigableString'>

# print soup.h2.string       # This is annotation
# print soup.h3.string        # None， it's because h3 not only cover annotation?
# print type(soup.h2.string)  # <class 'bs4.element.Comment'>, not bs4.element.NavigableString
# print type(soup.h3.string)  # <type 'NoneType'>

print soup.find_all('input')    # Return a list
print soup.find_all(re.compile('^h\d$'))    # Return h1, h2, h3
print soup.find_all(['h1', 'h2'])
for tag in soup.find_all(True):
    print tag.name      # Return all tag name


"""<div class="row lists">
      <div class="col-md-12" style="background:rgb(222, 236, 255);font-size: 15px; padding:10px">
        <div class="col-md-7" style="font-size:15px;padding-top:2px;">
          <div>
            <div style="color:rgb(37, 172, 37)">
            <i class="fa fa-circle-o-notch fa-spin"></i>&nbsp;进行中</div>
          </div>
        </div>
        <div class="col-md-5" style="padding-left:0px;padding-right:0px">
          <span style="display:inline-block; width:6em">实名</span>
          <span style="display:inline-block; width:7em">参与人数: 1</span>
          <span>截止时间: 2018-01-19 00:00</span>
        </div>
      </div>
      <div class="col-md-12" style=" font-size: 16px;margin:15px;margin-left:0px;margin-right:0px; padding-left:10px">
        <div class="col-md-6">
          <a href="javascript:;" style="margin-right:10px;color:black;text-decoration : none">公司员工家庭结构调查</a>
        </div>
        <div class="col-md-6" style=" font-size: 14px;padding-top:2px;padding-left:0px;padding-right:0px">
          <div style="float:right">
            <a href="javascript:;" style="cursor:not-allowed;margin-left:19px;margin-right:6px;color:rgb(150, 153, 159);display:inline-block;width:63px;">
                <i class="fa fa-edit">&nbsp;编辑</i>
              </a>
            <a href="javascript:;" style="margin-left:19px;margin-right:6px;color:black;display:inline-block;width:63px">
              <i class="fa fa-file-text-o">&nbsp;详情</i>
            </a>
            <a href="javascript:;" style="margin-left:19px;margin-right:6px;color:black;display:inline-block;width:63px">
              <i class="fa fa-line-chart">&nbsp;统计</i>
            </a>
            <a href="javascript:;" style="margin-left:19px;margin-right:6px;color:black;display:inline-block;width:63px">
              <i class="fa fa-clone">&nbsp;复制</i>
            </a>
            <a href="javascript:;" style="margin-left:19px;margin-right:6px;color:black;display:inline-block;width:63px">
              <i class="fa fa-trash-o">&nbsp;删除</i>
            </a>
          </div>
        </div>
      </div>
    </div>
"""
