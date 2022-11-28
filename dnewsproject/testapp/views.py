from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'testapp/index.html')

def movie_view(request):
    head_msg = 'Movies Information'
    msg1 = 'RRR movie is going to Aascar Award'
    msg2 = 'RadheShyam movie Awesome'
    msg3 = 'AadhiPurush movie is not up to the mark'
    my_dict = {
        'head_msg':head_msg,
        'msg1':msg1,
        'msg2':msg2,
        'msg3':msg3
    }
    return render(request,'testapp/demo.html',my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    msg1 = 'RRR movie is going to Aascar Award'
    msg2 = 'RadheShyam movie Awesome'
    msg3 = 'AadhiPurush movie is not up to the mark'
    my_dict = {
        'head_msg':head_msg,
        'msg1':msg1,
        'msg2':msg2,
        'msg3':msg3
    }
    return render(request,'testapp/demo.html',my_dict)

def politics_view(request):
    head_msg = 'Politics Information'
    msg1 = 'RRR movie is going to Aascar Award'
    msg2 = 'RadheShyam movie Awesome'
    msg3 = 'AadhiPurush movie is not up to the mark'
    my_dict = {
        'head_msg':head_msg,
        'msg1':msg1,
        'msg2':msg2,
        'msg3':msg3
    }
    return render(request,'testapp/demo.html',my_dict)
