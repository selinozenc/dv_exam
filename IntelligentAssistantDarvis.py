# ***********************************************************************************************

#                       INPUTs                                          EXPECTED OUTPUTs
#    1 " this isn't a relevant question , is it??? "         "This isn't a relevant question, is it?"
#    2 "Is this answer correct?"                             "Is this answer correct?"
#    3" Is,it correct , question"                            "Is, it correct, question?"
#    4 " s.",                                                "S.?"
#    5 "z?"                                                  "Z?"
#    6 "questionword ,anotherquestionword,"                  "Questionword, anotherquestionword, ?"
#    7 "where is F.A.Q.?"                                    "Where is F.A.Q.?"
#    8 "a,b,c,d,e "                                          "A, b, c, d, e?"

# Additional tests: ...
# zz,?
##      you think  ,is it correct , I don't think so..,    ??

# ***********************************************************************************************


import re
from string import punctuation
from pprint import pprint

# ALTERNATE W RegularExpression:

# pattern = re.compile(r'\s+')
# strippedSentence = re.sub(pattern, '', sentence)

# --------------------------------------------------------

# NOTE: for removing whitespaces (ONLY at the start & end):
# strippedSentence = sentence.strip()


def uppercaseFirstLetter(sentence):

    #uppercasedSentence = sentence.capitalize() # sentence[:1].upper()
    uppercasedSentence = sentence[:1].upper() + sentence[1:] # Doing :1 and not 0 to prevent exceptions in case the string is empty
    print("In uppercaseFirstLetter: " + uppercasedSentence)
    return uppercasedSentence


def singleQuestionMarkRegulation(sentence):

    patternSsS = r'\?+'
    singleQuestionMarkRegulation = re.sub(patternSsS, '?', sentence)

    print("In singleQuestionMarkRegulation " + singleQuestionMarkRegulation)
    return singleQuestionMarkRegulation


def clearAllWhitespaces(sentence):
    strippedSentence = " ".join(sentence.split())
    # strippedSentence = " ".join(strippedSentence.lstrip(punctuation))
    # strippedSentence = "".join(strippedSentence.lstrip().split())
    # sentence.translate(str.maketrans(',', ',', punctuation))
    print("In clearAllWhitespaces: " + strippedSentence)
    return strippedSentence


def punctuationRegulation(sentence):
        #pattern = r'\s+([?.!,;"](?:\s|$))'
        #newPunctuation = punctuation.replace(" ", "?")

        # removes more than one punctuation:
        # pattern2 = r'[(?=\?)]'
        # pattern2 = r'[+('+punctuation+'=\\'+punctuation+')]' # for all punctuation!..
        # punctuationRegulatedSentence = re.sub(pattern2, 'sSs', sentence)

    # cleans all spaces before punctuation :
    pattern = r'\s+(['+punctuation+'])'
    punctuationRegulatedSentence = re.sub(pattern, r'\1', sentence)

    print("In punctuationRegulation " + punctuationRegulatedSentence)
    return punctuationRegulatedSentence


def commaRegulation(sentence):
    punctuations = punctuation
    commaRegulatedSentence = sentence.replace(',', ', ')

    print("In commaRegulation: " + commaRegulatedSentence)
    return commaRegulatedSentence


def addQuestionMark(sentence):
    interrogativeSentence = sentence+"?"
    print("addQuestionMark: " + interrogativeSentence)
    return interrogativeSentence


def sentenceCorrector(sentence):

    correctSentence = ""

    # add a question mark at the end of the sentence:
    correctSentence = addQuestionMark(sentence)

    # comma regularition:
    correctSentence = commaRegulation(correctSentence)

    # punctuation regularition:
    correctSentence = punctuationRegulation(correctSentence)

    # comma regularition:
    correctSentence = commaRegulation(correctSentence)

    # removing whitespaces (left, right, bottom -also duplicates-):
    correctSentence = clearAllWhitespaces(correctSentence)

    # single question mark regularition:
    correctSentence = singleQuestionMarkRegulation(correctSentence)

    # Uppercase letter for the first letter.
    correctSentence = uppercaseFirstLetter(correctSentence)

    # printing the sentence for clear comparison on PythonConsole:
    print(correctSentence)

    #string.format("öyle,değil mi  ?")
    return correctSentence


def askDarvis():
    print("Hello! I'm your virtual assistant Darvis. :) You can ask me anything u want!(: \n What's the subject u wonder? o.O")

    sentence = input("Ask ME anything: ")
    # os.system("pause")
    return sentence



######################################### NOTES: ####################################################

# - I did not add any additional function, I used existing string functions because of the execution time concerns.
# - I seperated functions for modularity
# - Also, '\1' expression in regular expressions may a negative effect in the way of execution time but it is satisfactory for desired program performance ( [execution time limit] 4 seconds FOR Guaranteed constraints: question.length ≤ 100)
# - I did not any additional control in the way of given guaranteed constraints. (the first of these characters is a letter (possibly lowercase) etc.)
# - ADVANCED: A manual punctuation regularization lib may code OR existing librarie(s)(such as fastPunct) may use to make things easier. =)
    # REF: https://github.com/notAI-tech/fastPunct

    # The fastPunc library may also help for NLP spell correction process..

                                        # ... THANKS FOR YOUR TIME ... #
#####################################################################################################


