Create a REST API for an e-commerce website.
The architecture includes the following end points:
--->Products:
1.prodproductList : This endpoint handles a get request for displaying a list all the products.
2.productDetails/<int:pk> : This endpoint handles a get request for displaying details of a particular product.
3.updateProduct/<int:pk> : This endpoint handles a put request for updating product details.
4.createProduct : This endpoint handles a post request for creating a product.
--->Users:
5. members/register: This endpoint is used for registering a new user. 
6.memebrs/login: This endpoint is used for logging in.
7.members/logout: This endpoint is used for logging out.
--->Orders:
8.orders
9.



The project contains three separate apps for the spcific purposes:
1. product app:
  Models :
  Product Model : 1. product_name 2. Product_desc 3.Category 4.Price
  Views: 
  1. getProductList 2.getProductDetails 3.updateProduct 4.deleteProduct
  Serializers:
  1. ProductSerializer
  
2. memebers app:
  1. The members app uses the KNOX authentication model.
  Knox solves some problems found with the built-in TokenAuthentication in DjangoRestFramework as:
    1.Token is generated per one call in login views with Knox. This allows each user to have one active token that gets deleted when a user logs out.
    2.Knox provides an encrypted form of tokens before storing them in the database. This feature would not allow any hacker to have access even if the database is compromised.
    3.Expiration of tokens is also a key feature of Knox that is not inbuilt in DRF.
    
4. orders app:
  Models :
  Serializers : 
  Views:
