#!/bin/bash
COURSE=seabornp
docker compose run --rm rsmanage rsmanage addcourse --course-name $COURSE --basecourse $COURSE --login-required --institution UIUC
docker compose run --rm rsmanage rsmanage build $COURSE
CSV_FILE=users.csv

# # Read the CSV file line by line, skipping the header
tail -n +2 "$CSV_FILE" | while IFS=',' read -r VAR1 VAR2 VAR3 VAR4 VAR5 VAR6; do
    echo "Adding user: $VAR1"
    echo docker compose run --rm rsmanage rsmanage adduser --username "$VAR1" --password "$VAR5" --first_name "$VAR3" --last_name "$VAR4" --email "$VAR2" --course "$COURSE"
    docker compose run --rm -T rsmanage rsmanage adduser --username "$VAR1" --password "$VAR5" --first_name "$VAR3" --last_name "$VAR4" --email "$VAR2" --course "$COURSE"
done
docker compose run --rm rsmanage rsmanage addinstructor --username test_instructor --course $COURSE
