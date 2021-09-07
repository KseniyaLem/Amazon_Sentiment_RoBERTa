FROM pytorch/pytorch
ADD . /python-flask
WORKDIR /python-flask
EXPOSE 5000
ENV FLASK_APP=server.py
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "server.py" ]