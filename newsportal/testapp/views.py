from django.shortcuts import render

# Create your views here.
def newspage(request):
    return render(request,'testapp/index.html')
def dev_views(request):
    head_msg='Developers information'
    sub_msg1='Full Stack Developers'
    sub_msg2='Python Developers'
    sub_msg3="java Developers"

    type ='dev'

    my_dict={'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}

    return render(request,'testapp/news.html',my_dict)
def sports_view(request):
    head_msg='Sports imformation'
    sub_msg1='Cricket information'
    sub_msg2='Football information'
    sub_msg3='Hockey information'

    type ='sports'

    my_dict={'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
def politics_view(request):
    head_msg='Political Information'
    sub_msg1='Local information'
    sub_msg2='National information'
    sub_msg3='International information'

    type ='politics'

    my_dict={'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3, 'type':type}
    return render(request,'testapp/news.html',my_dict)