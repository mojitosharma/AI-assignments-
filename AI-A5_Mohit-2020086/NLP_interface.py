import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from pyswip import Prolog
import string


option = {'ai':'Artificial Intelligence', 'qrs':'Quantum Researcher', 'ds':'Data Scientist'
        ,'uiux':'UI/UX designer', 'econ':'Economists', 'na':'Not Decided'}

option_ssh = {'1':'acting','2':'reading','3':'poetry','4':'history'}

prev_courses_available = {'ssh214':'Introduction To The Study Of Literature',
            'ssh215':'Indian Poetry Through the Ages',
            'ssh211':'Theatre Appreciation',
            'ssh212':'Nation and her Narratives',
            'cse643':'Aritificial Intelligence',
            'cse343':'Machine Learning',
            'cse140':'Introduction to Intelligent Systems',
            'cse556':'Natural Language Processing',
            'cse506':'Data Mining',
            'cse342':'Statistical Machine Learning',
            'ece525':'Quantum Mechanics',
            'ece545':'Photonics: Fundamentals & Applications',
            'ece524':'Quantum Materials and Devices',
            'cse622':'Introduction to Quantum Computing',
            'cse202':'Fundamentals of Database Management System',
            'cse557':'Big Data Analytics',
            'cse606':'Data Warehouse',
            'cse507':'Database System Implementation',
            'des130':'Prototyping Interactive Systems',
            'des101':'Design Drawing & Visualization',
            'des205':'Design of Interactive Systems',
            'des202':'Visual Design & Communication',
            'des201':'Design Processes and Perspectives',
            'des204':'Human Computer Interaction',
            'des524':'Ergonomics/Human factors for Design',
            'eco221':'Econometrics I',
            'eco201':'Macroeconomics',
            'eco301':'Microeconomics',
            'eco311':'Game Theory',
            'eco331':'Foundations of Finance',
            'cse102':'Data Structures & Algorithms',
            'cse201':'Advanced Programming',
            'cse101':'Introduction to Programming',
            'cse222':'Algorithm Design and Analysis',
            'mth100':'Linear Algebra',
            'mth201':'Probability and Statistics',
            'mth203':'Multivariate Calculus',
            'ece230':'Fields and Waves'}

carrer_option = {}
ssh_option = {}
prev_courses_option = {}

def setting_env():
    non_useful_words = set(stopwords.words('english')) 
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    nltk.download('wordnet')
    wl = WordNetLemmatizer()
    ps = PorterStemmer()

    for carrer in option.keys():
        carrer_up = option[carrer].lower()    #helps while compairing values 
        carrer_up1 = ""
        for ch in carrer_up: 
            if ch not in string.punctuation:
                carrer_up1 += ch
            else:
                carrer_up1 += " "
        carrer_up1 = wl.lemmatize(carrer_up1)
        token = word_tokenize(carrer_up1) 
        carrer_option[carrer] = token

    for ssh in option_ssh.keys():
        ssh_up = option_ssh[ssh].lower()    #helps while compairing values    
        ssh_up1 = ""
        for ch in ssh_up: 
            if ch not in string.punctuation:
                ssh_up1 += ch
            else:
                ssh_up1 += " " 
        ssh_up1 = ps.stem(ssh_up1)
        token = word_tokenize(ssh_up1) 
        ssh_option[ssh] = token

    for course in prev_courses_available.keys():
        course_up = prev_courses_available[course].lower()    #helps while compairing values    
        course_up1 = ""
        for ch in course_up: 
            if ch not in string.punctuation:
                course_up1 += ch
            else:
                course_up1 += " " 
        course_up1 = wl.lemmatize(course_up1)
        token = word_tokenize(course_up1)
        token_1 = []
        for i in token:
            if i not in non_useful_words:
                token_1.append(i)
        prev_courses_option[course] = token_1
        

def student_info():
    print('------------------------------------------------------------')
    name= str(input('Please enter your name: '))
    file_ptr = open("input.txt", 'w')
    file_ptr.write('name('+name+').\n')
    file_ptr.close()


