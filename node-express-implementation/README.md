
# To Do App Backend


![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

This project is a simple Rest API for a To-Do App. It uses NodeJS, Express, and Sequelize to connect with MySQL.

## Table of contents

- [Architecture](#architecture)
- [Features](#features)
- [Build instructions](#build-instructions)

## Architecture

This Rest API is just to communicate with the database and execute CRUD operations.
 
**NodeJS 18**

Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that allows developers to run JavaScript code outside of a web browser. It uses an event-driven, non-blocking I/O model, which makes it lightweight and efficient, making it ideal for building scalable, high-performance applications. Node.js is built on top of the V8 JavaScript engine from Google, which compiles JavaScript into machine code, enabling Node.js to execute code at near-native speeds.

**Express**

Express is a minimal and flexible Node.js web application framework that provides a set of robust features for building web and mobile applications. It provides a simple and intuitive API for creating powerful web servers that can handle HTTP requests and responses, as well as routing, middleware, templating, and more. Express allows developers to quickly build and deploy web applications with minimal boilerplate code, making it an ideal choice for prototyping and developing MVPs (minimum viable products). Express is also highly extensible, with a large ecosystem of middleware modules that can be easily integrated into your application.

**Sequelize**

Sequelize is a Node.js ORM (Object-Relational Mapping) for relational databases, including MySQL. It provides a simple yet powerful API for working with databases, allowing developers to easily interact with their database using JavaScript instead of SQL. Sequelize handles complex relationships between tables and supports a variety of data types, making it easy to build robust, scalable applications. It also includes built-in support for migrations, which makes it easy to manage changes to the database schema over time. Sequelize is highly customizable and extensible, with a large number of plugins and extensions available in the npm ecosystem.

**MySQL**

MySQL is a popular open-source relational database management system (RDBMS) that uses structured query language (SQL) to manage data. It is widely used for web applications and is known for its scalability, security, and reliability. MySQL supports a wide range of programming languages, making it easy to integrate with different technologies. It provides features like transaction support, replication, and backups, making it a popular choice for large-scale applications.

## Features

Endpoints to every CRUD operation are available. Using the following address, it is possible to create, retrieve, update, and delete tasks, including an endpoint to delete all tasks and being able to retrieve filtering by name.

```bash
/api/tasks
```

## Build instructions

First of all, it is important to create the database on MySQL. For this, there is a docker-compose file inside the folder *database*.

```bash
cd database

docker-compose up
```

After the database, you need to install the dependencies of the project.

```bash
npm install
```

Then run.

```bash
node server.js
```
