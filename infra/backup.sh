#!/bin/bash
mkdir -p ./backups
FILENAME="backup_$(date +%Y%m%d_%H%M%S).sql.gz"

docker exec -t tracker_postgres_engine pg_dump -U admin core_telemetry_store | gzip > "./backups/$FILENAME"

find ./backups -type f -mtime +7 -name '*.sql.gz' -delete
