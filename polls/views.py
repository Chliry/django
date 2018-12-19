from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.


# def index(request):
#     return HttpResponse("""
#     <html>
#         <head></head>
#         <body>
#             <h3>Hello</h3>
#         </body>
#     </html>
#     """)


# def index(request):
#     """
#     展示问题列表
#     :return:
#     """
#     question_list = Question.objects.all().order_by('-pub_date')[:5]
#     # output = ''
#     # for q in question_list:
#     #     print(q.id, q.question_test, q.pub_date)
#     #     output = output + q.question_test + ','
#     #     print(output)
#
#     # output = ','.join([q.question_test for q in question_list])
#     # return HttpResponse(output)
#     output = loader.get_template('polls/index.html')
#     context = {
#         'question_list': question_list
#     }
#     # return render_template('.html', q_list = q_list, arg2=arg3)        flask写法
#     return HttpResponse(output.render(context, request))


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    显示问题详细信息、内容、发布时间、选项内容、每项票数。
    :param request:
    :param question_id:
    :return:
    """
    try:
        question = Question.objects.get(id=question_id)
        # choices = Choice.objects.filter(question_id=question_id)

        # orm框架的代劳，question可直接带出对应的choices
        # Question.choice_set.all()

        # 前端模板语言本质是后端代码，可以吧上句放在html网页中

    except Question.DoesNotExist:
        raise Http404("Don\'t have this id.")
    # question = Question.objects.get(id=question_id)
    # if not question:
    #     raise Http404("Don\'t have this id.")
    context = {
        'question': question,
        # 'choices': choices
    }
    return render(request, 'polls/detail.html', context)

    # question = get_object_or_404(Question, id=question_id)
    # return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    """
    投票
    :param request:
    :param question_id:
    :return:
    """
    try:
        question = Question.objects.get(id=question_id)
        choice = question.choice_set.all()
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(id=choice_id)
    except Question.DoesNotExist as e:
        error_message = "Don\'t have this id"
    except Choice.DoesNotExist as e:
        error_message = "Don\'t have this option"
        return render(request, 'polls/detail.html', context={
            'question': Question,
            'error_message': error_message
        })
    else:
        # sql update choice set vote=vote+1 where id=2
        selected_choice.votes += 1
        # commit
        selected_choice.save()
        # 投票完成重定向到 views.results(qid)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    """
    投票结果
    :param request:
    :param question_id:
    :return:
    """
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/results.html', {"question": question})


# 通用模板
# class SimpieView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'question_list'
#
#     def get_queryset(self):
#         return Question.objects.all()
