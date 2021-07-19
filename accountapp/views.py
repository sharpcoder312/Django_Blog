from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld
from accountapp.forms import AccountCustomForm, AccountUpdateForm
# from django.contrib.auth.forms import UserCreationForm

has_ownership = [account_ownership_required, login_required]


@login_required
# decorator의 login_required를 사용하게되면 로그인 유무를 확인하고 return해주는 것까지 기능하게된다.
# 대신 클래스형 view의 메서드에는 적용안됨.
def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        # data받기 - 사용자로부터 helloworldinput이라는 name을 가진 data를 임시변수 temp에 저장
        new_hello_world = HelloWorld()
        # helloworld에서 나온 새로운 객체(인스턴스) - newhelloworld에 저장.
        new_hello_world.text = temp
        new_hello_world.save()  # 실제로 helloworld DB에 저장
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # HttpResponseRedirect - accountapp의 helloworld로 재접속
        # reverse - accountapp:hello_world로 갈 경로를 다시 만들어줌
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User    # 무슨 모델? 장고에서 기본으로 제공해주는 모델 - User
    form_class = AccountCustomForm   # 장고에서 기본적으로 제공해주는 Form
    success_url = reverse_lazy('accountapp:hello_world')
    # reverse_lazy인 이유는 함수와 클래스가 파이썬에서 불러와지는 방식의 차이가 있기때문이다.
    # 계정 만들기에 성공했다면 어느 경로로 재연결 할 것인가?
    template_name = 'accountapp/create.html'  # 회원가입할 때 볼 template(html)


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    # 다른 사람이 특정 사람의 페이지의 정보를 볼 수있게함. mypage누르면 항상 본인 정보 x
    template_name = 'accountapp/detail.html'
    # 디테일 뷰는 create뷰와 달리 form이나 계정 생성 성공했을 때 리다이렉트할 경로를 지정해 주지않아도 되며 모델 안의 정보를 어떻게 시각화해줄지만 생각하면된다.


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
# 전역(일반)함수에서 사용하는 decorator를 메서드에서 사용할 수 있도록 변환해주는 decorator // @method_decorator(decorator, 적용할 메서드이름)
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    # def get(self, *args, **kwargs):
    #     # self는 현재 view를 가리키며 // 함수형 view에서 if문의 역할 (get,post방식 나누기)  <=> 클래스형 view에서 메서드의 역할
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         # get_object()는 현재 view에서 사용되고있는 User Object 중에서 pk에 해당하는 유저 객체를 가져옴
    #         return super().get(*args, **kwargs)  # 로그인 되어있으면 그대로 유지
    #     else:
    #         return HttpResponseForbidden()

    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
