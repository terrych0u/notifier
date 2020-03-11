FROM alpine:3

ENV PYTHONUNBUFFERED=yes

WORKDIR /opt

COPY . .

RUN apk --no-cache add curl python3 \
  && python3 -m ensurepip \
  && pip3 install --no-cache-dir -r requirements.txt

# RUN adduser -DH app
# USER app

ENTRYPOINT ["./main.py"]
CMD ["-h"]
