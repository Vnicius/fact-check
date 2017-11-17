#!/usr/bin/python3
# -*- coding:utf-8 -*-

class SyntacticAnalyser:
    def __init__(self):
        self.words = None
        self.current_index = 0
        self.pivot = 0

    def __next(self):
        '''
        Return the next token in the list
        '''
        try:
            aux = self.words[self.current_index]
            self.current_index += 1
            # print(aux)
            return aux
        except:
            return ["EOF","EOF"]
    
    def __back(self):
        '''
        Back one index
        '''
        self.current_index -= 1
        return self.words[self.current_index]

    def __is_EOF(self):
        if self.__next()[1] == "EOF":
            return True
        else:
            self.__back()
            return False

    def analysis(self, words):
        '''
        Star the analyse
        '''
        self.pivot = 0
        self.current_index = 0
        self.words = words
        ret = self.__S()
        return ret

    def __S(self):
        if self.__NP():
            if not self.pivot:
                self.pivot = self.current_index
            return self.__VP()

        elif self.__VP():
            if not self.pivot:
                self.pivot = self.current_index

            # print("MMMMMMMMMMMMMMMMM")
            return self.__NP()

        elif self.__ADVP():
            return self.__S()

        return False
    
    def __NP(self):
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
        else:
            self.__back()
        
        if self.__next()[1] == "PROADJ":
            if self.__N_ln():
               return True
            elif self.__NP():
                return True
            else:
                self.__back()
                return False
        else:
            self.__back()
        
        return self.__N_ln()
    
    def __N_ln(self):
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
        # print("N''")

        if self.__is_EOF():
            return True
        elif self.__N_ln():
            return True
        elif self.__AP():
            return self.__N_lnln()

        elif self.__PP():
            return self.__N_lnln()
        
        return True

    def __AP(self):
        # print("AP")
        if self.__ADJ_ln():
            if self.__ADVP():
                return True

            elif self.__PP():
                return True

            return True

        elif self.__ADVP():
            return self.__ADJ_ln()

        return False
    
    def __ADJ_ln(self):
        # print("ADJ'")
        if self.__next()[1] == "ADJ":
            if self.__ADJ_lnln():
                return True
            
            self.__back()
            return False
        else:
            self.__back()

        if self.__ADVP():
            if self.__ADJ_ln():
                return self.__ADJ_lnln()

            return False
        
        return False
    
    def __ADJ_lnln(self):
        # print("AP''")

        if self.__is_EOF():
            return True

        elif self.__ADVP():
            return self.__ADJ_lnln()
        
        elif self.__PP():
            return self.__ADJ_lnln()
        
        return True

    def __PP(self):
        # print("PP")
        if "PREP" in self.__next()[1]:
            if self.__NP():
                return True
            elif self.__ADVP():
                return True

            self.__back()
            return False
        else:
            self.__back()
            return False
    
    def __VP(self):
        # print("VP")
        if self.__V_ln():
            if self.__PP():
                return True
            elif self.__ADVP():
                return True

            return True
            
        elif self.__ADVP():
            if self.__V_ln():
                return True
            
            return False
        
        else:
            return False
    
    def __V_ln(self):
        # print("VP'")
        if self.__ADVP():
            if self.__V_ln():
                return self.__V_lnln()

            return False

        elif self.__VB():
            if self.__V_lnln():
                return True

            elif self.__NP():
                if self.__V_lnln():
                    return True
                return False

            elif self.__PP():
                if self.__V_lnln():
                    return True
                return False

            elif self.__AP():
                if self.__V_lnln():
                    return True
                return False

            elif self.__ADVP():
                if self.__V_lnln():
                    return True
                return False

            return False
        
        else:
            return False

    def __V_lnln(self):
        # print("V''")

        if self.__is_EOF():
            return True

        elif self.__NP():
            return self.__V_lnln()

        elif self.__PP():
            return self.__V_lnln()

        elif self.__ADVP():
            return self.__V_lnln()
        
        return True

    def __VB(self):
        # print("VB")
        if self.__next()[1] == "V":
            if self.__next()[1] != "PCP":
                self.__back()

            return True
        else:
            self.__back()
            return False

    def __ADVP(self):
        # print("ADVP")
        if self.__ADV_ln():
            if self.__ADVP_ln():
                return True
            elif self.__PP():
                return self.__ADVP_ln()
            
            return False

        else:
            return False
    
    def __ADVP_ln(self):
        # print("ADVP'")
        if self.__is_EOF():
            return True

        elif self.__ADV_ln():
            return self.__ADVP_ln()
        
        return True

    def __ADV_ln(self):
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
        # print("ADV''")
        if self.__is_EOF():
            return True

        elif self.__PP():
            return self.__ADV_lnln()

        return True

if __name__ == "__main__":
    import sys
    from tagger import Tagger

    # print(SyntacticAnalyser().analysis(Tagger().tag(sys.argv[1])))
