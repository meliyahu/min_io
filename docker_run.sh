#!/bin/bash

docker run -d -name minio-mosh -p 9000:9000   -e "MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE"   -e "MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"   minio/minio:edge server /data
