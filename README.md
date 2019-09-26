# User-Insights

User Insights System

Programming Language Used: Python3.6

How to run:

Please verify/place the csv files in the ‘user_insights’ folder location.
1.	Run the following command to build the docker from ‘user_insights’ directory.
docker build -t "docker-flask"
2.	Run the docker container.
docker run -it -d -p 5000:5000 docker-flask

Note:
Red - port number to access the api outside docker(can be anything)
Green - port number defined in flask and exposed from dockerfile(should be same as what we exposed in dockerfile)

finally API can be accessed by http://localhost:5000

End points available to fetch user insights:
1. /top-<n>_hotels/<user_id>
2. /top-<k>_amenities/<user_id>
3. /top-<n>_hotels&top-<k>_amenities/<user_id>

Top-N hotels clicked:

To know the top-N hotels clicked by a user, Use the following end point with corresponding input values. If the given input user_id is not present in the click.csv file you will get 'user_id doesn't exist' message. 
You will get top hotel_id’s and their counts ( in descending order) clicked by the given user in the output.
end point: '/top-<n>_hotels/<user_id>'
inputs:
	- <n> : top-N value
	- <user_id> : user_id
	
Example request url: http://localhost:5000/top-5_hotels/85141003911158
Example Response: 
 

Top-K Amenities selected:
To know the top-K amenities selected by a user, Use the following end point with corresponding input values. If the given input user_id is not present in the selections.csv file you will get 'user_id doesn't exist' message. 
You will get top amenity_id’s and their counts ( in descending order) selected by the given user in the output.
end point: '/top-<k>_amenities/<user_id>'


inputs:
	- <k> : top-K value
	- <user_id> : user_id
	
Example request url: http://localhost:5000/top-5_amenities/85141003911158
Example response:
 

Top-N hotels clicked & Top-K Amenities Selected:
To know the top-N hotels clicked and the top-K amenities selected by a user, Use the following end point with corresponding input values. If the given input user_id is not present in the csv files you will get 'user_id doesn't exist' message. 
You will get the combined output of enpoint1 and endpoint2 given above.
end point: '/top-<n>_hotels&top-<k>_amenities/<user_id>'
inputs:
	- <n> : top-N value for hotels clicked
	- <k> : top-K value for amenities selected
	- <user_id> : user_id
	
Example request url: http://localhost:5000/top-5_hotels&top-10_amenities/85141003911158



Example Response: 
 


Note: 
Please note that if the given top N/K value is greater than the total number of available values present, you will get only the available id values and their counts in the output (Assumption).
Example:
For this user_id ’85141003911158’, we have only 2 amenity values present. You will get only top-2 values for this user even if your N/K value is greater than 2.


Other Possible User Insights:
1.	We can generate total number of clicks made during a particular time period using the timestamp column provided.
2.	We can generate which hotels have got top clicks during a time period.
3.	Similarly we can able to generate top amenities selected during a time period.
4.	Using the data given, we can able to get user_id list who have clicked hotels but didn’t select any amenities and vice versa.
