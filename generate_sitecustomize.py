import os

# 현재 실행 중인 파일의 절대 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# 가상환경의 site-packages 폴더 찾기
import site
site_packages_dirs = site.getsitepackages()

# site-packages 경로 선택 (첫 번째 경로 사용)
site_packages_dir = site_packages_dirs[0]

# sitecustomize.py 파일 경로 설정
sitecustomize_path = os.path.join(site_packages_dir, "sitecustomize.py")

# sitecustomize.py 내용 생성
sitecustomize_content = f"""import sys
import os

# 프로젝트 폴더 경로 (자동 설정)
PROJECT_DIR = "{current_dir}"

# 프로젝트 경로를 sys.path에 추가
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)

print(f"Added project path to sys.path: {{PROJECT_DIR}}")  # 디버깅용 출력
"""

# 파일 생성
with open(sitecustomize_path, "w", encoding="utf-8") as f:
    f.write(sitecustomize_content)

print(f"✅ sitecustomize.py has been created at: {sitecustomize_path}")