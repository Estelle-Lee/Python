### TECH MAGAZINE SQL

# For Flask Implementation
Question 1:
Did you choose to go with the ORM or raw SQL approach? What was the reason for your choice?

>> raw SQL approach because I think my topic is similar with the example of tweets but with more tables.



Question 2:
What endpoints (URLs and HTTP verb/methods) did you choose to implement in your Flask application, including any special details? 

>> magazines: index [GET], create [POST], show [GET], update [PUT], delete [DELETE]

customers: index [GET], create [POST], show [GET], update [PUT], delete [DELETE], subscribed_magazine [GET]

articles: index [GET], create [POST], show [GET], update [PUT], delete [DELETE], written_by [GET], listed_magazine [GET]

authors: index [GET], create [POST], show [GET], update [PUT], delete [DELETE], supervised_by [GET]





Question 3:
Brainstorm and describe some potential endpoints that you could implement in the future, that make sense for your application. 

>> magazines: subscribe_count [GET], listed_article [GET]



Question 4:
What challenges did you face with the Flask implementation for your portfolio project this week, and did you learn anything new from these challenges?

>> Too many tables.