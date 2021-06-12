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

def uppercaseFirstLetter(sentence):

    uppercasedSentence = sentence[:1].upper() + sentence[1:]
    return uppercasedSentence


def singleQuestionMarkRegulation(sentence):

    patternSsS = r'\?+'
    singleQuestionMarkRegulation = re.sub(patternSsS, '?', sentence)
    return singleQuestionMarkRegulation


def clearAllWhitespaces(sentence):
    strippedSentence = " ".join(sentence.split())
    return strippedSentence


def punctuationRegulation(sentence):

    # cleans all spaces before punctuation :
    pattern = r'\s+(['+punctuation+'])'
    punctuationRegulatedSentence = re.sub(pattern, r'\1', sentence)
    return punctuationRegulatedSentence


def commaRegulation(sentence):
    commaRegulatedSentence = sentence.replace(',', ', ')
    return commaRegulatedSentence


def addQuestionMark(sentence):
    interrogativeSentence = sentence+"?"
    return interrogativeSentence


def sentenceCorrector(sentence):

    correctSentence = ""

    correctSentence = addQuestionMark(sentence)
    correctSentence = commaRegulation(correctSentence)
    correctSentence = punctuationRegulation(correctSentence)
    correctSentence = commaRegulation(correctSentence)
    correctSentence = clearAllWhitespaces(correctSentence)
    correctSentence = singleQuestionMarkRegulation(correctSentence)
    correctSentence = uppercaseFirstLetter(correctSentence)

    return correctSentence


def askDarvis():
    print("Hello! I'm your virtual assistant Darvis. :) You can ask me anything u want!(: \n What's the subject u wonder? o.O")

    sentence = input("Ask ME anything: ")
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


