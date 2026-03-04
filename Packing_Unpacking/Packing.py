import os

class Packing:
    @staticmethod
    def main():
        print("-----------------------------------------------------")
        print("------- Marvellous Packer Unpacker CUI Module -------")
        print("-----------------------------------------------------")

        print("----------------- Packing Activity ------------------")
        print()

        print("Enter the name of Directory that you want to open for packing : ")
        FolderName = input()

        fobj = FolderName

        print("Enter the name of packed file that you want to create : ")
        PackedFile = input()

        Packobj = PackedFile
        
        if os.path.exists(Packobj):
            print("Unable to create packed file")
            return

        foobj = open(Packobj, "wb")

        if os.path.exists(fobj) and os.path.isdir(fobj):
            i = 0
            j = 0
            iCount = 0

            Arr = os.listdir(fobj)

            Header = None
            iRet = 0
            Buffer = bytearray(1024)
            fiobj = None
            
            for i in range(len(Arr)):
                filepath = os.path.join(fobj, Arr[i])
                Header = Arr[i]
                
                if Header.endswith(".txt") and os.path.isfile(filepath):
                    print("File packed with name : " + Header)
                    
                    # Clean readable header
                    Header = "FILE_START\n"
                    Header = Header + "Filename: " + Arr[i] + "\n"
                    Header = Header + "Size: " + str(os.path.getsize(filepath)) + "\n"
                    Header = Header + "CONTENT_START\n"

                    foobj.write(bytes(Header, 'utf-8'))

                    fiobj = open(filepath, "rb")

                    while True:
                        Buffer = fiobj.read(1024)
                        if not Buffer:
                            break
                        foobj.write(Buffer)

                    # End separator
                    foobj.write(bytes("\nFILE_END\n\n", 'utf-8'))

                    fiobj.close()
                    iCount += 1

            print("-----------------------------------------------------")
            print("Packing activity completed..")
            print("Number of files scan : " + str(len(Arr)))
            print("Number of files packed : " + str(iCount))
            print("-----------------------------------------------------")

            print("Thank you for using Marvellous Packer Unpacker tool")
            foobj.close()
        else:
            print("There is no such directory")


if __name__ == '__main__':
    Packing.main()