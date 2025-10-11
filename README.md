# 자동 코드 생성기

## 목차
- [소개](#소개)
- [개요](#개요)
- [배경 및 선정 이유](#배경-및-선정-이유)
- [기술 스택](#기술-스택)
- [설치 및 실행 방법](#설치-및-실행-방법)
- [프로젝트 구조](#프로젝트-구조)
- [개발 과정](#개발)
- [최종 결과물](#최종-결과물)
- [참고 자료](#참고-자료)

# 소개
게임 제작 및 공유 메타버스 플랫폼인 메이플스토리 월드를 위해, Lua 스크립트 **자동 완성 및 코드 예시 생성**을 지원하는 Copilot 기능을 자체 파인튜닝 방식으로 개발하는 것을 목표로 한다.

이를 통해 다양한 도메인에 맞는 자동 코드 및 언어 생성 서비스가 가능하도록 한다.

## Quick Result

| 구분 | Perplexity(PPL) | eval_loss |
|-----|--|--|
학습 전  |  46.14            |  3.83       |  
학습 후  |  5.34             |  1.68       | 
```
Perplexity : math.exp(metrics["eval_loss"])

다음 토큰을 얼마나 자신 있게 예측하는지 나타내는 핵심 지표
```
- 아래와 같이 학습 후 플랫폼에 맞는 답변을 하는 것을 확인할 수 있다.

|입력 prompt | 학습 전 답변 | 학습 후 답변 | 기대값 |
|------------|--------------|---------------|--------|
|```# 두 수를 더하는 함수를```<br>``` 작성하시오. ```<br> ```function add(a,b)\n ```<br>```return a + ```|``b end`` | ``b``<br>``end``|``b``<br>``end``|
|```local currentTargetEntity = self.Entity.AI```| ```_TARGET```<br>```if not target then```<br>```return nil, "No Target"```<br>```end```|```ChaseComponent:```<br>```GetCurrentTarget()```| ```ChaseComponent:```<br>```GetCurrentTarget()```<br>[[코드 링크]](https://maplestoryworlds-creators.nexon.com/ko/apiReference/Components/AIChaseComponent)|
|```local pages = _BadgeService:```| ```get_badge_pages(user)```|```GetBadgesByUserId(userId)```|```GetBadgeInfosAndWait()``` <br>[[코드 링크]](https://maplestoryworlds-creators.nexon.com/ko/apiReference/Services/BadgeService)|
| ```self.ParticleComponent =```|```ParticleComponent```<br>```end```|```self.Entity.```<br>```ParticleComponent```| ```self.Entity.```<br>```AreaParticleComponent```<br>[ [코드 링크]](https://maplestoryworlds-creators.nexon.com/ko/apiReference/Components/AreaParticleComponent)|
    

# 개요 
본 프로젝트는 넥슨의 메이플스토리 월드 플랫폼에서 사용되는 Lua 기반 스크립트 코드를 대상으로, 자동 코드 생성(Auto Code Generation) 기능을 개발하는 것을 목표로 한다. 게임 개발에 특화된 Lua 스크립트와 메이플스토리 월드의 고유한 API 및 구조를 학습 데이터로 활용하여, 사용자 입력에 따라 자동으로 Lua 코드를 생성해주는 시스템을 구현한다. 이를 통해 개발의 효율성을 높이는 것을 주요 기대 효과로 삼았다.

# 배경 및 선정 이유
최근 IT 업계에서 각 기업들은 다양한 AI 프로젝트에 주목하고 있으며, 실제 공고나 프로젝트 사례를 살펴보면 코드 자동 생성, 자동 제안서 작성, 자동완성 등 사용자 입력을 기반으로 효율성을 높이는 시스템에 대한 수요가 꾸준히 증가하고 있음을 확인할 수 있습니다. 이러한 트렌드에 맞추어, 본 프로젝트에서는 자동 코드 생성 기능에 집중해보기로 결정하였습니다.

대상 플랫폼으로 메이플스토리 월드를 선정한 이유는, 이 플랫폼이 Lua를 기반으로 하면서도 자체적으로 커스텀된 문법, API, 함수 등을 폭넓게 제공하기 때문입니다.  또한, 활발한 개발자 커뮤니티와 풍부한 예시 코드 자료를 활용하여 충분한 학습 데이터를 수집할 수 있다는 점도 중요한 선정 기준이 되었습니다.

이러한 특성 덕분에 실제로 플랫폼별 특화 학습이 가능한지 확인할 수 있고, 자동 생성된 코드의 평가와 검증 과정도 상대적으로 명확하게 진행할 수 있다고 판단했습니다.

# 기술 스택
- 개발 및 실험 환경
    - Google Colab (모델 파인튜닝/실험)

- 프로그래밍 언어
    - Python (데이터 수집, 처리, 학습 파이프라인)
    - Lua (생성되는 스크립트 및 평가용)

- 데이터 수집/구성
    - BeautifulSoup (참고 사이트 크롤링, API·예시 코드 수집)
    - Perplexity 서비스(데이터셋 변환, jsonl 저장)

- 학습 데이터
    - Lua 기반 예시 코드, API 문서 등
    - [메이플스토리월드 API 레퍼런스](https://maplestoryworlds-creators.nexon.com/ko/apiReference/How-to-use-API-Reference)

- 모델 및 배포
    - Qwen/Qwen2.5-Coder-1.5B-Instruct
    - nuprl/MultiPLCoder-1b
    - Hugging Face로 모델 다운로드 및 배포

- 결과 활용/실행 환경
    - VS Code
    - Ollama, Continue(모델 연동 및 코드 테스트)

# 설치 및 실행 방법
## 모델 불러오기
```py
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("bangill/maplestoryworlds-lua-api-finetune")
model = AutoModelForCausalLM.from_pretrained("bangill/maplestoryworlds-lua-api-finetune")
```

## 모델 로컬 저장
- model과 tokenizer 모두 같은 곳에 저장 필요
```py
model.save_pretrained("폴더 주소", safe_serialization=True)
tokenizer.save_pretrained("폴더 주소", safe_serialization=True)
```

## gguf로 변환
- 위에서 저장한 폴더를 사용해서 gguf 파일로 변환
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
pip install -r requirements.txt
python convert-hf-to-gguf.py ../merged --outfile ../"원하는 모델명".gguf
```
## 학습된 모델로 기능 사용하기
[개발 부분 참고](#4-vs-code-적용)

# 프로젝트 구조

```
📦auto_gen_lang
 ┣ 📂1_train_data # 학습용 데이터 셋
 ┣ 📂api # 개발자 레퍼런스 사이트에 있는 api 종류. 예시 코드들 저장. 빈 파일은 예시 코드가 없다.
 ┃ ┣ 📂components_api
 ┃ ┣ 📂enums_api
 ┃ ┣ 📂logics_api
 ┃ ┣ 📂lua_api
 ┃ ┣ 📂miscs_api
 ┃ ┗ 📂services_api
 ┣ 📂huggingface # HuggingFace model에 README.md 업로드
 ┃ ┣ 📜hf_readme_upload.py
 ┃ ┗ 📜README.md
 ┣ 📜README.md
 ┣ 📜tree.txt
 ┣ 📜url_content.py # api 종류 저장 기능 코드
 ┗ 📜url_content_example_chrolling.py # 예시 코드 저장 기능 코드
 ```
# 개발
## 1. 모델 선정
- 선정 모델
    1) **Qwen/Qwen2.5-Coder-1.5B-Instruct** : 
        지난 한달 동안 10만 이상 다운로드를 할만큼 최근 개발자들 사이에서 경량화 llm 중 높은 성능을 보이는 모델이다. 대중적인 c, python, java와 같은 코드를 학습했을 뿐 아니라 lua언어도 학습을 진행하였기 때문에 모델로 선정하였다.
        뿐만 아니라 어댑터를 활용하여 ollama를 이용하려면 ollama에서 서비스 하는 모델을 사용해야하는 제약이 있었다.
    2) **nuprl/MultiPLCoder-1b** : 
        소형 llm임에도 불구하고, lua 같은 저자원 언어에 특화되어있다는 평이 있다. 즉, 이용 횟수는 적지만  현재 상황에 맞는 모델이라 선정하였다.

## 2. 데이터 수집

### 1) api 종류 수집
```
url_content.py 파일 활용
```
- Components (100개)
    - "AIChaseComponent","AIComponent", ...
- Events (179개)
    - "ActionStateChangedEvent","AnimationClipEvent", ...
- Services (38개)
    - "BadgeService","CameraService", ...
- Logics (8개)
    - "DefaultUserEnterLeaveLogic","Logic", ...
- Misc (94개)
    - "AnimationClip","AvatarBodyActionElement", ...
- Enums (94개)
    - "AccountRegion","AccountTrustLevel", ...
- Lua (7개)
    - "global","math", ...

### 2) 각 api의 예시 코드 수집
```
url_content_example_chrolling.py 파일 활용
```
각 카테코리에 맞게 폴더에 txt 파일로 예시 코드들 수집한다.
예시 코드가 없는 경우가 있어서, 빈 파일이 존재한다.

### 3) 데이터셋 생성
#### LLM을 활용하여 데이터셋 생성
생성된 txt 파일을 활용하여 LLM에 입력하고, 나온 값들을 데이터셋으로 활용한다. 사용한 모델과 프롬프트는 다음과 같다.

```
모델 : OpenAI GPT-4 Turbo
엔진 : Perplexity
프롬프트 : 

아래 규칙에 따라 소스코드를 자동 코드 완성 모델의 fine-tuning용 dataset으로 변환해줘.

- 각 prompt는 사용자가 실제 자동완성을 원할 만한 코드의 한 줄 또는 짧은 블록으로(줄바꿈 포함 가능), 앞에 오는 코드만 담는다.
- 각 completion은 그 prompt 다음 작성될 실제 코드(한 줄 또는 코드 블록)로, 줄바꿈이 필요하면 포함하게 해라.
- 불필요한 설명, 선언, 주석, 빈 줄 등은 모두 제외한다.
- prompt, completion을 key로 갖는 jsonl 샘플만 출력하라(예시 및 설명 없이 코드만).

아래의 소스를 위 기준에 맞춰 변환하라.

소스:

<여기에 붙여넣기>

```

이렇게 생성된 jsonl 파일을 1_train_data 폴더에 저장하여 추후 학습시에 불러내어 사용한다.

## 3. 파인튜닝
### PEFT 기법 활용 (LoRA)
PEFT란? : Parameter-Efficient Fine-Tuning 으로 계산 효율성과 자원 절약을 위해 쓰이는 방법

LoRA란? : Low-Rank Adaptation 으로 소수의 파라미터만 업데이트하는 방식

```
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    task_type="CAUSAL_LM",  # 텍스트 생성(코드 완성) 작업 유형
    inference_mode=False,   # 훈련 모드로 설정
    target_modules=["c_fc", "c_attn", "c_proj"], 
        # c_attn : 입력을 attention에 맞게 쿼리로 변환하는 레이어, 
        # c_proj : attention 결과를 다시 모델 내부 차원으로 투영하는 레이어,
        # c_fc : 입력을 변화하는 레이어
        # 주요 동자과 의미를 담당하는 부분만 업데이트.
    r=16,                    # Low-rank 행렬의 차원. (보통 8, 16, 32 사용)
    lora_alpha=32,          # 스케일링 요소. 보통 r의 2배 또는 4배로 설정.
    lora_dropout=0.1,       # LoRA 레이어에 적용할 드롭아웃 비율
)

model = get_peft_model(model, lora_config)
```

### train 파라미터 설정
```
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./multiplcoder-1b-lua-finetuned", # 모델 체크포인트와 로그 파일 등이 저장되는 디렉토리 경로
    per_device_train_batch_size=1, # 각 GPU/CPU별로 한 번에 처리할 데이터 샘플 개수
    gradient_accumulation_steps=4, # 미니배치 여러 번의 결과를 합산해서 한 번만 파라미터 업데이트
    max_steps=500, # 최대 학습 반복 횟수
    save_steps=200, # 지정 step마다 체크포인트 저장.
    save_total_limit=2, # 저장할 체크포인트 모델 개수. 오래된 것은 삭제.
    num_train_epochs=3, # 전체 데이터셋을 몇 반복할지.
    weight_decay=0.01, # 과적합 방지 규제 인자.
    warmup_ratio=0.03, # 초기 학습률 상승 규제 인자.
    logging_steps=10, # 로그 출력 정보
    bf16=False, # 연산에 부동소수점 계산을 사용할지 설정. 
    fp16=True,        
    optim="adamw_torch", 
    report_to=[],
    learning_rate=1.2e-4, # 학습률 지정
)
trainer = Trainer(
    model=model,
    args=training_args, # 위에서 설정한 세부 argument
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=data_collator,
    processing_class=tokenizer,
)
```
결과에 가장 많은 영향을 끼친 파라미터 :
model, max_steps, learning_rate

#### model
모델 Qwen/Qwen2.5-Coder-1.5B-Instruct 에서 모델 nuprl/MultiPLCoder-1b 으로 변경하였더니 
learning rate 1.5e-4 기준 학습후 eval_loss가 2.586 에서 1.66으로 감소

#### max_steps
모델 nuprl/MultiPLCoder-1b 기준, max_steps를 200에서 500으로 변경하였더니 Training Loss가 1.83 에서 1.14 까지 감소

#### learning_rate
rate를 높일수록 eval_loss가 줄어드는 것을 확인. 하지만, 어느 정도 이상이 되면 과적합이 일어나면서 **파멸적 망각** 상태가 되는 것을 확인. 이전에 학습되어 잘 결과가 나오던 것이 추가 학습후 잊어버리는 상황.

## 4. vs code 적용
ollama와 vscode의 확장 프로그램 continue를 활용해서 연동.

### Modelfile 작성
```
# Modelfile
FROM ./"원하는 모델명".gguf # FROM ./maple_finetune.gguf
PARAMETER temperature 0.2
TEMPLATE "{{ .System }}\n{{ .Prompt }}"
SYSTEM "You are a helpful coding assistant."
```

### ollama 이용 서버 등록
- ollama 다운 필요
#### 1) 서버 기동
```
ollama serve
```

#### 2) Modelfile로 모델 생성
```
ollama create "알아보기 위한 모델명 지정" -f ./Modelfile
# ollama create "maple_finetune" -f ./Modelfile
```

#### 3) 실행
ollama run "알아보기 위한 모델명 지정"

## VS code의 continue와 ollama 연결
- config.yaml 파일 작성
```
name: My Local Config
version: 1.0.0
schema: v1

models:
  - name: "실행시킬 모델명" # name: maple_finetune
    provider: ollama
    model: "실행시킬 모델명" # 만약 version이 있다면 명시. model : maple_finetune:latest
    # Ollama 서버 주소를 명시적으로 지정합니다.
    apiBase: http://127.0.0.1:11434
    # 요청 타임아웃을 60초(60000ms)로 넉넉하게 설정합니다.
    requestOptions:
      timeout: 60000
    roles:
      - autocomplete
```
Continue 설정 파일 config.yaml는 사용자 홈 디렉터리의 .continue 폴더에 있으며, 없으면 새로 생성하면 된다.

작업하는 root에서 .continuerc.json으로 프로젝트별 설정도 가능.

## 트러블 슈팅
###  i) 모델 선정 및 변경
- 로컬에서 원하는 모델을 사용하기 위해 ollama 서비스를 사용하기로 결정. 뿐만 아니라, 좀 더 편리하게 사용하려면 ollama에서 서비스하고 있는 모델을 사용하고 adapter를 활용하여 파인튜닝한 모델을 사용할 수 있었다. 하지만 빌드를 할 때 adapter 사용에 문제가 발생.
- 뿐만 아니라, adapter를 사용하지 않음으로써 똑같이 gguf 파일로 모델을 저장하여 local에서 서빙해서 사용하게 되었다. 따라서 lua에 특화되어 학습된 nuprl이 더 적합하다고 판단하여 변경하였다.

### ii) 데이터 수집 부분
- 코드 자동 생성이기 때문에 정제되고, 정갈한 코드 예시들이 필요했다. 하지만 github에 ``maplestory-world``, ``maplestoryworld``, ``nexon``으로 검색한 결과 lua 언어로 생성된 레포지토리가 20개 남짓뿐이라 학습할 수 있는 데이터들이 매우 적었다.
- 개발자 api reference 사이트에서 예시 코드들을 활용하였지만, 적합한 dataset을 구성하기 어려웠다. 실제 사용하는 코드들이 아니기 때문에, 어떤 코드가 maplestory world만의 특별한 코드인지 파악할 수 없었다. 따라서 학습의 정도와 예시 데이터를 명확하게 구분하지 못하여 학습용 데이터 세트의 질이 낮았다고 판단된다.

### iii) vs code 적용 부분

#### ollama
- ``save_pretrained``를 통해 저장된 토크나이저와 모델을 바로 사용할 수 없고, 한 번 더 변환을 거쳐야 하는 것이 번거로웠다.
- 하지만 이미 서비스 되어있는 모델이거나, gguf 파일로 변환된 모델이라면 쉽게 호출할 수 있어서 편리하였다.

#### continue
- ``github copilot``이 있다면 충돌이 일어나는 듯한 버벅임이 있었다. copilot도 삭제하고, continue도 삭제하고 다시 설치하였다.
- ollama의 모델과 continue와 연동을 하고자 config 파일을 수정해야한다. 일부 문서에서는 config.ts 파일을 생성 및 수정하게 안내를 하는데, 버전에 따라 맞지 않은 경우가 있는 듯하다. 본 프로젝트에서는 config.ts 파일이 아닌 config.yaml 파일을 사용하였다.
- google colab에서 prompt를 통해 얻은 답변과 학습된 해당 모델을 continue에 연결해서 얻어낼 때의 답변이 상이하다. 그 이유는 코드로 프롬프트를 통해 생성할 때는 generate할 때 세세하게 파라미터를 설정할 수 있는 반면, continue에서는 그러지 못해 생기는 차이라 판단하였다.

### iv) 생성 부분
- lua 언어 자체가 저자원 언어이기 때문에 제대로 학습이 된 모델이 없었다. 따라서 ``function add(a,b)\n return a+`` 와 같은 프롬프트를 작성했을 때 ``function add(a,b)\n return a+10*b \nend``와 같이 일반적이지 않은 답변을 하기도 하였다. ``# 두 수를 더하는 함수를 작성하시오. function add(a,b)\n return a + ``와 같이 주석으로 설명을 추가해야만 정확한 답변이 가능하였다.

# 최종 결과물

## Hugging Face 모델 등록
모델을 등록하였고, 기존 모델과 학습된 모델의 답변을 비교할 때는 ``AutoTokenizer``,``AutoModelForCausalLM``,``from_pretrained`` 를 활용하여 모델 사용을 하였다.
링크 : https://huggingface.co/bangill/maplestoryworlds-lua-api-finetune

## continue 연결
결과적으로는 학습된 모델을 활용해서 continue 프로그램에 연결을 하여 vs code에서 test를 진행할 수 있었다. 하지만 위에서 언급된 것처럼 colab에서 이루어지는 답변과 차이가 있었다.

- function add
<img width="480" alt="Image" src="https://github.com/user-attachments/assets/2f474dba-8489-46bf-a50e-0087e37abb49" />

- current target entity
<img width="480" height="1020" alt="Image" src="https://github.com/user-attachments/assets/5f8dc703-660d-486b-a136-cc41585f56b7" />

# 느낀점

1. 충분히 다양한 직군에서 활용할 수 있을 것이라고 판단된다. Lua 라는 저자원 언어를 가지고 파인 튜닝을 통해 학습시켜 어느 정도의 성과를 낼 수 있었기 때문이다. 이와 마찬가지로 회사의 보고서 양식이나 단어들을 학습시켜서 일반 LLM 모델과의 차이를 둘 수 있을 것이라 생각한다.
<br>

2. 파인 튜닝 뿐만 아니라 RAG를 활용해서 결과값을 도출하는 방법도 있다. 현재, 현업에 있는 개발자가 말하길 파인 튜닝도 좋지만 RAG를 사용을 고민하고 있는 상황이라고 하였다. 하지만 이 같은 경우에는 현 프로젝트처럼 continue 프로그램을 활용하기 보다는 회사의 자체 RAG 기반 LLM을 탑재한 프로그램을 개발하여야 한다.
<br>

3. 쓰레기 데이터를 넣으면 쓰레기 모델이 나온다. 학습을 시킬 때 정제되지 않은 프롬프트와 컴플리션을 제공하였기 때문에 추후 모델을 사용할 때도 답변을 진행할 때 깔끔하지 않은 답변이 제공되기도 하였다. 이는 실제 사용하는 언어가 아니라 무엇이 중요하고 필요한 코드인지 검사를 하지 않았기 때문이다. 실제 회사에서 적용할 때는 데이터셋부터 현업자의 협업이 필요하다.
<br>
 


# 참고 자료
https://github.com/ggerganov/llama.cpp

https://apidog.com/kr/blog/how-to-download-and-use-ollama-kr/

https://goddaehee.tistory.com/381

https://hyunicecream.tistory.com/123

https://maplestoryworlds-creators.nexon.com/ko/apiReference/How-to-use-API-Reference

https://ysg2997.tistory.com/11

https://ysg2997.tistory.com/8

https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct

https://huggingface.co/nuprl/MultiPL-T-StarCoderBase_1b

https://docs.continue.dev/reference

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.
