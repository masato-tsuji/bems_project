#!/bin/bash
# プロジェクトルートから FastAPI を起動するスクリプト

# 仮想環境を有効化
source .venv/bin/activate

# uvicorn 起動
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
