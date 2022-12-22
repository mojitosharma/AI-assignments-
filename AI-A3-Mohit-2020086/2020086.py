from durable.lang import *

available_course_list = {1 : 'introduction_to_intelligent_sytems', 2 : 'machine_learning',
                        3 : 'artificial_intelligence', 4 : 'quantum_mechanics',
                        5 : 'introduction_to_quantum_computing', 6 : 'quantum_materials_and_devices',
                        7 : 'fundamentals_of_database_management_system', 8 : 'big_data_analytics',
                        9 : 'database_system_implementation', 10 : 'design_drawing_and_visualization' ,
                        11 : 'prototyping_interactive_systems', 12 : 'human_computer_interaction' , 
                        13 : 'econometrics_I', 14: 'Microeconomics' , 
                        15 : 'Macroeconomics',
                        16 : 'theatre_appreciation',17 : 'introduction_to_the_study_of_literature',
                        18 : 'indian_poetry_through_the_ages', 19 : 'foundations_of_finance'}

available_interest_list = {1 : 'music', 2 : 'dancing', 3: 'design', 4 : 'performing', 5 : 'finance'}


# Rulset to check if user gave any input 
with ruleset('choice'):
    
    # if user gave any course done input 
    @when_all(m.course_count >= 1)
    def course(c):
        print("These are the career choice according to course done and their marks")
        c.assert_fact('course', {'course' : c.m.course})
        print("-------------------------------------------------------")

        
    #if user gave any interest input 
    @when_all(m.interest_count >= 1)
    def interest(c):
        print("These are the career choice according to your interests and interest levels")
        c.assert_fact('interest', {'interest' : c.m.interest})
        print("-------------------------------------------------------")
    
    #if user gave none course done input
    @when_all(m.course_count == 0)
    def course(c):
        print("-------------------------------------------------------")
        print("Don't worry first do some of the courses")
        print('Here are some of the courses you can try')
        c.assert_fact({ 'subject': 'artificial_intelligence', 'type': 'cse elective'})
        c.assert_fact({ 'subject': 'introduction_to_quantum_computing', 'type': 'ece elective'})
        c.assert_fact({ 'subject': 'fundamentals_of_database_management_system', 'type': 'cse elective'})
        c.assert_fact({ 'subject': 'econometrics_I', 'type': 'eco elective'})

    
    #if user gave none interest done input 
    @when_all(m.interest_count == 0)
    def interest(c):
        print("-------------------------------------------------------")
        print("Don't worry here are the some courses to see what what your interests are: ")
        c.assert_fact({ 'ssh': 'theatre_appreciation', 'type': 'ssh elective'})
        c.assert_fact({ 'ssh': 'introduction_to_the_study_of_literature', 'type': 'ssh elective'})
        c.assert_fact({ 'ssh': 'indian_poetry_through_the_ages', 'type': 'ssh elective'})
        c.assert_fact({ 'ssh': 'foundations_of_finance', 'type': 'eco elective'})

    @when_all(+m.subject)
    def output(c):
        print('Subject Recommended: {0} \t type : {1}'.format(c.m.subject, c.m.type))

    @when_all(+m.ssh)
    def output(c):
        print('Subject Recommended: {0} \t type : {1}'.format(c.m.ssh, c.m.type))


