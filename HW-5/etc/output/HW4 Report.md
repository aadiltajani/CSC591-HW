# Data Gathering

As instructed, we picked 3 people who we were going to gather data from, and chose movies as our topic of experiment as it is a very common domain with many possible attributes and everyone has a good knowledge about them. We started with the first person and asked them to name 10 movies that came to their mind. 
These movies were: 
- Mission Impossible
- Babylon
- Catch Me If You Can
- Conjuring 2
- 500 Days Of Summer
- Interstellar
- Jumanji
- American Sniper
- Citizenfour
- The Wizard Of Oz

Then, we asked them to name 8 parameters they would choose to describe these movies, and after we had them, we asked them to provide two opposite ends of those attributes and finally after ranking them, we had the examples and parameters ready for our first part. We then picked these 10 movies for our other 2 participants and asked them to come up with their own attributes and rank them accordingly.


# Analysis and Results

[testfile1](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/data/repgrid_test1.json)  ||  [testoutput1](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/output/repgrid_test1.out)

[testfile2](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/data/repgrid_test2.json)  ||  [testoutput2](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/output/repgrid_test2.out)

[testfile3](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/data/repgrid_test3.json)  ||  [testoutput3](https://github.com/aadiltajani/CSC591-HW/blob/main/etc/output/repgrid_test3.out)

We looked at the results and found some very expected results. This showed the clustering worked as expected and the attributes worked in favour as well. A very strong trend found in all these tests was movie pairings like  **_Mission Impossible-Jumanji, Catch Me If You Can-Interstellar-The Wizard Of Oz_**,  and the rest with some variety. This is possible because of some common and relating attributes among them like   **_Reviews, Budget, Ratings, Grossing Amt_**   and such. This is depicted by the pairing of Mission Impossible and Jumanji as both of them were high earning blockbusters with good reviews. Same would go for the second pairing as they had good reviews, some were rewatched and had good earnings and ratings. For the rest, the common attributes were rated near average and some uncommon attributes such as   **_Kids-Adult, PG-R, Home-Theatre, Fast-Slow_**   were successful enough to pair them apart from above to clusters but were not capable enough to give a more specialized and consistent clustering.
