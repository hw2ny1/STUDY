## Github 사용법

1. 폴더 주소에서 `cmd`입력하여 명령프롬프트 접속 후 `git init`으로 .git 생성

2. `git add [   ]`로 Staging Area로 추가

3. `git commit` 혹은 `git commit -m [   ]`로 commit 할 수 있다

4. `git push [   ] or origin`를 이용하여 Repository에 저장

   ---

## 포인트

- git config --global을 이용하여 email, user name 등록하기

- git origin 등록하기

- `git config --list`로 정보 확인 가능

- `git remote add origin [주소]`를 이용하여 origin 등록

- `git status`로 중간 현황 확인 가능

- `git add -A`를 이용하여 한번에 추가 가능

- `git branch` 그리고 `git checkout`으로 branch 변경 가능

- `git clone [주소]`로 Github에서 다운로드 가능

- 원격 Github를 가져와서 push 오류시

  `git pull origin (branchname) --allow-unrelated-histories` 이용

- 