from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

# .env 파일 내용 로드
load_dotenv()

# 환경 변수에서 키값을 불러오기
HG_FACE_KEY = os.getenv('HG_FACE')


repo_id = "bangill/maplestoryworlds-lua-api-finetune"
readme_path = "./README.md"

api = HfApi(token=HG_FACE_KEY)

api.upload_file(
    path_or_fileobj=readme_path,
    path_in_repo="README.md",
    repo_id=repo_id,
    commit_message="Update README"
)

print(f"Uploaded README to https://huggingface.co/{repo_id}")
