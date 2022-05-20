#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Word Vectors</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) Word Vectors (Word Embeddings)<br>
# 2) Matrix<br>
# 3) Bigrams and Trigrams<br>
# 4) Bag of Words<br>
# 

# ## Before you Start Reading!

# Before you star reading, I want you to do one thing. Think about the word concentation camp. Think about what concepts it evokes. Think about the first few words that come to mind. Write down a few proper nouns that come to mind as well.

# ## The Need to Represent Text Numerically

# Word vectors, or word embeddings, are numerical representations of words in multidimensional space through matrices. The purpose of the word vector is to get a computer system to understand a word. Computers cannot understand text efficiently. They can, however, process numbers quickly and well. For this reason, it is important to convert a word into a number.
# 
# Initial methods for creating word vectors in a pipeline take all words in a corpus and convert them into a single, unique number. These words are then stored in a dictionary that would look like this: {"the": 1, "a", 2} etc. This is known as a **bag of words**. This approach to representing words numerically, however, only allow a computer to understand words numerically to identify unique words. It does not, however, allow a computer to understand *meaning*.
# 
# Imagine this scenario:
# 
# Tom loves to eat chocolate.
# 
# Tom likes to eat chocolate.
# 
# These sentences represented as a numerical array (list) would look like this:
# 
# 1, 2, 3, 4, 5
# 
# 1, 6, 3, 4, 5
# 
# As we can see, as humans both sentences are nearly identical. The only difference is the degree to which Tom appreciates eating chocolate. If we examine the numbers, however, these two sentences seem quite close, but their semantical meaning is impossible to know for certain. How similar is 2 to 6? The number 6 could represent "hates" as much as it could represent "likes". This is where word vectors come in.
# 
# Word vectors take these one dimensional bag of words and gives them multidimensional meaning by representing them in higher dimensional space, noted above. This is achieved through machine learning and can be easily achieved via Python libraries, such as Gensim, which we will explore more closely in the next notebook.

# ## Why use Word Vectors?

# The goal of word vectors is to achieve numerical understanding of language so that a computer can perform more complex tasks on that corpus. Let's consider the example above. How do we get a computer to understand 2 and 6 are synonyms or mean something similar? One option you might be thinking is to simply give the computer a synonym dictionary. It can look up synonyms and then know what words mean. This approach, on the surface, makes perfect sense, but let's explore that option and see why it cannot possibly work.
# 
# For the example below, we will be using the Python library PyDictionary which allows us to look up definitions and synonyms of words.

# In[4]:


from PyDictionary import PyDictionary

dictionary=PyDictionary()
text = "Tom loves to eat chocolate"

words = text.split()
for word in words:
        syns = dictionary.synonym(word)
        print (f"{word}: {syns[0:5]}\n")


# Even with the simple sentence, the results are comically bad. Why? The reason is because synonym substitution, a common method of data augmentation, does not take into account syntactical differences of synonyms. I do not believe anyone would think "Felis domesticus", the Latin name of the common house cat, would be an adequite substitution for the name Tom. Nor is "garbage down" a really proper synonym for eat.
# 
# Perhaps, then we could use synonyms to find words that have cross-terms, or terms that appear in both synonym sets.
# 

# In[5]:


from PyDictionary import PyDictionary

dictionary=PyDictionary()

words  = ["like", "love"]
for word in words:
    syns = dictionary.synonym(word)
    print (f"{word}: {syns[0:5]}\n")


# This, as we can see, has some potential to work, but again it is not entirely reliable and to work with such a list would be computationally expensive. For both of these reasons, word vectors are prefered. The reason? Because they are formed by the computer on corpora for a specific task. Further, they are numerical in nature (not a dictionary of words), meaning the computer can process them more quickly.

# ## What do Word Vectors Look Like?

