FROM python:3.7
COPY . /app
RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]