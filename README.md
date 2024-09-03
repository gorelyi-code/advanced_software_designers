# Application continuity management service

## Project Specification

### Functional requirements

* Dynamic creation of backups and restoration of state
  * Service shall be able to backup the state of applications running within the framework on K8s
  * Service shall be able to restore the state of applications backed up by service

* Usage of DSL framework
  * The service shall use the DSL of the framework to determine the relevant application state and its backup policies

* Possibility of creating backups when the developer desires to
  *  Developers of an application should be able to backup
  *  Developers of an application should be able to restore a specific version from images and relevant state

* External storage of state backups
  * The application state shall be stored externally on the given S3-compatible object storage

### Stakeholder

* Developers
* 

## Team name: ASDs

### Students

* Gorelyi Mikhail
* Lukashin Daniil
* Derezovskiy Ilya
* Sigal Lev 
