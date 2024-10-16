# Databases

## SQL

<https://gvwilson.github.io/sql-tutorial/>

## PostgreSQL

### Docker compose

```yaml
  postgres_db:
    image: postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=some_password
      - POSTGRES_DB=my_db_name
    ports:
      - 5432:5432
    volumes:
      - ./path_to_migration_scripts:/docker-entrypoint-initdb.d/  # this will run all scripts in the folder
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 1s
      timeout: 3s
      retries: 30
```

In the container, run:

```bash
psql postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@"$POSTGRES_HOST":5432/"$POSTGRES_DB"
```

From outside the container, run:

```bash
psql postgresql://postgres:some_password@postgres_db:5432/my_db_name
```

### UUID

UUID as primary key:

- <https://www.cybertec-postgresql.com/en/unexpected-downsides-of-uuid-keys-in-postgresql/>
- <https://news.ycombinator.com/item?id=40884878>
- <https://planetscale.com/blog/the-problem-with-using-a-uuid-primary-key-in-mysql#use-an-ordered-uuid-variant>

### Links

- <https://postgres.ai/blog/20230722-10-postgres-tips-for-beginners>
- <https://postgres.ai/blog/20220525-common-db-schema-change-mistakes>
