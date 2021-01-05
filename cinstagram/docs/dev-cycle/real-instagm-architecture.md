
REAL LIFE ARCHITECTURES
Instagram Architecture – How Does It Store & Search Billions of Images

Instagram is the most popular photo-oriented social network on the planet today. With a user base of over a billion, it has become the first choice for businesses to run their marketing campaigns on.

This write-up is a deep dive into its platform architecture. What technologies does it use on the backend? How does it store such a crazy number of images been uploaded every second? How does it search for content in the massive data it has? Let’s find out.



1. What Technology Does Instagram Use on the Backend?
The server-side code is powered by Django Python. All the web & async servers run in a distributed environment & are stateless.

The below diagram shows the architecture of Instagram

Instagram architecture 8bitmen.com

The backend uses various storage technologies such as Cassandra, PostgreSQL, Memcache, Redis to serve personalized content to the users.

Follow the programming news feed to stay updated on the latest in the software tech, programming news & more



Asynchronous Behavior
RabbitMQ & Celery handle asynchronous tasks such as sending notifications to the users & other system background processes.

Celery is an asynchronous task queue based on distributed message communication, focused on real-time operations. It supports scheduling too. The recommended message-broker for celery is RabbitMQ.

RabbitMQ, on the other hand, is a popular open-source message broker written using the AMQP Advanced Messaging Queuing Protocol.

Gearman is used to distribute tasks across several nodes in the system. Also, for asynchronous task handling such as media uploads etc.

It’s an application framework for distributing tasks to other machines or processes that are more fit to execute those particular tasks. It has a gamut of applications ranging from high available websites to the transport of database backup events.



Storage
PostgreSQL is the primary database of the application it stores most of the data of the platform such as user data, photos, tags, meta-tags etc.

When the data grew huge over time, the engineering team at Insta meditated on different NoSQL solutions to scale & then finally decided to shard the existing PostgreSQL database as it best suited their requirements.

The main database cluster contains 12 replicas in different zones & involve 12 Quadruple extra large memory instances.

Hive is used for data archiving. A scheduled batch process runs at regular intervals to archive data from PostgreSQL DB to Hive.

It is a data warehousing software built on top of Apache Hadoop for data query & analytics capabilities.

Vmtouch a tool for learning about & managing the file system cache of Unix & Unix like servers is used to manage in-memory data when moving from one machine to another.

Using Pgbouncer to pool PostgreSQL connections when connecting with the backend web server resulted in a huge performance boost.

Redis an in-memory database is used to store the activity feed, sessions & other app’s real-time data.

Memcache an open source distributed memory caching system is used for caching throughout the service.



Data Management in the Cluster
Data across the cluster is eventually consistent, cache tiers are co-located with the web servers in the same data centre to avoid latency.

The data is classified into global & local data which helps the team to scale. Global data is replicated across different data centres across the geographical zones. On the other hand, the local data is confined to specific data centres.

Initially, the backend of the app was hosted on AWS Amazon web services but later migrated to Facebook data centres. That eased the integration of Instagram with other Facebook services, cut down latency & leverage the frameworks, tools for large scale deployments built by the Facebook engineering team.



Monitoring
With so many instances powering the service, monitoring plays a key role in ensuring the health & availability of the service.

Munin is an open-source resource, network & infrastructure monitoring tool used by the engineering team at Insta to track metrics across the service & get notified in case of any anomalies.

Pingdom is used for website’s external monitoring, ensuring expected performance & availability. PagerDuty for notifications & incident response.

 Now let’s move on to the search architecture.



How Does Instagram Searches Content through Billions of Images?
Instagram initially used Elasticsearch for its search feature but later migrated to Unicorn, a social graph aware search engine built by Facebook in-house.

Unicorn powers search at Facebook & has scaled to indexes containing trillions of documents. It allows the application to save locations, users, hashtags etc & the relationship between these entities.

Speaking of the Insta’s search infrastructure it has denormalized data stores for users, locations, hashtags, media etc.

These data stores can also be called as documents, which are grouped into sets to be processed by efficient set operations such as AND-OR & NOT

The search infrastructure has a system called Slipstream which breaks the user uploaded data, streams it through a Firehose & adds it to the search indexes.

The data stored by these search indexes is more search-oriented as opposed to the regular persistence of uploaded data to PostgreSQL DB.
