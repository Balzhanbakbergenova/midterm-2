#1 Functions. [25 %]
def translateLetter(*scores):
    points = []
    for score in scores:
        if score == 'A+':
            points.append(4.3)
        elif score == 'A':
            points.append(4.0)
        elif score == 'A-':
            points.append(3.7)
        elif score == 'B+':
            points.append(3.3)
        elif score == 'B':
            points.append(3.0)
        elif score == 'B-':
            points.append(2.7)
        elif score == 'C+':
            points.append(2.3)
        elif score == 'C':
            points.append(2.0)
        elif score == 'C-':
            points.append(1.7)
        elif score == 'D+':
            points.append(1.3)
        elif score == 'D':
            points.append(1.0)
        elif score == 'D-':
            points.append(0.7)
    return points

def translatePercentage(*scores):
    points = []
    for score in scores:
        if score >= 95:
            points.append(4.3)
        elif score >= 90:
            points.append(4.0)
        elif score >= 85:
            points.append(3.7)
        elif score >= 80:
            points.append(3.3)
        elif score >= 75:
            points.append(3.0)
        elif score >= 70:
            points.append(2.7)
        elif score >= 65:
            points.append(2.3)
        elif score >= 60:
            points.append(2.0)
        elif score >= 55:
            points.append(1.7)
        elif score >= 50:
            points.append(1.3)
        elif score >= 45:
            points.append(1.0)
        elif score >= 40:
            points.append(0.7)
    return points

def calculateGPA(*args):
    total_points = 0
    total_credits = 0
    for i in range(0, len(args), 2):
        total_points += args[i] * args[i+1]
        total_credits += args[i+1]
    gpa = total_points / total_credits
    return round(gpa, 2)


letter_scores = translateLetter('A', 'B+', 'C')
print(letter_scores) # [4.0, 3.3, 2.0]

percentage_scores = translatePercentage(85, 73, 91)
print(percentage_scores) # [3.7, 2.7, 4.0]

gpa = calculateGPA(3.3, 4, 2.7, 3, 4.0, 4)
print(gpa) # 3.7

#2 Working with files. [25 %]
import os
def readCredits():
    credits = []
    with open('grades/credits.txt', 'r') as f:
        for line in f:
            credits.append(int(line.strip()))
    return credits

def readAndTranslateScores(filename, translateFunc):
    scores = []
    with open('grades/' + filename, 'r') as f:
        for line in f:
            score = line.strip()
            points = translateFunc(score)
            scores.append(points)
    return scores

def calculateStudentGPA(credits, *scores):
    total_points = 0
    total_credits = sum(credits)
    for i in range(len(scores)):
        total_points += scores[i] * credits[i]
    gpa = total_points / total_credits
    return round(gpa, 2)

credits = readCredits()
math_scores = readAndTranslateScores('math.txt', translateLetter)
chemistry_scores = readAndTranslateScores('chemistry.txt', translatePercentage)
english_scores = readAndTranslateScores('english.txt', translatePercentage)
gpas = []
for i in range(len(math_scores)):
    math_score = math_scores[i]
    chemistry_score = chemistry_scores[i]
    english_score = english_scores[i]
    gpa = calculateStudentGPA(credits, math_score, chemistry_score, english_score)
    gpas.append(gpa)

with open('grades/overallGPAs.txt', 'w') as f:
    for gpa in gpas:
        f.write(str(gpa) + '')

overall_gpa = calculateGPA(*gpas, *credits)
print('Overall GPA:', overall_gpa)

#3 OOP. [30 %]
class Student:
    def init(self, name, courses_taken, scores):
        self.name = name
        self.courses_taken = courses_taken
        self.scores = scores
        self.gpa = self.calculateGPA()
        self.status = self.setStatus()

    def calculateGPA(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.scores:
            credits = self.scores[course]['credits']
            grade_points = self.scores[course]['score'] * credits
            total_credits += credits
            total_grade_points += grade_points
        gpa = total_grade_points / total_credits
        return round(gpa, 2)

    def setStatus(self):
        if self.gpa >= 1.0:
            return 'Passed'
        else:
            return 'Not Passed'

    def showGPA(self):
        print(f"self.name's GPA is self.gpa")

    def showStatus(self):
        print(f"self.name's status is self.status")

scores = 'math': 'score': 4.3, 'credits':4, 'chemistry': 'score': 3.3, 'credits':3, 'english': 'score': 4.0, 'credits':4
student1 = Student('John', 3, scores)
student1.showGPA()
student1.showStatus() 

#4 API. [10%]
#API stands for Application Programming Interface. It's a set of rules, protocols, and tools that allow different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information, enabling seamless interaction between various systems.
#Use cases of APIs are diverse and include:
#Integration: APIs facilitate the integration of different systems or services, allowing them to work together. For instance, integrating payment gateways into e-commerce websites.
#Data Access: They enable access to data or functionality of other services. Social media platforms often provide APIs for developers to access user data or post content programmatically.
#Building Applications: Developers use APIs to build new applications or enhance existing ones by leveraging functionalities offered by other services or platforms.
#APIs, while incredibly powerful in enabling seamless interaction between different software systems, do have limitations:
#Rate Limits: Many APIs have rate limits, which restrict the number of requests a user or application can make within a certain timeframe. Exceeding these limits can lead to temporary or permanent restrictions on access.
#Changes and Versioning: APIs can change over time. Updates or changes in API versions might lead to deprecated functionalities or alterations in the way data is structured or accessed. Developers relying on these APIs need to adapt their code accordingly.
#Security Concerns: If an API isn’t properly secured, it can pose security risks. Vulnerabilities such as insufficient authentication, data breaches, or unauthorized access might occur if security measures are not robust.
#Reliability and Downtime: Dependence on external APIs introduces the risk of downtime or interruptions. If the API provider experiences issues or undergoes maintenance, it can impact the functionality of applications relying on that API.
#Limited Functionality: Not all functionalities of a service may be exposed through its API. Some services might restrict certain features or data from being accessed or manipulated programmatically.
#Documentation and Support: Inadequate or unclear documentation can make it challenging for developers to understand and use an API effectively. Lack of robust support or community resources can also hinder the troubleshooting process.
import requests
api_key = 'YOUR_API_KEY'
base_url = 'http://api.openweathermap.org/data/2.5/weather'
city_name = 'London'  
params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'  
}
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()  
    city = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(f'Weather in {city}: {weather}, Temperature: {temp}°C')
else:
    print('Failed to retrieve data')

#5 Socket. [10%]
#A socket is a software structure that allows programs to communicate over a network. It provides an endpoint for sending or receiving data between systems through the network. Sockets utilize specific protocols to establish connections, send data, and close connections.
#Use cases of sockets include:
#Network Communication: Sockets are fundamental for various network communication applications such as client-server architectures, where programs on different devices communicate with each other.
#Real-Time Data Transfer: They are used for real-time data transfer applications like chat applications, online gaming, and streaming services.
#Distributed Systems: Sockets enable communication between different components of distributed systems, allowing them to exchange information and work together.
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)
print('Server listening...')
while True:
    client_socket, addr = server_socket.accept()
    print(f'Got connection from {addr}')
    message = 'Thank you for connecting!'
    client_socket.send(message.encode('utf-8'))
    client_socket.close()
