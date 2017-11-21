#!/usr/bin/python3
# -*- coding:utf-8 -*-

class SyntacticAnalyser:
    '''
    Syntactical analyser for text in portuguese
    '''
    def __init__(self):
        self.words = None
        self.current_index = 0
        self.pivot = 0

    def __next(self):
        '''
        Return the next token in the list
        '''
        try:
            if self.current_index == len(self.words) - 1 \
                and self.words[self.current_index][1] == "PU":
                raise ValueError("PU")

            aux = self.words[self.current_index]
            self.current_index += 1

            if aux[1] == "PU":
                return self.__next()

            # print(aux)

            return aux

        except IndexError:
            return ["EOF", "EOF"]
        
        except ValueError:
            return ["EOF", "EOF"]

    def __back(self):
        '''
        Back one index
        '''
        self.current_index -= 1
        return self.words[self.current_index]

    def __is_EOF(self):
        '''
        Check if the setence is over
        '''
        if self.__next()[1] == "EOF":
            return True
        else:
            self.__back()
            return False

    def analysis(self, words):
        '''
        Start the analyse
        '''
        self.pivot = 0
        self.current_index = 0
        self.words = words
        ret = self.__S()
        return ret

    def __S(self):
        '''
        S -> NP VP
        S -> VP NP
        S -> VP
        S -> ADVP S
        '''
        if self.__NP():
            if not self.pivot:
                self.pivot = self.current_index
            return self.__VP()

        elif self.__VP():
            if self.current_index == len(self.words) \
                or self.words[self.current_index][1] == "PU":
                return True

            if not self.pivot:
                self.pivot = self.current_index

            return self.__NP()

        elif self.__ADVP():
            return self.__S()

        return False

    def __NP(self):
        '''
        NP -> art N’
        NP -> prosub N’
        NP -> proadj N’
        NP -> num N’
        NP -> N’
        NP -> proadj NP
        '''
        # print("NP")
        if self.__next()[1] in ["ART", "NUM"]:
            if self.__N_ln():
                return True
            else:
                self.__back()
                return False

        else:
            self.__back()

        if self.__next()[1] == "PROSUB":
            if self.__N_ln():
                return True

            self.__back()
            return False
        else:
            self.__back()

        if self.__next()[1] == "PROADJ":
            if self.__N_ln() or self.__NP():
                return True

            self.__back()
            return False
        else:
            self.__back()

        return self.__N_ln()

    def __N_ln(self):
        '''
        N’ -> pro N’’
        N’ -> n N’’
        N’ -> nprop N’’
        N’ -> AP N’ N’’
        '''
        # print("N'")

        if self.__next()[1] in ["N", "NPROP"]:
            if self.__N_lnln():
                return True
            else:
                self.__back()
                return False
        else:
            self.__back()

        if "PRO" in self.__next()[1]:
            if self.__N_lnln():
                return True
            else:
                self.__back()
                return False
        else:
            self.__back()

        if self.__AP():
            if self.__N_ln():
                return self.__N_lnln()

            return False
        else:
            return False

    def __N_lnln(self):
        '''
        N’’ -> AP N’’
        N’’ -> PP N’’
        N’’ -> ɛ
        '''
        # print("N''")

        if self.__is_EOF():
            return True

        elif self.__AP() or self.__PP():
            return self.__N_lnln()

        return True

    def __AP(self):
        '''
        AP -> ADJ’ ADVP
        AP -> ADJ’ PP
        AP -> ADJ’
        AP -> ADVP ADJ’
        '''
        # print("AP")

        if self.__ADJ_ln():
            if self.__ADVP() or self.__PP():
                return True

            return True

        elif self.__ADVP():
            return self.__ADJ_ln()

        return False

    def __ADJ_ln(self):
        '''
        ADJ’ -> adj ADJ’’ ADJ’’’
        '''
        # print("ADJ'")

        if self.__next()[1] == "ADJ":
            if self.__ADJ_lnln():
                return self.__ADJ_lnlnln()

            self.__back()
            return False
        else:
            self.__back()

        return False

    def __ADJ_lnln(self):
        '''
        ADJ’’ -> ADVP ADJ’’
        ADJ’’ -> PP ADJ’’
        ADJ’’ -> ɛ
        '''
        # print("AP''")

        if self.__is_EOF():
            return True

        elif self.__ADVP() or self.__PP():
            return self.__ADJ_lnln()

        return True

    def __ADJ_lnlnln(self):
        '''
        ADJ’’’ -> ADVP ADJ’’ ADJ‘’’
        ADJ’’’ -> ɛ
        '''
        # print("AJ'''")
        if self.__is_EOF():
            return True
        elif self.__ADVP():
            if self.__ADJ_lnln():
                return self.__ADJ_lnlnln()
            return False
        return True

    def __PP(self):
        '''
        PP -> prep NP
        PP -> prep ADVP
        '''
        # print("PP")

        if "PREP" in self.__next()[1]:
            if self.__NP() or self.__ADVP():
                return True

            self.__back()
            return False
        else:
            self.__back()
            return False

    def __VP(self):
        '''
        VP -> V’
        VP -> V’ PP
        VP -> V’ ADVP
        VP -> ADVP V’
        '''
        # print("VP")

        if self.__V_ln():
            if self.__PP() or self.__ADVP():
                pass

            return True

        elif self.__ADVP():
            return self.__V_ln()

        else:
            return False

    def __V_ln(self):
        '''
        V’ -> ADVP V’ V’’
        V’ -> VB V’’
        V’ -> VB NP V’’
        V’ -> VB PP V’’
        V’ -> VB AP V'’
        V’ -> VB ADVP V’’
        '''
        # print("V'")

        if self.__ADVP():
            if self.__V_ln():
                return self.__V_lnln()

            return False

        elif self.__VB():
            if self.__V_lnln():
                return True

            elif self.__NP() or self.__PP() \
                 or self.__AP() or self.__ADVP():

                return self.__V_lnln()

            return False
        else:
            return False

    def __V_lnln(self):
        '''
        V’’ -> NP V’’
        V’’ -> PP V’’
        V’’ -> ADVP V’’
        V’’ -> ɛ
        '''
        # print("V''")

        if self.__is_EOF():
            return True

        elif self.__NP() \
             or self.__PP() \
             or self.__ADVP():

            return self.__V_lnln()

        return True

    def __VB(self):
        '''
        VB -> v
        VB -> v pcp
        '''
        # print("VB")

        if self.__next()[1] == "V":
            if self.__next()[1] != "PCP":
                self.__back()

            return True
        else:
            self.__back()
            return False

    def __ADVP(self):
        '''
        ADVP -> ADV’ ADVP’
        ADVP -> ADV’ PP ADVP’
        '''
        # print("ADVP")

        if self.__ADV_ln():
            if self.__ADVP_ln():
                return True
            elif self.__PP():
                return self.__ADVP_ln()

        return False

    def __ADVP_ln(self):
        '''
        ADVP’ -> ADV’ ADVP’
        ADVP’ -> ɛ
        '''
        # print("ADVP'")

        if self.__is_EOF():
            return True

        elif self.__ADV_ln():
            return self.__ADVP_ln()

        return True

    def __ADV_ln(self):
        '''
        ADV’ -> adv ADV’’
        '''
        # print("ADV'")

        if self.__next()[1] == "ADV":
            if self.__ADV_lnln():
                return True
            else:
                self.__back()
                return False
        else:
            self.__back()
            return False

    def __ADV_lnln(self):
        '''
        ADV’’ -> PP ADV’’
        ADV’’ -> ɛ
        '''
        # print("ADV''")

        if self.__is_EOF():
            return True

        elif self.__PP():
            return self.__ADV_lnln()

        return True

if __name__ == "__main__":
    import sys
    from tagger import Tagger

    print(SyntacticAnalyser().analysis(Tagger().tag(sys.argv[1])))
