# Unpacking Activity

import os

class Unpacking:
    @staticmethod
    def main():
        
        Header = None
        iRet = 0
        HeaderX = None
        obj = None
        FileSize = 0
        foobj = None
        iCount = 0
        
        print("-----------------------------------------------------")
        print("------- Marvellous Packer Unpacker CUI Module -------")
        print("-----------------------------------------------------")

        print("---------------- Unpacking Activity -----------------")
        print()

        print("Enter the name of Packed that you want to open : ")
        PackedFile = input()

        fobj = PackedFile

        if not os.path.exists(fobj):
            print("Unable to proceed as Packed file is missing...")
            return  

        fiobj = open(fobj, "rb")

        while True:
            Line = fiobj.readline()

            if not Line:
                break

            HeaderX = Line.decode().strip()

            if not HeaderX:
                continue

            if HeaderX == "FILE_START":

                HeaderX = fiobj.readline().decode().strip()
                Tokens = HeaderX.split(": ")
                obj = Tokens[1]

                print("File drop with name : " + obj)

                fiobj.readline()
                fiobj.readline()

                foobj = open(obj, "wb")

                while True:
                    Line = fiobj.readline()

                    if Line.decode().strip() == "FILE_END":
                        break

                    foobj.write(Line)

                foobj.close()
                iCount += 1

        print("-----------------------------------------------------")
        print("Unpacking activity completed..")
        print("Number of files unpacked : " + str(iCount))
        print("-----------------------------------------------------")

        print("Thank you for using Marvellous Packer Unpacker tool")
        
        fiobj.close()


if __name__ == '__main__':
    Unpacking.main()