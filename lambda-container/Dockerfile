FROM public.ecr.aws/lambda/python:3.8

ENV SOME_BUCKET=dk.bucket.something.

RUN python -m pip install --upgrade pip

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt --quiet

COPY src/ ${LAMBDA_TASK_ROOT}

CMD ["handler.handler"]