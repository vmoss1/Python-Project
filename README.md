# Python-Project


# **Database Schema**

![database-schema]

[database-schema]: ./images/Database_Schema.png

## `users`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| username    | varchar   | not null, unique      |
| first_name  | varchar   | not null              |
| last_name   | varchar   | not null              |
| email       | varchar   | not null, unique      |
| password    | varchar   | not null              |
| role        | varchar   | not null              |
| created_at  | datetime  | not null              |

## `boards`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| name        | varchar   | not null              |
| user_id     | integer   | not null, foreign key |
| created-at  | datetime  | not null              |

- `user_id` references `users` table

## `cardUserJoin`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| user_id     | integer   | not null, foreign key |
| card_id     | integer   | not null, foreign key |

- `user_id` references `users` table
- `card_id` references `cards` table

## `lists`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| board_id    | integer   | not null, foreign key |
| user_id     | integer   | not null, foreign key |
| list_title  | varchar   | not null              |
| created-at  | datetime  | not null              |
| updated     | datetime  | not null              |

- `board_id` references `boards` table
- `user_id` references `users` table

## `cards`

| column name   | data type | details               |
| ------------- | --------- | --------------------- |
| id            | integer   | not null, primary key |
| user_id       | integer   | not null, foreign key |
| list_id       | integer   | not null, foreign key |
| title         | varchar   | not null              |
| labels        | varchar   | not null              |
| notifications | boolean   | not null              |
| description   | varchar   | not null              |
| start_date    | varchar   | not null              |
| end_date      | varchar   | not null              |
| checklist     | varchar   | not null              |
| created-at    | datetime  | not null              |

- `user_id` references `users` table
- `list_id` references `lists` table

## `cardImages`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| card_id     | integer   | not null, foreign key |
| url         | varchar   | not null              |
| cover -at   | boolean   | not null              |

- `card_id` references `cards` table

## `comments`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| user_id     | integer   | not null, foreign key |
| card_id     | integer   | not null, foreign key |
| body        | varchar   | not null              |
| created-at  | datetime  | not null              |

- `board_id` references `boards` table
- `card_id` references `cards` table