# Word vectors have a preset number of dimensions. These dimensions are honed via machine learned. Models take into account word frequency alongside words across a corpus and the appearance of other words in similar contexts. This allows for the the computer to determin the syntactical similarity of words numerically. It then needs to represent these relationships numerically. It does this through the vector, or a matrix of matrices. To represent these more concisely, models flatten a matrix to a float (decimal number). The number of dimensions represent the number of floats in the matrix.
# 
# Below is a pretrained model's output of word vectors for Holocaust documents. This is how the word "know" looks in vectors:
# 
# know -0.19911548 -0.27387282 0.04241912 -0.58703226 0.16149549 -0.08585547 -0.10403373 -0.112367705 -0.28902963 -0.42949626 0.051096343 -0.04708015 -0.051914077 -0.010533272 -0.23334776 0.031974062 -0.015784053 -0.21945408 0.07359381 0.04936823 -0.15373217 -0.18460844 -0.055799782 -0.057939123 0.14816307 -0.46049833 0.16128318 0.190906 -0.29180774 -0.08877125 0.23563664 -0.036557104 -0.23812544 0.21938106 -0.2781296 0.5112853 0.049084224 0.14876273 0.20611146 -0.04535578 -0.35051352 -0.26381743 0.20824358 0.29732847 -0.013382204 -0.19970295 -0.34890386 -0.16214448 -0.23497184 0.1656344 0.15815939 0.012848561 -0.22887675 -0.21618247 0.13367777 0.1028471 0.25068823 -0.13625076 -0.11771541 0.4857257 0.102198474 0.06380113 -0.22328818 -0.05281015 0.0059655504 0.095453635 0.39693353 -0.066147 -0.1920163 0.5153346 0.24972811 -0.0076305643 -0.05530072 -0.24668717 -0.074051596 0.29288396 -0.0849124 0.37786478 0.2398532 -0.10374063 0.5445305 -0.41955113 0.39866814 -0.23992492 -0.15373677 0.34488577 -0.07166888 -0.48001364 0.0660652 0.061260436 0.32197484 -0.12741785 0.024006622 -0.07915035 -0.04467735 -0.2387938 -0.07527494 0.07079664 0.074456714 0.17877163 -0.002122373 -0.16164272 0.12381973 -0.5908519 0.5827627 -0.38076186 0.095964395 0.020342976 -0.5244792 0.24467848 -0.12481717 0.2869162 -0.34473857 -0.19579992 -0.18069582 0.015281798 -0.18330036 -0.08794056 0.015334953 -0.5609912 0.17393902 0.04283724 -0.07696586 0.2040299 0.34686008 0.31219167 0.14669564 -0.26249585 -0.42771882 0.5381632 -0.123247474 -0.29142144 -0.29963812 -0.32800657 -0.10684048 -0.08594837 0.19670585 0.13474767 0.18349588 -0.4734125 0.15554792 -0.21062694 -0.14191462 -0.12800062 0.2053445 -0.05258381 0.10878109 0.56381494 0.22724482 -0.17778987 -0.061046753 0.10789692 -0.015310492 0.16563527 -0.31812978 -0.1478078 0.4323269 -0.2543924 -0.25956103 0.38653126 0.5080214 -0.18796602 -0.10318089 0.023921987 -0.14618908 0.22923793 0.37690258 0.13323267 -0.34325415 -0.048353776 -0.30283198 -0.2839813 -0.2627738 -0.07422618 -0.31940162 0.38072023 0.56700015 -0.023362642 -0.3786432 0.084006436 0.0729958 0.09483505 -0.2665334 0.12699558 -0.37927982 -0.39073908 0.0063185897 -0.34464878 -0.24011964 0.09303968 -0.15488827 -0.018486138 0.3560308 -0.26005003 0.089302294 0.116130605 0.07684872 -0.085253105 -0.28178927 -0.17346472 -0.20008522 0.004347025 0.34192443 0.017453942 0.06926512 -0.15926014 -0.018554512 0.18478563 -0.040194467 0.38450953 0.4104423 -0.016453728 0.013374495 -0.011256633 0.09106963 0.20074937 0.17310189 -0.12467103 0.16330549 -0.0009963055 0.12181527 -0.05295286 -0.0059491103 -0.04697837 0.38616535 -0.21074814 -0.32234505 0.47269863 0.27924335 0.13548143 -0.2677968 0.03536313 0.3248672 0.2062973 0.29093853 0.1844036 -0.43359983 0.025519002 -0.06319317 -0.2427806 -0.22732906 0.08803728 -0.041860744 -0.151291 0.3400458 -0.29143015 0.25334117 0.06265491 0.26399022 -0.20121849 0.22156847 -0.50599706 0.069224015 0.52325517 -0.34115726 -0.105219565 -0.37346402 -0.02126528 0.09619415 0.017722093 -0.3621799 -0.109912336 0.021542747 -0.13361925 0.2087667 -0.08780184 0.09494446 -0.25047818 -0.07924239 0.21750642 0.2621652 -0.52888566 0.081884995 -0.20485449 0.18029206 -0.5623824 -0.03897387 0.3213515 0.057455678 -0.26524526 0.14741589 0.1257589 0.04708992 0.026751317 -0.014696863 -0.11038961 0.004459205 -0.01394376 0.091146186 -0.15486309 0.20662159 -0.0987916 -0.07740813 0.009704136 0.28866896 0.3916269 0.35061485 0.31678385 0.43233085 0.44510433
# 
# For these vectors, I used the industry-standard of 300 dimensions. We see each of these dimensions represented by each of the floats, separated by whitespace. As the model passes over the corpus it is being trained on, it hones these numbers and changes them for each word. Over multiple epochs, or generations, it gains a clearer sense of the similarity of words, or at least words that are used in similar contexts.

