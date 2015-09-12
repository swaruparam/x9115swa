##**Reading Assignment 1: Summary**


####**i. Reference**

**Swapna Gottipati, David Lo, and Jing Jiang. ASE 2011. Finding Relevant Answers in Software Forums.**

**Link to the paper: ** [Paper] ( https://github.com/swaruparam/x9115swa/blob/master/hw/read/1/Finding%20Relevant%20Answers%20in%20Software%20Forums.pdf )


####**ii. Keywords**

**ii1. Software Forums** 
These are webpages that consist of Question-Answer type conversations for users (typically developers) and serve as platforms where they can discuss the issues faced and go about suggesting ways on how to go about resolving them. These threads can be of extreme value in content when accurately searched for the necessary tags.

**ii2. Normalized discounted cumulative gain (NDCG)**
This metric is used to rank quality by measuring the performance of a recommendation system based on the graded relevance of the entities used. It ranges from 0.0 to 1.0, with 1.0 representing the ideal ranking. It is commonly used in information retrieval tools and to evaluate the performance of web search engines.

**ii3. Positive/Negative Feedback**
The answers posted on the thread in a web forum can be classified as positive, negative or junk based on the content, in order to efficiently filter the number of posts and extract only the relevant data. Positive feedback answers are those which resolve or provide solutions to the question being asked, negative feedback are those posts which indicate that the proposed solution fails and that the issue is yet to be resolved.

**ii4. Feature Vector**
Before processing large amounts of text data, they are usually converted into feature vectors, which are simplified words obtained from the original text. These processed words hold the main content and can be used for classification purposes. Examples of processes, which aid in producing feature vectors, are stop word removal (which removes non-descriptive words such as prepositions and pronouns) and stemming (extracting affixes).


####**iii. Brief Notes**

**iii1. Motivational Statements**
Software forums are rich in content and knowledge, which are also easily accessible. However, the problem with these portals is that the thread of posts increases to a very large number, accumulating junk along with useful information. When a user logs onto the portal to lookup a particular issue or question, he may have to go through a large thread, in order to obtain the solution. There may be cases where the positive feedback may not show up amidst the high volume of posts. It is important that data retrieval is as efficient as the database, so that the software forums could be used to its utmost capabilities.

**iii2. Hypotheses**
The authors have come with a model that would serve as an efficient search engine within these forums, in order to capture the required data from the abundant text present. Based on some learning and extraction of feature vectors, the model would be able to filter the desired posts in a thread according to the user's needs. This would produce an accurate response when the user inputs his issue that needs to be resolved. In addition to indexing and classifying the text data, this new model also tags and filters it. Thus, the model does not require the initial information to be input as tagged as it would take care of it by itself. Also, the filterer extracts only the necessary posts that the user may have to go through to obtain the required solution.

**iii3. New Results**

The new model's framework defers from the previous models in the aspect of the additional Tagger and Filterer. The structure and flow of the operations conducted on the text is shown in the diagram below.

![search_engine](search_engine.png)

The proposed framework claims to increase mean average precision from 17% to 71% in retrieving relevant answers to various queries. Based on effective classification of positive feedback, negative feedback and junk, the desired posts are extracted and are filtered to achieve this high precision ratio.

**iii4. Related Work**

<ul>
<li> S. Thummalapenta and T. Xie. Spotweb: Detecting framework hotspots and coldspots via mining open source code on the web. In ASE, pages 327–336, 2008. - is similar in the sense that information is extracted from the web but uses code from Google code instead of textual data. </li>

<li> X. Wang, L. Zhang, T. Xie, J. Anvik, and J. Sun. An approach to detecting duplicate bug reports using natural language and execution information. In ICSE, pages 461–470, 2008. - analyzes textual information and executes trace in bug reports to detect duplicate bug reports. </li>

<li> H. Zhong, L. Zhang, T. Xie, and H. Mei. Inferring resource specifications from natural language API documentation. In ASE, pages 307–318,2009. - infers tags from software documentation instead of from software forums as in this paper.

</ul>


####**iv. Suggested Improvements**

<ul>
<li> In addition to retrieving valuable solutions for the user's query, the model can be extended to detect the questions which are yet to be answered, or sub-queries within a thread which are yet to be resolved, and sent to the experts to be answered. </li>

<li> Posts may consists of spelling and grammatical errors. Certain important keywords may also be lost due to such errors. This can be looked into to eradicate false results occurring due to these words.</li>

<li> The current macro (post) model can be extended to the micro (sentence) level. An automated approach can be designed that could arrange or cluster the forum posts in a hierarchical fashion to help users in finding the right answer to the question. </li>
</ul>


