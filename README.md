# AWS-Data-Exchange-for-APIs-Challenge

##Sending requests to IMDb’s Real-time API via
Postman


● Before you begin: Have your AWS Access Key ID and AWS Secret Access Key ready.
○ Please be aware that saving your AWS Access Key ID and AWS Secret Access Key in Postman is considered a
security risk and you should fully protect your Postman workspace/collection/request from unauthorized access
to avoid the disclosure of your AWS credentials


● Create a new request in Postman
○ Set the Method to POST
○ The request URL should be https://api-fulfill.dataexchange.us-east-1.amazonaws.com/v1
![image](https://user-images.githubusercontent.com/52241389/202828626-2f62021c-eb94-4c56-be9e-a1da52da9542.png)


● On the Authorization tab
○ Set Type to be AWS Signature
○ Set Add authorization data to to be Request Headers
○ Set AccessKey to your AWS Access Key ID
○ Set SecretKey to your AWS Secret Access Key
○ Set AWS Region to us-east-1
○ Set Service Name to dataexchange
○ Leave Session Token empty

![image](https://user-images.githubusercontent.com/52241389/202828659-a94cf154-444b-4082-923c-369c95025229.png)


● On the Body tab
○ Select GraphQL
○ And paste this into the text editor:

{
  mainSearch(
    first: 10
    options: {searchTerm: "The Matrix", titleSearchOptions: {type: MOVIE}, type: TITLE, isExactMatch: true}
  ) {
    edges {
      node {
        id
        entity {
          ... on Title {
            titleText {
              text
            }
            ratingsSummary {
              aggregateRating
              voteCount
            }
          }
        }
      }
    }
  }
}
![image](https://user-images.githubusercontent.com/52241389/202829357-4bdbf8df-c35b-43c7-8121-8abca621d05e.png)

![image](https://user-images.githubusercontent.com/52241389/202828700-b7e44eb4-8715-48e1-a349-c34f37eb3861.png)

● On the Headers tab
○ Make sure Content-Type is set to application/json
○ Add a new key x-amzn-dataexchange-data-set-id with a value of 4b1f47d86b35356cf8fb6f15cc758c0e
○ Add a new key x-amzn-dataexchange-revision-id with a value of 4915c8e5e666a284124fc532ca8fbbe2
○ Add a new key x-amzn-dataexchange-asset-id with a value of f05f6f7ca415c8be7341f95bf1db34c5
These 3 Ids are getting from IMDB API view tab after subscribe to IMDB through AWS data exchange, foollowed by activating through AWS License manager.

![image](https://user-images.githubusercontent.com/52241389/202829179-890282b4-7680-471a-b262-98d554584a27.png)


![image](https://user-images.githubusercontent.com/52241389/202828749-fad6a676-8817-467c-ae00-d93738219077.png)

Now you can press Send and you should see a response with rating and vote values.



##Training the Model"Million Dollar Movie Classifier"

Objective:To predict the likelihood of a movie to be earning Million dollar or Not.

1.Importing Dataset( Billio_data and BillionLess data)and cleaning NAN value.
2.Importing Merge data after auditing
![image](https://user-images.githubusercontent.com/52241389/202829643-c4aca99d-d542-4e91-a0f1-47ba17f3fd12.png)

3.Splitting data into train and test as 80:20 also sorting data class wise for at some next step use.
![image](https://user-images.githubusercontent.com/52241389/202829716-2824f5c6-d4fc-48d6-b449-8a4d2a9afa56.png)

4.Traing model(pred) with Naive Bays Binary Classifier having threshold as 0.5.
![image](https://user-images.githubusercontent.com/52241389/202829817-16536287-e272-4532-ba70-eb72f88d5aea.png)

5.Calculating train error
![image](https://user-images.githubusercontent.com/52241389/202829831-0a5467d9-a417-452a-8b8d-98d94062c04f.png)

6.Testing The model
![image](https://user-images.githubusercontent.com/52241389/202829846-31c35678-5d94-4dc0-83d1-706e516cfa7c.png)

7.Calculating Testing error
![image](https://user-images.githubusercontent.com/52241389/202829856-a6c0a6b7-703c-4549-ba2a-05788724fbf6.png)

8.Getting the output with user data.
![image](https://user-images.githubusercontent.com/52241389/202829862-de347dad-623f-40a9-a450-8b7dbd5db90a.png)