# course ruleset 
with ruleset('course'):

    # --------------------------------------------------------------------------
    #For Artificial Intelligence 
    # took introduction_to_intelligent_sytems and machine_learning
    @when_all(m.course.anyItem((item.introduction_to_intelligent_sytems >= 9)) & m.course.anyItem((item.machine_learning >= 8)) & m.course.anyItem((item.artificial_intelligence <= 0)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Artificial Intelligence' })

    # took introduction_to_intelligent_sytems and artificial_intelligence
    @when_all(m.course.anyItem((item.introduction_to_intelligent_sytems >= 9)) & m.course.anyItem((item.machine_learning <= 0)) & m.course.anyItem((item.artificial_intelligence >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Artificial Intelligence' })

    # took introduction_to_intelligent_sytems, machine_learning and artificial_intelligence passed last with less grades 
    @when_all(m.course.anyItem((item.introduction_to_intelligent_sytems >= 9)) and m.course.anyItem((item.machine_learning >= 8)) & m.course.anyItem((item.artificial_intelligence > 3)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Artificial Intelligence' })

   # took introduction_to_intelligent_sytems, machine_learning and artificial_intelligence passed sencond with less grades 
    @when_all(m.course.anyItem((item.introduction_to_intelligent_sytems >= 9)) & m.course.anyItem((item.machine_learning > 3)) & m.course.anyItem((item.artificial_intelligence >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Artificial Intelligence' })


    # --------------------------------------------------------------------------
    #For Quantum Researcher
    # took introduction_to_quantum_computing and quantum_mechanics
    @when_all(m.course.anyItem((item.introduction_to_quantum_computing >= 9)) & m.course.anyItem((item.quantum_mechanics >= 8)) & m.course.anyItem((item.quantum_materials_and_devices <= 0)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Quantum Researcher' })

    # took introduction_to_quantum_computing and quantum_materials_and_devices
    @when_all(m.course.anyItem((item.introduction_to_quantum_computing >= 9)) & m.course.anyItem((item.quantum_mechanics <= 0)) & m.course.anyItem((item.quantum_materials_and_devices >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Quantum Researcher' })

    # took introduction_to_quantum_computing, quantum_mechanics and quantum_materials_and_devices passed last with less grades 
    @when_all(m.course.anyItem((item.introduction_to_quantum_computing >= 9)) and m.course.anyItem((item.quantum_mechanics >= 8)) & m.course.anyItem((item.quantum_materials_and_devices > 3)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Quantum Researcher' })

   # took introduction_to_quantum_computing, quantum_mechanics and quantum_materials_and_devices passed sencond with less grades 
    @when_all(m.course.anyItem((item.introduction_to_quantum_computing >= 9)) & m.course.anyItem((item.quantum_mechanics > 3)) & m.course.anyItem((item.quantum_materials_and_devices >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Quantum Researcher' })


    # --------------------------------------------------------------------------
    #For Data Scientist
    # took fundamentals_of_database_management_system and big_data_analytics
    @when_all(m.course.anyItem((item.fundamentals_of_database_management_system >= 9)) & m.course.anyItem((item.big_data_analytics >= 8)) & m.course.anyItem((item.database_system_implementation <= 0)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Data Scientist' })

    # took fundamentals_of_database_management_system and database_system_implementation
    @when_all(m.course.anyItem((item.fundamentals_of_database_management_system >= 9)) & m.course.anyItem((item.big_data_analytics <= 0)) & m.course.anyItem((item.database_system_implementation >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Data Scientist' })

    # took fundamentals_of_database_management_system, big_data_analytics and database_system_implementation passed last with less grades 
    @when_all(m.course.anyItem((item.fundamentals_of_database_management_system >= 9)) and m.course.anyItem((item.big_data_analytics >= 8)) & m.course.anyItem((item.database_system_implementation > 3)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Data Scientist' })

   # took fundamentals_of_database_management_system, big_data_analytics and database_system_implementation passed sencond with less grades 
    @when_all(m.course.anyItem((item.fundamentals_of_database_management_system >= 9)) & m.course.anyItem((item.big_data_analytics > 3)) & m.course.anyItem((item.database_system_implementation >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Data Scientist' })


    # --------------------------------------------------------------------------
    #For UI/UX designer
    # took design_drawing_and_visualization and prototyping_interactive_systems
    @when_all(m.course.anyItem((item.design_drawing_and_visualization >= 9)) & m.course.anyItem((item.prototyping_interactive_systems >= 8)) & m.course.anyItem((item.human_computer_interaction <= 0)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'UI/UX designer' })

    # took design_drawing_and_visualization and human_computer_interaction
    @when_all(m.course.anyItem((item.design_drawing_and_visualization >= 9)) & m.course.anyItem((item.prototyping_interactive_systems <= 0)) & m.course.anyItem((item.human_computer_interaction >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'UI/UX designer' })

    # took design_drawing_and_visualization, prototyping_interactive_systems and human_computer_interaction passed last with less grades 
    @when_all(m.course.anyItem((item.design_drawing_and_visualization >= 9)) and m.course.anyItem((item.prototyping_interactive_systems >= 8)) & m.course.anyItem((item.human_computer_interaction > 3)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'UI/UX designer' })

   # took design_drawing_and_visualization, prototyping_interactive_systems and human_computer_interaction passed sencond with less grades 
    @when_all(m.course.anyItem((item.design_drawing_and_visualization >= 9)) & m.course.anyItem((item.prototyping_interactive_systems > 3)) & m.course.anyItem((item.human_computer_interaction >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'UI/UX designer' })


    # --------------------------------------------------------------------------
    #For Economist
    # took econometrics_I and Microeconomics
    @when_all(m.course.anyItem((item.econometrics_I >= 9)) & m.course.anyItem((item.Microeconomics >= 8)) & m.course.anyItem((item.Macroeconomics <= 0)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })

    # took econometrics_I and Macroeconomics
    @when_all(m.course.anyItem((item.econometrics_I >= 9)) & m.course.anyItem((item.Microeconomics <= 0)) & m.course.anyItem((item.Macroeconomics >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })

    # took econometrics_I, Microeconomics and Macroeconomics passed last with less grades 
    @when_all(m.course.anyItem((item.econometrics_I >= 9)) and m.course.anyItem((item.Macroeconomics >= 8)) & m.course.anyItem((item.Macroeconomics > 3)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })

   # took econometrics_I, Microeconomics and Macroeconomics passed sencond with less grades 
    @when_all(m.course.anyItem((item.econometrics_I >= 9)) & m.course.anyItem((item.Microeconomics > 3)) & m.course.anyItem((item.Macroeconomics >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })
        

    # If completed ssh course with good grades recommend respective career option to user
    @when_all(m.course.anyItem((item.theatre_appreciation >= 9)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Actor' })

    @when_all(m.course.anyItem((item.introduction_to_the_study_of_literature >= 9)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Paper Reviewer' })
    
    @when_all(m.course.anyItem((item.indian_poetry_through_the_ages == 10)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Poet' })

    @when_all(m.course.anyItem((item.foundations_of_finance >= 8)))
    def course(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })
        

#iterest ruleset 
with ruleset('interest'):
    # interest level in music is greater than 4 recommend musician as career 
    @when_all(m.interest.anyItem((item.music >= 4)))
    def interest(c):
        c.assert_fact('career_choice' ,{'choice': 'Musician' })

    # interest level in dancing is greater than 4 recommend dancer as career 
    @when_all(m.interest.anyItem((item.dancing >= 4)))
    def interest(c):
        c.assert_fact('career_choice' ,{'choice': 'Dancer' })

    # interest level in design is greater than 3 recommend UI/UX designer as career 
    @when_all(m.interest.anyItem((item.design >= 3)))
    def interest(c):
        c.assert_fact('career_choice' ,{'choice': 'UI/UX designer' })

    # interest level in performing is greater than 4 recommend actor as career 
    @when_all(m.interest.anyItem((item.performing >= 4 )))
    def interest(c):
        c.assert_fact('career_choice' ,{'choice': 'Actor'})
    
    # interest level in finance is greater than 3 recommend Economist as career 
    @when_all(m.interest.anyItem((item.finance >= 3)))
    def interest(c):
        c.assert_fact('career_choice' ,{'choice': 'Economist' })



# ruleset for career_choice to print details if any for the career else normally print them 
with ruleset('career_choice'):
    # @when_all(m.choice == 'Artificial Intelligence')
    # def fun(c):
    #     print("Lorem ipsum")
    
    @when_all(+m.choice)
    def output(c):
        print('career Option: {0}'.format(c.m.choice))


# fucntion that take user courses and grades
def course():
    career_list = []
    selected_list = []
    career_count = 0
    option = 1
    grade = 0
    grade_list = []
    print('--------------------------------------------------------------------')
    print("Please enter the courses done if any enter '-1' to end")
    print("-------------------------------------------")
    for i in available_course_list:
        print(str(i)+" : "+ available_course_list[i])
        grade_list.append(0)
    print("-------------------------------------------")
    
    while(1):
        option = int(input("Enter Course Number : "))
        if(option == -1):
            break
        grade = int(input("Enter Course grade : "))
        if((option <= 0 or option > len(available_course_list)) or (grade < 0 or grade > 10)):
            print("Invaild option !! Try again !")
            print("-----------------------------")
        elif(selected_list.count(option) == 0):
            print("course : "+str(available_course_list[option])+"   grades : "+ str(grade))
            print("-----------------------------")
            selected_list.append(option)
            grade_list[option-1] = grade
            career_count = career_count+1
            
    for i in range(0, len(grade_list)):
        career_list.append({ available_course_list[i+1] : grade_list[i]})
    print(career_list)
    return career_count,career_list


# fucntion that take user interest and grades
def interest():
    interest_list = []
    selected_list = []
    interest_count = 0
    option = 1
    interest_level = 0
    interest_level_list = []
    print()
    print('--------------------------------------------------------------------')
    print("Please enter interest if any enter '-1' to end")
    print("-------------------------------------------")
    for i in available_interest_list:
        print(str(i)+" : "+ available_interest_list[i])
        interest_level_list.append(0)
    print("-------------------------------------------")
    while(1):
        option = int(input("Enter Interest Number : "))
        if(option == -1):
            break
        interest_level = int(input("Enter Interest level (1 to 5) : "))

        if(option <= 0 or option > len(available_interest_list) or (interest_level < 1 or interest_level > 5)):
            print("Invaild option !! Try again !")
            print("-----------------------------")
        elif(selected_list.count(option) == 0):
            print("Inerest : "+str(available_interest_list[option])+"   Interest level : "+ str(interest_level))
            selected_list.append(option)
            interest_level_list[option -1] = interest_level
            print("-----------------------------")
            interest_count = interest_count+1

    for i in range(0, len(interest_level_list)):
        interest_list.append({ available_interest_list[i+1] : interest_level_list[i]})
    return interest_count,interest_list

def main():
    print("---------------------career advisory system-------------------------")
    print("Enter your name: ",end='')
    name = input()
    print('--------------------------------------------------------------------')
    print("Hi! "+name+", welcome to the career advisory system for a graduating student of IIITD")
    print('--------------------------------------------------------------------')
    print("Please answer the questions: ")
    course_count, course_list = course()
    interest_count, interest_list = interest()
    print("-------------------------------------------------------")
    assert_fact('choice', {'course_count': course_count,'course': course_list, 'interest_count' : interest_count, 'interest': interest_list})

main()