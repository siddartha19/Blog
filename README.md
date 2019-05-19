# Blog

### App Overview
> TThis application allows a user to login using their gmail and allow him to post any news in the BLOG. The all posts
of the users are categorised into different types and is provided with a good interface to access the posts in the BLOG.


### Here is the Fist version of the App

![BLOG](https://github.com/siddartha19/Blog/blob/master/Blog.png)



### What I have done?
  * Develop a RESTful web application using the Python framework Flask.
  * Implementing third-party OAuth authentication.
  * Implementing CRUD (create, read, update and delete) operations.
  
### How to Run?

#### PreRequisites
  * [Python ~2.7](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Find the BLOG zip file.
  3. Extract the zip file and place BLOG folder in your Vagrant directory.

#### Launch Project
  1. Launch the Vagrant VM using command:

  ```
  $ Vagrant up 
  ```

  2. Run Vagrant

  ```
  $ Vagrant ssh
  ```

  3. Change directory to `/vagrant/BLOG/`

  ```
  $ cd /vagrant/BLOG
  ```

  4. Initialize the database

  ```
  $ python database.py
  ```

  5. Launch application

  ```
  $ Python blog.py
  ```
