from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # 首页 http://ip:port/polls/
    path('', views.index, name='index'),
    # 首页 问题列表 /polls/index/
    path('index', views.index, name='index'),
    # 问题详情 ex:/polls/1/
    path('<int:question_id>', views.detail, name='detail'),
    # 去投票，选项加一 /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    # 投票结果 /polls/2/results
    path('<int:question_id>/results', views.results, name='results'),

    #
    # path('simple/', views.SimpleView.as_view(), name='simple')

]

# django 1.x 写法 正则
# from django.conf.urls import url
# urlpatterns = [
#     # /polls/
#     url(r'^$', views.index, name='index'),
#     # /polls/index/
#     url(r'index$', views.index, name='index'),
#     # /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/s$'),
# ]

# 引入视图函数
# path()函数定义的路由会在项目启动时加载
# path('路由规则')
