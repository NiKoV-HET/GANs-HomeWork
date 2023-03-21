# Лабораторная работа №5
Нужно было Перенести лица:
 1. Анджелина Джоли — Вупи Голдберг
 1. Джейсон Стейтем — Сильвестр Сталлоне
 1. Сергей Бурунов — Джек Блэк

 Можно было попробовать разные лосы, но не смог попробовать, т.к. не влезло на видеокарту.
 

# 1. Анджелина Джоли — Вупи Голдберг

## В качестве фото для переноса были использованы следующие фото:

<img src="./Images/AJoly1.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/VGoldberg1.png" alt="alt text" width="whatever" height=300> 
 
И

<img src="./Images/AJoly2.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/VGoldberg2.png" alt="alt text" width="whatever" height=300> 

## Нормализация:
После этого, был использован метод "Align Images" и получили следующие изображения.

<img src="./Images/AJoly3.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/VGoldberg3.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/AJoly4.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/VGoldberg4.jpg" alt="alt text" width="whatever" height=200>  

Попробовал получить вектора с помощью "Latent Optimization", вышло не очень. 

<img src="./Images/AJoly5.png" alt="alt text" width="whatever" height=300>  <img src="./Images/VGoldberg5.png" alt="alt text" width="whatever" height=300> 
 
## Пересадка
Решил использовать метод e4e. Получили следующий результат. Лучший перенос был с psi=0.5.


![AJoly-VGoldberg](./Images/AJoly-VGoldberg1.gif)  <img src="./Images/AJoly-VGoldberg1.jpg" alt="alt text" width="whatever" height=250> 

![AJoly-VGoldberg](./Images/AJoly-VGoldberg2.gif) <img src="./Images/AJoly-VGoldberg2.jpg" alt="alt text" width="whatever" height=250> 


# 2. Джейсон Стейтем — Сильвестр Сталлоне

Реализация повторяет все то же что и выше.

## Базовые фото:

<img src="./Images/JStethem1.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/SStalone1.jpg" alt="alt text" width="whatever" height=300> 

И

<img src="./Images/JStethem2.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/SStalone2.jpeg" alt="alt text" width="whatever" height=300> 

## Нормализация:

<img src="./Images/JStethem3.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/SStalone3.jpg" alt="alt text" width="whatever" height=200>
<img src="./Images/JStethem4.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/SStalone4.jpg" alt="alt text" width="whatever" height=200> 

## Пересадка

![AJoly-VGoldberg](./Images/JStethem-SStalone1.gif) <img src="./Images/JStethem-SStalone1.jpg" alt="alt text" width="whatever" height=250> 

![AJoly-VGoldberg](./Images/JStethem-SStalone2.gif) <img src="./Images/JStethem-SStalone2.jpg" alt="alt text" width="whatever" height=250> 


# 3. Сергей Бурунов — Джек Блэк

Реализация повторяет все то же что и выше.

## Базовые фото:

<img src="./Images/SBurunov1.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/JBlack1.jpg" alt="alt text" width="whatever" height=300> 

И

<img src="./Images/SBurunov2.jpg" alt="alt text" width="whatever" height=300>  <img src="./Images/JBlack2.jpg" alt="alt text" width="whatever" height=300> 

## Нормализация:

<img src="./Images/SBurunov3.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/JBlack3.jpg" alt="alt text" width="whatever" height=200>
<img src="./Images/SBurunov4.jpg" alt="alt text" width="whatever" height=200>  <img src="./Images/JBlack4.jpg" alt="alt text" width="whatever" height=200> 

## Пересадка

![AJoly-VGoldberg](./Images/SBurunov-JBlack1.gif) <img src="./Images/SBurunov-JBlack1.jpg" alt="alt text" width="whatever" height=250> 

![AJoly-VGoldberg](./Images/SBurunov-JBlack2.gif) <img src="./Images/SBurunov-JBlack2.jpg" alt="alt text" width="whatever" height=250> 

