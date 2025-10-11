---
language:
  - en
  - ko
tags:
  - text-generation
  - code
  - lua
  - maple
  - lora
license: apache-2.0
datasets:
  - maple-api-examples
base_model: nuprl/MultiPL-T-StarCoderBase_1b
---

# MapleStory Worlds Lua Fine-tuned Language Model

## 📖 Model Overview
This model is fine-tuned on MapleStory Worlds Lua API sample code.
It is optimized for game script automation, code generation, and context-aware API usage.

## 🤖 How to Use
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained('your-hf-id/model-name')
model = AutoModelForCausalLM.from_pretrained('your-hf-id/model-name')

inputs = tokenizer("local currentTargetEntity = self.Entity.AI", return_tensors='pt')
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs))
```


## ⚙️ Training & Experiment Settings
- Batch size: 1
- gradient_accumulation_steps: 4
- Epochs: 3
- Learning rate: 1.2e-4
- Optimizer: AdamW, fp16
- LoRA(PEFT) fine-tuning

## 📊 Performance

|        | Before   | After    | Change  |
|--------|----------|----------|---------|
| Perplexity  | 46.14    | 5.34     | ↓8.6x   |
| Eval loss   | 3.83     | 1.68     | ↓       |
| Speed(sec)  | 1.30s    | 1.28s    | -       |

Perplexity measures prediction difficulty for language models. Lower values mean more accurate predictions.

## 🗃️ Data
- Official MapleStory Worlds Developer API sample code
- [API Reference](https://maplestoryworlds-creators.nexon.com/ko/apiReference/How-to-use-API-Reference)

## 📄 License
Base model: nuprl/MultiPL-T-StarCoderBase_1b  
Hugging Face: [nuprl/MultiPL-T-StarCoderBase_1b](https://huggingface.co/nuprl/MultiPL-T-StarCoderBase_1b)

## Contact
name: bangill  
mail: [95potter95@gmail.com](mailto:95potter95@gmail.com)

---

# MapleStory Worlds Lua 파인튜닝 언어모델

## 📖 모델 개요
이 모델은 MapleStory Worlds Lua API 예제 코드로 파인튜닝된 특화 LLM입니다.  
게임 스크립트 자동화, 코드 생성, 문맥 기반 API 활용에 최적화됐습니다.

## 🤖 모델 사용법
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained('your-hf-id/model-name')
model = AutoModelForCausalLM.from_pretrained('your-hf-id/model-name')

inputs = tokenizer("local currentTargetEntity = self.Entity.AI", return_tensors='pt')
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs))
```

## ⚙️ 학습/실험 세팅
- Batch size: 1
- gradient_accumulation_steps: 4
- Epochs: 3
- Learning rate: 1.2e-4
- Optimizer: AdamW, fp16
- LoRA(PEFT) 기반 파인튜닝

## 📊 성능 변화 및 지표

|        | 학습 전   | 학습 후    | 변화폭  |
|--------|----------|----------|--------|
| Perplexity  | 46.14    | 5.34     | ↓8.6배 |
| Eval loss   | 3.83     | 1.68     | ↓      |
| 평가속도    | 1.30s    | 1.28s    | -      |

Perplexity: 언어모델의 예측 난이도를 나타내는 지표로, 값이 작을수록 정답에 가까운 예측입니다.

## 🗃️ 데이터
- MapleStory Worlds 공식 Developer API 예제 코드 활용
- [https://maplestoryworlds-creators.nexon.com/ko/apiReference/How-to-use-API-Reference](https://maplestoryworlds-creators.nexon.com/ko/apiReference/How-to-use-API-Reference)

## 📄 라이센스
기본 모델: nuprl/MultiPL-T-StarCoderBase_1b  
허깅페이스: [https://huggingface.co/nuprl/MultiPL-T-StarCoderBase_1b](https://huggingface.co/nuprl/MultiPL-T-StarCoderBase_1b)

## 문의
이름: bangill  
이메일: [95potter95@gmail.com](mailto:95potter95@gmail.com)

