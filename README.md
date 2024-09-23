# Version Controller

## Summary

The system is designed to automate the collection and analysis of data on the publication activity of teachers and their participation in conferences, as well as on the scientific events of departments. It tracks publication activity, calculates metrics that are not available in HSE systems, and analyzes publication texts. Based on this analysis, the system can generate additional metrics, which contributes to a more comprehensive assessment of scientific activity.

## Stakeholders

* Administration of the FCS and HSE
* Employees of the FCS
* Scientific departments of the FCS
* Students and applicants of the FCS
* Computer Science scientists and researchers from all over the world

## Project Specification

### Features

* Parsing HSE sites
  * The system can parse embedded HSE sites to gather the necessary information
  * The system can perform parsing at intervals to update the data

* Pubilcation text analysis
  * The system can analyze the text of publications to build metrics on the text

* Automatic classification of publications (*hard to realize)
  * Automatic classification of publications by topic using natural language processing, which will allow analyzing the research directions of the department.

* Displaying key metrics
  * The system displays key metrics and indicators such as publication frequency, quantity, periodicity, etc

* Comparative Analysis
  * A function for comparing metrics from different units or faculty members to see differences on various metrics.

* Admin panel
  * Ability to manage system resources using a user-friendly interface

* Public web page
  * A public resource for interacting with the system
 
### Constraints

* Data limitations
  * Data sources may vary widely, requiring more complex data parsing
  * Large amount of data that would require a large data warehouse

* Maintainability
  * The system should be easy to maintain and update. Updates and patches should be deployable without significant downtime or the need for a complete system restart

* Access to the system
  * It is necessary to provide a proper system for differentiating access rights so that data does not get to unauthorized users.

* User-friendly user interface
  * A user-friendly interface is important for end users and from the experience of using the system

## Team name: ASDs

### Students

* Gorelyi Mikhail
* Lukashin Daniil
* Derezovskiy Ilya
* Sigal Lev 
