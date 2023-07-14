# 1. 원격저장소 만들기
* git remote
  * git remote add origin https://github.com/Sohyeon-Choi/intro.git
  
## 1-1 push

* git remote -v origin  https://github.com/Sohyeon-Choi/intro.git (fetch)
origin  https://github.com/Sohyeon-Choi/intro.git (push)



# Git 버전관리 방법

1. `폴더` 생성

* `~`는 맨 처음 폴더이기 때문에, 실습할 폴더 생성
   * 처음에는 "origin"이라는 폴더 생성 
   * `mkdir [폴더명]`

2. `파일` 생성
* touch [a.txt]

3. git add [a.txt]

4. git commit -m "Add.a.txt" 

5. `Github 업로드`
* git push origin master

6. `Github에서 버젼 관리 확인`

# 2. Colaboration

## 1. `git clone `

* 다른 사람 폴더 복제

 1. git clone [주소] [지정폴더이름]
 1. cd [해당폴더]/
 1.  code.

## 2. `깃 허브에서 가져오기`

* git pull origin master

##### 기타

* `q`창 나가기

* ###### `git clean`

  1. 추적되지 않은 파일 제거: `git clean -n` 또는 `git clean --dry-run` 명령은 어떤 파일들이 제거될 것인지 미리 확인할 수 있습니다. 실제로 파일을 제거하지 않고, 제거될 파일 목록만 표시됩니다.
  2.  추적되지 않은 파일 실제 제거: `git clean -f` 또는 `git clean --force` 명령은 추적되지 않은 파일을 실제로 제거합니다. 제거할 파일 목록은 `git clean -n` 명령으로 사전에 확인하는 것이 좋습니다.
  3. 디렉토리 제거: `git clean -df` 명령은 추적되지 않은 파일뿐만 아니라 추적되지 않은 디렉토리까지 제거합니다. `-d` 옵션은 디렉토리를 제거하도록 지정하고, `-f` 옵션은 강제로 제거하도록 지정합니다.
  4. `.gitignore`에 지정된 파일 제외하고 제거: `.gitignore` 파일에 지정된 파일은 기본적으로 `git clean` 명령의 대상에서 제외됩니다. 하지만 `-x` 옵션을 사용하여 `.gitignore`에 지정된 파일도 제거할 수 있습니다. 예를 들어, `git clean -xf` 명령은 `.gitignore`에 지정된 파일도 제거합니다.
  5. 디렉토리 및 서브모듈 제거: `-d` 옵션을 사용하여 디렉토리를 제거하는 경우, 해당 디렉토리에 있는 Git 서브모듈도 함께 제거합니다. `-f` 옵션은 강제로 제거하도록 지정합니다. 예를 들어, `git clean -df` 명령은 디렉토리와 서브모듈을 제거합니다.
  
  주의할 점은 `git clean` 명령은 제거한 파일을 복구할 수 없으므로 신중하게 사용해야 합니다. 제거되는 파일은 로컬 저장소에서만 제거되며, 원격 저장소에는 영향을 주지 않습니다.
  
  ### git stash
  
  `git stash` 명령은 현재 작업 중인 변경사항을 일시적으로 저장하는 데 사용되는 Git의 기능입니다. 이를 통해 커밋하지 않은 변경사항을 임시로 보관하고, 다른 작업이나 브랜치로 전환할 수 있습니다. `git stash`를 사용하면 변경사항을 커밋하지 않고도 안전하게 작업을 전환할 수 있습니다.
  
  `git stash` 명령의 주요 사용법은 다음과 같습니다:
  
1. 현재 변경사항 보관: `git stash` 명령은 현재 작업 디렉토리의 변경사항을 스택에 저장합니다. 커밋되지 않은 변경사항만 저장되며, 추적되지 않는 파일은 제외됩니다.
1. 스태시 목록 확인: `git stash list` 명령은 스태시 스택에 저장된 모든 스태시 목록을 보여줍니다. 각 스태시에는 고유한 식별자와 저장된 날짜 및 시간이 표시됩니다.
1. 스태시 적용: `git stash apply` 명령은 가장 최근의 스태시를 작업 디렉토리에 적용합니다. 변경사항이 적용되지만 스태시는 스택에 그대로 남아 있습니다.
1. 특정 스태시 적용: `git stash apply stash@{n}` 명령은 특정 스태시를 작업 디렉토리에 적용합니다. `stash@{n}`은 스태시 목록에서 해당 스태시의 식별자를 의미합니다.
1. 스태시 제거: `git stash drop` 명령은 가장 최근의 스태시를 제거합니다. 스태시를 사용한 후에는 필요 없는 경우에 해당 스태시를 제거할 수 있습니다.

6. 특정 스태시 제거: `git stash drop stash@{n}` 명령은 특정 스태시를 제거합니다.
7. 스태시 적용 및 제거: `git stash pop` 명령은 가장 최근의 스태시를 적용하고, 해당 스태시를 스택에서 제거합니다. 한 번에 적용하고 제거하려는 경우 유용합니다.

스태시는 현재 작업 중인 변경사항을 일시적으로 저장하고 다른 브랜치로 전환하거나 다른 작업을 수행하는 동안 유용합니다. 필요한 경우 스태시를 다시 적용하여 변경사항을 가져올 수 있습니다.

# 하나의 파일로 다른 사람과 협업을 해보자

> 우선 팀장은 시작전에 github에서 wordchain이라는 Repositories를 만들어 준 뒤 팀원을 초대해 주자

## 팀장부터 시작

1. git으로 Home에 새로운 폴더를 만들어준 뒤 `git init` 으로 git을 시작해 준다.

   > github에서는 readme 파일은 바로 미리보기를 할 수 있게 만들어져 있다.

```
$ mkdir wordchain
```



1. git init으로 git을 실행시켜준다.

```
$ git init
Initialized empty Git repository in C:/Users/lsjls/wordchain/.git/
```



1. vs code를 열어준다.

vs code는 git에서 `code .`을 이용해 켤 수 있다.

```
$ code .
```



1. vs code 내에서 파일을 새로 만들고 파일 이름을 README.me로 만들어준다.

2. 이후 아래에 터미널을 열어 git bash로 설정

3. 해당 파일을 `git add` `git commint``git remote add origin [주소]` `git push`

   순서대로 진행해 준다.

```gitbash
$ git add README.md

$ git commit -m "add 침구류"
[master 27911c9] add 침구류
 1 file changed, 2 insertions(+), 1 deletion(-)
 
$ git remote add origin https://github.com/mizima1015/wordchain.git
 
$ git remote  #remote 상태 확인
origin

$ git push origin master
```



## 팀원

1. 팀원은 git에서 `clone`을 통해 복사해 준 뒤

   ```
   git clone [받아올 주소] [파일명 지정]
   ```

2. cd [파일명]/   

3. 폴더 안으로 들어가 `code .` 으로 vs code를 열어 사용

4. 파일을 수정한 뒤 ***vs code 상에서 저장***

5. `git add [파일이름]` `git commit -m "설명추가"` `git push` 순서로 쭉 진행해 주면된다.

6. 이후 팀장은 vs code에서 `git pull`을 이용해 파일을 다시 받아 들인 뒤 이후는 반복작업이다.
