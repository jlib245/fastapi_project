#!/bin/bash
cd backend || exit 1
uvicorn src.app.main:app --reload