% Type start. to run the code

:-style_check(-singleton).
:-style_check(-discontiguous).
career(1,ai, 'Artificial Intelligence').
career(2,qrs, 'Quantum Researcher').
career(3,ds, 'Data Scientist').
career(4,uiux, 'UI/UX designer').
career(5,econ, 'Economist').
career(6,na, 'Not Decided').

ssh(1,acting).
ssh(2,reading).
ssh(3,poerty).
ssh(4,history).
ssh(5,non).

start:-                                                 
    nl,write('_________Electives advisory / prediction system for BTech or MTech student of IIITD__________'),nl,
    setting_env,
    student_info,
    career_choice,
    interest_course,
    career_selected(na) ->nan,exiting;
    pre_req_done(List),
    print_choice_availble,
    exiting.


setting_env:-                             % helper funtion used to set all facts and rules 
    retractall(name(_)),
    retractall(course_done_or_not()),
    retractall(career_selected(_)),
    retractall(course_choosen(_,_)),
    retractall(course(_,_,_,_)),
    retractall(course_to_print(_,_)),
    retractall(pre_req(_,_)),
    define_course,
    define_prereq.

define_course:-  
    retractall(course(_,_,_,_)),
    retractall(course_to_print(_,_)),
    assert(course(acting,'Theatre Appreciation',ssh211,2)),
    assert(course(reading,'Introduction To The Study Of Literature',ssh214,2)),
    assert(course(poerty,'Indian Poetry Through the Ages',ssh215,2)),
    assert(course(history,'Nation and her Narratives',ssh215,2)),

    assert(course(ai,'Introduction to Intelligent Systems',cse140,1)),
    assert(course(ai,'Aritificial Intelligence',cse643,6)),
    assert(course(ai,'Machine Learning',cse343,3)),
    assert(course(ai,'Natural Language Processing',cse556,5)),
    assert(course(ai,'Data Mining',cse506,5)),
    assert(course(ai,'Statistical Machine Learning',cse342,3)),

    assert(course(qrs,'Quantum Mechanics',ece525,5)),
    assert(course(qrs,'Photonics: Fundamentals & Applications',ece545,5)),
    assert(course(qrs,'Quantum Materials and Devices',ece524,5)),
    assert(course(qrs,'Introduction to Quantum Computing',cse622,6)),

    assert(course(ds,'Fundamentals of Database Management System',cse202,2)),
    assert(course(ds,'Big Data Analytics',cse557,5)),
    assert(course(ds,'Data Warehouse',cse606,6)),
    assert(course(ds,'Database System Implementation',cse507,5)),

    assert(course(uiux,'Prototyping Interactive Systems',des130,1)),
    assert(course(uiux,'Design Drawing & Visualization',des101,1)),
    assert(course(uiux,'Design of Interactive Systems',des205,2)),
    assert(course(uiux,'Visual Design & Communication',des202,2)),
    assert(course(uiux,'Design Processes and Perspectives',des201,2)),
    assert(course(uiux,'Human Computer Interaction',des204,2)),
    assert(course(uiux,'Ergonomics/Human factors for Design',des524,5)),

    assert(course(econ,'Econometrics I',eco221,2)),
    assert(course(econ,'Macroeconomics',eco201,2)),
    assert(course(econ,'Microeconomics',eco301,3)),
    assert(course(econ,'Game Theory',eco311,3)),
    assert(course(econ,'Foundations of Finance',eco331,3)),

    assert(course(cse,'Data Structures & Algorithms',cse102,1)),
    assert(course(cse,'Advanced Programming',cse201,2)),
    assert(course(cse,'Introduction to Programming',cse101,1)),
    assert(course(cse,'Algorithm Design and Analysis',cse222,2)),

    assert(course(mth,'Linear Algebra',mth100,1)),
    assert(course(mth,'Probability and Statistics',mth201,2)),
    assert(course(mth,'Multivariate Calculus',mth203,2)),
    assert(course(ece,'Fields and Waves',ece230,2)).

define_prereq:-
    retractall(pre_req(_,_)),
    assert(pre_req(cse643,cse102)),
    assert(pre_req(cse622,mth100)),
    assert(pre_req(cse202,cse102)),
    assert(pre_req(cse201,cse102)),
    assert(pre_req(cse201,cse101)),
    assert(pre_req(cse102,cse101)),
    assert(pre_req(cse222,cse102)),
    assert(pre_req(ece230,mth203)),
    assert(pre_req(des202,des101)),
    assert(pre_req(des201,des101)),
    assert(pre_req(cse343,mth100)),
    assert(pre_req(cse343,mth201)),
    assert(pre_req(cse343,cse101)),
    assert(pre_req(cse343,mth203)),
    assert(pre_req(cse556,cse101)),
    assert(pre_req(cse556,mth201)),
    assert(pre_req(cse556,cse222)),
    assert(pre_req(cse556,mth100)),
    assert(pre_req(cse506,cse101)),
    assert(pre_req(cse506,mth100)),
    assert(pre_req(cse506,mth201)),
    assert(pre_req(cse342,cse101)),
    assert(pre_req(cse342,mth201)),
    assert(pre_req(cse557,cse202)),
    assert(pre_req(cse606,cse202)),
    assert(pre_req(cse507,cse102)),
    assert(pre_req(cse507,cse202)),
    assert(pre_req(ece525,mth100)),
    assert(pre_req(cse622,mth100)),
    assert(pre_req(ece545,ece230)),
    assert(pre_req(eco221,mth201)).

