# Rock_paper_scissor
An unbeatable rock/paper/scissor game using opencv and tensorflow 

## Getting started
* Give a star to this repo (at the top)
* Clone the repository

```
https://github.com/vanarp0915/Rock_paper_scissor
```
* Installing the dependencies
```
cd Rock_paper_scissor
pip install -r requirements.txt 
```
* Creating a folder for collecting the data set
```
mkdir data
```
## Collecting training data
Before training the model collecting the data set is a required. The script image_collecting.py is used to collect the data set by capturing the image of your hand doing the rock, paper and scissor and stores it accordingly in the respective folders. 

### Collecting the data set for Rock
By Executing the command below a cv2 window will be pop out with the square box in it. User has to make the guesture of the rock in his hand and place it inside the box. By pressing "a" button on the keyboard, the script starts continouesly takes 500 snap short of the guesture and stores it in a folder naming the same.  
```
python3 image_collecting.py rock 500
```
### Collecting the data set for paper
By Executing the command below a cv2 window will be pop out with the square box in it. User has to make the guesture of the paper in his hand and place it inside the box. By pressing "a" button on the keyboard, the script starts continouesly takes 500 snap short of the guesture and stores it in a folder naming the same.
```
python3 image_collecting.py paper 500
```
### Collecting the data set for scissor
By Executing the command below a cv2 window will be pop out with the square box in it. User has to make the guesture of the scissor in his hand and place it inside the box. By pressing "a" button on the keyboard, the script starts continouesly takes 500 snap short of the guesture and stores it in a folder naming the same.
```
python3 image_collecting.py scissor 500
```
### Collecting the data set for none
By Executing the command below a cv2 window will be pop out with the square box in it. By pressing "a" button on the keyboard, the script starts continouesly takes 500 snap short of the box. No guestures should be shown during this execution
```
python3 image_collecting.py scissors 500
```
## Training the data
By execting the script below it creates a model "rock_paper_scissor.h5"
```
python3 train.py
```
## Testing and Playing with the model
By executing the script a cv2 window will pop out which has two sub windows. The user has to show his guesture(rock/paper/scissor) in the right side window, meanwhile the computer will be showing the counter guesture making it unbeatble.
```
python3 game.py
```