def career_choice():
    non_useful_words = set(stopwords.words('english')) 
    wl = WordNetLemmatizer()
    #taking a complete sentance as an input 
    print('------------------------------------------------------------')
    print("Which career you want to pursue?")
    carrer_input = input()
    carrer_input_list = []
    wl = WordNetLemmatizer()

    carrer_input = carrer_input.lower()    #helps while compairing values  
    carrer_input1 = ""
    for ch in carrer_input: 
        if ch not in string.punctuation:
            carrer_input1 += ch
        else:
            carrer_input1 += " "    
    carrer_input1 = wl.lemmatize(carrer_input1)
    carrer_input_list = word_tokenize(carrer_input1) 

    count = 0
    carrer_choosen = ''
    for i in carrer_option:
        for j in carrer_input_list:
            if j not in non_useful_words and carrer_option[i].count(j): 
                carrer_choosen = i
                count = count + 1
                break

    if count > 1: 
        print('Only one carrer choice is allowed, Procceding with one of the input choices')
    # If it didn't match with any 
    elif count == 0:
        carrer_choosen = 'na'
    file_ptr = open('input.txt', 'a')
    file_ptr.write('career_selected('+carrer_choosen+').\n')
    file_ptr.close()


def ssh_choice():
    non_useful_words = set(stopwords.words('english')) 
    ps = PorterStemmer()
    print('------------------------------------------------------------')
    print("What Are Your Interest Area?")
    ssh_input = input()
    ssh_input_list = []

    ssh_input = ssh_input.lower()    #helps while compairing values     
    ssh_input1 = ""
    for ch in ssh_input: 
        if ch not in string.punctuation:
            ssh_input1 += ch
        else:
            ssh_input1 += " "   
    ssh_input_list = word_tokenize(ssh_input1) 
    for i in range(0, len(ssh_input_list)):
        ssh_input_list[i] = ps.stem(ssh_input_list[i])

    ssh_choosed = []
    for i in ssh_option:
        for j in ssh_input_list:
            if j not in non_useful_words and ssh_option[i].count(j): 
                ssh_choosed.append(i)

    if len(ssh_choosed) == 0:
        ssh_choosed.append('5')

    file_ptr = open('input.txt', 'a')
    for i in ssh_choosed:
        file_ptr.write('ssh_selected('+i+').\n')    
    file_ptr.close()


def prev_done_course():
    non_useful_words = set(stopwords.words('english')) 
    wl = WordNetLemmatizer()
    print('------------------------------------------------------------')
    print("What are the courses that you have completed ? ")
    prev_courses_input = input()
    prev_courses_input_list = []

    prev_courses_input = prev_courses_input.lower()    #helps while compairing values     
    prev_courses_input1 = ""
    for ch in prev_courses_input: 
        if ch not in string.punctuation:
            prev_courses_input1 += ch
        else:
            prev_courses_input1 += " "   
    prev_courses_input1 = wl.lemmatize(prev_courses_input1)
    prev_courses_input_list = word_tokenize(prev_courses_input1) 

    course_done = []
    score = {}
    # if user added the course code 
    for i in prev_courses_option:
        score[i] = 0
        if prev_courses_input_list.count(i):
            course_done.append(i)

    for i in prev_courses_option:
        for j in prev_courses_input_list:
            if j not in non_useful_words and prev_courses_option[i].count(j): 
                score[i] += 1

    for i in score:
        score[i] = score[i]/len(prev_courses_option[i])
    
    print('\n------------------------------------------------------------')
    print("Please Verify the courses : ")
    for i in score:
        if score[i] >= 0.5:
            option = str(input("Completed: "+prev_courses_available[i]+ "(y or n) ? "))
            if option == 'y':
                course_done.append(i)

    file_ptr = open('input.txt', 'a')
    for i in course_done:
        file_ptr.write('done_course('+i+').\n')    
    file_ptr.close()

def main():
    setting_env()
    student_info()
    career_choice()
    ssh_choice()
    prev_done_course()

    # swipl = Prolog()
    # swipl.consult('2020086.pl')
    # list(swipl.query('start'))
    print('------------------------------------------------------')
    print("Text file of facts named 'input.txt' generated")
    print('------------------------------------------------------')

main()