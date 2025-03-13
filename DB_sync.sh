#!/bin/bash
cd backend || exit 1
alembic revision --autogenerate
alembic upgrade head