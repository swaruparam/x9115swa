##**Reading Assignment 2: Summary**


####**i. Reference**

**Raymond P.L. Buse and Westley Weimer. The University of Virginia. ASE 2010. Automatically Documenting Program Changes.**

**Link to the paper: ** [Paper] ( https://github.com/swaruparam/x9115swa/blob/master/hw/read/2/Automatically%20Documenting%20Program%20Changes.pdf )


####**ii. Keywords**

**ii1. Commit Messages** 
Commit messages or log messages are key components of software maintenance. They are descriptive content, clarifying the purpose of code revision or providing information about the bugs present. In the field of software development, it is important for such messages to accompany changes in code, so as to enable easy referencing of the changes and program flow in future.

**ii2. Differencing**
This phenomenon states the exact lines of program code, which have been changed from the previous version. There are multiple tools that point to these blocks of code, so as to efficiently let the developer compare the alterations.

**ii3. Code Summarization**
Code summarization refers to the documentation of the program, explaining the changes made if any. Modification in code, future changes that needs to accounted, present bugs, test cases that need to be included, etc. are the information which are provided by code summarization. 

**ii4. Path Predicates**
These are formulae, which indicate the path of program flow, i.e., the statements that would be executed in a particular case or condition. In order to obtain efficient code documentation, it is necessary to iterate through all loop-free path predicates in a program and document the steps taken for all cases exhaustively.


####**iii. Brief Notes**

**iii1. Motivational Statements**
At the rate of the creation of Android apps today, there are increasing number of applications amidst these which have undocumented bugs and errors which aren't always picked up by the traditional compilers and IDE. Since these apps follow a structured approach, many underlying errors are commonly looked past during the deployment. Additionally, though the programming language is predominantly Java, it is seen that many apps are developed without exercising the right usage of 'Activity' component lifecycle, an additional plugin of Android not supported by Java. In the cases of multithreading operations, multiple execution and rigorous testing can only raise the code faults. To cater to these needs, the authors of the paper propagate an automated testing tool, AndroidRipper, which does a through structured check on the developed app using the GUI, pointing out faults which aren't previously documented or detected.

**iii2. Hypotheses**
AndroidRipper would prevent applications from being developed with faulty errors in the underlying code and make the framework stable even in cases of odd edge cases. The program flow structure is observed en-to-end using this model by observing the application’s GUI and exploits all possible situations that may arise. Using this would prompt even the previously undetected or undocumented errors and thus, improve the efficiency of the application as a whole. The authors of the paper believed that this would also reduce the time spent on debugging and would prove as a much better alternative to Monkey, the existing standard debugging tool for Android applications. 


**iii3. New Results**

The proposed model, AndroidRipper, is designed to dynamically analyze the application's GUI, looking out for sequences of events fire able through the GUI widgets. It maintains a state machine model or tree to save the state transitions and events occurred during each stage. Concepts such as events, tasks, actions, and exploration criteria are clearly defined during each execution stage on the GUI tree model. Based on this, the structured program flow of the framework is observed, debugging for errors at all stages in parallel. The results of this model are compared against the Monkey debugging tool and it is observed that AndroidRipper picks up undocumented faults at a fast rate, all performed by the automated tool. Monkey masked the occurrences of certain masks and did not throw an exception in such cases. AndroidRipper also revealed a much higher percentage of covered LOCs when compared to Monkey.

The results observed are tabulated as shown, where R1, R2 and R3 are three phases of AndroidRipper and RM is a single execution of Monkey:
![new_results](new_results.png)

**iii4. Related Work**

<ul>
<li> Cuixiong Hu and Iulian Neamtiu. 2011. Automating GUI testing for Android applications. In Proceedings of the 6th International Workshop on Automation of Software Test (AST '11). ACM, New York, NY, USA, 77-83. - Reports specific Android bugs, classified according to Event, Activity, API, etc. </li> 

<li> Android Developers, The Developer’s Guide. UI/Application Exerciser Monkey,http://developer.android.com/guide/developing/tools/monkey.html last accessed on February 29th, 2012. - Generates random or deterministic sequences of events automatically and supports the interaction with the mobile device. </li> 

<li> Tommi Takala, Mika Katara, and Julian Harty. 2011. Experiences of System-Level Model-Based GUI Testing of an Android Application. In Proceedings of the 2011 Fourth IEEE International Conference on Software Testing, Verification and Validation (ICST '11). IEEE Computer Society, Washington, DC, USA, 377-386. - Proposes a model-based approach for Android GUI testing.  </li>

</ul>


####**iv. Suggested Improvements**

<ul>
<li> The detection of faults can be made much faster by speeding up the generation of GUI model tree for the application. </li>

<li> The existing model caters to the bugs and fixes which are originated by actions, tasks, events or exploration criteria. This can be expanded to include consideration of code exceptions during parallel operations, non-structured program flow and account for activity-based interactive applications. </li>

</ul>