# ## Why use Word Vectors?

# Once a word vector model is trained, we can do similarity matches very quickly and very reliably. At the start of the notebook, I asked you to consider the word concentration camp. Let's now use these word vectors to find the 10 most similar words to concentration camp.

# In[ ]:


[
    ('extermination_camp', 0.5768706798553467),
    ('camp', 0.5369070172309875),
    ('Flossenbiirg', 0.5099129676818848),
    ('Sachsenhausen', 0.5068483948707581),
    ('Auschwitz', 0.48929861187934875),
    ('Dachau', 0.4765608310699463),
    ('concen', 0.4753464460372925),
    ('Majdanek', 0.4740387797355652),
    ('Sered', 0.47086501121520996),
    ('Buchenwald', 0.4692303538322449)
]


# These are the items that are most similar to concentration camp in our word vectors. The tuple has two indices. Index 0 is the word and index 1 is the similarity, represented as a float.
# 
# Exterimination camp is not a direct synonym, as it has a distinction in what happened to prisoners, i.e. execution, however, these are very similar. Seeing this as the most similar word is a sign that the word vectors are well-aligned. Camp is expected as it is a singular word that has similar meaning in context to contentration camp. The remainder of this list are proper nouns, all of which were concentration camps with one exception: "concen". This is clearly a result of poor cleaning. Concen is not a word, rather a type of concen-tration, most likely. The fact that this is here is also a good sign that our word vectors have aligned well enough to have typos in near vector space.
# 
# Let's do something similar with Auschwitz.

# In[ ]:


[
    ('Auschwitz_Birkenau', 0.6649479866027832),
    ('Birkenau', 0.5385118126869202),
    ('subcamp', 0.5343026518821716),
    ('camp', 0.533636748790741),
    ('III', 0.5323576927185059),
    ('stutthof', 0.518073320388794),
    ('Ravensbriick', 0.5084848403930664),
    ('Berlitzer', 0.5083401203155518),
    ('Malchow', 0.5051567554473877),
    ('Oswiecim', 0.5016494393348694)
]


# As we can see, the words closest to Auchwitz are places assocaited with Auschwitz, such as Birkenau, subcamps (of which Auschwitz had many), other concentration camps (such as Ravensbriick), and the location of the Auschwitz memorial, Oswiecim.
# 
# In other words, we have words closely associated with Auschwitz in particular.
# 
# In the next video, we will be looking closely at how to generate word vectors via the library Gensim. To get a better sense of word vectors, please watch the video below.

# ## Video

# In[6]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/eZJm7PisZvk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')

