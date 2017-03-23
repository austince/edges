# Assignment 2 Writeup

This assignment add _Feature Detection_ via *Hessian*, as
well as _Two Line Detectors_ via *RANSAC* and *Hough Transform*.

The algorithms will be briefly explained in each section, as well
as a summary of the results.


## Images

The results of this assignment use mainly the Road.  
  
Road  
![Road](./tests/images/road.png "Road")  

Kangaroo  
![Kangaroo](./tests/images/kangaroo.png "Kangaroo")  
  
Red  
![Red](./tests/images/red.png "Red")    
  
Plane  
![Plane](./tests/images/plane.png "Plane")  
  
## Hessian Feature Detection

### Algorithm Overview
Calculated the second moment matrix and determinant for each point in the image,
using the formulas: 
```
Hessian(I) = [Ixx Ixy] 
             [Ixy Iyy] 
             
Determinant(I) = Ixx * Iyy - Ixy ^ 2
```

Then threshold the determinants, casting aside everything that doesn't pass.

Finally, apply non-max suppression in 3x3 neighborhoods.


### Results
Low threshold: 1000  
![low threshold](./results/hessian/road-t1000.png "1000 threshold")  

Medium threshold: 31000  
![med threshold](./results/hessian/road-t31000.png "31000 threshold")  

High threshold: 51000  
![high threshold](./results/hessian/road-t51000.png "51000 threshold")  

Very High threshold: 71000  
![very high threshold](./results/hessian/road-t71000.png "71000 threshold")  

Extremely High threshold: 91000   
![Extremely high threshold](./results/hessian/road-t91000.png "91000 threshold")  

Even More Extremely High threshold: 111000   
![Even More Extremely high threshold](./results/hessian/road-t111000.png "111000 threshold")

Absurdly High threshold: 151000  
![Even More Extremely high threshold](./results/hessian/road-t151000.png "151000 threshold")

### Analysis
The absurdly high thresholds tend to produce better features that are less likely to have
 mass amounts of outliers.

## RANSAC Line Detection

### Algorithm Overview

First, process the image for feature points.  
Then choose a small subset, in this case: 2, points uniformly at random.  
Then fit a linear model to that subset and find 'inlier points', or points that are within a
	thresholded distance from the model.
Next, if there are more than a certain number of inliers, record the line and refit a model
 	using the new inliers.
Reject the rest of the points as outliers.
Choose the best line based the total error.  
Repeat, then plot the lines.

**Parameter choosing:**  
* inlier threshold: sqrt(3.84 * gaus_sig ^ 2) for Zero-mean Gaussian noise
* num sample runs : N = log (1 - p) / log (1 - (1 - e)) where:
	* p is the probability that at least one random sample is outlier free
	* e is the outlier ratio

### Results
Low minimum inlier threshold: 2  
![low threshold](./results/ransac/road-t51000-minInliers2.png "2 threshold")

Medium minimum inlier threshold: 7  
![med threshold](./results/ransac/road-t51000-minInliers7.png "7 threshold")

High minimum inlier threshold: 15  
![high threshold](./results/ransac/road-t51000-minInliers15.png "15 threshold")

### Analysis

The main problem are the gaps in the lines caused by parallel lines in the image. Many of 
windows frames in the `road.png` photo are collinear, causing the inlier calculation to extend
 the line's bounds past where the singular window stops.  

ex:  
![parallel problem](./results/ransac/road-t71000.png "Parallel Problem")  

Here, the algorithm correctly identifies many of the common lines in the image, but links them
together in ways that distort the true line. 

This could be remedied with a clipping function that only allows so much space between inliers,
or one that casts away points that are dissimilar from the rest of the line. 

**Minimum Inlier Threshold:**  
Though there are the parallel problems, raising the number of inliers to be considered a 'line' seems 
to help the algorithm choose only the lines that are closest together. 


## Hough Transform Line Detection

### Algorithm Overview

First, discretize parameter space into bins for vote accumulation.  
Then, process the image for feature points.  
For each feature point, cast a vote into every bin that could have generated this point.
After, find the bins that have the most votes.  

For drawing the lines, I have opted to simply record which feature points vote where, and then 
plot all feature points that cast a vote in the highest bins, as per Professor's recommendation.  

### Results

### Analysis