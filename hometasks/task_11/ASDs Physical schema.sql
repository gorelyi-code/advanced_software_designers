CREATE TABLE "Application" (
  "id" uuid PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "description" varchar,
  "user_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "update_at" timestamp NOT NULL DEFAULT (now()),
  "current_version" uuid,
  "status" integer NOT NULL DEFAULT 0
);

CREATE TABLE "Version" (
  "id" uuid PRIMARY KEY,
  "name" varchar,
  "appName" varchar,
  "app_id" uuid NOT NULL,
  "reated_at" timestamp NOT NULL DEFAULT (now()),
  "backup_path" varchar NOT NULL,
  "status" integer NOT NULL DEFAULT 0
);

CREATE TABLE "User" (
  "id" uuid PRIMARY KEY,
  "username" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "status" integer NOT NULL DEFAULT 0,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "role" string NOT NULL,
  "last_login" timestamp NOT NULL
);

CREATE TABLE "Kubernetes_updates" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "timestamp" timestamp NOT NULL DEFAULT (now()),
  "request" varchar,
  "entity_type" varchar,
  "operation_type" integer NOT NULL,
  "previous_value" varchar,
  "new_value" varchar,
  "response" varchar,
  "kubernetes_status" integer,
  "description" varchar
);

CREATE TABLE "User_role" (
  "id" uuid PRIMARY KEY,
  "role_id" integer NOT NULL,
  "role_str" varchar NOT NULL
);

CREATE TABLE "Status_code" (
  "id" uuid PRIMARY KEY,
  "status_id" integer NOT NULL,
  "status_str" varchar NOT NULL
);

CREATE TABLE "Operation_code" (
  "id" uuid PRIMARY KEY,
  "operation_id" integer NOT NULL,
  "operation_str" varchar NOT NULL
);

ALTER TABLE "Application" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Application" ADD FOREIGN KEY ("current_version") REFERENCES "Version" ("id");

ALTER TABLE "Version" ADD FOREIGN KEY ("app_id") REFERENCES "Application" ("id");

ALTER TABLE "Kubernetes_updates" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "User" ADD FOREIGN KEY ("role") REFERENCES "User_role" ("role_id");

ALTER TABLE "User" ADD FOREIGN KEY ("status") REFERENCES "Status_code" ("status_id");

ALTER TABLE "Application" ADD FOREIGN KEY ("status") REFERENCES "Status_code" ("status_id");

ALTER TABLE "Version" ADD FOREIGN KEY ("status") REFERENCES "Status_code" ("status_id");

ALTER TABLE "Kubernetes_updates" ADD FOREIGN KEY ("operation_type") REFERENCES "Operation_code" ("operation_id");
