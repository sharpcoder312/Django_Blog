from django.contrib.auth.forms import UserCreationForm


class AccountCustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = False
        self.fields['password1'].help_text = '기호, 영어 소문자, 숫자를 혼합하여 10자리 이상'
        self.fields['password2'].help_text = False


class AccountUpdateForm(UserCreationForm):  # UserCreationForm 상속
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   # 기존의 UserCreationForm 초기화

        self.fields['username'].disabled = True
        self.fields['username'].help_text = False
        self.fields['password1'].help_text = '기호, 영어 소문자, 숫자를 혼합하여 10자리 이상'
        self.fields['password2'].help_text = False

# fields로 가지고있는 값 중에
# 아이디를 마음대로 바꾸지 못하게 하기위해서 아이디 인풋창을 비활성화 시킨다.
