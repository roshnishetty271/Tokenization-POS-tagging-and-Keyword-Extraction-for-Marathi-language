Abstract:


Part of speech plays a very major role in NLP task as it is important to know how a word is used in every sentences.POS tagging is a process of assigning the words in a text corresponding to  a particular part of  speech. A  fundamental  version  of  POS  tagging  is  the  identification  of words  as  nouns,  verbs,  adjectives  etc.  For  processing  natural languages, Part of Speech tagging is a prominent tool. It is one of the  simplest  as well  as  most  constant  and  statistical  model  for many  NLP applications.  
POS  Tagging  is  an  initial  stage  of linguistics,  text  analysis  like  information  retrieval,  machine translator, text to speech synthesis, information extraction etc. In POS Tagging we  assign a  Part  of  Speech tag to  each  word  in a sentence and literature.Various approaches have been  proposed to implement POS taggers. 
POS tagging is difficult for Marathi language due to unavailability of corpus for computational processing.
We have used a  Marathi  part  of  speech tagger.  It  is morphologically rich  language. Marathi is spoken by  the  native people  of  Maharashtra.  The  general  approach  used  for assigning POS tagging is with the help of TnT(Trigrams ‘n’ Tags) tagger that works on Second order Markov Model.  It also introduces a tag set for Marathi which can  be  used  for  tagging Marathi text. POS tagging is used mostly for Keyword Extractions, phrase extractions, Named Entity Recognition, etc.
 
Project Inputs and Outputs:


 Inputs Details

     Text =" सनातनवाद्यांनी व प्रतिगाम्यांनी समाज रसातळाला नेला असताना या अंधारात बाळशास्त्री जांभेकर
       यांनी माध्यमातून पहिली ज्ञानज्योत तेववली , प्रतिपादन नटसम्राट प्रभाकर पणशीकर यांनी केले."


 Evaluation Parameters Details


For Evalutation purpose, the tagged file compared with the original manually tagged file 
and the differences were recorded. Considering the tagging accuracy as the 
percentage of correctly assigned tags, we have evaluated the performance of the taggers from two 
different aspects: 
(1) the overall accuracy (taking into account all tokens in the test corpus) 
(2) the accuracy for known and unknown words, respectively. 
It is interesting to know how it would cope with words that did not appear in its training. 
In general: 

1. The overall part-of-speech tagging accuracy of TnT tagger is very high.
2. The accuracy of known tokens is significantly higher than that of unknown tokens



	
	
	
	
	
	
	
	

	
	
	
 Output Details and Screenshots


[1] Tokenization:

![image](https://github.com/roshnishetty271/Tokenization-POS-tagging-and-Keyword-Extraction-for-Marathi-language/assets/144407427/4fca6840-3f0c-4b0e-aab6-20b42754364d)





[2] POS Tagging:

![image](https://github.com/roshnishetty271/Tokenization-POS-tagging-and-Keyword-Extraction-for-Marathi-language/assets/144407427/912ca96b-fd8d-4fad-8e6c-5689b15d6601)

 
[3]Keyword Extraction:


![image](https://github.com/roshnishetty271/Tokenization-POS-tagging-and-Keyword-Extraction-for-Marathi-language/assets/144407427/66f67d82-15a3-4e49-b261-f9aedeaa73ca)






















Summary
	
The Part-of-speech tagging is playing an important role invarious speech and language processing applications. Currently many tools are available to do this task of part of speech tagging. The POS taggers described here is very simple and efficient for automatic tagging, but the morphological
complexity of the Marathi makes it little hard. The results ofall the taggers are impressive. The performance of the current system is good and the results achieved by methods are excellent. 

Future Scope

We believe that future enhancements of this work would be to improve the tagging accuracy by increasing the size of tagged corpus. Also, we will further be working on minimizing the language dependency of the systems. We can improve our model by making it into a hybrid POS tagger by using morphological analysis for the respective language and getting a high accuracy of the text.

