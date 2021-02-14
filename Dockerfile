FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL author="Soumit Das <contact@soumitdas.com>"

WORKDIR /app

COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

COPY ./backend/app .

ENV PORT 8081

EXPOSE ${PORT}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", PORT, "--log-level", "error"]