### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  The syntax between Python and JavaScript are different. Python uses whitespace to indicate code blocks, while JavaScript uses curly braces. Python also is more focused on readability while JavaScript is primarily focused on web developement.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  First, you can use the following: .get() method on a dictionary with the same key you want to retrieve.  
  Second, you can use the following: try-except block on a dictionary with the same key you want to retrieve from the try block.


- What is a unit test?  
  a unit test is a type of software test that focuses on an individual unit isolated test that differs from the rest of the system.

- What is an integration test?  
  integration tests are typically performed after unit tests and before system tests. It tests how other components work together and if they are working.

- What is the role of web application framework, like Flask?  
  providing a set of tools and libraries that simplify the development process. The primary role of flask is to provide a structured way to handle incoming requests and generate responses based on those requests.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  If only simple info is needed a route URL would be more useful. But, on the other hand a URL query param would be more useful for an applicstion with more sensitive or descriptve info

- How do you collect data from a URL placeholder parameter using Flask?  
  By using the route() decorator and by using less than, greater than '<>'

- How do you collect data from the query string using Flask?  
  By using the route() decorator and then using the request.args.get('q') is how you would collect data from the query string

- How do you collect data from the body of the request using Flask?  
  by using the route() decorator and then using the request.form method to collect data from the request

- What is a cookie and what kinds of things are they commonly used for?  
  a cookie refers to a small piece of data that a web server sends to a users web browser. Commonly used to maintain a user's session on a website

- What is the session object in Flask?  
  it enables web applications to store user-specific info across multiple requests  
  

- What does Flask's `jsonify()` do?  
  a function that returns a JSON response from the data passed on
