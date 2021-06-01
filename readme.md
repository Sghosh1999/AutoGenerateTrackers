


# Awesome Daily Tracker ++ [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

[<img src="https://media.istockphoto.com/vectors/unique-modern-creative-elegant-letter-d-based-vector-icon-logo-vector-id1125625274?k=6&m=1125625274&s=612x612&w=0&h=U-fRNFEEezcFQ5M8EPjiqUTiqvhHt3lUN2s9CbaVX94=" align="right" height="75" width="75">](https://streamlit.io)

> The fastest way to build **Daily, Weekly & Monthly  Trackres**! Powered by **Python**!

## Description
This is a automatic Tracker generation Web Application which can generate daily, weekly and monthly trackers. It has been enhanced to generate group level trackers also.

## Usecase 1 : Daily Trcaker Generation :smiley:
In this use case, user can generate his daily tracker for a **single day as well as multiple days** (*In case he/she forgot to fill daily*).

## Features

* Automatic Generates ***Daily Trackers*** based on Date and corrosponding Tasks.
* If a user is not filling his daily tracker for consecutive two days , **an email notification will be sent** to the given email-address.
* User need to give **Start date and end date** in order o fill up the tasks.

### Application Demo

![Application Demo](https://github.com/Sghosh1999/AutoGenerateTrackers/blob/49d6ce9efecaf581b7227c97dc5d3c6f3d24ef75/demos/daily_trcaker_demo.gif)

## Usecase 2 : Weekly & Monthly  Generation :smiley:
In this use case, user can generate his **weekly as well as monthly tracker** by giving his daily tracker as Input. Not only that, if a users want to generate **group weekly trackers and group monthly trackers** he can also do that by giving the users daily trackers.
## Features

* Automatic Generates ***Weekly Trackers*** and ***Monthly Trackers*** based on Daily Trackers.
* Text preprocessing is handled. Automatic **new line** and **Number formatting** is being taken care of.
* Unnecessary phrases **( Holiday, Leave) is excluded**.
* **Text Wrapping of the csv** file is handled. **Proper Orientation** is handled.
* **Null value exception** is handled.
* Ex ( Group weekly Trackers): 

| Name | Week 1 | Week 2 | ... | Week n |
|--|--|--|--|--|
|Person 1  | 1. Completed Task A. | 1. Task C | ...| 1. Task D |
|Person 2  | 1. Completed Task B  | 1. Task E | ... | 1. Task F |
|...  | ...  | ... | ... | ... |
|Person n  | 1. Completed Task n  | 1. Task n | ... | 1. Task n |

### Application Demo

![Application Demo](https://github.com/Sghosh1999/AutoGenerateTrackers/blob/49d6ce9efecaf581b7227c97dc5d3c6f3d24ef75/demos/daily_trcaker_demo.gif)

### Built With

This section should list any major frameworks that we have used to build the application. 
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```


## Installation

```python
$python -m pip install virtualenv

$virtualenv myenv

$myenv\scripts\activate

$python -m pip install -r requirements.txt
```

## Running

```python
$streamlit run app.py
```

Enjoy!!
