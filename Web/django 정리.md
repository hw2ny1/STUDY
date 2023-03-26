# Django

### django 기본

- 서버를 구성하기 위한 Framework
- Framework 란 서비스 개발에 필요한 기능을 미리 구현해 모아 놓은 툴.



### django 순서

- 설치
  - 가상 환경 생성 :  python -m venv venv
  - 가상 환경 활성 : source venv/Scripts/activate <-> deactivate
  - django 설치 : pip install django==3.2.18
  - 프로젝트 생성 : django-admin startproject 프로젝트이름 .
  - 서버 실행 : python manage.py runserver
  - 가상환경 패키지 저장 : pip freeze > requirements.txt
  - 가상환경 패키지 설치 : pip install -r requirementx.txt
- 요청과 응답
  - Model & View & Template : MTV 구조
  - urls -> view -> template 의 흐름으로 진행됨을 기억하자.
  - view에서 render 함수로 html을 불러올 때, 앱이름/templates/앱이름/html파일 로 경로를 잡아준다.
  - HttpResponse(f"출력할 태그") 로 출력 가능
  - render (request, template_name, context)
    - request : 응답을 생성하는데 사용되는 요청 객체
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
    - 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)
  - url에서 path(경로, views.함수) -> view에서 render(html) -> template의 html
- django template
  - {{ Varialbe }} : 변수명은 밑줄로는 시작할 수 없고 dot(.)을 사용하여 속성에 접근 가능.
  - Filters : 변수를 수정할 때 사용 ex) {{ name|lower }} : 소문자로 출력
  - Tags : 출력 텍스트를 만들거나, 반복 또는 논리를 수행하는 등 복잡한 일 수행.
  - context로 전달할 데이터가 많아질 경우 딕셔너리로 전달하는 것이 바람직.
  - 템플릿 상속은 상단에 {% extends '' %} 사용. {% block name %}{% endblock name %}으로 지정.
  - base 에서 templates 사용시 settings.py 의DIRS에 표시해 줘야함.
- django urls
  - variable routing : URL 주소를 변수로 사용하는 것을 의미.
  - path ('페이지/<타입>/', views.함수) 를 이용하여 views에 있는 함수의 인자로 할당.
  - 함수에서는 request 외에 할당된 변수를 인자로 받고 템플릿 변수로 사용.

- App URL mapping

  - urlpattern은 언제든지 다른 URLconf 모듈을 포함할 수 있다.

  - path에서 include('appname.urls')로 넘김.

  - Naming URL patterns : path 만들 때, name='url태그' 를 정의하여 URL 이름을 지정.

  - URL namespace : 서로 다른앱에서 동일한 URL 이름을 사용해도 고유하게 사용 가능.

    ex) {% url 'articles:index' %}



- Authentication System

  - 커스텀 유저 모델을 사용하기 위해서 settings.py에 AUTH_USER_MODEL = 'auth.User'을 추가해 줘야함.

  - models에 from django.contrib.auth.models import AbstractUser 해주고 User 작성.

  - admin site에 등록하기 위해 djang.contrib.auth.admin import UserAdmin 해주고 

    admin.site.register(User,UserAdmin)

  - from django.contrib.auth import login as auth_login

  - form = AuthenticationForm(request, request.POST)

  - auth_login(request, form.get_user()) 에서 get_user() 은 AuthenticationForm의 매서드.

  - settings에서 설정되어 있기 때문에, context 없이도 user 변수를 사용할 수 있다. 

  - logout은 from django.contrib.auth import logout as auth_logout해주고  auth_logout(request)

- Authentication System 활용

  - 회원 가입 페이지 작성은 User CreationForm 사용, Post로 받아 온 후 is_valid()후 save()
  - 커스텀form 이용시 오류가 뜨므로 UserCreationForm() 커스텀 필요
  - django.contrib.auth.forms import UserCreationForm, UserChangeForm 이용
  - UserCreationForm을 요소로 하는 클레스에서 Meta(UserCreationForm.Meta): model = get_user_model() 작성. UserChangeForm도 동일하게 작성.
  - form.save()에서 user값을 반환하므로 그 값으로 login하면 됨.
  - UserChangeForm사용시 instance = request.user 인자로 넘기기.
  - fields = ('설정')시 필요한 값만 노출 가능.
  - 비밀번호 변경 페이지는 PasswordChangeForm 사용하여 동일하게 진행.
  - 비밀번호 변경후 로그인 유지를 위해 update_session)_auth_hash(request, form.user) 사용

- HTTP decorators

  - django.views.decorators.http 에서 import
  - require_http_methods, post, safe 등 사용 가능

- Limiting access

  - request.user.is_authenticated를 이용하여 로그인과 비로그인 상태에서의 차이 출력 가능.
  - if request.user.is_authenticated를 이용하여 로그인 로직 수행할 수 없게 처리 가능.
