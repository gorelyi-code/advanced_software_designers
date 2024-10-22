# Jobs to be done

## Product features

### Restoring

Restoration from latest saved version, available to developers and DevOps

### Creating regular backups

Automatic regular backup creation

### Creating on-demand backups

Easy backup creation from UI, available to developers and DevOps

## Job stories

### Pasha

#### Restoring

When Pasha pushes new commit and breaks production servers

He wants to get latest working versions of binaries

To restore servers

#### Creating regular backups

When Pasha accidentally breaks production servers

He wants to have latest backups

To not have to manually back up before every release

#### Creating on-demand backups

When Pasha wants to release a dangerous new feature to production

He wants to be able to quickly create a backup

To be able to deploy new feature as soon as possible

### Alyona

#### Restoring

When Alyona updates to a new k8s version and breaks other people's production servers

She wants to quickly restore servers without the help of the team managing the application

To not bring downtime to servers of other teams

#### Creating regular backups

When Alyona updates to a new k8s version

She wants to have backups of the target servers already available

To speedup the process of updating

#### Creating on-demand backups

When Alyona updates to a new k8s version

She wants to be able to create an extra backup without the help of the team managing the application

To be able to quickly update to a new version
