# ASDs

## Summary

An application continuity service dynamically backs up and restores the state of applications running within the framework on K8s. The service shall use the DSL of the framework to determine the relevant application state and its backup policies. Developers of an application should be able to backup and restore a specific version from images and relevant state from the service. The application state shall be stored externally on the given S3-compatible object storage.

## Stakeholders

* Developers
* DevOps
* Engineers
* Information Security
* Product managers
* Investors

## Project Specification

### Features

* Dynamic creation of backups and restoration of state
  * Service shall be able to backup the state of applications running within the framework on K8s
  * Service shall be able to restore the state of applications backed up by service
  * Users shall be able to select custom backup policies

* Usage of DSL framework
  * The service shall use the DSL framework to determine the relevant application state and its backup policies and take automatic actions

* Possibility of creating backups when the developer desires to
  *  Developers shall be able to backup their applications
  *  Developers shall be able to restore a specific version of their applications from images and relevant state

* External storage of state backups
  * The application state shall be stored externally on the given S3-compatible object storage

* UI and API control over backups
  *  The system should notify the user about the time it will take to create and restore a backup
  *  Users have to be able to view the history of backups
  *  Integration with other DevOps tools
 
### Constraints

* Performance Limitations
  * The system should take into account limitations related to backup creation and restore time, possible system load parameters and network limitations
  * The backup recovery time should not exceed the backup creation time

* Limitations on the amount of data
  * The storage capacity of the system must be constantly monitored so that there is no overflow of the storage

* Accessibility
  * The system should have a high level of availability (e.g. 99,9%) and be able to continue operating or gracefully complete current operations in the event of failures

* Compatibility
  * Different versions of k8s may have their own peculiarities of operation, which can cause problems with backup and restore states. Supporting different versions requires additional testing and updating efforts

* Security
  * The system must ensure data protection at all stages (extraction, transformation, loading), including authentification, authorization, data encryption and access auditing
  * The data has to stay in consistent state

* Maintainability
  * The system should be easy to maintain and update. Updates and patches should be deployable without significant downtime or the need for a complete system restart

* Usability
  * The system interface should be intuitive for users with different technical backgrounds

* Boot up time
  * System is able to turn on quickly after a reboot or shutdown

## Team name: ASDs

### Students

* Gorelyi Mikhail
* Lukashin Daniil
* Derezovskiy Ilya
* Sigal Lev 
