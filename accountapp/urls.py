from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
    # 클래스형은 클래스를 불러올때 as_view함수를 꼭 써줘야한다.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # loginview는 logoutview와는 다르게 template는 지정해주어야 한다.
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    # detail은 특정 유저의 정보를 봐야하기에 특정 유저의 primary key(id)가 필요하다. 특정 유저객체에 대한 고유한 key.
    # <int:pk> - pk라는 이름의 integer정보를 받겠다. ex) 몇 번 유저의 객체에 접근할 것인가.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
