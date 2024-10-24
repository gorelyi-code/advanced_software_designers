#Alternative use case diagram

Here we present alternative scenarios of system operation under different situations

# First scenario
Use case describes a situation when a user cannot log in to an account. The diagram shows the following scenarios:
* The user recovers the password
* The user receives an authorization error and his account is blocked.
* Administrator locks the user's account
* Administrator restores the user's account

![image](/hometasks/task_6/img/alt_use_case_1.png)

# Second scenario
The use case describes a situation where an error occurs while creating a backup and we can roll back the backup. This scenario is necessary to be able to clear the system of unnecessary files and restore the state before the backup was started.

![image](/hometasks/task_6/img/alt_use_case_2.png)

# Third scenario
The use case describes a situation where an error occurs while installing a version of an application, which may cause us to revert to a previous version. This scenario is necessary for reliable, stable and continuous operation of the application and system when an error occurs. 

![image](/hometasks/task_6/img/alt_use_case_3.png)