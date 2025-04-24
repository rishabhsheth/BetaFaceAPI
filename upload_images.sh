#!/bin/bash

# FREE TIER and PUBLIC BetaFaceAPI Key
API_KEY="d45fd466-51e2-4701-8da8-04351c872236"

for i in {11..30}
do
  IMAGE="image_${i}.jpg"
  OUTPUT="../output${i}.json"

  echo "Processing $IMAGE -> $OUTPUT"

  curl -X POST "https://www.betafaceapi.com/api/v2/media/file" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "api_key=${API_KEY}" \
    -F "file=@${IMAGE};type=image/jpeg" >> "$OUTPUT"
done
