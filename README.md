# GRE Playing
For me, the most difficult part in GRE is vocabularies!  
Currently my simple tool has two function:  
1. GRE.py  
2. review_mis.py

## Set up
1. clone the project  
```
git clone https://github.com/shinmao/GRE_Playing.git
cd GRE_Playing/
```
2. create the ```dict.txt``` in folder
```
vim dict.txt
```
3. the format in the file  
```php
synthesis;strain;speculative;..........
```
with each words end with ```;``` !!  

## Play it!
1. run GRE.py  
```
./GRE.py
```
![](https://github.com/shinmao/GRE_Playing/blob/master/screenshot/GRE.png)  
With the picture, you will need to choose how many words you want to learn first. Of course, the number should be less than the words you have in your ```dict.txt```. After giving the number, you just need to answer ```y``` or ```n``` to the program! If you answer ```n``` to show that you don't know the word, the word will be added as a record to the ```mistake.txt```!  

2. run review_mis.py  
```
./review_mis.py
```
![](https://github.com/shinmao/GRE_Playing/blob/master/screenshot/review.png)  
With this program, it will test with all the words you have made mistake! If you answer ```n``` again in this review, it will be added one more time in this file, and it means the fact that the probabilities of its occurence will also be greater!  
  
### Expectation
I am just use it for my GRE tool, so there are many code which is very ugly and even have safety problem. Maybe I will find some day to fix it or even add more functions to it.


