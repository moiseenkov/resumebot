FROM python:3.11-alpine

COPY api/ /api/

RUN pip install -r /api/requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "api.main:app", "--port", "8080", "--host", "0.0.0.0"]
