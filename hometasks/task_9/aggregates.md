# Aggregates description

## Application Manager

This aggregate is responsible for managing Application entities and storing them in a S3-compatible storage. Application entities each store general information, status and Version mapping and can be modified via CRUD interface of the manager, activated and deactivated.

## Version Manager

This aggreagate is responsible for managing Version entities and storing them in a S3-compatible storage. Version entities each store general information and creation date and can be modified via CRUD interface of the manager.

## Kubernetes Manager

This aggreagate is responsible for interaction with Kubernetes. Manager modifies kubernetes settings to reach the desired state of the application.

## Account Manager

This aggregate is responsible for managing Account entities and storing them in a S3-compatible storage. Account entities have roles, which are enumerations and can be either Admin or User. Account entities each store general information and can be modified via CRUD interface of the manager.