student_info:-
    nl,write('Please enter your name: '),nl,
	read(Name),nl,assert(name(Name)),
    write('Hi '),write(Name),write('!, Welcome, to Electives advisory / prediction system.'),nl,write('Please answer the questions:'),nl.


career_choice:-
    write('------------------------------------------------------------'),nl,
    write('              Which career you want to pursue? '),nl,
    forall(career(X,Y,Z), (write(X),write('. '),write(Z),nl)),
    write('Enter option: '),
    read(Option),(career(Option,X,Y),assert(career_selected(X))).


helper1([Ch|List]):-            % get choice for area of interest
    write('Enter Choice '),
    read(Ch),
    Ch \= 5->
    (ssh(Ch,Type),course(Type,X,Y,Z)->(assert(course_choosen(X,Y)),helper1(List));helper1(List)).
helper1([]).

interest_course:-
    nl,write('------------------------------------------------------------'),nl,
    write('                  Ohter Area of Interest'),nl,
    write('1. Acting'),nl,
    write('2. Reading'),nl,
    write('3. Poetry'),nl,
    write('4. History'),nl,
    write('5. No/Done'),nl,
    helper1(List),nl.

helper2:- 
    career_selected(ai),retractall(course(qrs,_,_,_)),retractall(course(ds,_,_,_)),retractall(course(uiux,_,_,_)),retractall(course(econ,_,_,_));
    career_selected(qrs),retractall(course(ai,_,_,_)),retractall(course(ds,_,_,_)),retractall(course(uiux,_,_,_)),retractall(course(econ,_,_,_));
    career_selected(ds),retractall(course(qrs,_,_,_)),retractall(course(ai,_,_,_)),retractall(course(uiux,_,_,_)),retractall(course(econ,_,_,_));
    career_selected(uiux),retractall(course(qrs,_,_,_)),retractall(course(ds,_,_,_)),retractall(course(ai,_,_,_)),retractall(course(econ,_,_,_));
    career_selected(econ),retractall(course(qrs,_,_,_)),retractall(course(ds,_,_,_)),retractall(course(uiux,_,_,_)),retractall(course(ai,_,_,_)),
    fail;true.

helper3:-
    course(A,B,C,D),
    retract(course(A,B,C,D)),
    assert(course_to_print(B,C)),
    helper3,
    fail;true.

helper4([]).                % delete all the course and pre_req facts for the course that uses has completed
helper4([A|B]):-
    (retractall(pre_req(_,A));retractall(course(_,_,A,_))),helper4(B).

helper5([Ch|List]):-        % get pre_req course code
    write('Enter course code (Enter stop. for stopping): '),
    read(Ch),
    dif(Ch,stop),
    course(A,B,Ch,D), retract(course(A,B,Ch,D)),helper5(List).
helper5([]).

helper6(X):-            % print available course to select pre_req done
    course_to_print(A,B),
    retract(course_to_print(A,B)),
    write(X),write("        "),write(B),write("      "),write(A),nl,
    Y is X + 1,
    helper6(Y),fail;true.


pre_req_done(List):-
    write('------------------------------------------------------------'),nl,
    write('Please Select Courses that you have done from given list of Pre-requisites'),nl,
    write('S.no.  Course Code  Course Name'),nl,
    helper2,
    helper3,
    helper6(1),
    define_course,
    helper5(List),
    helper2,
    helper4(List).

helper7:-
    pre_req(A,B),
    retractall(pre_req(A,B)),retractall(course(C,D,A,F)),helper7,fail;true.

helper8:-
    career_selected(Ch),course(Ch,A,B,C),retractall(course(Ch,A,B,C)),assert(course_choosen(A,B)).

helper9(X):-
    course_choosen(A,B),define_course,course(M,N,B,P),
    retract(course_choosen(A,B)),
    write(P),write("            "),write(B),write("      "),write(A),nl,
    Y is X + 1,
    helper9(Y),fail;true.

print_choice_availble:-
    nl,write('------------------------------------------------------------'),nl,
    write('Here are the recomended list of Electives according to your answers'),nl,
    write('Course Level  Course Code  Course Name'),nl,
    helper7,
    helper8,
    helper9(1),
    fail;true.

nan:-
    career_selected(na),
    write('------------------------------------------------------------'),nl,
    write('Looks like you haven\'t decided yet'),nl,
    write('No worries! Here are some Introductory courses to Help you.'),nl,
    write('1: Introduction to Intelligent Systems - cse140'),nl,
    write('2: Human Computer Interaction - des204'),nl,
    write('3: Fundamentals of Database Management System - cse202'),nl,
    write('4: Fundamentals of Database Management System - cse202'),nl,
    write('5: Econometrics I -eco221'),nl,
    fail;true.

exiting:-
    nl,write('------------------------------------------------------------'),nl,
    write('Thanks for using our course prediction system'),nl,
    write('------------------------------------------------------------'),nl.