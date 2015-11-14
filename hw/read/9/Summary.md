##**Reading Assignment 9: Summary**


####**i. Reference**

**Andrea Arcuri, Gordon Fraser, Juan Pablo Galeotti. ASE 2014. Automated Unit Test Generation for Classes with Environment Dependencies**

**Link to the paper: ** [Paper] ( https://github.com/swaruparam/x9115swa/blob/master/hw/read/9/Automated%20Unit%20Test%20Generation%20for%20Classes%20with%20Environment%20Dependencies.pdf )


####**ii. Keywords**

**ii1. Environment**
This refers to the file system, network or user-interactions that the classes of a program interact with. These may cause a problem in the case of automatic test-case generation, since the environment may hinder the execution of a process or mess up dependent executions of one program flow.

**ii2. EVOSUITE** 
It is a Java test generation tool, satisfying a coverage criterion, which also includes effective assertions for programs summarizing the behavior of the current execution. The authors of this paper have extended this tool in order to let it accommodate test-case generation of programs in which environment-dependent classes are present.

**ii3. Mocking**
It is mechanisms by which classes are isolated form their dependencies. Replacing classes during the testing phase, instead of retaining the original classes, does this. The behavior of this replaced class can be predetermined and programmed in favour of the developer.

**ii4. Dynamic Symbolic Execution**
It is the combination of concrete execution and symbolic execution, in order to achieve higher efficiency in terms of providing security and automated testing purposes. It is applicable directly to the binaries and works better in programs with multiple loops.


####**iii. Brief Notes**

**iii1. Motivational Statements**

Object-oriented software consists of user-level classes, which depend on the environments of the program. Generating automatic test cases for such programs results in a number of problems, since the program flow does not remain static and becomes unpredictable with changes in the environment. One problem is that, models working on such problem so not yield maximum coverage as it becomes impossible to cover all cases by mere function and class calls. If a particular class depends on the contents of a file, it is not possible to traverse this case without turning to the hardware support. Another problem that arises is that even if the class can be covered within the test-case, the resulting tests may be unstable. If a particular class takes the system time as input, it may pass for that one time but would fail for repeated trials. Thus, it is important that for efficient test-case generation, the environment-dependent classes must be separated from the remaining program before processing. 

**iii2. Study Instruments**

The authors used the SF100 corpus, a collection of 11,219 Java classes from 100 Java projects randomly selected from Source Forge, as the medium to verify their developed tool. Three different sets of experiments were carried out, to determine if the tool accounted for the efficient program coverage and unstable classes. All these experiments were conducted on a cluster of computers using six cores (12 considering hyper-threading) at 2.6 GHz.

* 30 Java classes were manually selected from the SF100 corpus that interact with the environment, for example, require write access to files). Only such a biased set of classes were selected in order to be able to study what improvements could be made on these classes to most benefit from the proposed technique. Experiments were run with different random seeds and their behavior was noted down. On this set of 30 classes, EVOSUITE was applied with six different configurations: Base, Console, VFS, JVM, Static and All of them. For each configuration, the authors ran EVOSUITE 100 times on each Class Under Test (CUT) and recorded that each run lasted up to three minutes.

* Again, 30 Java classes were manually selected from the SF100 corpus that leads to unstable tests. It should be noted that not all classes interacting with the environment lead to unstable tests. The classes were selected based on the results obtained from EVOSUITE running on the generated tests. This experiment was also repeated 100 times with the same six configurations.

* For the third set of experiment, the whole SF100 corpus was used, consisting of all the 11,219 classes. Since this includes a large number of experiments, only two configurations were ran on each, namely Base and All. Each experiment was repeated five times with different random seeds.


**iii3. New Results**

The following research questions were answered by running the experiments as mentioned above.

* Does controlling the environment successfully increase coverage on known cases of environmental interactions? - Controlling the environment has a large impact on branch coverage, even in the order of +80%/+90%. It depends on the type of configuration used (Base giving rise to 29% average branch coverage while All achieves 82%) and the types of processes the class attempted on the file system (read, write, etc). 

* Does controlling the environment successfully resolve known issues of unstable tests? - Controlling the environment removes unstable tests for intended sources of non-determinism. For most cases, resetting the static state or mocking non-deterministic JVM calls removes all unstable tests. However, there are still a number of cases which prove to be the corner cases and still require further engineering to rectify the instability in them.

* How do results generalize to the SF100 corpus? - Coverage on SF100 increased significantly, and half reduced the number of unstable tests. The default version of EVOSUITE achieves 76.5% branch coverage when run on all the classes. It fails to meet a perfect 100% due to the varied class types and the differences in I/O processes each works on. In general, this number can be further increased if the tool were to generate relevant content for the files.

* How many unsafe environmental interactions does EVOSUITE now handle? - The implementation covers a large share of I/O, but fully covering the Java standard library is ongoing engineering effort. Since not all Java API classes are mocked, some CUTs may access the each file system even when EVOSUITE runs on a virtual file system. When this occurs, the default sandbox will prevent harmful operations, but only a fraction of the I/O issues are solved. 


**iii4. Related Work**

<ul>
<li> P. Godefroid, N. Klarlund, and K. Sen. DART: directed automated random testing. In PLDI’05: Proceedings of the 2005 ACM SIGPLAN Conference on Programming Language Design and Implementation, pages 213–223. ACM, 2005. - Dynamic Symbolic Execution (DSE), technique of automated test generation for high code coverage. </li> 

<li> P. McMinn. Search-based software test data generation: A survey. Software Testing, Verification and Reliability, 14(2):105–156, 2004. - Search Based Software Testing (SBST), technique of automated test generation for high code coverage. </li> 

<li> G. Fraser and A. Arcuri. Sound empirical evidence in software testing. In ACM/IEEE International Conference on Software Engineering (ICSE), pages 178–188, 2012. - Describes occurrence of environment interactions by running experiments with EVOSUITE unit generation tool on 100 randomly selected Java projects from SourceForge.  </li>
</ul>


####**iv. Suggested Improvements**

<ul>
<li> Further sources of non-determinism can be handled in the currently developed implementation, so as to account for the remaining unstable tests.  </li>

<li> The mocking of APIs has been curtailed only to the file-related APIs in this paper, this can be improvised to run on different APIs which are mocked in order to separate dependency. </li>

<li> The current implementation does not categorize based on the input type, it only deals with optimizing the environmental state and inputs. If inputs are grouped by the input type (XML, binary), they can be processed accordingly, thereby improving the optimization technique. </li>

</ul>


