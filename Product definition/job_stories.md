# Jobs to be done

## Product features

### Restoring

Restoration from the list of the latest saved backups. Available to users, who have the required permissions.

### Creating automatic backups

Automatic regular backup creation with configurable timetable.

### Creating on-demand backups

Easy backup creation from UI, which is done by pressing a button. Available to users, who have the required permissions.

## Job stories

### Pasha

#### Restoring after bad commit

When Pasha pushes a new commit and breaks production servers

He wants to get the latest working versions of binaries

To quickly restore servers and not lose much money

#### Having a prepared backup

When Pasha accidentally breaks production servers due to any reason

He wants to have the latest backups already available to him

To not have to manually back up before every release

#### Creating backups when needed

When Pasha wants to release a dangerous new feature to production servers

He wants to be able to quickly create a backup

To be able to deploy new feature as soon as possible

### Alyona

#### Restoring after k8s change

When Alyona updates to a new k8s version and breaks other people's production servers

She wants to quickly restore servers without the help of the team managing the application

To not bring downtime to servers of other teams

#### Having others' backups

When Alyona updates to a new k8s version

She wants to have backups of the target servers already available

To speedup the process of updating

#### Creating backups in others' services

When Alyona updates to a new k8s version

She wants to be able to create an extra backup without the help of the team managing the application

To be able to quickly update to a new version
